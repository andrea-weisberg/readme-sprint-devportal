"""Report writers for migration control outputs."""

from __future__ import annotations

import csv
from collections import Counter
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterable, Sequence, Type

from .models import ParityRow, ReadMeInventory, RiskItem, WordPressExport


def write_reports(
    output_dir: Path,
    wordpress_export: WordPressExport,
    readme_inventory: ReadMeInventory,
    parity_rows: Sequence[ParityRow],
    risks: Sequence[RiskItem],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    _write_wordpress_inventory(output_dir / "wordpress_inventory.csv", wordpress_export)
    _write_wordpress_attachments(output_dir / "wordpress_attachments.csv", wordpress_export)
    _write_readme_inventory(output_dir / "readme_inventory.csv", readme_inventory)
    _write_readme_assets(output_dir / "readme_assets.csv", readme_inventory)
    _write_readme_order_entries(output_dir / "readme_order_entries.csv", readme_inventory)
    _write_dataclass_csv(output_dir / "parity_map.csv", parity_rows, ParityRow)
    _write_dataclass_csv(output_dir / "risk_queue.csv", risks, RiskItem)
    _write_summary(output_dir / "summary.md", wordpress_export, readme_inventory, parity_rows, risks)


def _write_wordpress_inventory(path: Path, export: WordPressExport) -> None:
    fieldnames = [
        "source_id",
        "title",
        "slug",
        "status",
        "url",
        "parent_id",
        "menu_order",
        "content_chars",
        "acf_key_count",
        "acf_keys",
        "link_count",
        "links",
    ]
    rows = [
        {
            "source_id": page.source_id,
            "title": page.title,
            "slug": page.slug,
            "status": page.status,
            "url": page.url,
            "parent_id": page.parent_id,
            "menu_order": page.menu_order,
            "content_chars": page.content_chars,
            "acf_key_count": len(page.acf_keys),
            "acf_keys": _join_values(page.acf_keys),
            "link_count": len(page.links),
            "links": _join_values(page.links),
        }
        for page in export.pages
    ]
    _write_csv(path, fieldnames, rows)


def _write_wordpress_attachments(path: Path, export: WordPressExport) -> None:
    fieldnames = ["source_id", "title", "url", "filename", "mime_type"]
    rows = [
        {
            "source_id": attachment.source_id,
            "title": attachment.title,
            "url": attachment.url,
            "filename": attachment.filename,
            "mime_type": attachment.mime_type,
        }
        for attachment in export.attachments
    ]
    _write_csv(path, fieldnames, rows)


def _write_readme_inventory(path: Path, inventory: ReadMeInventory) -> None:
    fieldnames = [
        "path",
        "title",
        "slug",
        "content_chars",
        "link_count",
        "links",
        "image_count",
        "images",
        "legacy_wordpress_link_count",
        "legacy_wordpress_links",
    ]
    rows = [
        {
            "path": page.path,
            "title": page.title,
            "slug": page.slug,
            "content_chars": page.content_chars,
            "link_count": len(page.links),
            "links": _join_values(page.links),
            "image_count": len(page.images),
            "images": _join_values(page.images),
            "legacy_wordpress_link_count": len(page.legacy_wordpress_links),
            "legacy_wordpress_links": _join_values(page.legacy_wordpress_links),
        }
        for page in inventory.pages
    ]
    _write_csv(path, fieldnames, rows)


def _write_readme_assets(path: Path, inventory: ReadMeInventory) -> None:
    _write_csv(path, ["path"], [{"path": asset} for asset in inventory.assets])


def _write_readme_order_entries(path: Path, inventory: ReadMeInventory) -> None:
    _write_csv(path, ["entry"], [{"entry": entry} for entry in inventory.order_entries])


def _write_dataclass_csv(path: Path, rows: Sequence[object], row_type: Type[Any]) -> None:
    fieldnames = list(row_type.__dataclass_fields__.keys())
    dict_rows = [asdict(row) for row in rows]
    _write_csv(path, fieldnames, dict_rows)


def _write_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _write_summary(
    path: Path,
    export: WordPressExport,
    inventory: ReadMeInventory,
    parity_rows: Sequence[ParityRow],
    risks: Sequence[RiskItem],
) -> None:
    status_counts = Counter(row.migration_status for row in parity_rows)
    priority_counts = Counter(risk.priority for risk in risks)
    published_pages = sum(1 for page in export.pages if page.launch_scope)
    non_public_pages = len(export.pages) - published_pages

    lines = [
        "# Migration Control Summary",
        "",
        "## Inventory",
        "",
        f"- WordPress published pages: {published_pages}",
        f"- WordPress non-public pages: {non_public_pages}",
        f"- WordPress attachments: {len(export.attachments)}",
        f"- ReadMe Markdown pages: {len(inventory.pages)}",
        f"- ReadMe assets: {len(inventory.assets)}",
        "",
        "## Parity Status",
        "",
    ]

    for status in ("matched", "needs-review", "missing", "duplicate", "out-of-scope"):
        lines.append(f"- {status}: {status_counts.get(status, 0)}")

    lines.extend(["", "## Risk Queue", ""])
    for priority in (0, 1, 2):
        lines.append(f"- P{priority}: {priority_counts.get(priority, 0)}")

    lines.extend(
        [
            "",
            "## Generated Files",
            "",
            "- `wordpress_inventory.csv`",
            "- `wordpress_attachments.csv`",
            "- `readme_inventory.csv`",
            "- `readme_assets.csv`",
            "- `readme_order_entries.csv`",
            "- `parity_map.csv`",
            "- `risk_queue.csv`",
        ]
    )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _join_values(values: Sequence[str]) -> str:
    return " | ".join(values)
