from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

from tools.migration_control.wxr import parse_wxr
from tools.readme_rebuild.models import RebuildInventory, SourcePage


def build_inventory(wordpress_export: Path, repo_root: Path) -> RebuildInventory:
    _ = repo_root  # Reserved for later tasks that blend XML inventory with reference-repo signals.

    export = parse_wxr(wordpress_export)
    pages = tuple(
        SourcePage(
            source_id=page.source_id,
            title=page.title,
            source_url=page.url,
            slug=page.slug,
            section_hint=_section_hint(page.url),
            content_text=page.content_text,
            links=page.links,
            content_markdown=page.content_markdown or page.content_text,
            parent_id=page.parent_id,
            menu_order=page.menu_order,
            source_index=index,
        )
        for index, page in enumerate(export.pages, start=1)
        if page.launch_scope
    )
    attachments = tuple(attachment.url for attachment in export.attachments)
    return RebuildInventory(pages=pages, attachments=attachments)


def _section_hint(source_url: str) -> str:
    return urlparse(source_url).path.lstrip("/")
