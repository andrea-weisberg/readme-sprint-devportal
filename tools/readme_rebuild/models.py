from dataclasses import dataclass


@dataclass(frozen=True)
class RebuildSummary:
    source_pages: int
    rendered_pages: int
    rewritten_links: int
