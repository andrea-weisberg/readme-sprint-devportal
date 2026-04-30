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
    source_url: str
    path: str
    title: str
    top_bar: str
    subsection: str
    slug: str


@dataclass(frozen=True)
class LinkRewrite:
    source_page: str
    original_url: str
    rewritten_url: str
    status: str
