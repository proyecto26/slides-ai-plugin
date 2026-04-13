---
name: slide-design
description: Used when the user asks to "create slides", "make a presentation", "build a deck", "design slides", "generate a pitch deck", "create a conference talk", "make a keynote", "presentation design", "slide layout", "slide template", "presentation structure", or mentions slides, presentations, decks, or talks in any context. Also triggers when the user wants to plan the content and visual direction of a presentation before generating it. This is the entry-point orchestrator that drives the full slide creation workflow across both HTML and PPTX formats. Examples: "I need to create slides for my conference talk about AI adoption", "can you turn this markdown into a presentation?", "I have a product demo tomorrow and need visual materials", "convert my existing PowerPoint to interactive HTML slides".
version: 0.5.0
context: fork
agent: general-purpose
effort: medium
allowed-tools: Read Write Edit Bash Glob Grep Skill
argument-hint: [topic, content file, or .pptx to convert]
---

# Slide Design — Presentation Planning & Orchestration

Entry-point pipeline for creating professional presentations. This skill orchestrates the full workflow from content planning through format-specific generation, programmatically invoking the `html-slides` or `pptx-slides` skill for the final output.

Execute the steps below in order. Do NOT skip steps or ask the user to choose which steps to run — the pipeline is sequential.

## Step 1: Content Discovery

Gather presentation requirements before generating anything. If `$ARGUMENTS` was provided, use it as the topic or content source.

1. **Topic & purpose** — Identify the subject, key message, and call to action
2. **Audience** — Technical level, interests, expected takeaways
3. **Duration & format** — Map to the slide count guidelines below
4. **Language & tone** — Bilingual (e.g., Spanish headings + English terms), formal, playful, meme-driven
5. **Existing content** — Check for PPTX files to convert, markdown outlines, documents to adapt, or template PDFs to reference

Check for per-project settings that override defaults by reading `.claude/slides-ai-plugin.local.md` from the user's project directory (if it exists). This file may contain YAML frontmatter with preferences like default format, theme, language, or speaker-notes style.

Produce: `slide-outline.md` in the working directory with topic, audience, duration, language, and existing content summary.

Immediately continue to Step 2.

## Step 2: Structure Planning

Build an outline following the talk-duration-indexed slide count:

| Duration | Slide Count | Structure |
|----------|-------------|-----------|
| 5 min (Lightning) | 5-7 slides | Hook -> 2-3 key points -> CTA |
| 15 min (Short talk) | 12-18 slides | Intro -> 3-4 sections -> Summary -> CTA |
| 30 min (Conference) | 25-35 slides | Title -> Agenda -> 5-6 sections -> Q&A |
| 45 min (Keynote) | 35-50 slides | Title -> Agenda -> 7-8 sections -> Summary -> CTA |
| 60 min (Workshop) | 40-60 slides | Title -> Agenda -> Sections with exercises -> Wrap-up |

Apply the **one idea per slide** rule. Each slide communicates a single concept with supporting evidence.

### Slide Type Vocabulary

Tag each slide in the outline with a type: `title`, `section-divider`, `content`, `image-focus`, `comparison`, `quote`, `code`, `feature-grid`, `timeline`, `metrics`, `meme-gif`, `diagram`, `demo-divider`, `audience-question`, `closing`.

Produce: Updated `slide-outline.md` with tagged slide outline.

### Format Capabilities (Planning Reference)

Use this table when tagging slide types — some types work better in specific formats:

| Capability | HTML | PPTX | Notes |
|------------|------|------|-------|
| GSAP animations (timeline, scroll, spring) | Yes | No | Use for cinematic reveals, parallax, scroll-driven navigation |
| CSS transitions (fade, scale, blur) | Yes | No | Lightweight entrance animations |
| Mermaid diagrams | Yes | No | Flowcharts, sequence diagrams, ER diagrams |
| Inline video/embed | Yes | No | YouTube, Loom, demos |
| Editable text boxes | No | Yes | Recipients modify content directly in PowerPoint |
| Native shapes & charts | No | Yes | Architecture diagrams, org charts via PptxGenJS |
| Speaker notes (exportable) | Limited | Yes | PPTX speaker notes integrate with Presenter View |
| Offline sharing | No | Yes | PPTX works without a browser/server |
| `contenteditable` inline edit | Yes | No | Browser-based live editing before presenting |
| Syntax highlighting | Prism.js (CDN) | PptxGenJS `codeToRuns()` | Both supported, different rendering |
| Responsive/mobile viewing | Yes | No | HTML adapts to viewport; PPTX is fixed layout |

When tagging slides: prefer `meme-gif`, `diagram`, `timeline` with animations for HTML; prefer `comparison`, `feature-grid`, `metrics` with native shapes for PPTX. Both formats handle `title`, `content`, `quote`, `code`, `image-focus` equally well.

Immediately continue to Step 3.

## Step 3: Style Selection

Present 3 distinct visual directions. For each direction, provide: a one-line mood description, the typography pair, primary + accent colors, and the background recipe.

Read style presets from: `${CLAUDE_SKILL_DIR}/references/style-presets.md`

**Mixed-background decks**: Some presentations use multiple background colors across slide groups. When the user's content suggests distinct sections with different moods, propose a mixed-background approach.

Produce: Updated `slide-outline.md` with selected style preset.

Immediately continue to Step 4.

## Step 4: Format Selection & Generation

Determine which output format to generate:

- **HTML** — Interactive, animated, browser-based. Best for web sharing, embedded videos, GSAP animations.
- **PPTX** — Editable PowerPoint. Best for corporate settings, offline sharing, template reuse.
- **Both** — Generate HTML for presenting and PPTX for sharing/editing.

If the user already specified a format (or both) in the prompt or in `$ARGUMENTS`, use that — do not ask again.

### Single-format generation

Invoke the appropriate generation skill, passing the full slide outline content:

- If **HTML**: Run `/html-slides` with the slide outline
- If **PPTX**: Run `/pptx-slides` with the slide outline

Pass the full slide outline (content + style + structure) as the argument to the downstream skill. Then proceed to Step 5.

### Dual-format generation (Both)

To avoid long-running forks, generate **one format at a time**:

1. Save the finalized `slide-outline.md` with all planning context (topic, structure, style, format notes)
2. Run `/html-slides` with the slide outline — wait for completion, then proceed to Step 5 validation for HTML
3. Run `/pptx-slides` with the same slide outline — wait for completion, then proceed to Step 5 validation for PPTX
4. Report both output file paths to the user

## Step 5: Validation

After generation completes, verify the output:

1. **Slide count** matches duration guidelines from Step 2
2. **Speaker notes** present on every content slide
3. **For PPTX**: Confirm the generation script included `h.validateDeck(pptx)` before saving
4. **For HTML**: Verify viewport fitting (`100vh`/`100dvh`), `prefers-reduced-motion` support, and `clamp()` font sizing
5. **Content density** respects per-slide limits (see below)
6. **Visual consistency** across all slides (fonts, colors, spacing)

Report validation results to the user and provide the output file path.

## Content Density Limits

For each slide type, enforce maximum content:

| Slide Type | Maximum Content |
|------------|----------------|
| Title | 1 heading + 1 subtitle + optional image |
| Section divider | 1 heading + 1 sentence |
| Content | 1 heading + 4-6 bullet points (1-2 sentences each) |
| Image focus | 1 heading + 1 image + 1 caption |
| Comparison | 1 heading + 2 columns (3-4 items each) |
| Quote | 1 quote + attribution |
| Code | 1 heading + 1 code block (max 15 lines) |
| Feature grid | 1 heading + max 6 cards |
| Timeline | 1 heading + max 5 milestones |
| Metrics | 3-4 large numbers with labels |
| Meme/GIF | 1 image placeholder + 1 caption |

Exceeding limits triggers automatic splitting — never cram content.

### Auto-Split Logic

When content exceeds the density limits, split intelligently:
- **Long bullet lists** (>6 items) -> Split into "Part 1/2" slides with consistent heading
- **Dense code** (>15 lines) -> Extract key snippet for slide, link to full example
- **Multiple images** -> One image per slide with caption, or a grid slide (max 4)
- **Complex diagrams** -> Build up incrementally across 2-3 slides (progressive revelation)

Never reduce font size to fit more content. The minimum body text is 18pt — non-negotiable for audience readability.

## Design Anti-Patterns

Avoid these common mistakes:

- **Font soup** — More than 2 font families. Pick one heading + one body font.
- **Color rainbow** — More than 3 colors. Apply the 60-30-10 rule.
- **Wall of text** — Distill to keywords and phrases.
- **Clip art syndrome** — Every visual must earn its place.
- **Transition carnival** — One entrance animation, used consistently.
- **AI slop aesthetics** — Purple gradients, Inter/Roboto everywhere, generic card layouts. Each deck deserves a distinct visual identity.

## Formatting Goal Protocol

Before generating any slide, define and propagate these design parameters:

- **Primary color** — Brand or theme accent
- **Background style** — Solid, gradient, image, pattern, or mixed-per-section
- **Typography pair** — Heading font + body font (Google Fonts or Fontshare)
- **Layout aesthetic** — Minimal, bold, editorial, technical, or playful
- **Aspect ratio** — 16:9 (default) or 4:3
- **Atmosphere** — Background recipe from `${CLAUDE_SKILL_DIR}/references/style-presets.md`
- **Personality elements** — Mascots, emoji density, meme/GIF frequency, decorative illustrations

## PPTX Conversion Workflow

To convert an existing PowerPoint to HTML:

1. Run extraction: `python ${CLAUDE_PLUGIN_ROOT}/skills/html-slides/scripts/extract-pptx.py <input.pptx>`
2. Review extracted JSON (slides, images, speaker notes)
3. Let the user curate the outline
4. Select a style preset
5. Generate HTML using the `/html-slides` skill

## Additional Resources

### Reference Files

- **`references/style-presets.md`** — 12 curated visual style presets with typography, colors, and signature elements
- **`references/design-principles.md`** — Typography, color theory, layout, accessibility, and professional polish guidelines

### Related Skills

- **`html-slides`** — HTML generation with GSAP animations and viewport fitting
- **`pptx-slides`** — PowerPoint generation with PptxGenJS and validation
