from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from tools.migration_control.wxr import parse_wxr


WXR_FIXTURE = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <item>
      <title>Activate Card</title>
      <link>https://developer.sprint.paymentology.com/profile-api-reference/activate/</link>
      <content:encoded><![CDATA[<p>Use <a href="https://developer.sprint.paymentology.com/card-api/">Card API</a>.</p>]]></content:encoded>
      <wp:post_id>101</wp:post_id>
      <wp:post_name>activate</wp:post_name>
      <wp:status>publish</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>7</wp:post_parent>
      <wp:menu_order>3</wp:menu_order>
      <wp:postmeta>
        <wp:meta_key>api_content_builder_0_request</wp:meta_key>
        <wp:meta_value>request xml</wp:meta_value>
      </wp:postmeta>
    </item>
    <item>
      <title>Draft API</title>
      <link>https://developer.sprint.paymentology.com/draft-api/</link>
      <content:encoded><![CDATA[Draft body]]></content:encoded>
      <wp:post_id>102</wp:post_id>
      <wp:post_name>draft-api</wp:post_name>
      <wp:status>draft</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>9</wp:menu_order>
    </item>
    <item>
      <title>Dispute Form</title>
      <link>https://developer.sprint.paymentology.com/wp-content/uploads/dispute.docx</link>
      <wp:post_id>201</wp:post_id>
      <wp:post_type>attachment</wp:post_type>
      <wp:attachment_url>https://developer.sprint.paymentology.com/wp-content/uploads/dispute.docx</wp:attachment_url>
      <wp:postmeta>
        <wp:meta_key>_wp_attached_file</wp:meta_key>
        <wp:meta_value>2026/04/dispute.docx</wp:meta_value>
      </wp:postmeta>
    </item>
  </channel>
</rss>
"""


class WxrParserTests(TestCase):
    def test_parse_wxr_extracts_pages_attachments_and_acf_keys(self):
        with TemporaryDirectory() as tmp:
            xml_path = Path(tmp) / "export.xml"
            xml_path.write_text(WXR_FIXTURE, encoding="utf-8")

            export = parse_wxr(xml_path)

        self.assertEqual(len(export.pages), 2)
        self.assertEqual(len(export.attachments), 1)

        page = export.pages[0]
        self.assertEqual(page.source_id, "101")
        self.assertEqual(page.title, "Activate Card")
        self.assertEqual(page.slug, "activate")
        self.assertEqual(page.status, "publish")
        self.assertEqual(page.parent_id, "7")
        self.assertEqual(page.menu_order, 3)
        self.assertTrue(page.launch_scope)
        self.assertIn("api_content_builder_0_request", page.acf_keys)
        self.assertEqual(page.links, ("https://developer.sprint.paymentology.com/card-api/",))
        self.assertIn("Use Card API.", page.content_text)
        self.assertEqual(
            page.content_markdown,
            "Use [Card API](https://developer.sprint.paymentology.com/card-api/).",
        )

        draft = export.pages[1]
        self.assertFalse(draft.launch_scope)

        attachment = export.attachments[0]
        self.assertEqual(attachment.source_id, "201")
        self.assertEqual(attachment.filename, "dispute.docx")

    def test_parse_wxr_includes_builder_content_and_links(self):
        builder_fixture = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <item>
      <title>Get Started</title>
      <link>https://developer.sprint.paymentology.com/get-started/</link>
      <content:encoded><![CDATA[]]></content:encoded>
      <wp:post_id>301</wp:post_id>
      <wp:post_name>get-started</wp:post_name>
      <wp:status>publish</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>1</wp:menu_order>
      <wp:postmeta>
        <wp:meta_key>page_content_builder_0_content</wp:meta_key>
        <wp:meta_value><![CDATA[<h2>Choose an API</h2><p>Read <a href="https://developer.sprint.paymentology.com/get-started/our-apis/">Our APIs</a>.</p><ul><li>First task</li><li>Second task</li></ul>]]></wp:meta_value>
      </wp:postmeta>
    </item>
  </channel>
</rss>
"""
        with TemporaryDirectory() as tmp:
            xml_path = Path(tmp) / "export.xml"
            xml_path.write_text(builder_fixture, encoding="utf-8")

            export = parse_wxr(xml_path)

        page = export.pages[0]
        self.assertIn("Choose an API", page.content_text)
        self.assertIn("Read Our APIs.", page.content_text)
        self.assertIn("First task", page.content_text)
        self.assertIn("Second task", page.content_text)
        self.assertEqual(
            page.content_markdown,
            "## Choose an API\n\nRead [Our APIs](https://developer.sprint.paymentology.com/get-started/our-apis/).\n\n- First task\n- Second task",
        )
        self.assertEqual(
            page.links,
            ("https://developer.sprint.paymentology.com/get-started/our-apis/",),
        )

    def test_parse_wxr_orders_builder_fragments_and_pairs_column_titles(self):
        builder_fixture = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <item>
      <title>Get Started</title>
      <link>https://developer.sprint.paymentology.com/get-started/</link>
      <content:encoded><![CDATA[]]></content:encoded>
      <wp:post_id>302</wp:post_id>
      <wp:post_name>get-started</wp:post_name>
      <wp:status>publish</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>1</wp:menu_order>
      <wp:postmeta>
        <wp:meta_key>page_content_builder_11_content</wp:meta_key>
        <wp:meta_value><![CDATA[<h2>Helpful tools</h2>]]></wp:meta_value>
      </wp:postmeta>
      <wp:postmeta>
        <wp:meta_key>page_content_builder_8_columns_0_text</wp:meta_key>
        <wp:meta_value><![CDATA[<h3>Test environment</h3><p>Simulate transactions in a test environment</p>]]></wp:meta_value>
      </wp:postmeta>
      <wp:postmeta>
        <wp:meta_key>page_content_builder_2_columns_0_text</wp:meta_key>
        <wp:meta_value><![CDATA[<p>Use this API if you want us to store balances.</p>]]></wp:meta_value>
      </wp:postmeta>
      <wp:postmeta>
        <wp:meta_key>page_content_builder_2_columns_0_title</wp:meta_key>
        <wp:meta_value><![CDATA[Card API]]></wp:meta_value>
      </wp:postmeta>
      <wp:postmeta>
        <wp:meta_key>page_content_builder_8_columns_1_text</wp:meta_key>
        <wp:meta_value><![CDATA[<h3>Live environment</h3><p>Simulate transactions in a live environment</p>]]></wp:meta_value>
      </wp:postmeta>
    </item>
  </channel>
</rss>
"""
        with TemporaryDirectory() as tmp:
            xml_path = Path(tmp) / "export.xml"
            xml_path.write_text(builder_fixture, encoding="utf-8")

            export = parse_wxr(xml_path)

        page = export.pages[0]
        self.assertIn("**Card API**", page.content_markdown)
        self.assertLess(
            page.content_markdown.index("**Card API**"),
            page.content_markdown.index("## Helpful tools"),
        )
        self.assertLess(
            page.content_markdown.index("### Test environment"),
            page.content_markdown.index("## Helpful tools"),
        )
        self.assertLess(
            page.content_markdown.index("### Live environment"),
            page.content_markdown.index("## Helpful tools"),
        )
