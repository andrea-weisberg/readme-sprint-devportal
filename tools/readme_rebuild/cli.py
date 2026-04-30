"""Command-line entrypoint for the ReadMe rebuild pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build a staging ReadMe site from the Sprint WordPress XML export."
    )
    parser.add_argument("--wordpress-export", required=True, type=Path)
    parser.add_argument("--repo-root", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--report-root", required=True, type=Path)
    parser.parse_args(argv)
    raise NotImplementedError("Rebuild pipeline not implemented yet.")


if __name__ == "__main__":
    raise SystemExit(main())
