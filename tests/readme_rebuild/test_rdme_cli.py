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
      <title>Get Started</title>
      <link>https://developer.sprint.paymentology.com/get-started/get-started/</link>
      <content:encoded><![CDATA[<p>Welcome.</p>]]></content:encoded>
      <wp:post_id>100</wp:post_id>
      <wp:post_name>get-started</wp:post_name>
      <wp:status>publish</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>1</wp:menu_order>
    </item>
    <item>
      <title>Card API Reference</title>
      <link>https://developer.sprint.paymentology.com/card-api/api-reference/</link>
      <content:encoded><![CDATA[<p>Landing.</p>]]></content:encoded>
      <wp:post_id>101</wp:post_id>
      <wp:post_name>api-reference</wp:post_name>
      <wp:status>publish</wp:status>
      <wp:post_type>page</wp:post_type>
      <wp:post_parent>0</wp:post_parent>
      <wp:menu_order>2</wp:menu_order>
    </item>
  </channel>
</rss>
"""


class RdmeExportCliSmokeTests(TestCase):
    def test_cli_can_emit_rdme_upload_source(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            xml_path = root / "export.xml"
            xml_path.write_text(WXR_FIXTURE, encoding="utf-8")
            output_root = root / "rebuild" / "readme-site"
            report_root = root / "review" / "rebuild"
            rdme_root = root / "rebuild" / "rdme-upload"

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
                    "--rdme-output-root",
                    str(rdme_root),
                ],
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(f"ReadMe upload source: {rdme_root}", result.stdout)
            self.assertEqual(
                (rdme_root / "docs" / "guides" / "get-started.md").read_text(encoding="utf-8"),
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
                (rdme_root / "reference" / "card-api" / "api-reference.md").read_text(encoding="utf-8"),
                "---\n"
                "title: Card API Reference\n"
                "category:\n"
                "  uri: Card API\n"
                "slug: api-reference\n"
                "position: 1\n"
                "---\n\n"
                "Landing.\n",
            )
