from unittest import TestCase

from tools.readme_rebuild.links import rewrite_links
from tools.readme_rebuild.models import DestinationPage, SourcePage


class LinkRewriteTests(TestCase):
    def test_rewrite_links_updates_wordpress_internal_targets(self):
        page = SourcePage(
            "1",
            "Client Testing Guide",
            "https://developer.sprint.paymentology.com/get-started/client-testing-guide/",
            "client-testing-guide",
            "",
            "See https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/ next.",
            ("https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",),
        )
        destinations = {
            "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/": DestinationPage(
                "2",
                "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/",
                "API Reference/card-api/activatetoken.md",
                "ActivateToken",
                "API Reference",
                "Card API",
                "activatetoken",
            )
        }

        rewritten, audit_rows = rewrite_links(page, destinations)

        self.assertIn("/api-reference/card-api/activatetoken", rewritten)
        self.assertEqual(len(audit_rows), 1)

    def test_rewrite_links_leaves_unmapped_links_unchanged(self):
        page = SourcePage(
            "1",
            "Guide",
            "https://developer.sprint.paymentology.com/get-started/guide/",
            "guide",
            "",
            "See https://developer.sprint.paymentology.com/missing/.",
            ("https://developer.sprint.paymentology.com/missing/",),
        )

        rewritten, audit_rows = rewrite_links(page, {})

        self.assertIn("https://developer.sprint.paymentology.com/missing/", rewritten)
        self.assertEqual(audit_rows, ())
