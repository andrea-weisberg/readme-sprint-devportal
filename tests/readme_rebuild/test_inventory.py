from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tests.migration_control.test_wxr import WXR_FIXTURE
from tools.readme_rebuild.inventory import build_inventory


class InventoryTests(TestCase):
    def test_build_inventory_extracts_launch_pages_and_links(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text(
                WXR_FIXTURE.replace(
                    "https://developer.sprint.paymentology.com/profile-api-reference/activate/",
                    "https://developer.sprint.paymentology.com/card-api/activate/",
                ).replace("Activate Card", "Activate"),
                encoding="utf-8",
            )

            inventory = build_inventory(xml_path, root)

        self.assertEqual(len(inventory.pages), 1)
        self.assertEqual(inventory.pages[0].source_id, "101")
        self.assertEqual(inventory.pages[0].title, "Activate")
        self.assertEqual(
            inventory.pages[0].source_url,
            "https://developer.sprint.paymentology.com/card-api/activate/",
        )
        self.assertEqual(inventory.pages[0].slug, "activate")
        self.assertIn("card-api", inventory.pages[0].source_url)
        self.assertEqual(inventory.pages[0].section_hint, "card-api/activate/")
        self.assertIn("Use Card API.", inventory.pages[0].content_text)
        self.assertEqual(
            inventory.pages[0].content_markdown,
            "Use [Card API](https://developer.sprint.paymentology.com/card-api/).",
        )
        self.assertEqual(
            inventory.pages[0].links,
            ("https://developer.sprint.paymentology.com/card-api/",),
        )
        self.assertEqual(inventory.pages[0].parent_id, "7")
        self.assertEqual(inventory.pages[0].menu_order, 3)
        self.assertEqual(inventory.pages[0].source_index, 1)
        self.assertGreaterEqual(len(inventory.attachments), 1)
        self.assertEqual(
            inventory.attachments,
            ("https://developer.sprint.paymentology.com/wp-content/uploads/dispute.docx",),
        )

    def test_build_inventory_section_hint_ignores_query_and_fragment(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text(
                WXR_FIXTURE.replace(
                    "https://developer.sprint.paymentology.com/profile-api-reference/activate/",
                    "https://developer.sprint.paymentology.com/card-api/activate/?v=1#frag",
                ),
                encoding="utf-8",
            )

            inventory = build_inventory(xml_path, root)

        self.assertEqual(inventory.pages[0].section_hint, "card-api/activate/")
