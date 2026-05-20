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
                    "1",
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
                    "1",
                    "https://developer.sprint.paymentology.com/get-started/get-started/",
                    "Guides/get-started.md",
                    "Get Started",
                    "Guides",
                    "Shared",
                    "get-started",
                ),
                DestinationPage(
                    "2",
                    "https://developer.sprint.paymentology.com/tools/",
                    "Tools/tools.md",
                    "Tools",
                    "Tools",
                    "Tools",
                    "tools",
                ),
                DestinationPage(
                    "3",
                    "https://developer.sprint.paymentology.com/tools/xml-poster/",
                    "Tools/xml-poster.md",
                    "XML Poster",
                    "Tools",
                    "Tools",
                    "xml-poster",
                    "2",
                ),
                DestinationPage(
                    "4",
                    "https://developer.sprint.paymentology.com/card-api/api-reference/",
                    "API Reference/card-api/api-reference.md",
                    "Card API Reference",
                    "API Reference",
                    "Card API",
                    "api-reference",
                ),
                DestinationPage(
                    "5",
                    "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",
                    "API Reference/card-api/activatetoken.md",
                    "ActivateToken",
                    "API Reference",
                    "Card API",
                    "activatetoken",
                    "4",
                ),
                DestinationPage(
                    "6",
                    "https://developer.sprint.paymentology.com/reports/card-api/reports/",
                    "Reports/card-api/reports.md",
                    "Reports",
                    "Reports",
                    "Card API",
                    "reports",
                ),
                DestinationPage(
                    "7",
                    "https://developer.sprint.paymentology.com/reports/card-api/card-balance-report/",
                    "Reports/card-api/card-balance-report.md",
                    "Card Balance Report",
                    "Reports",
                    "Card API",
                    "card-balance-report",
                    "6",
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
            self.assertEqual(manifest.reference_count, 3)
            self.assertEqual(
                manifest.guide_categories,
                ("Guides", "Reports", "Tools"),
            )
            self.assertEqual(manifest.reference_categories, ("Card API", "Shared"))

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
                (output_root / "reference" / "shared" / "api-reference.md").read_text(encoding="utf-8"),
                "---\n"
                "title: API Reference\n"
                "category:\n"
                "  uri: Shared\n"
                "slug: api-reference\n"
                "position: 1\n"
                "---\n\n"
                "Browse the API families below using ReadMe's native reference navigation.\n\n"
                "- Card API\n"
                "- Companion API\n"
                "- QR Payments\n"
                "- Chargeback API\n"
                "- Profile API Reference\n"
                "- Shared\n",
            )
            self.assertEqual(
                (output_root / "docs" / "reports" / "card-api" / "card-balance-report.md").read_text(encoding="utf-8"),
                "---\n"
                "title: Card Balance Report\n"
                "category:\n"
                "  uri: Reports\n"
                "slug: card-api-card-balance-report\n"
                "position: 2\n"
                "parent:\n"
                "  uri: card-api-reports\n"
                "---\n\n"
                "Body.\n",
            )

    def test_export_rdme_source_namespaces_report_parent_pages_by_family(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "1",
                    "https://developer.sprint.paymentology.com/reports/card-api/reports/",
                    "Reports/card-api/reports.md",
                    "Reports",
                    "Reports",
                    "Card API",
                    "reports",
                ),
                DestinationPage(
                    "2",
                    "https://developer.sprint.paymentology.com/reports/companion-api/reports/",
                    "Reports/companion-api/reports.md",
                    "Reports",
                    "Reports",
                    "Companion API",
                    "reports",
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {
                    "Reports/card-api/reports.md": "# Reports\n\nCard.\n",
                    "Reports/companion-api/reports.md": "# Reports\n\nCompanion.\n",
                },
            )

            self.assertIn(
                "slug: card-api-reports\n",
                (output_root / "docs" / "reports" / "card-api" / "reports.md").read_text(encoding="utf-8"),
            )
            self.assertNotIn(
                "parent:\n  uri: card-api-reports\n",
                (output_root / "docs" / "reports" / "card-api" / "reports.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "slug: companion-api-reports\n",
                (output_root / "docs" / "reports" / "companion-api" / "reports.md").read_text(encoding="utf-8"),
            )
            self.assertNotIn(
                "parent:\n  uri: card-api-reports\n",
                (output_root / "docs" / "reports" / "companion-api" / "reports.md").read_text(encoding="utf-8"),
            )

    def test_export_rdme_source_quotes_yaml_sensitive_titles(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "1",
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
                    "1",
                    "https://developer.sprint.paymentology.com/get-started/companion-api/",
                    "Guides/companion-api.md",
                    "Companion API",
                    "Guides",
                    "Shared",
                    "companion-api",
                ),
                DestinationPage(
                    "2",
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

    def test_export_rdme_source_strips_legacy_back_links(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "1",
                    "https://developer.sprint.paymentology.com/card-api/api-reference/ordercard/",
                    "API Reference/card-api/ordercard.md",
                    "OrderCard",
                    "API Reference",
                    "Card API",
                    "ordercard",
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {
                    "API Reference/card-api/ordercard.md": "# OrderCard\n\nBody.\n\n[Back to Card API Menu](/api-reference/card-api/api-reference)\n"
                },
            )

            self.assertNotIn(
                "Back to Card API Menu",
                (output_root / "reference" / "card-api" / "ordercard.md").read_text(encoding="utf-8"),
            )

    def test_export_rdme_source_uses_source_index_for_guide_positions(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "2",
                    "https://developer.sprint.paymentology.com/get-started/testing/",
                    "Guides/testing.md",
                    "Testing",
                    "Guides",
                    "Shared",
                    "testing",
                    "",
                    1,
                    2,
                ),
                DestinationPage(
                    "1",
                    "https://developer.sprint.paymentology.com/get-started/get-started/",
                    "Guides/get-started.md",
                    "Get Started",
                    "Guides",
                    "Shared",
                    "get-started",
                    "",
                    0,
                    1,
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {
                    "Guides/testing.md": "# Testing\n\nTesting body.\n",
                    "Guides/get-started.md": "# Get Started\n\nGet Started body.\n",
                },
            )

            self.assertIn(
                "position: 1\n",
                (output_root / "docs" / "guides" / "get-started.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "position: 2\n",
                (output_root / "docs" / "guides" / "testing.md").read_text(encoding="utf-8"),
            )

    def test_export_rdme_source_uses_wordpress_guide_menu_order_over_source_order(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "2",
                    "https://developer.sprint.paymentology.com/get-started/ask-ai/",
                    "Guides/ask-ai.md",
                    "Ask AI",
                    "Guides",
                    "Shared",
                    "ask-ai",
                    "1",
                    0,
                    20,
                ),
                DestinationPage(
                    "1",
                    "https://developer.sprint.paymentology.com/get-started/get-started/",
                    "Guides/get-started.md",
                    "Get Started",
                    "Guides",
                    "Shared",
                    "get-started",
                    "",
                    0,
                    30,
                ),
                DestinationPage(
                    "3",
                    "https://developer.sprint.paymentology.com/get-started/our-apis/",
                    "Guides/our-apis.md",
                    "Our APIs",
                    "Guides",
                    "Shared",
                    "our-apis",
                    "1",
                    0,
                    10,
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {
                    "Guides/ask-ai.md": "# Ask AI\n\nBody.\n",
                    "Guides/get-started.md": "# Get Started\n\nBody.\n",
                    "Guides/our-apis.md": "# Our APIs\n\nBody.\n",
                },
            )

            self.assertIn(
                "position: 1\n",
                (output_root / "docs" / "guides" / "get-started.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "position: 2\n",
                (output_root / "docs" / "guides" / "ask-ai.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "position: 3\n",
                (output_root / "docs" / "guides" / "our-apis.md").read_text(encoding="utf-8"),
            )

    def test_export_rdme_source_applies_known_slug_overrides(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "1",
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

    def test_export_rdme_source_disambiguates_duplicate_titles(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "1",
                    "https://developer.sprint.paymentology.com/card-api/disputes/",
                    "Guides/disputes-card-api.md",
                    "Disputes",
                    "Guides",
                    "Shared",
                    "disputes-card-api",
                ),
                DestinationPage(
                    "2",
                    "https://developer.sprint.paymentology.com/tools/simpos/help/",
                    "Tools/simpos-help.md",
                    "Help",
                    "Tools",
                    "Tools",
                    "simpos-help",
                ),
                DestinationPage(
                    "3",
                    "https://developer.sprint.paymentology.com/card-api/reports/",
                    "Reports/card-api/reports.md",
                    "Reports",
                    "Reports",
                    "Card API",
                    "reports",
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {
                    "Guides/disputes-card-api.md": "# Disputes\n\nBody.\n",
                    "Tools/simpos-help.md": "# Help\n\nBody.\n",
                    "Reports/card-api/reports.md": "# Reports\n\nBody.\n",
                },
            )

            self.assertIn(
                "title: Disputes (Card API)\n",
                (output_root / "docs" / "guides" / "disputes-card-api.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "title: SIMPOS Help\n",
                (output_root / "docs" / "tools" / "simpos-help.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                "title: Card API Reports\n",
                (output_root / "docs" / "reports" / "card-api" / "reports.md").read_text(encoding="utf-8"),
            )

    def test_export_rdme_source_uses_parent_child_hierarchy_for_guides(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "rdme-upload"
            pages = (
                DestinationPage(
                    "10",
                    "https://developer.sprint.paymentology.com/get-started/",
                    "Guides/get-started.md",
                    "Get Started",
                    "Guides",
                    "Shared",
                    "get-started",
                    "",
                    0,
                    10,
                ),
                DestinationPage(
                    "11",
                    "https://developer.sprint.paymentology.com/get-started/our-apis/",
                    "Guides/our-apis.md",
                    "Our APIs",
                    "Guides",
                    "Shared",
                    "our-apis",
                    "10",
                    1,
                    11,
                ),
            )

            export_rdme_source(
                output_root,
                pages,
                {
                    "Guides/get-started.md": "# Get Started\n\nRoot.\n",
                    "Guides/our-apis.md": "# Our APIs\n\nChild.\n",
                },
            )

            self.assertIn(
                "parent:\n  uri: get-started\n",
                (output_root / "docs" / "guides" / "our-apis.md").read_text(encoding="utf-8"),
            )
