"""Command-line entrypoint for migration control report generation."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence

from .matching import build_parity_map
from .readme_repo import scan_readme_repo
from .review_report import parse_review_report
from .risk import generate_risk_queue
from .writers import write_reports
from .wxr import parse_wxr


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Sprint developer portal migration control reports.")
    parser.add_argument("--wordpress-export", required=True, type=Path, help="Path to the WordPress WXR XML export.")
    parser.add_argument("--readme-root", required=True, type=Path, help="Path to the ReadMe repository root.")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory where reports will be written.")
    parser.add_argument(
        "--review-report",
        type=Path,
        default=None,
        help="Path to an existing review report. Defaults to review/review_report_2026-02-16.md under the ReadMe root.",
    )
    args = parser.parse_args(argv)

    review_report = args.review_report or args.readme_root / "review" / "review_report_2026-02-16.md"

    wordpress_export = parse_wxr(args.wordpress_export)
    readme_inventory = scan_readme_repo(args.readme_root)
    review_risks = parse_review_report(review_report)
    parity_rows = build_parity_map(wordpress_export, readme_inventory, review_risks)
    risks = generate_risk_queue(args.readme_root, wordpress_export, readme_inventory, parity_rows, review_risks)

    write_reports(args.output_dir, wordpress_export, readme_inventory, parity_rows, risks)

    published_pages = sum(1 for page in wordpress_export.pages if page.launch_scope)
    non_public_pages = len(wordpress_export.pages) - published_pages
    print(
        f"Parsed WordPress: {published_pages} published pages, "
        f"{non_public_pages} non-public pages, {len(wordpress_export.attachments)} attachments"
    )
    print(f"Scanned ReadMe: {len(readme_inventory.pages)} markdown files, {len(readme_inventory.assets)} assets")
    print(f"Generated parity rows: {len(parity_rows)}")
    print(f"Generated risk items: {len(risks)}")
    print(f"Wrote {args.output_dir / 'summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
