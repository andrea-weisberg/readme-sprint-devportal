import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

WXR_FIXTURE = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <item>
      <title>Client Testing Guide</title>
      <link>https://developer.sprint.paymentology.com/get-started/client-testing-guide/</link>
      <content:encoded><![CDATA[]]></content:encoded>
      <wp:post_id>100</wp:post_id>
      <wp:post_name>client-testing-guide</wp:post_name>
      <wp:status>publish</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>1</wp:menu_order>
      <wp:postmeta>
        <wp:meta_key>page_content_builder_0_content</wp:meta_key>
        <wp:meta_value><![CDATA[<h2>Choose an API</h2><p>Read <a href="https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/">ActivateToken</a>.</p><ul><li>First task</li><li>Second task</li></ul>]]></wp:meta_value>
      </wp:postmeta>
    </item>
    <item>
      <title>ActivateToken</title>
      <link>https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/</link>
      <content:encoded><![CDATA[<p>Activation details.</p>]]></content:encoded>
      <wp:post_id>101</wp:post_id>
      <wp:post_name>activatetoken</wp:post_name>
      <wp:status>publish</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>2</wp:menu_order>
      <wp:postmeta>
        <wp:meta_key>api_content_builder_0_request</wp:meta_key>
        <wp:meta_value>request xml</wp:meta_value>
      </wp:postmeta>
    </item>
  </channel>
</rss>
"""


class RebuildCliSmokeTests(TestCase):
    def test_cli_renders_staging_site_and_writes_audit_reports(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text(WXR_FIXTURE, encoding="utf-8")
            (root / "docs").mkdir()
            output_root = root / "rebuild" / "readme-site"
            report_root = root / "review" / "rebuild"

            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "tools.readme_rebuild.cli",
                    "--wordpress-export",
                    str(xml_path),
                    "--repo-root",
                    str(root),
                    "--output-root",
                    str(output_root),
                    "--report-root",
                    str(report_root),
                ],
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Source pages: 2", result.stdout)
            self.assertIn("Rendered pages: 2", result.stdout)
            self.assertIn("Rewritten links: 1", result.stdout)
            self.assertIn(f"Staging site: {output_root}", result.stdout)
            self.assertIn(f"Audit reports: {report_root}", result.stdout)
            self.assertEqual(
                (output_root / "Guides" / "client-testing-guide.md").read_text(encoding="utf-8"),
                "# Client Testing Guide\n\n## Choose an API\n\nRead [ActivateToken](/api-reference/card-api/activatetoken).\n\n- First task\n- Second task\n",
            )
            self.assertEqual(
                (output_root / "API Reference" / "card-api" / "activatetoken.md").read_text(encoding="utf-8"),
                "# ActivateToken\n\nActivation details.\n",
            )
            self.assertEqual(
                (report_root / "page_mapping.csv").read_text(encoding="utf-8"),
                "source_url,top_bar,subsection,title,destination_path\n"
                "https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/,API Reference,Card API,ActivateToken,API Reference/card-api/activatetoken.md\n"
                "https://developer.sprint.paymentology.com/get-started/client-testing-guide/,Guides,Shared,Client Testing Guide,Guides/client-testing-guide.md\n",
            )
            self.assertEqual(
                (report_root / "link_rewrites.csv").read_text(encoding="utf-8"),
                "source_page,original_url,rewritten_url,status\n"
                "https://developer.sprint.paymentology.com/get-started/client-testing-guide/,https://developer.sprint.paymentology.com/card-api/api-reference/activatetoken/,/api-reference/card-api/activatetoken,rewritten\n",
            )
            self.assertEqual(
                (report_root / "summary.md").read_text(encoding="utf-8"),
                "# ReadMe Rebuild Summary\n\n"
                "- Source pages: 2\n"
                "- Rendered pages: 2\n"
                "- Rewritten links: 1\n",
            )
