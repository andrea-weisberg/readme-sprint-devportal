"""Parser for the existing v1.0_codex review report."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict


RISK_HEADING_RE = re.compile(r"^###\s+(High|Medium|Low)\s+Risk", re.IGNORECASE)
PATH_RE = re.compile(r"^-\s+`([^`]+)`")


def parse_review_report(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}

    risks: Dict[str, str] = {}
    current_level = ""

    for line in path.read_text(encoding="utf-8").splitlines():
        heading = RISK_HEADING_RE.match(line)
        if heading:
            current_level = heading.group(1).lower()
            continue

        match = PATH_RE.match(line)
        if current_level and match:
            risks[match.group(1)] = current_level

    return risks
