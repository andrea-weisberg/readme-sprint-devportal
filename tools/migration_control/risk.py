"""Launch risk queue generation."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple

from .matching import mapped_wordpress_paths
from .models import ParityRow, ReadMeInventory, ReadMePage, RiskItem, WordPressExport
from .paths import normalize_path, resolve_local_target


MUST_KEEP_SECTIONS = (
    "Getting Started",
    "profile-api-reference",
    "companion-api",
    "card-api",
    "NOTIFICATIONS",
    "tools",
)

ASSET_EXTENSIONS = {".csv", ".doc", ".docx", ".gif", ".jpeg", ".jpg", ".pdf", ".png", ".svg", ".xls", ".xlsx"}


def generate_risk_queue(
    repo_root: Path,
    wordpress_export: WordPressExport,
    readme_inventory: ReadMeInventory,
    parity_rows: Sequence[ParityRow],
    review_risks: Dict[str, str],
) -> Tuple[RiskItem, ...]:
    risks: List[RiskItem] = []

    risks.extend(_must_keep_section_risks(readme_inventory))
    risks.extend(_parity_risks(parity_rows))
    risks.extend(_readme_page_risks(repo_root, readme_inventory.pages, parity_rows))
    risks.extend(_manual_review_risks(review_risks))

    return tuple(sorted(_dedupe(risks), key=lambda risk: (risk.priority, risk.category, risk.file_or_source, risk.message)))


def _must_keep_section_risks(readme_inventory: ReadMeInventory) -> Iterable[RiskItem]:
    present = {_top_level(page.path) for page in readme_inventory.pages}
    order_present = set(readme_inventory.order_entries)

    for section in MUST_KEEP_SECTIONS:
        if section not in present and section not in order_present:
            yield RiskItem(
                priority=0,
                category="missing_must_keep_section",
                file_or_source=section,
                message=f"Must-keep section is absent from docs and navigation: {section}",
                evidence=section,
                recommended_action="Add or restore the section before launch.",
            )


def _parity_risks(parity_rows: Sequence[ParityRow]) -> Iterable[RiskItem]:
    for row in parity_rows:
        if row.migration_status == "missing":
            yield RiskItem(
                priority=0,
                category="missing_page",
                file_or_source=row.wp_url,
                message=f"Published WordPress page has no ReadMe match: {row.wp_title}",
                evidence=row.notes,
                recommended_action="Create or map the equivalent ReadMe page.",
            )
        elif row.migration_status == "duplicate":
            yield RiskItem(
                priority=0,
                category="duplicate_match",
                file_or_source=row.wp_url,
                message=f"Published WordPress page matched multiple ReadMe candidates: {row.wp_title}",
                evidence=row.notes,
                recommended_action="Choose the canonical ReadMe destination and update matching data.",
            )
        elif row.migration_status == "needs-review":
            yield RiskItem(
                priority=1,
                category="low_confidence_match",
                file_or_source=row.wp_url,
                message=f"Published WordPress page matched with low confidence: {row.wp_title}",
                evidence=f"{row.match_kind} confidence {row.match_confidence}",
                recommended_action="Review the match and confirm or remap the destination.",
            )


def _readme_page_risks(
    repo_root: Path,
    pages: Sequence[ReadMePage],
    parity_rows: Sequence[ParityRow],
) -> Iterable[RiskItem]:
    mapped_paths = mapped_wordpress_paths(parity_rows)

    for page in pages:
        for link in page.legacy_wordpress_links:
            normalized = normalize_path(link)
            if normalized in mapped_paths:
                yield RiskItem(
                    priority=1,
                    category="rewriteable_legacy_link",
                    file_or_source=page.path,
                    message="Legacy WordPress link can be rewritten to a mapped ReadMe destination.",
                    evidence=link,
                    recommended_action=f"Rewrite to target represented by {mapped_paths[normalized]}.",
                )
            else:
                yield RiskItem(
                    priority=0,
                    category="unmapped_legacy_link",
                    file_or_source=page.path,
                    message="Legacy WordPress link has no mapped ReadMe target.",
                    evidence=link,
                    recommended_action="Map the target page or keep the link only with an explicit launch waiver.",
                )

        for image in page.images:
            if _is_local_asset(image) and not resolve_local_target(repo_root, page.path, image).exists():
                yield RiskItem(
                    priority=0,
                    category="missing_asset",
                    file_or_source=page.path,
                    message="Referenced local asset is missing from the repository.",
                    evidence=image,
                    recommended_action="Restore the asset or update the page to a valid asset path.",
                )

        if "ICON_URL" in page.content_text:
            yield RiskItem(
                priority=1,
                category="icon_token",
                file_or_source=page.path,
                message="ReadMe page contains unresolved icon token text.",
                evidence="ICON_URL",
                recommended_action="Replace with a real asset reference or remove the broken visual token.",
            )

        if re.search(r"^image\.\s*$", page.content_text, re.MULTILINE):
            yield RiskItem(
                priority=1,
                category="image_token",
                file_or_source=page.path,
                message="ReadMe page contains a literal image token line.",
                evidence="image.",
                recommended_action="Replace with the intended image or remove the orphaned text.",
            )

        if "```,```" in page.content_text or re.search(r"```,```\w+", page.content_text):
            yield RiskItem(
                priority=1,
                category="malformed_code_fence",
                file_or_source=page.path,
                message="ReadMe page contains adjacent malformed code fences.",
                evidence="```,```",
                recommended_action="Split the fences into valid Markdown code blocks after checking rendered examples.",
            )


def _manual_review_risks(review_risks: Dict[str, str]) -> Iterable[RiskItem]:
    for path, level in review_risks.items():
        priority = 1 if level == "high" else 2
        yield RiskItem(
            priority=priority,
            category="manual_review",
            file_or_source=path,
            message=f"Existing v1.0_codex review marks this page as {level} risk.",
            evidence=level,
            recommended_action="Review against WordPress source content and record approval or required fixes.",
        )


def _top_level(path: str) -> str:
    parts = Path(path).parts
    if len(parts) >= 2 and parts[0] == "docs":
        return parts[1]
    return ""


def _is_local_asset(target: str) -> bool:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return False
    suffix = Path(target.split("#", 1)[0].split("?", 1)[0]).suffix.lower()
    return suffix in ASSET_EXTENSIONS


def _dedupe(risks: Iterable[RiskItem]) -> List[RiskItem]:
    seen: Set[Tuple[int, str, str, str, str]] = set()
    deduped: List[RiskItem] = []
    for risk in risks:
        key = (risk.priority, risk.category, risk.file_or_source, risk.message, risk.evidence)
        if key not in seen:
            deduped.append(risk)
            seen.add(key)
    return deduped
