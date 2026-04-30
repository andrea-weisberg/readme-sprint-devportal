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
