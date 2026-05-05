from dataclasses import dataclass


@dataclass(frozen=True)
class RebuildSummary:
    source_pages: int
    rendered_pages: int
    rewritten_links: int


@dataclass(frozen=True)
class SourcePage:
    source_id: str
    title: str
    source_url: str
    slug: str
    section_hint: str
    content_text: str
    links: tuple[str, ...]
    content_markdown: str = ""
    parent_id: str = ""
    menu_order: int = 0
    source_index: int = 0


@dataclass(frozen=True)
class RebuildInventory:
    pages: tuple[SourcePage, ...]
    attachments: tuple[str, ...]


@dataclass(frozen=True)
class Classification:
    top_bar: str
    subsection: str
    reason: str


@dataclass(frozen=True)
class DestinationPage:
    source_id: str
    source_url: str
    path: str
    title: str
    top_bar: str
    subsection: str
    slug: str
    parent_source_id: str = ""
    menu_order: int = 0
    source_index: int = 0


@dataclass(frozen=True)
class LinkRewrite:
    source_page: str
    original_url: str
    rewritten_url: str
    status: str
