from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.readme_rebuild.models import DestinationPage
from tools.readme_rebuild.render import render_site


class RenderTests(TestCase):
    def test_render_site_replaces_existing_output(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            stale_file = root / "API Reference" / "shared" / "legacy.md"
            stale_file.parent.mkdir(parents=True, exist_ok=True)
            stale_file.write_text("# Legacy\n", encoding="utf-8")

            pages = (
                DestinationPage(
                    "1",
                    "https://developer.sprint.paymentology.com/profile-api-reference/activate/",
                    "API Reference/profile-api-reference/activate.md",
                    "Activate",
                    "API Reference",
                    "Profile API Reference",
                    "activate",
                ),
            )

            render_site(
                root,
                pages,
                {
                    "API Reference/profile-api-reference/activate.md": "# Activate\n",
                },
            )

            self.assertFalse(stale_file.exists())
            self.assertEqual(
                (root / "API Reference" / "profile-api-reference" / "activate.md").read_text(encoding="utf-8"),
                "# Activate\n",
            )

    def test_render_site_writes_markdown_and_order_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            pages = (
                DestinationPage(
                    "1",
                    "https://developer.sprint.paymentology.com/get-started/our-apis/",
                    "Guides/our-apis.md",
                    "Our APIs",
                    "Guides",
                    "Shared",
                    "our-apis",
                ),
                DestinationPage(
                    "2",
                    "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",
                    "API Reference/card-api/activatetoken.md",
                    "ActivateToken",
                    "API Reference",
                    "Card API",
                    "activatetoken",
                ),
            )

            render_site(
                root,
                pages,
                {
                    "Guides/our-apis.md": "# Our APIs\n",
                    "API Reference/card-api/activatetoken.md": "# ActivateToken\n",
                },
            )

            self.assertEqual((root / "Guides" / "our-apis.md").read_text(encoding="utf-8"), "# Our APIs\n")
            self.assertEqual(
                (root / "API Reference" / "card-api" / "activatetoken.md").read_text(encoding="utf-8"),
                "# ActivateToken\n",
            )
            self.assertEqual((root / "_order.yaml").read_text(encoding="utf-8"), "- API Reference\n- Guides\n")
            self.assertEqual(
                (root / "API Reference" / "_order.yaml").read_text(encoding="utf-8"),
                "- card-api\n",
            )
            self.assertEqual((root / "Guides" / "_order.yaml").read_text(encoding="utf-8"), "- our-apis\n")
            self.assertEqual((root / "_order.yaml").read_text(encoding="utf-8"), "- API Reference\n- Guides\n")
            self.assertEqual((root / "API Reference" / "_order.yaml").read_text(encoding="utf-8"), "- card-api\n")
            self.assertEqual(
                (root / "API Reference" / "card-api" / "_order.yaml").read_text(encoding="utf-8"),
                "- activatetoken\n",
            )
