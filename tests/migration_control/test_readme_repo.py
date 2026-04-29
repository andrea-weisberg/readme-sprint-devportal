from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.migration_control.readme_repo import scan_readme_repo


class ReadMeRepoScannerTests(TestCase):
    def test_scan_readme_repo_extracts_markdown_assets_order_and_links(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "docs" / "profile-api-reference"
            docs.mkdir(parents=True)
            (root / "assets").mkdir()
            (root / "assets" / "sample.csv").write_text("a,b\n", encoding="utf-8")
            (root / "docs" / "_order.yaml").write_text("- profile-api-reference\n", encoding="utf-8")
            (docs / "activate.md").write_text(
                "---\n"
                "title: Activate Card\n"
                "slug: activate\n"
                "---\n"
                "# Activate Card\n"
                "See [legacy](https://developer.sprint.paymentology.com/card-api/).\n"
                "![Report](../../assets/sample.csv)\n"
                '<img src="../../assets/missing.png" />\n',
                encoding="utf-8",
            )

            inventory = scan_readme_repo(root)

        self.assertEqual(inventory.assets, ("assets/sample.csv",))
        self.assertEqual(inventory.order_entries, ("profile-api-reference",))
        self.assertEqual(len(inventory.pages), 1)

        page = inventory.pages[0]
        self.assertEqual(page.path, "docs/profile-api-reference/activate.md")
        self.assertEqual(page.title, "Activate Card")
        self.assertEqual(page.slug, "activate")
        self.assertIn("https://developer.sprint.paymentology.com/card-api/", page.links)
        self.assertIn("../../assets/sample.csv", page.images)
        self.assertIn("../../assets/missing.png", page.images)
        self.assertEqual(page.legacy_wordpress_links, ("https://developer.sprint.paymentology.com/card-api/",))
