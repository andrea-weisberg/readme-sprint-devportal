# Lume Release Note Word Template Design

## Goal

Update the existing Banking.Live Word release-note templates into client-facing Lume templates that follow the live Paymentology design system visible in `https://designsystemcosmic.lovable.app/`, while preserving the existing release-note wording and document structure.

The update should:

- keep the current release-note copy intact
- replace `Banking.Live` references with `Lume`
- preserve the existing release-note information model and section order
- restyle the client-facing and internal Word templates so they reflect the live product design system rather than the legacy Banking.Live visual language
- produce updated `.docx` templates as the implementation outcome

## Source of Truth

The primary source files for implementation are:

- client-facing template: `/Users/andreaweisberg/Library/CloudStorage/OneDrive-Paymentology/Product Team - Product Operations/Release Letters/BL Release notes/Release_Notes_Template/Release_Notes_BLN.NN.docx`
- internal template: `/Users/andreaweisberg/Library/CloudStorage/OneDrive-Paymentology/Product Team - Product Operations/Release Letters/BL Release notes/Release_Notes_Template/Release_Notes_BLN.NN INTERNAL.docx`

The primary visual source of truth is the live Paymentology design system at:

- `https://designsystemcosmic.lovable.app/colors`
- `https://designsystemcosmic.lovable.app/typography`
- `https://designsystemcosmic.lovable.app/icons`
- `https://designsystemcosmic.lovable.app/shape`

Observed design-system tokens and rules relevant to this work:

- primary font: `Inter`
- primary accent: `Electric Purple #783CFF`
- dark foundation: `Midnight Blue #15154A`
- secondary dark/operational accent: `Orbit Blue #3E4D9C`
- soft accent: `Astral Lilac #D1AFFE`
- neutral surface: `Moonstone Grey #EEEAE7`
- white surfaces: `#FFFFFF`
- radius scale: `8px` default, `16px` for larger premium surfaces, `999px` for pills

Because the deliverable is Microsoft Word, the final typography may need to approximate `Inter` if the font is not available in the execution environment. The structural hierarchy should still follow the design system even if exact font fidelity is not possible.

## Core Rules

- Do not rewrite release-note copy except for renaming `Banking.Live` to `Lume`.
- Do not redesign the information architecture of the release notes.
- Preserve the current release-note category model:
  - `What you must know`
  - `What you should know`
  - `What’s good to know`
- Preserve the per-item content structure already in use, including sections such as:
  - `Applicability`
  - `Description`
  - `Enablement`
  - `Technical info`
- Restyle the templates using the live product-system language, not the retired Banking.Live palette or older Paymentology document branding.
- Optimize first for the client-facing template; the internal template should remain aligned but can be denser and more operational.

## Target Deliverables

The implementation must end with updated Word template files, not only mockups or specs.

Expected deliverables:

- updated client-facing `.docx` template
- updated internal `.docx` template
- preserved template usability for future release-note authors

## Design Direction

The release-note templates should feel like product-system communications rather than static legacy documents.

This means:

- softer, cleaner surfaces instead of dense text blocks
- rounded modules that echo the live product UI
- purple-to-indigo accents rather than legacy navy-heavy branding
- stronger visual scanning and section separation
- clear category emphasis without changing content meaning

The overall tone should be premium and technical at the same time:

- premium through spacing, restraint, rounded surfaces, and cleaner visual rhythm
- technical through disciplined hierarchy, compact metadata handling, and consistent section framing

## Template Structure

### Opening Section

The opening section should remain the release-note introduction, but its presentation should be upgraded.

It should include:

- a system-aligned header band using the live purple/indigo styling
- the release title in the form `Lume X.XX`
- the existing introductory paragraph unchanged except for the `Lume` rename
- a visual summary treatment for the three release categories

The goal of the opening section is to make the document feel deliberate and modern without changing any underlying message.

### Category Summary Treatment

The three release-note categories should be presented as pill-like or card-like summary modules rather than plain bullets.

They should use differentiated emphasis:

- `What you must know`: strongest emphasis
- `What you should know`: medium emphasis
- `What’s good to know`: quietest emphasis

This is visual hierarchy only. No category wording should change.

### Release Item Pattern

Each release item should follow a reusable visual module that preserves the current content pattern.

Each item should visually include:

- JIRA ID as small utility text
- item title as the primary heading
- separated content blocks for `Applicability`, `Description`, `Enablement`, and `Technical info`

The document should not become a marketing page. The module should remain document-friendly and editable in Word.

## Visual System Mapping

### Color

The templates should use the live design-system palette in a restrained way suitable for Word.

Recommended mapping:

- `Midnight Blue #15154A` for primary headings and dark anchor areas
- `Electric Purple #783CFF` for key accents, pills, dividers, and priority emphasis
- `Orbit Blue #3E4D9C` for secondary emphasis and supportive contrast
- `Astral Lilac #D1AFFE` for soft highlight backgrounds
- `Moonstone Grey #EEEAE7` and white for content surfaces

Avoid:

- old Banking.Live navy blocks
- older cobalt-centric document treatment
- aggressive dark-page layouts that reduce readability in Word

### Typography

The design system uses `Inter`, and the Word templates should follow that visual behavior as closely as practical:

- bold, clear headings
- quieter small metadata labels
- readable body text with strong spacing discipline
- compact utility text for IDs and labels

If `Inter` is not available, use the closest practical fallback while preserving hierarchy.

### Shape and Surface

The design should follow the observed system shape model:

- `8px` radius for most small content modules
- `16px` radius for larger grouped panels or opening summary surfaces
- `999px` radius for pills and badges

The Word design should imitate these shapes where Word styling reasonably allows, without becoming fragile for editors.

## Client-Facing vs Internal Variant

### Client-Facing Template

The client-facing template is the priority surface.

It should emphasize:

- cleaner whitespace
- stronger polish
- more obvious category hierarchy
- clearer sectional grouping for easier reading by external clients

### Internal Template

The internal template should reuse the same system language, but with slightly denser treatment:

- less decorative spacing
- more compact metadata handling
- clearer operational scanning

It should still look like the same family as the client-facing template, not like a separate visual system.

## Editing and Authoring Constraints

The updated templates must remain practical for real authoring in Microsoft Word.

That means the implementation should avoid:

- fragile hand-placed design elements that break when text length changes
- highly custom layouts that are difficult for non-designers to maintain
- text embedded inside non-editable decorative shapes unless necessary
- styling choices that depend on a precise export path to remain readable

Preferred implementation traits:

- reusable paragraph styles
- stable heading and section treatments
- predictable spacing
- editable tables or content blocks only where they simplify maintenance

## Content Preservation Rules

Allowed content changes:

- replace `Banking.Live` with `Lume`
- update visible template labels only when required for consistency with that rename

Not allowed:

- rewriting release-note prose
- simplifying, condensing, or reordering the release-note content
- changing the meaning of category descriptions
- removing existing technical sections because they seem too dense

## Implementation Shape

Implementation should proceed in four phases:

### Phase 1: Template inspection

- inspect both source Word templates
- identify reusable styles, repeated structures, and current formatting constraints
- confirm where `Banking.Live` appears and where visual updates are needed

### Phase 2: System restyling

- update typography, spacing, colors, heading hierarchy, pills, and section surfaces
- restyle the opening release block
- restyle repeated release item modules

### Phase 3: Variant alignment

- apply the same system language to the internal template
- tighten density where needed while preserving family resemblance

### Phase 4: Validation

- review the updated `.docx` output visually
- confirm the wording stayed intact except for the `Lume` rename
- confirm the documents remain editable and structurally stable

## Validation Criteria

The work is ready when:

- both Word templates are updated
- `Banking.Live` has been replaced with `Lume` where relevant
- the live design-system palette and shape language are visibly reflected
- the templates no longer look tied to the old Banking.Live visual identity
- the existing wording remains intact
- the category structure and item structure remain intact
- the client-facing template reads clearly as a polished external communication
- the internal template remains aligned but slightly denser
- the documents are still practical to maintain in Word

## Risks and Constraints

- exact `Inter` fidelity may depend on local font availability
- Word may not support every UI-style surface treatment with pixel-perfect parity to the browser system
- some gradient or pill effects may need a simplified Word-native approximation
- rendering verification in this environment may require extra tooling if LibreOffice or equivalent converters are unavailable

These constraints should be handled by choosing robust Word-native approximations rather than drifting back to the older branding.

## Non-Goals

This design does not include:

- rewriting the release-note content
- redesigning the ReadMe developer portal
- restructuring the release-note taxonomy
- changing the authoring workflow outside the templates themselves
- introducing a separate Lume visual identity disconnected from the live Paymentology design system
