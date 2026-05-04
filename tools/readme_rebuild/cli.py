"""Command-line entrypoint for the ReadMe rebuild pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence

from tools.readme_rebuild.audit import write_audit
from tools.readme_rebuild.inventory import build_inventory
from tools.readme_rebuild.links import rewrite_links
from tools.readme_rebuild.mapping import map_page
from tools.readme_rebuild.rdme_export import export_rdme_source
from tools.readme_rebuild.render import render_site


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build a staging ReadMe site from the Sprint WordPress XML export."
    )
    parser.add_argument("--wordpress-export", required=True, type=Path)
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--report-root", required=True, type=Path)
    parser.add_argument("--rdme-output-root", type=Path)
    args = parser.parse_args(argv)

    inventory = build_inventory(args.wordpress_export, args.repo_root)
    mapped_pages = tuple(map_page(page) for page in inventory.pages)
    destinations_by_source = {
        destination.source_url: destination for destination in mapped_pages
    }
    content_by_path = {}
    link_rewrites = []

    for page, destination in zip(inventory.pages, mapped_pages):
        rewritten_content, page_rewrites = rewrite_links(page, destinations_by_source)
        content_by_path[destination.path] = _render_page_content(
            destination.title, rewritten_content
        )
        link_rewrites.extend(page_rewrites)

    render_site(args.output_root, mapped_pages, content_by_path)
    summary = write_audit(args.report_root, mapped_pages, tuple(link_rewrites))
    if args.rdme_output_root:
        export_rdme_source(args.rdme_output_root, mapped_pages, content_by_path)
    print(
        "\n".join(
            tuple(
                line
                for line in (
                    f"Source pages: {summary.source_pages}",
                    f"Rendered pages: {summary.rendered_pages}",
                    f"Rewritten links: {summary.rewritten_links}",
                    f"Staging site: {args.output_root}",
                    f"Audit reports: {args.report_root}",
                    (
                        f"ReadMe upload source: {args.rdme_output_root}"
                        if args.rdme_output_root
                        else ""
                    ),
                )
                if line
            )
        )
    )
    return 0


def _render_page_content(title: str, body: str) -> str:
    normalized_body = body.strip()
    if not normalized_body:
        return f"# {title}\n"
    return f"# {title}\n\n{normalized_body}\n"


if __name__ == "__main__":
    raise SystemExit(main())
