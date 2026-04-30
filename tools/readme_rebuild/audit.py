from __future__ import annotations

import csv
from pathlib import Path

from tools.readme_rebuild.models import DestinationPage, LinkRewrite, RebuildSummary


def write_audit(
    report_root: Path,
    pages: tuple[DestinationPage, ...],
    link_rewrites: tuple[LinkRewrite, ...],
) -> RebuildSummary:
    report_root.mkdir(parents=True, exist_ok=True)

    _write_page_mapping(report_root / "page_mapping.csv", pages)
    _write_link_rewrites(report_root / "link_rewrites.csv", link_rewrites)

    summary = RebuildSummary(
        source_pages=len(pages),
        rendered_pages=len(pages),
        rewritten_links=len(link_rewrites),
    )
    _write_summary(report_root / "summary.md", summary)
    return summary


def _write_page_mapping(path: Path, pages: tuple[DestinationPage, ...]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["source_url", "top_bar", "subsection", "title", "destination_path"]
        )
        for page in sorted(pages, key=lambda item: item.source_url):
            writer.writerow(
                [
                    page.source_url,
                    page.top_bar,
                    page.subsection,
                    page.title,
                    page.path,
                ]
            )


def _write_link_rewrites(path: Path, link_rewrites: tuple[LinkRewrite, ...]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["source_page", "original_url", "rewritten_url", "status"])
        for rewrite in sorted(
            link_rewrites, key=lambda item: (item.source_page, item.original_url)
        ):
            writer.writerow(
                [
                    rewrite.source_page,
                    rewrite.original_url,
                    rewrite.rewritten_url,
                    rewrite.status,
                ]
            )


def _write_summary(path: Path, summary: RebuildSummary) -> None:
    path.write_text(
        "# ReadMe Rebuild Summary\n\n"
        f"- Source pages: {summary.source_pages}\n"
        f"- Rendered pages: {summary.rendered_pages}\n"
        f"- Rewritten links: {summary.rewritten_links}\n",
        encoding="utf-8",
    )
