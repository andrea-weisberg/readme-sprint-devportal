from unittest import TestCase

from tools.readme_rebuild.ia import classify_page
from tools.readme_rebuild.models import SourcePage


class IaTests(TestCase):
    def test_classify_client_testing_guide_as_guides(self):
        page = SourcePage(
            "1",
            "Client Testing Guide",
            "https://developer.sprint.paymentology.com/get-started/client-testing-guide/",
            "client-testing-guide",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "Guides")

    def test_classify_card_method_page_as_api_reference(self):
        page = SourcePage(
            "2",
            "ActivateToken",
            "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",
            "activatetoken",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "API Reference")
        self.assertEqual(result.subsection, "Card API")
        self.assertEqual(result.reason, "reference path")

    def test_classify_companion_method_page_as_api_reference(self):
        page = SourcePage(
            "8",
            "GetCardDetails",
            "https://developer.sprint.paymentology.com/companion-api/api-reference/getcarddetails/",
            "getcarddetails",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "API Reference")
        self.assertEqual(result.subsection, "Companion API")

    def test_classify_qr_method_page_as_api_reference(self):
        page = SourcePage(
            "9",
            "Receiving Institution",
            "https://developer.sprint.paymentology.com/qr-payments-api/api-reference/receiving-institution/",
            "receiving-institution",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "API Reference")
        self.assertEqual(result.subsection, "QR Payments")

    def test_classify_shared_report_page_as_reports_shared(self):
        page = SourcePage(
            "3",
            "Implementation Report",
            "https://developer.sprint.paymentology.com/implementation-report/",
            "implementation-report",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "Reports")
        self.assertEqual(result.subsection, "Shared")

    def test_classify_report_title_as_reports(self):
        page = SourcePage(
            "6",
            "Monthly Report Summary",
            "https://developer.sprint.paymentology.com/monthly-report-summary/",
            "monthly-report-summary",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "Reports")

    def test_classify_profile_api_reference_page_as_api_reference_shared(self):
        page = SourcePage(
            "7",
            "ListAllTokens",
            "https://developer.sprint.paymentology.com/profile-api-reference/listalltokens-2/",
            "listalltokens-2",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "API Reference")
        self.assertEqual(result.subsection, "Shared")

    def test_classify_api_reference_with_report_in_title_as_api_reference(self):
        page = SourcePage(
            "10",
            "Settlement Report",
            "https://developer.sprint.paymentology.com/card-api/api-reference/settlement-report/",
            "settlement-report",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "API Reference")
        self.assertEqual(result.subsection, "Card API")

    def test_classify_tools_page_as_tools(self):
        page = SourcePage(
            "4",
            "Checksum Generator",
            "https://developer.sprint.paymentology.com/tools/checksum-generator/",
            "checksum-generator",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "Tools")
        self.assertEqual(result.subsection, "Tools")

    def test_classify_chargeback_page_as_api_reference(self):
        page = SourcePage(
            "5",
            "Connectivity",
            "https://developer.sprint.paymentology.com/chargeback-api/connectivity/",
            "connectivity",
            "",
            "body",
            (),
        )

        result = classify_page(page)

        self.assertEqual(result.top_bar, "API Reference")
        self.assertEqual(result.subsection, "Chargeback API")
