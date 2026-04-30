"""Command-line entrypoint for the ReadMe rebuild pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence

from tools.readme_rebuild.inventory import build_inventory
from tools.readme_rebuild.mapping import map_page
from tools.readme_rebuild.render import render_site


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build a staging ReadMe site from the Sprint WordPress XML export."
    )
    parser.add_argument("--wordpress-export", required=True, type=Path)
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--report-root", required=True, type=Path)
    args = parser.parse_args(argv)

    inventory = build_inventory(args.wordpress_export, args.repo_root)
    mapped_pages = tuple(map_page(page) for page in inventory.pages)
    content_by_path = {
        destination.path: f"# {destination.title}\n" for destination in mapped_pages
    }

    render_site(args.output_root, mapped_pages, content_by_path)
    print(f"Rendered staging site: {args.output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
