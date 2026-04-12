---
name: slide-design
description: This skill should be used when the user asks to "create slides", "make a presentation", "build a deck", "design slides", "generate a pitch deck", "create a conference talk", "make a keynote", "presentation design", "slide layout", "slide template", "presentation structure", or mentions slides, presentations, decks, or talks in any context. Also triggers when the user wants to plan the content and visual direction of a presentation before generating it. This is the entry-point orchestrator that drives the full slide creation workflow across both HTML and PPTX formats.
version: 0.2.0
---

# Slide Design — Presentation Planning & Orchestration

Entry-point skill for creating professional presentations. Orchestrates the full workflow from content planning through format selection and generation, delegating to `html-slides` or `pptx-slides` skills for the final output.

## Core Workflow

### Phase 1: Content Discovery

Gather presentation requirements before generating anything:

1. **Topic & purpose** — Identify the subject, key message, and call to action
2. **Audience** — Technical level, interests, expected takeaways
3. **Duration & format** — Map to the slide count guidelines below
4. **Language & tone** — Bilingual (e.g., Spanish headings + English terms), formal, playful, meme-driven
5. **Existing content** — Check for PPTX files to convert, markdown outlines, documents to adapt, or template PDFs to reference

### Phase 2: Structure Planning

Build an outline following the talk-duration-indexed slide count:

| Duration | Slide Count | Structure |
|----------|-------------|-----------|
| 5 min (Lightning) | 5–7 slides | Hook → 2-3 key points → CTA |
| 15 min (Short talk) | 12–18 slides | Intro → 3-4 sections → Summary → CTA |
| 30 min (Conference) | 25–35 slides | Title → Agenda → 5-6 sections → Q&A |
| 45 min (Keynote) | 35–50 slides | Title → Agenda → 7-8 sections → Summary → CTA |
| 60 min (Workshop) | 40–60 slides | Title → Agenda → Sections with exercises → Wrap-up |

Apply the **one idea per slide** rule. Each slide communicates a single concept with supporting evidence.

#### Slide Type Vocabulary

Each slide in the outline must be tagged with a type. Supported types: `title`, `section-divider`, `content`, `image-focus`, `comparison`, `quote`, `code`, `feature-grid`, `timeline`, `metrics`, `meme-gif`, `diagram`, `demo-divider`, `audience-question`, `closing`.

### Phase 3: Style Selection

Present 3 distinct visual directions. For each direction, provide: a one-line mood description, the typography pair, primary + accent colors, and the background recipe. Draw from the curated presets in `references/style-presets.md`.

**Mixed-background decks**: Some presentations use multiple background colors across different slide groups (e.g., coral for opener/closer, white for content, black for demo slides, cream for infographics). When the user's content suggests distinct sections with different moods, propose a mixed-background approach rather than forcing a single color throughout.

### Phase 4: Format Selection & Generation

Ask the user which output format to generate:

- **HTML** — Interactive, animated, browser-based. Best for web sharing, embedded videos, GSAP animations. Delegate to the `html-slides` skill.
- **PPTX** — Editable PowerPoint. Best for corporate settings, offline sharing, template reuse. Delegate to the `pptx-slides` skill.
- **Both** — Generate HTML for presenting and PPTX for sharing/editing.

### Phase 5: Content Generation

For each slide, enforce content density limits:

| Slide Type | Maximum Content |
|------------|----------------|
| Title | 1 heading + 1 subtitle + optional image |
| Section divider | 1 heading + 1 sentence |
| Content | 1 heading + 4–6 bullet points (1-2 sentences each) |
| Image focus | 1 heading + 1 image + 1 caption |
| Comparison | 1 heading + 2 columns (3-4 items each) |
| Quote | 1 quote + attribution |
| Code | 1 heading + 1 code block (max 15 lines) |
| Feature grid | 1 heading + max 6 cards |
| Timeline | 1 heading + max 5 milestones |
| Metrics | 3–4 large numbers with labels |
| Meme/GIF | 1 image placeholder + 1 caption |

Exceeding limits triggers automatic splitting across multiple slides — never cram content.

#### Auto-Split Logic

When content exceeds the density limits, split intelligently:
- **Long bullet lists** (>6 items) → Split into "Part 1/2" slides with consistent heading
- **Dense code** (>15 lines) → Extract key snippet for slide, link to full example
- **Multiple images** → One image per slide with caption, or a grid slide (max 4)
- **Complex diagrams** → Build up incrementally across 2-3 slides (progressive revelation pattern)

Never reduce font size to fit more content. The minimum body text is 18pt — this is non-negotiable for audience readability.

### Phase 6: Validation

After generation, validate the output:

1. **Slide count** matches duration guidelines
2. **Content density** respects per-slide limits
3. **Visual consistency** across all slides (fonts, colors, spacing)
4. **Readability** — minimum 18pt body text, high contrast ratios
5. **Image handling** — all images sized appropriately, no overflow
6. **Speaker notes** — every content slide includes talking points

## Design Anti-Patterns

Avoid these common mistakes that make presentations look generic or unprofessional:

- **Font soup** — More than 2 font families in one deck. Pick one heading + one body font and commit.
- **Color rainbow** — More than 3 colors (primary, secondary, accent). Apply the 60-30-10 rule: 60% dominant, 30% secondary, 10% accent.
- **Wall of text** — If a paragraph is needed, it belongs in a document, not a slide. Distill to keywords and phrases.
- **Clip art syndrome** — Generic stock icons/images that add no meaning. Every visual must earn its place.
- **Transition carnival** — Different animations on every slide. Pick one entrance animation and use it consistently.
- **AI slop aesthetics** — Purple gradients on white, Inter/Roboto everywhere, generic card layouts. Each presentation deserves a distinct visual identity tied to its content and audience.

## Formatting Goal Protocol

Before generating any slide, define and propagate these design parameters:

- **Primary color** — Brand or theme accent
- **Background style** — Solid, gradient, image, pattern, or mixed-per-section
- **Typography pair** — Heading font + body font (load from Google Fonts or Fontshare, never rely on system fonts for headings)
- **Layout aesthetic** — Minimal, bold, editorial, technical, or playful
- **Aspect ratio** — 16:9 (default) or 4:3
- **Atmosphere** — Background recipe (noise, gradient mesh, grid, grain, or starfield) from `references/style-presets.md`
- **Personality elements** — Recurring mascots, emoji density, meme/GIF frequency, decorative illustrations

Pass these parameters to every generation step for visual continuity.

## PPTX Conversion Workflow

To convert an existing PowerPoint to HTML:

1. Run the extraction script: `python ${CLAUDE_PLUGIN_ROOT}/skills/html-slides/scripts/extract-pptx.py <input.pptx>`
2. Review the extracted JSON (slides, images, speaker notes)
3. Let the user curate the outline (reorder, edit, remove)
4. Select a style preset
5. Generate HTML using the `html-slides` skill

## Additional Resources

### Reference Files

- **`references/style-presets.md`** — 12 curated visual style presets with typography, colors, and signature elements
- **`references/design-principles.md`** — Typography, color theory, layout, accessibility, and professional polish guidelines

### Related Skills

- **`html-slides`** — HTML generation with GSAP animations and viewport fitting
- **`pptx-slides`** — PowerPoint generation with PptxGenJS and validation
