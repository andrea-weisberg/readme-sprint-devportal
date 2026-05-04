# ReadMe Rebuild Tools

This package rebuilds the Sprint developer portal from the WordPress XML export
into a staged ReadMe site layout and writes matching audit artifacts.

## CLI

Run the rebuild pipeline with:

```bash
python3 -m tools.readme_rebuild.cli \
  --wordpress-export /path/to/export.xml \
  --repo-root /path/to/repo \
  --output-root /path/to/rebuild/readme-site \
  --report-root /path/to/review/rebuild \
  --rdme-output-root /path/to/rebuild/rdme-upload
```

The pipeline currently performs these steps in order:

1. Build the launch-scope page inventory from the WordPress XML.
2. Classify and map each page into the approved ReadMe information architecture.
3. Rewrite embedded internal links when a mapped destination exists.
4. Render staged Markdown pages and `_order.yaml` navigation files.
5. Write deterministic audit outputs:
   - `page_mapping.csv`
   - `link_rewrites.csv`
   - `summary.md`
6. Optionally emit an `rdme` upload source tree with YAML frontmatter for:
   - `docs upload`
   - `reference upload`
