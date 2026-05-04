from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import shutil

from tools.migration_control.paths import slugify
from tools.readme_rebuild.models import DestinationPage

SLUG_OVERRIDES = {
    "Guides/companion-api.md": "companion-api-guide",
}


@dataclass(frozen=True)
class RdmeExportManifest:
    docs_count: int
    reference_count: int
    guide_categories: tuple[str, ...]
    reference_categories: tuple[str, ...]


def export_rdme_source(
    output_root: Path,
    pages: tuple[DestinationPage, ...],
    content_by_path: dict[str, str],
) -> RdmeExportManifest:
    shutil.rmtree(output_root, ignore_errors=True)
    docs_count = 0
    reference_count = 0
    guide_categories: set[str] = set()
    reference_categories: set[str] = set()
    ordered_pages = _sorted_pages(pages)
    pages_by_bucket = _group_pages_by_bucket(ordered_pages)
    parent_slugs = _parent_slugs_by_bucket(pages_by_bucket)

    for bucket, bucket_pages in pages_by_bucket.items():
        for position, page in enumerate(bucket_pages, start=1):
            export_path = output_root / _relative_export_path(page)
            export_path.parent.mkdir(parents=True, exist_ok=True)

            category_title = _category_title_for_page(page)
            body = _sanitize_body_for_rdme(
                _strip_leading_title(content_by_path[page.path], page.title)
            )
            frontmatter = _build_frontmatter(
                title=page.title,
                category_title=category_title,
                slug=_slug_for_export(page),
                position=position,
                parent_slug=_parent_slug_for_page(page, parent_slugs.get(bucket)),
            )
            export_path.write_text(f"{frontmatter}\n\n{body}", encoding="utf-8")

            if page.top_bar == "API Reference":
                reference_count += 1
                reference_categories.add(category_title)
            else:
                docs_count += 1
                guide_categories.add(category_title)

    return RdmeExportManifest(
        docs_count=docs_count,
        reference_count=reference_count,
        guide_categories=tuple(sorted(guide_categories)),
        reference_categories=tuple(sorted(reference_categories)),
    )


def _sorted_pages(pages: tuple[DestinationPage, ...]) -> tuple[DestinationPage, ...]:
    return tuple(sorted(pages, key=lambda page: (page.path.count("/"), page.path)))


def _group_pages_by_bucket(
    pages: tuple[DestinationPage, ...],
) -> dict[tuple[str, str], list[DestinationPage]]:
    grouped: dict[tuple[str, str], list[DestinationPage]] = defaultdict(list)
    for page in pages:
        grouped[_bucket_for_page(page)].append(page)

    for bucket_pages in grouped.values():
        bucket_pages.sort(key=_bucket_page_sort_key)

    return grouped


def _bucket_for_page(page: DestinationPage) -> tuple[str, str]:
    if page.top_bar == "API Reference":
        return ("reference", page.subsection)
    if page.top_bar == "Reports":
        return ("docs", "Reports")
    if page.top_bar == "Tools":
        return ("docs", "Tools")
    return ("docs", "Guides")


def _relative_export_path(page: DestinationPage) -> Path:
    path = Path(page.path)
    top = path.parts[0]

    if top == "API Reference":
        return Path("reference", path.parts[1], path.name)
    if top == "Reports":
        return Path("docs", "reports", slugify(page.subsection), path.name)
    if top == "Tools":
        return Path("docs", "tools", path.name)
    return Path("docs", "guides", path.name)


def _category_title_for_page(page: DestinationPage) -> str:
    if page.top_bar == "API Reference":
        return page.subsection
    if page.top_bar == "Reports":
        return "Reports"
    if page.top_bar == "Tools":
        return "Tools"
    return "Guides"


def _slug_for_export(page: DestinationPage) -> str:
    if page.top_bar == "Reports":
        subsection_slug = slugify(page.subsection)
        if page.slug == "reports":
            return f"{subsection_slug}-reports"
        return f"{subsection_slug}-{page.slug}"
    return SLUG_OVERRIDES.get(page.path, page.slug)


def _parent_slugs_by_bucket(
    pages_by_bucket: dict[tuple[str, str], list[DestinationPage]]
) -> dict[tuple[str, str], str]:
    parent_slugs: dict[tuple[str, str], str] = {}

    for bucket, pages in pages_by_bucket.items():
        for page in pages:
            if page.slug in {"api-reference", "reports", "tools"}:
                parent_slugs[bucket] = _slug_for_export(page)
                break

    return parent_slugs


def _bucket_page_sort_key(page: DestinationPage) -> tuple[int, str]:
    priority = 0 if page.slug in {"api-reference", "reports", "tools"} else 1
    return (priority, page.path)


def _parent_slug_for_page(page: DestinationPage, parent_slug: str | None) -> str | None:
    if not parent_slug or _slug_for_export(page) == parent_slug:
        return None
    return parent_slug


def _strip_leading_title(content: str, title: str) -> str:
    lines = content.splitlines()
    heading = f"# {title}".strip()

    if lines and lines[0].strip() == heading:
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]

    body = "\n".join(lines).rstrip()
    return f"{body}\n" if body else ""


def _build_frontmatter(
    *,
    title: str,
    category_title: str,
    slug: str,
    position: int,
    parent_slug: str | None,
) -> str:
    lines = [
        "---",
        f"title: {_yaml_string(title)}",
        "category:",
        f"  uri: {_yaml_string(category_title)}",
        f"slug: {slug}",
        f"position: {position}",
    ]

    if parent_slug:
        lines.extend(
            (
                "parent:",
                f"  uri: {parent_slug}",
            )
        )

    lines.append("---")
    return "\n".join(lines)


def _yaml_string(value: str) -> str:
    if value == "":
        return '""'
    if any(character in value for character in ':#[]{}&*!|>\'"%@`"') or value != value.strip():
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return value


def _sanitize_body_for_rdme(body: str) -> str:
    sanitized = body.replace("![", "\n\n![")
    sanitized = re.sub(r"\n{3,}", "\n\n", sanitized)
    sanitized = _wrap_xml_blocks(sanitized)
    return sanitized


def _wrap_xml_blocks(body: str) -> str:
    lines = body.splitlines()
    output: list[str] = []
    buffer: list[str] = []

    def flush_buffer() -> None:
        nonlocal buffer
        if not buffer:
            return
        output.append("```xml")
        output.extend(buffer)
        output.append("```")
        buffer = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("<?xml") or stripped.startswith("<methodCall>") or stripped.startswith("<methodResponse>"):
            buffer.append(line)
            continue
        if buffer and stripped.startswith("<"):
            buffer.append(line)
            continue
        flush_buffer()
        output.append(line)

    flush_buffer()
    rendered = "\n".join(output).rstrip()
    return f"{rendered}\n" if rendered else ""
