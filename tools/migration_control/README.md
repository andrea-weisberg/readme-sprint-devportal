# Migration Control

This package generates and hardens the migration control outputs for moving `developer.sprint.paymentology.com` from WordPress to ReadMe.

## Run

```bash
python3 -m tools.migration_control.cli \
  --wordpress-export "/Users/andreaweisberg/Downloads/paymentologysprintdeveloper.WordPress.2026-04-24.xml" \
  --readme-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex" \
  --output-dir "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/migration-control"
```

## Reports

- `wordpress_inventory.csv`: every WordPress page from the WXR export with status, slug, URL, parent, content size, ACF key count, ACF key names, link count, and link targets.
- `wordpress_attachments.csv`: every WordPress attachment from the WXR export with source ID, title, URL, filename, and MIME type.
- `readme_inventory.csv`: every portal Markdown page under `docs/` with title, slug, content size, link count, link targets, image count, image targets, legacy WordPress link count, and legacy WordPress link targets.
- `readme_assets.csv`: every local file under `assets/`.
- `readme_order_entries.csv`: every entry discovered in ReadMe `_order.yaml` navigation files.
- `parity_map.csv`: one row per published WordPress page showing the matched ReadMe file, match confidence, migration status, review risk, and notes.
- `risk_queue.csv`: prioritized launch risks generated from missing pages, duplicate matches, missing must-keep sections, unmapped legacy links, missing assets, unresolved icon tokens, malformed code fences, and the existing manual review report.
- `summary.md`: human-readable counts for the current run.

## Phase 2 Hardening

Apply the conservative mechanical hardening pass after generating fresh reports:

```bash
python3 -m tools.migration_control.hardening \
  --repo-root "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex" \
  --risk-queue "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/migration-control/risk_queue.csv" \
  --parity-map "/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex/review/migration-control/parity_map.csv"
```

This pass intentionally rewrites only legacy links whose target page is already an exact, high-confidence parity match with no review flag, and it splits malformed adjacent code fences without guessing languages.

## Priority Meanings

- `P0`: launch blocker until fixed, mapped, restored, or explicitly waived.
- `P1`: should be resolved before launch when the target is clear.
- `P2`: review or cleanup candidate that can be scheduled after launch if stakeholders accept it.

## Migration Rule

Keep content by default. The initial migration is not a content reduction exercise, and QR Payments remains present for launch unless separate usage and engineering validation approves removal.
