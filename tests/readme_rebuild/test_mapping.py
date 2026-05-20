from unittest import TestCase

from tools.readme_rebuild.mapping import map_page
from tools.readme_rebuild.models import SourcePage


class MappingTests(TestCase):
    def test_map_api_reference_page_to_canonical_path(self):
        page = SourcePage(
            "2",
            "ActivateToken",
            "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",
            "activatetoken",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.path, "API Reference/card-api/activatetoken.md")
        self.assertEqual(destination.source_index, 0)

    def test_map_choose_api_page_to_guides(self):
        page = SourcePage(
            "3",
            "Our APIs",
            "https://developer.sprint.paymentology.com/get-started/our-apis/",
            "our-apis",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.path, "Guides/our-apis.md")

    def test_map_shared_report_page_to_shared_reports_path(self):
        page = SourcePage(
            "4",
            "Implementation Report",
            "https://developer.sprint.paymentology.com/implementation-report/",
            "implementation-report",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.top_bar, "Reports")
        self.assertEqual(destination.subsection, "Shared")
        self.assertEqual(destination.path, "Reports/shared/implementation-report.md")

    def test_map_profile_api_reference_page_to_profile_api_reference_path(self):
        page = SourcePage(
            "6",
            "ListAllTokens",
            "https://developer.sprint.paymentology.com/profile-api-reference/listalltokens-2/",
            "listalltokens-2",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.top_bar, "API Reference")
        self.assertEqual(destination.subsection, "Profile API Reference")
        self.assertEqual(destination.path, "API Reference/profile-api-reference/listalltokens-2.md")

    def test_map_tools_page_to_tools_path(self):
        page = SourcePage(
            "7",
            "Checksum Generator",
            "https://developer.sprint.paymentology.com/tools/checksum-generator/",
            "checksum-generator",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.top_bar, "Tools")
        self.assertEqual(destination.path, "Tools/checksum-generator.md")

    def test_map_tool_help_page_to_parent_specific_slug(self):
        page = SourcePage(
            "70",
            "Help",
            "https://developer.sprint.paymentology.com/tools/xml-generator/help/",
            "help",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.slug, "xml-generator-help")
        self.assertEqual(destination.path, "Tools/xml-generator-help.md")

    def test_map_companion_api_page_to_companion_reference_path(self):
        page = SourcePage(
            "8",
            "GetCardDetails",
            "https://developer.sprint.paymentology.com/companion-api/api-reference/getcarddetails/",
            "getcarddetails",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.path, "API Reference/companion-api/getcarddetails.md")

    def test_map_qr_api_page_to_qr_reference_path(self):
        page = SourcePage(
            "9",
            "Receiving Institution",
            "https://developer.sprint.paymentology.com/qr-payments-api/api-reference/receiving-institution/",
            "receiving-institution",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.path, "API Reference/qr-payments/receiving-institution.md")

    def test_map_chargeback_api_page_to_chargeback_reference_path(self):
        page = SourcePage(
            "10",
            "Connectivity",
            "https://developer.sprint.paymentology.com/chargeback-api/connectivity/",
            "connectivity",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.path, "API Reference/chargeback-api/connectivity.md")

    def test_map_page_falls_back_to_title_slug_when_slug_missing(self):
        page = SourcePage(
            "5",
            "API Overview: V2",
            "https://developer.sprint.paymentology.com/get-started/api-overview/",
            "",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.slug, "api-overview-v2")
        self.assertEqual(destination.path, "Guides/api-overview-v2.md")

    def test_map_card_api_duplicate_guide_to_family_specific_slug(self):
        page = SourcePage(
            "71",
            "Manage funds",
            "https://developer.sprint.paymentology.com/card-api/manage-funds/",
            "manage-funds",
            "",
            "body",
            (),
        )

        destination = map_page(page)

        self.assertEqual(destination.slug, "manage-funds-card-api")
        self.assertEqual(destination.path, "Guides/manage-funds-card-api.md")
