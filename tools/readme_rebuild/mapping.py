from __future__ import annotations

from tools.readme_rebuild.ia import classify_page
from tools.readme_rebuild.models import DestinationPage, SourcePage
from tools.migration_control.paths import slugify

CARD_API_GUIDE_COLLISION_SLUGS = {
    "disputes",
    "manage-cards",
    "manage-funds",
    "offline-pin",
    "secure-cards",
}


def map_page(page: SourcePage) -> DestinationPage:
    classification = classify_page(page)
    section_slug = slugify(classification.subsection)
    slug = _destination_slug(page, classification.top_bar)

    if classification.top_bar == "API Reference":
        path = f"API Reference/{section_slug}/{slug}.md"
    elif classification.top_bar == "Reports":
        path = f"Reports/{section_slug}/{slug}.md"
    elif classification.top_bar == "Tools":
        path = f"Tools/{slug}.md"
    else:
        path = f"Guides/{slug}.md"

    return DestinationPage(
        source_id=page.source_id,
        source_url=page.source_url,
        path=path,
        title=page.title,
        top_bar=classification.top_bar,
        subsection=classification.subsection,
        slug=slug,
        parent_source_id=page.parent_id,
        menu_order=page.menu_order,
        source_index=page.source_index,
    )


def _destination_slug(page: SourcePage, top_bar: str) -> str:
    slug = page.slug or slugify(page.title)
    url = page.source_url.lower()

    if top_bar == "Guides" and "/card-api/" in url and slug in CARD_API_GUIDE_COLLISION_SLUGS:
        return f"{slug}-card-api"

    if top_bar == "Tools" and slug == "help":
        parent_slug = _tool_parent_slug(url)
        if parent_slug:
            return f"{parent_slug}-help"

    return slug


def _tool_parent_slug(url: str) -> str:
    marker = "/tools/"
    if marker not in url:
        return ""
    remainder = url.split(marker, 1)[1].strip("/")
    parts = [part for part in remainder.split("/") if part]
    if len(parts) >= 2 and parts[-1] == "help":
        return slugify(parts[-2])
    return ""
