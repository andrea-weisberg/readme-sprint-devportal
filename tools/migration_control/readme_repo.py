"""ReadMe repository scanner."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple

from .models import ReadMeInventory, ReadMePage
from .paths import clean_text, filename_slug, relative_posix


MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"""href=["']([^"']+)["']""", re.IGNORECASE)
HTML_IMAGE_RE = re.compile(r"""src=["']([^"']+)["']""", re.IGNORECASE)
ORDER_RE = re.compile(r"^\s*-\s+(.+?)\s*$")
MIGRATED_FROM_RE = re.compile(r"^\s*Migrated-From:\s*(\S.*?)\s*$", re.MULTILINE)
LEGACY_HOST = "developer.sprint.paymentology.com"
INTERNAL_DOC_DIRS = {"superpowers"}


def scan_readme_repo(repo_root: Path) -> ReadMeInventory:
    docs_root = repo_root / "docs"
    pages = tuple(
        _scan_page(repo_root, path)
        for path in sorted(docs_root.rglob("*.md"))
        if _is_readme_doc(path, docs_root)
    )
    assets = tuple(
        sorted(relative_posix(path, repo_root) for path in (repo_root / "assets").rglob("*") if path.is_file())
    )
    order_entries = tuple(_scan_order_entries(docs_root))

    return ReadMeInventory(pages=pages, assets=assets, order_entries=order_entries)


def _is_readme_doc(path: Path, docs_root: Path) -> bool:
    rel_path = path.relative_to(docs_root)
    return not (rel_path.parts and rel_path.parts[0] in INTERNAL_DOC_DIRS)


def _scan_page(repo_root: Path, path: Path) -> ReadMePage:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = _parse_frontmatter(text)
    markdown_links = _clean_targets(MARKDOWN_LINK_RE.findall(body))
    html_links = _clean_targets(HTML_LINK_RE.findall(body))
    markdown_images = _clean_targets(MARKDOWN_IMAGE_RE.findall(body))
    html_images = _clean_targets(HTML_IMAGE_RE.findall(body))
    links = tuple(markdown_links + html_links)
    images = tuple(markdown_images + html_images)
    legacy_links = tuple(link for link in links if LEGACY_HOST in link)
    rel_path = relative_posix(path, repo_root)

    return ReadMePage(
        path=rel_path,
        title=frontmatter.get("title") or _first_heading(body) or path.stem.replace("-", " ").title(),
        slug=frontmatter.get("slug") or filename_slug(rel_path),
        content_chars=len(body),
        content_text=body,
        links=links,
        images=images,
        legacy_wordpress_links=legacy_links,
        migrated_from=_migrated_from(text),
    )


def _parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    block = text[4:end]
    body = text[end + 5 :]
    data: Dict[str, str] = {}

    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[clean_text(key)] = clean_text(value).strip('"\'')

    return data, body


def _first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return clean_text(line[2:])
    return ""


def _clean_targets(targets: List[str]) -> List[str]:
    cleaned: List[str] = []
    for target in targets:
        value = clean_text(target).strip("<>")
        if value and " " in value:
            value = value.split(" ", 1)[0]
        if value:
            cleaned.append(value)
    return cleaned


def _migrated_from(text: str) -> str:
    match = MIGRATED_FROM_RE.search(text)
    if not match:
        return ""
    return clean_text(match.group(1))


def _scan_order_entries(docs_root: Path) -> List[str]:
    entries: List[str] = []
    for order_file in sorted(docs_root.rglob("_order.yaml")):
        for line in order_file.read_text(encoding="utf-8").splitlines():
            match = ORDER_RE.match(line)
            if match:
                entries.append(match.group(1).strip('"\''))
    return entries
