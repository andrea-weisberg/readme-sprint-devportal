"""Shared data models for migration control reports."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class WordPressPage:
    source_id: str
    title: str
    slug: str
    status: str
    url: str
    parent_id: str
    menu_order: int
    content_chars: int
    content_text: str
    acf_keys: Tuple[str, ...]
    links: Tuple[str, ...]
    post_type: str = "page"

    @property
    def launch_scope(self) -> bool:
        return self.post_type == "page" and self.status == "publish"


@dataclass(frozen=True)
class WordPressAttachment:
    source_id: str
    title: str
    url: str
    filename: str
    mime_type: str


@dataclass(frozen=True)
class WordPressExport:
    pages: Tuple[WordPressPage, ...]
    attachments: Tuple[WordPressAttachment, ...]


@dataclass(frozen=True)
class ReadMePage:
    path: str
    title: str
    slug: str
    content_chars: int
    content_text: str
    links: Tuple[str, ...]
    images: Tuple[str, ...]
    legacy_wordpress_links: Tuple[str, ...]
    migrated_from: str = ""


@dataclass(frozen=True)
class ReadMeInventory:
    pages: Tuple[ReadMePage, ...]
    assets: Tuple[str, ...]
    order_entries: Tuple[str, ...]


@dataclass(frozen=True)
class ParityRow:
    wp_id: str
    wp_title: str
    wp_url: str
    wp_slug: str
    wp_status: str
    matched_path: str
    match_kind: str
    match_confidence: float
    migration_status: str
    review_risk: str
    notes: str


@dataclass(frozen=True)
class RiskItem:
    priority: int
    category: str
    file_or_source: str
    message: str
    evidence: str
    recommended_action: str
