"""Path and slug normalization helpers."""

from __future__ import annotations

import os
import re
from pathlib import Path
from urllib.parse import unquote, urlparse


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def slugify(value: str) -> str:
    cleaned = clean_text(value).lower()
    cleaned = re.sub(r"[^a-z0-9]+", "-", cleaned)
    return cleaned.strip("-")


def normalize_path(value: str) -> str:
    if not value:
        return ""

    parsed = urlparse(value)
    raw_path = parsed.path if parsed.scheme or parsed.netloc else value
    raw_path = unquote(raw_path).split("#", 1)[0].split("?", 1)[0]
    raw_path = raw_path.replace("\\", "/")
    raw_path = re.sub(r"/+", "/", raw_path)
    raw_path = raw_path.strip("/")

    if raw_path.endswith(".html"):
        raw_path = raw_path[:-5]
    if raw_path.endswith("/index"):
        raw_path = raw_path[:-6]

    return raw_path.lower()


def readme_doc_key(markdown_path: str) -> str:
    path = Path(markdown_path)
    parts = path.parts
    if parts and parts[0] == "docs":
        path = Path(*parts[1:])
    path_without_suffix = path.with_suffix("")
    return normalize_path(path_without_suffix.as_posix())


def filename_slug(markdown_path: str) -> str:
    return slugify(Path(markdown_path).stem)


def relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def resolve_local_target(repo_root: Path, source_file: str, target: str) -> Path:
    target_without_fragment = target.split("#", 1)[0].split("?", 1)[0]
    source_dir = (repo_root / source_file).parent
    return (source_dir / os.path.normpath(target_without_fragment)).resolve()
