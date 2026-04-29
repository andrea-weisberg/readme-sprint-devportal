"""Phase 2 hardening helpers for migrated ReadMe docs."""

from __future__ import annotations

import argparse
import csv
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse

from .paths import normalize_path


RECOMMENDED_TARGET_RE = re.compile(r"Rewrite to target represented by (.+)\.$")
ADJACENT_FENCE_RE = re.compile(r"```,```([A-Za-z0-9_-]*)")


@dataclass(frozen=True)
class HardeningResult:
    rewritten_links: int
    fixed_fences: int
    files_changed: int


@dataclass(frozen=True)
class _Replacement:
    source_file: str
    legacy_url: str
    target_path: str


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Apply Phase 2 migration hardening to ReadMe docs.")
    parser.add_argument("--repo-root", required=True, type=Path, help="Path to the ReadMe repository root.")
    parser.add_argument("--risk-queue", required=True, type=Path, help="Path to the generated risk_queue.csv file.")
    parser.add_argument("--parity-map", required=True, type=Path, help="Path to the generated parity_map.csv file.")
    args = parser.parse_args(argv)

    result = apply_hardening(args.repo_root, args.risk_queue, args.parity_map)
    print(f"Rewritten legacy links: {result.rewritten_links}")
    print(f"Fixed malformed fences: {result.fixed_fences}")
    print(f"Files changed: {result.files_changed}")
    return 0


def apply_hardening(repo_root: Path, risk_queue_path: Path, parity_map_path: Path) -> HardeningResult:
    replacements = _safe_replacements(risk_queue_path, parity_map_path)
    rewrite_groups: Dict[str, List[_Replacement]] = {}
    for replacement in replacements:
        rewrite_groups.setdefault(replacement.source_file, []).append(replacement)

    fence_files = tuple(_fence_files(risk_queue_path))
    candidate_files = sorted(set(rewrite_groups) | set(fence_files))

    rewritten_links = 0
    fixed_fences = 0
    files_changed = 0

    for relative_path in candidate_files:
        source_path = repo_root / relative_path
        original = source_path.read_text(encoding="utf-8")
        updated = original

        for replacement in sorted(rewrite_groups.get(relative_path, ()), key=lambda item: len(item.legacy_url), reverse=True):
            target = _relative_doc_link(relative_path, replacement.target_path, replacement.legacy_url)
            if replacement.legacy_url in updated:
                updated = updated.replace(replacement.legacy_url, target)
                rewritten_links += 1

        updated, file_fence_fixes = _fix_adjacent_fences(updated)
        fixed_fences += file_fence_fixes

        if updated != original:
            source_path.write_text(updated, encoding="utf-8")
            files_changed += 1

    return HardeningResult(
        rewritten_links=rewritten_links,
        fixed_fences=fixed_fences,
        files_changed=files_changed,
    )


def _safe_replacements(risk_queue_path: Path, parity_map_path: Path) -> Tuple[_Replacement, ...]:
    safe_paths = _safe_wordpress_paths(parity_map_path)
    replacements: List[_Replacement] = []

    with risk_queue_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["category"] != "rewriteable_legacy_link":
                continue

            normalized = normalize_path(row["evidence"])
            if normalized not in safe_paths:
                continue

            target = _recommended_target(row["recommended_action"])
            if not target:
                continue

            replacements.append(
                _Replacement(
                    source_file=row["file_or_source"],
                    legacy_url=row["evidence"],
                    target_path=target,
                )
            )

    return tuple(replacements)


def _safe_wordpress_paths(parity_map_path: Path) -> set[str]:
    safe_paths: set[str] = set()
    with parity_map_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["migration_status"] != "matched":
                continue
            if row["match_kind"] != "url_path":
                continue
            if row["match_confidence"] != "1.0":
                continue
            if row["review_risk"].strip():
                continue
            safe_paths.add(normalize_path(row["wp_url"]))
    return safe_paths


def _fence_files(risk_queue_path: Path) -> Iterable[str]:
    with risk_queue_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["category"] == "malformed_code_fence":
                yield row["file_or_source"]


def _recommended_target(recommended_action: str) -> str:
    match = RECOMMENDED_TARGET_RE.search(recommended_action)
    if not match:
        return ""
    return match.group(1)


def _relative_doc_link(source_file: str, target_path: str, legacy_url: str) -> str:
    source_dir = (Path("/") / source_file).parent
    target_file = Path("/") / target_path
    relative = os.path.relpath(target_file, start=source_dir).replace(os.sep, "/")
    fragment = urlparse(legacy_url).fragment

    if relative.endswith("/index.md"):
        relative = relative[: -len("/index.md")]
    elif relative == "index.md":
        relative = "."
    elif relative.endswith(".md"):
        relative = relative[:-3]

    if fragment:
        relative = f"{relative}#{fragment}"
    return relative


def _fix_adjacent_fences(text: str) -> Tuple[str, int]:
    replacements = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replacements
        replacements += 1
        language = match.group(1)
        if language:
            return f"```\n\n```{language}"
        return "```\n\n```"

    return ADJACENT_FENCE_RE.sub(replace, text), replacements


if __name__ == "__main__":
    raise SystemExit(main())
