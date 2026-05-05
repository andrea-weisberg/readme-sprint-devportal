from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time
from typing import Callable
from urllib.parse import urlparse
from urllib.request import Request, urlopen


MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
WORDPRESS_UPLOAD_PATH = "/wp-content/uploads/"
READ_ME_RATE_LIMIT_WAIT_SECONDS = 310


class RateLimitError(RuntimeError):
    pass


@dataclass(frozen=True)
class ImageSyncSummary:
    files_scanned: int
    image_references_rewritten: int
    uploaded_images: int
    reused_images: int


def sync_wordpress_images(
    output_root: Path,
    api_key: str,
    cache_root: Path,
    *,
    downloader: Callable[[str, Path], None] | None = None,
    uploader: Callable[[Path, str], str] | None = None,
) -> ImageSyncSummary:
    downloader = downloader or _download_image
    uploader = uploader or _upload_image
    cache_root.mkdir(parents=True, exist_ok=True)

    manifest_path = cache_root / "rdme-image-map.json"
    manifest = _load_manifest(manifest_path)

    markdown_files = sorted(output_root.rglob("*.md"))
    files_scanned = len(markdown_files)
    references_rewritten = 0
    uploaded_images = 0
    reused_images = 0

    for markdown_file in markdown_files:
        original = markdown_file.read_text(encoding="utf-8")
        rewritten = original

        for image_url in _wordpress_image_urls(original):
            mapped_url = manifest.get(image_url)
            if mapped_url:
                reused_images += 1
            else:
                downloaded_path = _download_path_for_url(cache_root, image_url)
                if not downloaded_path.exists():
                    downloader(image_url, downloaded_path)
                mapped_url = _upload_with_retries(downloaded_path, api_key, uploader)
                manifest[image_url] = mapped_url
                _write_manifest(manifest_path, manifest)
                uploaded_images += 1

            replacement_count = rewritten.count(image_url)
            if replacement_count:
                rewritten = rewritten.replace(image_url, mapped_url)
                references_rewritten += replacement_count

        if rewritten != original:
            markdown_file.write_text(rewritten, encoding="utf-8")

    _write_manifest(manifest_path, manifest)
    return ImageSyncSummary(
        files_scanned=files_scanned,
        image_references_rewritten=references_rewritten,
        uploaded_images=uploaded_images,
        reused_images=reused_images,
    )


def _wordpress_image_urls(content: str) -> tuple[str, ...]:
    seen: set[str] = set()
    urls: list[str] = []
    for _, url in MARKDOWN_IMAGE_RE.findall(content):
        if _is_wordpress_image(url) and url not in seen:
            seen.add(url)
            urls.append(url)
    return tuple(urls)


def _is_wordpress_image(url: str) -> bool:
    parsed = urlparse(url)
    return (
        parsed.scheme in {"http", "https"}
        and WORDPRESS_UPLOAD_PATH in parsed.path
    )


def _download_path_for_url(cache_root: Path, url: str) -> Path:
    parsed = urlparse(url)
    original_name = Path(parsed.path).name or "image"
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return cache_root / "downloads" / f"{digest}-{original_name}"


def _download_image(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = Request(url, headers={"User-Agent": "Codex/ReadMeRebuild"})
    with urlopen(request) as response:
        destination.write_bytes(response.read())


def _upload_image(image_path: Path, api_key: str) -> str:
    result = subprocess.run(
        [
            "curl",
            "-sS",
            "-w",
            "\n%{http_code}",
            "-X",
            "POST",
            "https://api.readme.com/v2/images",
            "-H",
            f"Authorization: Bearer {api_key}",
            "-F",
            f"file=@{image_path}",
        ],
        check=True,
        text=True,
        capture_output=True,
    )
    payload, _, status = result.stdout.rpartition("\n")
    if status == "429":
        raise RateLimitError(
            f"ReadMe image upload rate-limited for {image_path.name}: {payload}"
        )
    if status not in {"200", "201"}:
        raise RuntimeError(
            f"ReadMe image upload failed with HTTP {status} for {image_path.name}: {payload}"
        )

    body = json.loads(payload)
    if "data" not in body or "url" not in body["data"]:
        raise RuntimeError(
            f"Unexpected ReadMe image upload response for {image_path.name}: {payload}"
        )

    return body["data"]["url"]


def _upload_with_retries(
    image_path: Path,
    api_key: str,
    uploader: Callable[[Path, str], str],
    *,
    max_attempts: int = 5,
) -> str:
    attempt = 1
    while True:
        try:
            return uploader(image_path, api_key)
        except RateLimitError:
            if attempt >= max_attempts:
                raise
            time.sleep(READ_ME_RATE_LIMIT_WAIT_SECONDS)
            attempt += 1
        except Exception as exc:  # pragma: no cover - exercised in live runs
            raise RuntimeError(
                f"Failed to upload image {image_path.name}"
            ) from exc


def _load_manifest(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _write_manifest(path: Path, manifest: dict[str, str]) -> None:
    path.write_text(
        json.dumps(dict(sorted(manifest.items())), indent=2) + "\n",
        encoding="utf-8",
    )
