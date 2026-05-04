from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.readme_rebuild.models import DestinationPage
from tools.readme_rebuild.rdme_export import export_rdme_source


class RdmeExportTests(TestCase):
    def test_export_rdme_source_replaces_existing_output(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            stale_file = output_root / "docs" / "guides" / "stale.md"
            stale_file.parent.mkdir(parents=True, exist_ok=True)
            stale_file.write_text("stale", encoding="utf-8")

            pages = (
                DestinationPage(
                    "https://developer.sprint.paymentology.com/get-started/get-started/",
                    "Guides/get-started.md",
                    "Get Started",
                    "Guides",
                    "Shared",
                    "get-started",
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {"Guides/get-started.md": "# Get Started\n\nWelcome.\n"},
            )

            self.assertFalse(stale_file.exists())

    def test_export_rdme_source_writes_frontmatter_for_docs_and_reference(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "https://developer.sprint.paymentology.com/get-started/get-started/",
                    "Guides/get-started.md",
                    "Get Started",
                    "Guides",
                    "Shared",
                    "get-started",
                ),
                DestinationPage(
                    "https://developer.sprint.paymentology.com/tools/",
                    "Tools/tools.md",
                    "Tools",
                    "Tools",
                    "Tools",
                    "tools",
                ),
                DestinationPage(
                    "https://developer.sprint.paymentology.com/tools/xml-poster/",
                    "Tools/xml-poster.md",
                    "XML Poster",
                    "Tools",
                    "Tools",
                    "xml-poster",
                ),
                DestinationPage(
                    "https://developer.sprint.paymentology.com/card-api/api-reference/",
                    "API Reference/card-api/api-reference.md",
                    "Card API Reference",
                    "API Reference",
                    "Card API",
                    "api-reference",
                ),
                DestinationPage(
                    "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",
                    "API Reference/card-api/activatetoken.md",
                    "ActivateToken",
                    "API Reference",
                    "Card API",
                    "activatetoken",
                ),
                DestinationPage(
                    "https://developer.sprint.paymentology.com/reports/card-api/reports/",
                    "Reports/card-api/reports.md",
                    "Reports",
                    "Reports",
                    "Card API",
                    "reports",
                ),
                DestinationPage(
                    "https://developer.sprint.paymentology.com/reports/card-api/card-balance-report/",
                    "Reports/card-api/card-balance-report.md",
                    "Card Balance Report",
                    "Reports",
                    "Card API",
                    "card-balance-report",
                ),
            )
            content_by_path = {
                "Guides/get-started.md": "# Get Started\n\nWelcome.\n",
                "Tools/tools.md": "# Tools\n\nOverview.\n",
                "Tools/xml-poster.md": "# XML Poster\n\nPoster.\n",
                "API Reference/card-api/api-reference.md": "# Card API Reference\n\nLanding.\n",
                "API Reference/card-api/activatetoken.md": "# ActivateToken\n\nDetails.\n",
                "Reports/card-api/reports.md": "# Reports\n\nLanding.\n",
                "Reports/card-api/card-balance-report.md": "# Card Balance Report\n\nBody.\n",
            }

            manifest = export_rdme_source(output_root, pages, content_by_path)

            self.assertEqual(manifest.docs_count, 5)
            self.assertEqual(manifest.reference_count, 2)
            self.assertEqual(
                manifest.guide_categories,
                ("Guides", "Reports - Card API", "Tools"),
            )
            self.assertEqual(manifest.reference_categories, ("Card API",))

            self.assertEqual(
                (output_root / "docs" / "guides" / "get-started.md").read_text(encoding="utf-8"),
                "---\n"
                "title: Get Started\n"
                "category:\n"
                "  uri: Guides\n"
                "slug: get-started\n"
                "position: 1\n"
                "---\n\n"
                "Welcome.\n",
            )
            self.assertEqual(
                (output_root / "docs" / "tools" / "xml-poster.md").read_text(encoding="utf-8"),
                "---\n"
                "title: XML Poster\n"
                "category:\n"
                "  uri: Tools\n"
                "slug: xml-poster\n"
                "position: 2\n"
                "parent:\n"
                "  uri: tools\n"
                "---\n\n"
                "Poster.\n",
            )
            self.assertEqual(
                (output_root / "reference" / "card-api" / "activatetoken.md").read_text(encoding="utf-8"),
                "---\n"
                "title: ActivateToken\n"
                "category:\n"
                "  uri: Card API\n"
                "slug: activatetoken\n"
                "position: 2\n"
                "parent:\n"
                "  uri: api-reference\n"
                "---\n\n"
                "Details.\n",
            )
            self.assertEqual(
                (output_root / "docs" / "reports-card-api" / "card-balance-report.md").read_text(encoding="utf-8"),
                "---\n"
                "title: Card Balance Report\n"
                "category:\n"
                "  uri: Reports - Card API\n"
                "slug: card-balance-report\n"
                "position: 2\n"
                "parent:\n"
                "  uri: reports\n"
                "---\n\n"
                "Body.\n",
            )

    def test_export_rdme_source_quotes_yaml_sensitive_titles(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "https://developer.sprint.paymentology.com/chargeback-api/remote-messaging-api-chargeback-notification/",
                    "API Reference/chargeback-api/remote-messaging-api-chargeback-notification.md",
                    "Remote Messaging API: chargeback notification",
                    "API Reference",
                    "Chargeback API",
                    "remote-messaging-api-chargeback-notification",
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {
                    "API Reference/chargeback-api/remote-messaging-api-chargeback-notification.md": "# Remote Messaging API: chargeback notification\n\nBody.\n"
                },
            )

            self.assertEqual(
                (
                    output_root
                    / "reference"
                    / "chargeback-api"
                    / "remote-messaging-api-chargeback-notification.md"
                ).read_text(encoding="utf-8"),
                "---\n"
                "title: \"Remote Messaging API: chargeback notification\"\n"
                "category:\n"
                "  uri: Chargeback API\n"
                "slug: remote-messaging-api-chargeback-notification\n"
                "position: 1\n"
                "---\n\n"
                "Body.\n",
            )

    def test_export_rdme_source_sanitizes_readme_unfriendly_body_patterns(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "https://developer.sprint.paymentology.com/get-started/companion-api/",
                    "Guides/companion-api.md",
                    "Companion API",
                    "Guides",
                    "Shared",
                    "companion-api",
                ),
                DestinationPage(
                    "https://developer.sprint.paymentology.com/card-api/api-reference/togglevoucherfeature/",
                    "API Reference/card-api/togglevoucherfeature.md",
                    "ToggleVoucherFeature",
                    "API Reference",
                    "Card API",
                    "togglevoucherfeature",
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {
                    "Guides/companion-api.md": "# Companion API\n\nIt is hosted by you![Alt](https://example.com/image.png)\n",
                    "API Reference/card-api/togglevoucherfeature.md": "# ToggleVoucherFeature\n\n<methodCall>\n<methodName>ToggleVoucherFeature</methodName>\n</methodCall>\n",
                },
            )

            self.assertEqual(
                (output_root / "docs" / "guides" / "companion-api.md").read_text(encoding="utf-8"),
                "---\n"
                "title: Companion API\n"
                "category:\n"
                "  uri: Guides\n"
                "slug: companion-api-guide\n"
                "position: 1\n"
                "---\n\n"
                "It is hosted by you\n\n"
                "![Alt](https://example.com/image.png)\n",
            )
            self.assertEqual(
                (output_root / "reference" / "card-api" / "togglevoucherfeature.md").read_text(encoding="utf-8"),
                "---\n"
                "title: ToggleVoucherFeature\n"
                "category:\n"
                "  uri: Card API\n"
                "slug: togglevoucherfeature\n"
                "position: 1\n"
                "---\n\n"
                "```xml\n"
                "<methodCall>\n"
                "<methodName>ToggleVoucherFeature</methodName>\n"
                "</methodCall>\n"
                "```\n",
            )

    def test_export_rdme_source_applies_known_slug_overrides(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "https://developer.sprint.paymentology.com/get-started/companion-api/",
                    "Guides/companion-api.md",
                    "Companion API",
                    "Guides",
                    "Shared",
                    "companion-api",
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {"Guides/companion-api.md": "# Companion API\n\nBody.\n"},
            )

            self.assertIn(
                "slug: companion-api-guide\n",
                (output_root / "docs" / "guides" / "companion-api.md").read_text(encoding="utf-8"),
            )
