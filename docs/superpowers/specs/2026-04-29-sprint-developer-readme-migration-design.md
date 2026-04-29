# Sprint Developer Portal ReadMe Rebuild Design

## Goal

Rebuild `developer.sprint.paymentology.com` into Paymentology's enterprise ReadMe tenant from the WordPress XML export as the source of truth, using ReadMe-native structure and templates instead of preserving the current migrated structure.

The rebuild should:

- preserve all source information
- reorganize content into a cleaner ReadMe information architecture
- rewrite embedded internal links to the new canonical ReadMe destinations
- reduce or eliminate legacy HTML-heavy page layouts
- prepare `API Reference` so it can support both manual ReadMe updates and future GitHub-sync-backed updates

## Source of Truth

The primary source of truth for content and page inventory is:

- WordPress export: `/Users/andreaweisberg/Downloads/paymentologysprintdeveloper.WordPress.2026-04-24.xml`

Secondary references:

- current ReadMe repository in this workspace, used only as a reference for wording, migrated assets, and prior conversion clues
- live WordPress site: `https://developer.sprint.paymentology.com/`
- Slack context: `https://paymentology.slack.com/archives/C0AP72PUTJT`

The existing ReadMe structure in this repository is not considered structurally correct and should not drive the rebuilt information architecture.

## Core Rules

- Do not delete source information during the rebuild.
- If content is moved, split, merged, or normalized, record exactly where it went.
- Preserve recognizable product and content groupings where possible, but do not preserve broken or awkward legacy structure for its own sake.
- Rebuild pages in ReadMe-native Markdown and navigation patterns rather than carrying forward arbitrary HTML-heavy WordPress layouts.
- Rewrite embedded internal WordPress links to the new canonical ReadMe URLs.
- Keep `API Reference` stable enough for future GitHub sync, while still allowing manual ReadMe-managed pages in the same section.

## Information Architecture

### Top Bar

The new top-level navigation should be organized by content type:

- `Guides`
- `API Reference`
- `Reports`
- `Tools`

We are not forcing a separate shared-docs bucket up front. Shared pages should be placed where they are most relevant after inventory review.

### Guides

`Guides` should contain shared onboarding and implementation content, including pages such as:

- choosing an API
- account setup
- credentials
- client testing
- implementation process
- shared how-to material

Guide pages should link directly to the relevant API reference destinations where appropriate.

### API Reference

`API Reference` should be a single top-bar section, with sub-sections by API family:

- `Card API`
- `Companion API`
- `QR Payments`
- `Chargeback API`

This section should support both:

- future GitHub-synced content
- manual ReadMe updates

That means the rebuild should prefer stable page boundaries, predictable hierarchy, and clean canonical slugs.

### Reports

`Reports` should remain a top-level section, but only for genuine report content. Inside the section, reports can be grouped by API family where helpful.

### Tools

`Tools` should remain a top-level section for standalone utilities such as:

- checksum generator
- XML generator
- XML poster
- SIMPOS

## Content Placement Guidance

Because the user has not yet reviewed every shared page category, pages such as contact, notifications, response codes, and other operational content should be placed only after XML inventory review.

Default placement guidance:

- onboarding and workflow content belongs in `Guides`
- reference-like technical material belongs in `API Reference`
- report catalogs and report details belong in `Reports`
- standalone utilities belong in `Tools`

Where a page spans categories, prefer the primary user intent of the page rather than the old WordPress section.

## URL and Link Strategy

The rebuild should define a new canonical URL map rather than inheriting the current migrated URL structure.

Rules:

- every WordPress internal link should be mapped to a new ReadMe destination when the destination exists
- `Guides` should cross-link into the relevant `API Reference` pages
- API-family landing pages and section index pages may be represented differently from WordPress, but the content they summarize must still be preserved
- new slugs should be predictable and consistent with ReadMe navigation

The rebuild should produce a documented mapping of:

- WordPress page URL -> new ReadMe page
- rewritten internal WordPress link -> new ReadMe link

## No-Information-Loss Requirement

No source information should be deleted as part of the rebuild.

Allowed transformations:

- moving content to a more appropriate section
- splitting a large page into multiple clearer pages
- merging near-duplicate structural wrappers when the content itself is preserved
- converting HTML-heavy layout treatment into cleaner ReadMe-native structure

Required follow-through:

- record where moved content ended up
- record when one source page becomes multiple destination pages
- record when multiple source pages are consolidated into one destination page

If content appears redundant, preserve it unless the user explicitly approves consolidation or removal.

## Migration Outputs

The rebuild must produce an explicit migration report after execution.

The report should include:

- WordPress source page -> rebuilt ReadMe destination mapping
- any page splits or merges
- internal link rewrites
- shared pages and why they were placed in their chosen top-level section
- assets restored or remapped
- items that required manual handling

The goal is that the user can review exactly what changed after the rebuild, not just inspect the final site.

## GitHub Sync Readiness

`API Reference` should be designed with future GitHub integration in mind.

This does not require implementing the integration yet, but it does require planning for it:

- stable section boundaries by API family
- predictable slugs
- separation between reference-like content and richer editorial guide content where practical
- avoiding deeply inconsistent page structures that would make later sync workflows fragile

Because the user wants `API Reference` to support both synced and manual content, the design should remain flexible rather than forcing a pure generated-reference model.

## Execution Shape

The rebuild should be executed in five phases:

### Phase 1: Inventory and IA

- inventory all WordPress XML pages, attachments, and link relationships
- define the new canonical information architecture
- classify every page into `Guides`, `API Reference`, `Reports`, or `Tools`

### Phase 2: Mapping

- map every WordPress source page into the new IA
- define canonical rebuilt page destinations
- define new canonical slugs
- define internal link rewrite rules

### Phase 3: Rebuild

- rebuild content into ReadMe-native pages section by section
- preserve source information while improving structure
- remove unnecessary HTML-heavy carryover where possible

### Phase 4: Validation

- verify content coverage against the XML source
- verify internal link rewrites
- verify assets
- verify no information loss
- verify section placement consistency

### Phase 5: Migration Report

- produce a final audit showing exactly what changed
- show source-to-destination mappings
- show link rewrites
- show any manual exceptions

## Validation Criteria

The rebuild is ready for implementation completion when:

- every in-scope WordPress source page is mapped into the new IA
- internal WordPress links have planned rebuilt destinations
- no source information has been dropped
- `Guides` and `API Reference` cross-link correctly where relevant
- `API Reference` has stable structure suitable for later GitHub sync
- `Reports` contains only genuine report content
- `Tools` contains the standalone utilities
- a final migration report can explain exactly what changed

## Non-Goals

This design does not yet decide:

- the exact final placement of every shared operational page before XML inventory review
- whether any source content can be retired or removed
- the technical implementation details of GitHub-to-ReadMe sync

Those decisions should come later, but the rebuild should leave room for them without losing content or forcing a second structural reset.
