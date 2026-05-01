from __future__ import annotations

from tools.readme_rebuild.models import DestinationPage, LinkRewrite, SourcePage


def rewrite_links(
    page: SourcePage, destinations: dict[str, DestinationPage]
) -> tuple[str, tuple[LinkRewrite, ...]]:
    rewritten = page.content_markdown or page.content_text
    rows = []

    for link in page.links:
        destination = destinations.get(link)
        if not destination:
            continue
        new_url = "/" + (
            destination.path.replace(".md", "")
            .replace("API Reference", "api-reference")
            .replace("Guides", "guides")
            .replace("Reports", "reports")
            .replace("Tools", "tools")
        )
        rewritten = rewritten.replace(link, new_url)
        rows.append(LinkRewrite(page.source_url, link, new_url, "rewritten"))

    return rewritten, tuple(rows)
