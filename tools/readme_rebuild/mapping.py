from __future__ import annotations

from tools.readme_rebuild.ia import classify_page
from tools.readme_rebuild.models import DestinationPage, SourcePage
from tools.migration_control.paths import slugify


def map_page(page: SourcePage) -> DestinationPage:
    classification = classify_page(page)
    section_slug = slugify(classification.subsection)
    slug = page.slug or slugify(page.title)

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
