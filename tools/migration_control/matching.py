"""Match WordPress export pages to ReadMe inventory pages."""

from __future__ import annotations

from collections import defaultdict
from pathlib import PurePosixPath
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

from .models import ParityRow, ReadMeInventory, ReadMePage, WordPressExport, WordPressPage
from .paths import filename_slug, normalize_path, readme_doc_key, slugify

CandidateIndex = Mapping[str, Sequence[ReadMePage]]


def build_parity_map(
    wordpress_export: WordPressExport,
    readme_inventory: ReadMeInventory,
    review_risks: Mapping[str, str],
) -> Tuple[ParityRow, ...]:
    """Return one parity row per launch-scope WordPress page."""

    indexes = _build_readme_indexes(readme_inventory.pages)
    rows = []

    for page in wordpress_export.pages:
        if not page.launch_scope:
            continue

        match_kind, confidence, matches = _find_matches(page, indexes)
        if len(matches) == 1:
            matched_page = matches[0]
            migration_status = "matched" if _is_confident_match(page, match_kind, confidence) else "needs-review"
            rows.append(
                _row(
                    page=page,
                    matched_path=matched_page.path,
                    match_kind=match_kind,
                    match_confidence=confidence,
                    migration_status=migration_status,
                    review_risk=review_risks.get(matched_page.path, ""),
                    notes="",
                )
            )
        elif len(matches) > 1:
            rows.append(
                _row(
                    page=page,
                    matched_path="",
                    match_kind=match_kind,
                    match_confidence=confidence,
                    migration_status="duplicate",
                    review_risk="high",
                    notes="Multiple ReadMe candidates: " + ", ".join(match.path for match in matches),
                )
            )
        else:
            rows.append(
                _row(
                    page=page,
                    matched_path="",
                    match_kind="",
                    match_confidence=0.0,
                    migration_status="missing",
                    review_risk="high",
                    notes="No ReadMe candidate matched URL path, slug, filename, or title.",
                )
            )

    return tuple(rows)


def mapped_wordpress_paths(rows: Iterable[ParityRow]) -> Dict[str, str]:
    """Map normalized WordPress URL paths and slugs to matched ReadMe paths."""

    mapped = {}
    for row in rows:
        if row.migration_status not in {"matched", "needs-review"}:
            continue

        wp_path = normalize_path(row.wp_url)
        wp_slug = normalize_path(row.wp_slug)
        if wp_path:
            mapped[wp_path] = row.matched_path
        if wp_slug and wp_slug == _leaf(wp_path):
            mapped[wp_slug] = row.matched_path

    return mapped


def _build_readme_indexes(pages: Sequence[ReadMePage]) -> Dict[str, CandidateIndex]:
    indexes = {
        "url_path": defaultdict(list),
        "slug": defaultdict(list),
        "url_leaf": defaultdict(list),
        "title": defaultdict(list),
    }

    for page in pages:
        _append_index(indexes["url_path"], readme_doc_key(page.path), page)
        _append_index(indexes["url_path"], normalize_path(page.migrated_from), page)
        _append_index(indexes["slug"], normalize_path(page.slug), page)
        _append_index(indexes["url_leaf"], filename_slug(page.path), page)
        _append_index(indexes["title"], slugify(page.title), page)

    return indexes


def _append_index(index: Dict[str, List[ReadMePage]], key: str, page: ReadMePage) -> None:
    if key and all(existing.path != page.path for existing in index[key]):
        index[key].append(page)


def _find_matches(
    page: WordPressPage,
    indexes: Mapping[str, CandidateIndex],
) -> Tuple[str, float, Tuple[ReadMePage, ...]]:
    duplicate_match: Tuple[str, float, Tuple[ReadMePage, ...]] = ("", 0.0, ())

    for kind, confidence, key in _wordpress_candidates(page):
        matches = tuple(indexes[kind].get(key, ()))
        if len(matches) == 1:
            title_key = slugify(page.title)
            title_matches = tuple(indexes["title"].get(title_key, ()))
            if kind == "url_leaf" and key == title_key and title_matches == matches:
                return "title", 0.75, title_matches
            return kind, confidence, matches
        if len(matches) > 1 and not duplicate_match[2]:
            duplicate_match = (kind, confidence, matches)

    if duplicate_match[2]:
        return duplicate_match

    return "", 0.0, ()


def _wordpress_candidates(page: WordPressPage) -> Tuple[Tuple[str, float, str], ...]:
    url_path = normalize_path(page.url)
    slug = normalize_path(page.slug)
    leaf = _leaf(url_path)
    title = slugify(page.title)

    candidates = [
        ("url_path", 1.0, url_path),
        ("url_leaf", 0.85, leaf),
    ]

    if slug == leaf:
        candidates.append(("slug", 0.9, slug))

    candidates.append(("title", 0.75, title))
    return tuple(candidates)


def _is_confident_match(page: WordPressPage, match_kind: str, confidence: float) -> bool:
    if confidence >= 0.8:
        return True

    url_path = normalize_path(page.url)
    leaf = _leaf(url_path)
    return match_kind == "title" and leaf == slugify(page.title) and leaf != normalize_path(page.slug)


def _leaf(path: str) -> str:
    return PurePosixPath(path).name if path else ""


def _row(
    page: WordPressPage,
    matched_path: str,
    match_kind: str,
    match_confidence: float,
    migration_status: str,
    review_risk: str,
    notes: str,
) -> ParityRow:
    return ParityRow(
        wp_id=page.source_id,
        wp_title=page.title,
        wp_url=page.url,
        wp_slug=page.slug,
        wp_status=page.status,
        matched_path=matched_path,
        match_kind=match_kind,
        match_confidence=match_confidence,
        migration_status=migration_status,
        review_risk=review_risk,
        notes=notes,
    )
