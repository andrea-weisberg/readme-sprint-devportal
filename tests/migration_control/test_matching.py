from unittest import TestCase

from tools.migration_control.matching import build_parity_map, mapped_wordpress_paths
from tools.migration_control.models import ReadMeInventory, ReadMePage, WordPressExport, WordPressPage


def wp_page(source_id, title, slug, url, status="publish"):
    return WordPressPage(
        source_id=source_id,
        title=title,
        slug=slug,
        status=status,
        url=url,
        parent_id="0",
        menu_order=0,
        content_chars=10,
        content_text="body",
        acf_keys=(),
        links=(),
    )


def readme_page(path, title, slug):
    return ReadMePage(
        path=path,
        title=title,
        slug=slug,
        content_chars=10,
        content_text="body",
        links=(),
        images=(),
        legacy_wordpress_links=(),
    )


class MatchingTests(TestCase):
    def test_build_parity_map_matches_by_url_slug_and_title(self):
        export = WordPressExport(
            pages=(
                wp_page("1", "Activate Card", "activate", "https://developer.sprint.paymentology.com/profile-api-reference/activate/"),
                wp_page("2", "Card Detail", "card-detail", "https://developer.sprint.paymentology.com/card-detail/"),
                wp_page("3", "Client Testing Guide", "client-testing", "https://developer.sprint.paymentology.com/client-testing-guide/"),
            ),
            attachments=(),
        )
        inventory = ReadMeInventory(
            pages=(
                readme_page("docs/profile-api-reference/activate.md", "Activate Card", "activate"),
                readme_page("docs/card-api/carddetail.md", "Card Detail", "carddetail"),
                readme_page("docs/Getting Started/client-testing-guide.md", "Client Testing Guide", "client-testing-guide"),
            ),
            assets=(),
            order_entries=(),
        )

        rows = build_parity_map(export, inventory, {})

        self.assertEqual([row.migration_status for row in rows], ["matched", "needs-review", "matched"])
        self.assertEqual(rows[0].matched_path, "docs/profile-api-reference/activate.md")
        self.assertEqual(rows[0].match_kind, "url_path")
        self.assertEqual(rows[1].match_kind, "title")
        self.assertEqual(rows[1].match_confidence, 0.75)
        self.assertEqual(rows[2].match_kind, "title")
        self.assertEqual(rows[2].migration_status, "matched")

    def test_build_parity_map_marks_missing_and_duplicates(self):
        export = WordPressExport(
            pages=(
                wp_page("1", "Missing Page", "missing-page", "https://developer.sprint.paymentology.com/missing-page/"),
                wp_page("2", "Activate", "activate", "https://developer.sprint.paymentology.com/activate/"),
                wp_page("3", "Private Page", "private-page", "https://developer.sprint.paymentology.com/private-page/", "private"),
            ),
            attachments=(),
        )
        inventory = ReadMeInventory(
            pages=(
                readme_page("docs/profile-api-reference/activate.md", "Activate", "activate"),
                readme_page("docs/card-api/activate.md", "Activate", "activate"),
            ),
            assets=(),
            order_entries=(),
        )

        rows = build_parity_map(export, inventory, {})

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0].migration_status, "missing")
        self.assertEqual(rows[1].migration_status, "duplicate")
        self.assertIn("Multiple ReadMe candidates", rows[1].notes)

    def test_build_parity_map_uses_url_leaf_when_slug_is_stale(self):
        export = WordPressExport(
            pages=(
                wp_page("1", "Legacy Label", "stale-slug", "https://developer.sprint.paymentology.com/carddetail/"),
            ),
            attachments=(),
        )
        inventory = ReadMeInventory(
            pages=(
                readme_page("docs/card-api/carddetail.md", "Card Detail", "card-detail"),
            ),
            assets=(),
            order_entries=(),
        )

        rows = build_parity_map(export, inventory, {})

        self.assertEqual(rows[0].migration_status, "matched")
        self.assertEqual(rows[0].matched_path, "docs/card-api/carddetail.md")
        self.assertEqual(rows[0].match_kind, "url_leaf")
        self.assertEqual(rows[0].match_confidence, 0.85)

    def test_build_parity_map_uses_later_unique_match_when_slug_duplicates(self):
        export = WordPressExport(
            pages=(
                wp_page("1", "Legacy Label", "activate", "https://developer.sprint.paymentology.com/carddetail/"),
            ),
            attachments=(),
        )
        inventory = ReadMeInventory(
            pages=(
                readme_page("docs/profile-api-reference/activate.md", "Activate", "activate"),
                readme_page("docs/card-api/activate.md", "Activate", "activate"),
                readme_page("docs/card-api/carddetail.md", "Card Detail", "card-detail"),
            ),
            assets=(),
            order_entries=(),
        )

        rows = build_parity_map(export, inventory, {})

        self.assertEqual(rows[0].migration_status, "matched")
        self.assertEqual(rows[0].matched_path, "docs/card-api/carddetail.md")
        self.assertEqual(rows[0].match_kind, "url_leaf")

    def test_build_parity_map_prefers_permalink_leaf_over_stale_slug(self):
        export = WordPressExport(
            pages=(
                wp_page("1", "Legacy Label", "activate", "https://developer.sprint.paymentology.com/carddetail/"),
            ),
            attachments=(),
        )
        inventory = ReadMeInventory(
            pages=(
                readme_page("docs/profile-api-reference/activate.md", "Activate", "activate"),
                readme_page("docs/card-api/carddetail.md", "Card Detail", "card-detail"),
            ),
            assets=(),
            order_entries=(),
        )

        rows = build_parity_map(export, inventory, {})

        self.assertEqual(rows[0].matched_path, "docs/card-api/carddetail.md")
        self.assertEqual(rows[0].match_kind, "url_leaf")

    def test_mapped_wordpress_paths_omits_stale_slug_aliases(self):
        export = WordPressExport(
            pages=(
                wp_page("1", "Legacy Label", "activate", "https://developer.sprint.paymentology.com/carddetail/"),
            ),
            attachments=(),
        )
        inventory = ReadMeInventory(
            pages=(
                readme_page("docs/card-api/carddetail.md", "Card Detail", "card-detail"),
            ),
            assets=(),
            order_entries=(),
        )
        rows = build_parity_map(export, inventory, {})

        mapped = mapped_wordpress_paths(rows)

        self.assertEqual(mapped, {"carddetail": "docs/card-api/carddetail.md"})
