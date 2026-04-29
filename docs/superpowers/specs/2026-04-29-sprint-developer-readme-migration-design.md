# Sprint Developer Portal ReadMe Migration Design

## Goal

Migrate `developer.sprint.paymentology.com` from its current WordPress-hosted developer portal into Paymentology's enterprise ReadMe tenant while preserving all active product documentation by default, improving ReadMe-native structure, and creating measurable launch gates for content parity, link health, asset completeness, and API example quality.

## Source Context

The migration starts from the existing ReadMe export in this repository:

- Baseline repository: `/Users/andreaweisberg/Desktop/Dev Portal/.tmp-readme-sprint-devportal-v1.0_codex`
- Baseline content count: 313 Markdown docs under `docs/`
- Prior review artifact: `review/review_report_2026-02-16.md`
- WordPress export: `/Users/andreaweisberg/Downloads/paymentologysprintdeveloper.WordPress.2026-04-24.xml`
- Live WordPress site: `https://developer.sprint.paymentology.com/`
- Slack context: `https://paymentology.slack.com/archives/C0AP72PUTJT`

The WordPress WXR export contains 307 published pages, 298 attachments, 16 draft pages, and 3 private pages. It also includes Advanced Custom Fields metadata such as `api_content_builder`, which is important for reconstructing structured API documentation when the ReadMe conversion is incomplete.

The Slack decision record says this is not a clean-slate rebuild and not a content reduction exercise. The default rule is: keep content unless there is clear evidence it can be safely removed.

## Must-Keep Scope

The new ReadMe portal must preserve these areas in the initial migration:

- Get Started content
- Profile API, including Programme Management usage
- Companion API
- Card API
- Notifications / Transaction Stream
- Reports
- Tools for self-service and testing

Companion API and Card API are still used by new clients, including Orange SL, Mikaty, and Supreme Ventures. Notifications are widely used. Tools must remain available for client self-service.

QR Payments is the only area flagged as a possible deprecation candidate. It must stay in the initial migration unless usage or engineering validation confirms it can be removed. That validation is separate from the initial migration launch gate.

## Non-Goals

The initial migration will not perform method-level API cleanup or product deprecation decisions. Those require detailed usage analysis and Product ownership.

The initial migration will not replace ReadMe as the platform. ReadMe is the current compliance and low-effort migration path, with direct ReadMe support available through Slack and weekly calls.

The initial migration will not treat draft or private WordPress pages as public launch content unless a reviewer explicitly promotes a page into scope.

## Current Baseline Findings

The `v1.0_codex` export is a strong starting point but is not launch-ready.

Known issues:

- 530 remaining links to `https://developer.sprint.paymentology.com`
- 174 malformed adjacent code-fence patterns such as ```` ``` , ``` ```` joins
- Missing and broken asset links in report pages and dispute forms
- Broken anchors in API reference and process pages
- Placeholder images such as `ICON_URL_1` and literal `image.`
- API examples with malformed XML, duplicated examples, or WordPress conversion artifacts
- Pages with embedded HTML/JSX that may work in ReadMe but still need visual and content review
- Review report identifies 85 high-risk and 20 medium-risk pages from 105 reviewed pages

## Recommended Approach

Use the existing ReadMe export as the baseline and harden it with a migration control layer.

The migration control layer compares three sources:

1. ReadMe baseline Markdown in this repository.
2. WordPress WXR export for source-of-truth page, content, metadata, and attachment inventory.
3. Live WordPress site for navigation, rendered content, and final visual reference.

The control layer produces a parity map, risk queue, automated fixes, and launch gate reports. This preserves the current migration work while making gaps visible and measurable.

## Architecture

### Inventory

Build a structured inventory of:

- Published WordPress pages from the WXR export.
- Draft and private WordPress pages, marked out of launch scope by default.
- WordPress attachments and their URLs.
- ReadMe Markdown pages and frontmatter.
- ReadMe navigation entries from `_order.yaml`.
- Legacy WordPress links inside ReadMe Markdown.
- Existing assets under `assets/`.

The inventory should normalize URLs and slugs so that WordPress pages can be matched to ReadMe pages even when the ReadMe folder structure has changed.

### Parity Map

Create a CSV or Markdown report with one row per WordPress published page:

- WordPress title
- WordPress URL
- WordPress slug
- Source status
- Matched ReadMe file
- Match confidence
- Migration status
- Review risk
- Notes

Migration statuses:

- `matched`
- `missing`
- `duplicate`
- `needs-review`
- `out-of-scope`

The map is the central working surface for review and launch readiness.

### Risk Queue

Create a prioritized queue from automated checks and the existing review report.

Priority 0 blocks launch:

- Missing must-keep sections.
- Missing published WordPress pages with no ReadMe equivalent.
- Broken links from must-keep pages to missing internal targets.
- Missing assets required to understand a page.
- Malformed API examples on high-traffic or reference pages.

Priority 1 should be fixed before launch:

- Legacy WordPress links that can be converted to ReadMe-relative links.
- Broken anchors that have clear ReadMe equivalents.
- Placeholder image references.
- Duplicated examples caused by conversion errors.

Priority 2 can be scheduled after launch if explicitly accepted:

- Cosmetic layout differences.
- Non-critical embedded HTML cleanup.
- Low-traffic pages with minor formatting defects.

### Automated Fixes

Automate mechanical fixes only when the source and target are unambiguous:

- Convert old WordPress internal links to ReadMe-relative links using the parity map.
- Replace known attachment URLs with local ReadMe asset links after assets are downloaded or confirmed.
- Split malformed adjacent code fences.
- Repair recurring XML example escaping problems where the pattern is deterministic.
- Remove known sample/test pages that are already outside the `v1.0_codex` baseline.

All automated changes must be reviewable in small commits and backed by before/after reports.

### Manual Review

Manual review focuses on pages where automation cannot prove correctness:

- API reference pages with XML examples.
- Pages listed as high-risk in `review/review_report_2026-02-16.md`.
- Pages with custom visual layouts, tables, or diagrams.
- Pages where the WordPress XML contains ACF structured content not faithfully reflected in Markdown.
- QR Payments pages, which require a keep-or-deprecate decision outside this launch track.

The review output should update the parity map and risk queue rather than live only in free-form notes.

### ReadMe Sync

The repository structure should remain compatible with ReadMe's documented Git sync shape:

- `docs/` for guide content.
- `reference/` for ReadMe API reference configuration and pages.
- `custom_blocks/` for reusable custom blocks.
- `_order.yaml` files for navigation.

The migration should avoid direct production pushes until launch gates pass. If ReadMe branch/version workflows are available in the tenant, use a staging branch/version for validation before switching the public custom domain.

## Data Flow

1. Parse the WordPress WXR export.
2. Extract published pages, non-public pages, attachments, parent relationships, slugs, links, and content metadata.
3. Scan the ReadMe repository for Markdown files, frontmatter, `_order.yaml`, links, images, and assets.
4. Match WordPress pages to ReadMe files by URL, slug, title, and normalized path.
5. Generate the parity map and risk queue.
6. Apply approved mechanical fixes.
7. Re-run the checks and update the reports.
8. Manually review high-risk pages.
9. Validate the ReadMe staging environment.
10. Prepare redirect and launch checklist.

## Validation

Launch readiness requires:

- Every must-keep WordPress section has a ReadMe destination.
- Every published WordPress page is mapped, marked out of scope with a reason, or flagged as a launch blocker.
- No high-priority broken internal links remain.
- No missing assets remain on launch-blocking pages.
- No placeholder images remain on launch-blocking pages.
- High-risk API example pages are reviewed or explicitly waived.
- The ReadMe navigation contains the required top-level sections.
- A redirect plan exists for legacy WordPress URLs.
- QR Payments has an explicit interim decision: keep for launch unless separately validated for removal.

Validation artifacts should live under `review/` or a dedicated migration report folder and be regenerated after each fix batch.

## Error Handling

If the XML parser cannot process a page, the page is recorded in the parity map with `needs-review` and the parser error.

If a WordPress URL maps to multiple ReadMe files, the row is marked `duplicate` and no automatic link rewrite is performed for that URL.

If a ReadMe file contains a legacy WordPress link with no mapped target, the link remains unchanged and is added to the risk queue.

If an attachment URL exists in WordPress but cannot be downloaded or matched locally, affected pages are flagged for asset review.

If a mechanical XML example fix changes parseable content in a way that cannot be validated, the file is flagged for manual review and the fix is not applied automatically.

## Rollout Plan

Phase 1: Control layer and reports.

- Build the WXR inventory.
- Build the ReadMe inventory.
- Generate the parity map.
- Generate the first risk queue.

Phase 2: Mechanical hardening.

- Fix unambiguous internal links.
- Fix deterministic code-fence and XML formatting defects.
- Download or map missing assets where possible.
- Re-run validation reports.

Phase 3: Manual review and content decisions.

- Review high-risk pages.
- Confirm must-keep sections.
- Confirm QR Payments interim status.
- Record waivers for non-blocking defects.

Phase 4: ReadMe staging validation.

- Sync or import into a staging ReadMe branch/version.
- Validate navigation, search, Ask AI behavior if enabled, assets, and key page rendering.
- Prepare redirects and launch notes.

Phase 5: Launch.

- Freeze WordPress content or define a final delta-capture window.
- Re-run parity checks against the final XML/live snapshot.
- Switch domain or publish the ReadMe version according to the tenant's launch process.
- Monitor support feedback and broken links.

## Success Criteria

The migration is ready to launch when:

- The parity map accounts for all 307 published WordPress pages.
- All must-keep sections are present and navigable in ReadMe.
- Launch-blocking links, anchors, assets, and XML examples are fixed or explicitly waived.
- The old WordPress URL redirect plan is complete.
- Stakeholders accept that QR Payments remains present for launch unless validated separately.
- ReadMe staging review confirms that the portal can support existing clients without losing active content.

## Open Decisions To Track

QR Payments requires a usage or engineering validation decision before removal. Until then, it remains in scope.

Draft and private WordPress pages require explicit promotion before they are included in public launch scope.

The final domain cutover method depends on the ReadMe enterprise tenant configuration and should be confirmed with ReadMe support before launch.

## Self-Review Notes

This spec covers the approved baseline-first approach, the Slack keep-by-default constraint, the WordPress XML source, the existing ReadMe export, validation strategy, error handling, and rollout gates. It intentionally scopes method-level API cleanup and QR deprecation out of the initial launch path.
