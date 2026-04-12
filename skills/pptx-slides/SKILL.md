---
name: pptx-slides
description: This skill should be used when the user asks to "create a PowerPoint", "generate PPTX slides", "make a PowerPoint presentation", "build a .pptx deck", "create editable slides", "PptxGenJS", "editable presentation", "corporate deck", "slide deck for sharing", or when the output format is PPTX for any presentation task. Also triggers on "export to PowerPoint", "pitch deck PPTX", "offline presentation", or when the context implies an editable/corporate format. Generates OOXML-compliant .pptx files with PptxGenJS, precise layout, text measurement, and overlap validation.
version: 0.2.0
---

# PPTX Slides — Programmatic PowerPoint Generation

Generate professional, editable PowerPoint presentations using PptxGenJS (Node.js). Produces OOXML-compliant `.pptx` files with precise layout, text measurement, and overlap validation.

## Architecture

### Technology Stack

- **PptxGenJS** — Node.js library for programmatic PPTX creation
- **skia-canvas** — Font-aware text measurement for accurate layout
- **Prism.js** — Syntax highlighting for code slides
- **MathJax** — LaTeX equation rendering (optional)

### Helper Setup

Every PPTX generation script begins with these imports and configuration:

```javascript
const pptxgen = require('pptxgenjs');
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_16x9'; // 10" x 5.625"

// Define reusable theme constants
const THEME = {
  bg: '0a0a0a',
  bgSecondary: '1a1a1a',
  text: 'ffffff',
  textSecondary: '999999',
  accent: '4a9eff',
  fontHeading: 'Arial',  // Substitute with available system font
  fontBody: 'Arial',
  titleSize: 36,
  bodySize: 20,
  captionSize: 14,
};
```

Install dependencies before running: `npm install pptxgenjs` (add `skia-canvas` for font-aware text measurement).

### Generation Workflow

1. **Plan layout** — Map content outline to slide types and layout patterns
2. **Generate slides** — Create PPTX using PptxGenJS with helper functions
3. **Validate layout** — Check for text overflow, boundary violations, and element overlaps
4. **Render preview** — Convert to PNG for visual inspection (via LibreOffice or similar)
5. **Fix issues** — Adjust layout based on validation results
6. **Deliver** — Provide the `.pptx` file. Include speaker notes on every content slide. If the user needs to regenerate or customize, also provide the source `.js` generation script.

## Core Design Rules

### Typography

- **Minimum body text**: 18pt (24-28pt preferred)
- **Title text**: 36-44pt
- **Caption/footnote**: 14-16pt minimum
- **Font families**: Declare explicitly — never rely on defaults
- **Leading**: `fontSize / 72 * leading` for line height calculation

### Layout

- **Slide dimensions**: 10" × 5.625" (widescreen 16:9) or 10" × 7.5" (standard 4:3)
- **Safe margins**: 0.5" from all edges
- **White space**: Target 40-50% empty space per slide
- **Alignment**: Use helper functions for precise element positioning

### Color & Accessibility

- **Contrast ratio**: WCAG AA minimum (4.5:1 for body text, 3:1 for large text)
- **Color-blind safe**: Use Wong or IBM color palettes for data visualization
- **Background**: Consistent across slide groups; avoid distracting patterns

## PptxGenJS Helper Functions

Refer to `references/pptxgenjs-helpers.md` for the full helper function API reference. Implement these helpers in the generation script for precise layout control.

### Key Helpers

**Text Measurement & Auto-Sizing**:
- `measureText(text, fontFamily, fontSize)` — Measure text dimensions using skia-canvas
- `autoFontSize(text, box, fontFamily, options)` — Binary search for optimal font size to fit a box
- `calcTextBoxHeightSimple(text, width, fontSize, leading)` — Analytical height calculation

**Layout Builders**:
- `addImageTextCard(slide, options)` — Image + caption card component
- `addCardRow(slide, cards, region, options)` — Row of cards with auto-spacing
- `addThreeLevelTree(slide, data, region)` — Organizational tree diagram
- `addTimeline(slide, milestones, region)` — Horizontal timeline with markers

**Validation**:
- `warnIfSlideHasOverlaps(slide)` — Detect overlapping elements with geometry analysis
- `warnIfSlideElementsOutOfBounds(slide, pptx)` — Check elements stay within slide boundaries
- `getSlideDimensions(slide, pptx)` — Extract slide dimensions (handles EMU conversion)

**Alignment & Distribution**:
- `alignSlideElements(elements, axis, alignment)` — Align elements (left/center/right/top/bottom)
- `distributeSlideElements(elements, axis)` — Evenly distribute elements along an axis

**Image Handling**:
- `imageSizingCrop(width, height)` — Aspect-ratio-aware crop sizing
- `imageSizingContain(width, height)` — Contain image within bounds

## Slide Type Patterns

### Title Slide
```javascript
slide.addText(title, { x: 0.5, y: 1.5, w: 9, h: 1.5, fontSize: 44, bold: true, align: 'center' });
slide.addText(subtitle, { x: 1, y: 3.2, w: 8, h: 0.8, fontSize: 24, color: '666666', align: 'center' });
```

### Content with Bullets
```javascript
slide.addText(heading, { x: 0.5, y: 0.3, w: 9, h: 0.8, fontSize: 32, bold: true });
slide.addText(bullets.map(b => ({ text: b, options: { bullet: true, fontSize: 20, breakLine: true } })),
  { x: 0.7, y: 1.3, w: 8.5, h: 3.8, valign: 'top', lineSpacing: 28 });
```

### Two-Column Layout
```javascript
// Left column: text
slide.addText(leftContent, { x: 0.5, y: 1.2, w: 4.2, h: 3.8, fontSize: 18, valign: 'top' });
// Right column: image
slide.addImage({ path: imagePath, x: 5.2, y: 1.0, w: 4.3, h: 4.0, sizing: { type: 'contain' } });
```

### Code Slide
For syntax-highlighted code, use a monospace font with a dark background shape. See `references/slide-patterns.md` for the full Code Slide pattern with rounded rectangle background and proper font sizing.

## Validation Workflow

After generating every deck, run validation:

1. **Check overlaps**: `warnIfSlideHasOverlaps()` on every slide
2. **Check boundaries**: `warnIfSlideElementsOutOfBounds()` on every slide
3. **Check text overflow**: Verify `autoFontSize()` didn't hit minimum bounds
4. **Check bullet count**: Max 6 bullets per slide
5. **Check font sizes**: No text smaller than 14pt
6. **Visual review**: Render to PNG and inspect

If validation fails, adjust layout and re-validate. Repeat until all checks pass, typically 1-2 cycles.

## Render & Preview

To preview generated PPTX:

1. Convert PPTX → PDF using LibreOffice: `libreoffice --headless --convert-to pdf deck.pptx`
2. Convert PDF → PNG per slide: Use `scripts/render-slides.py`
3. Create montage for quick review: Stitch PNGs into a contact sheet
4. Inspect for overflow, misalignment, or readability issues

## Anti-Patterns

- Text smaller than 14pt anywhere
- More than 6 bullets per slide
- Elements extending beyond slide boundaries
- Relying on default fonts (always declare font family)
- Skipping validation step
- Hard-coded absolute positions without helper functions
- Missing speaker notes on content slides

## Editability Guidance

Design for editability — recipients must be able to modify the deck:

- **Use native text boxes** — Recipients click and edit text directly. Never flatten text into images.
- **Group related elements** — Use PptxGenJS groups so card layouts move as a unit.
- **Avoid embedded SVG where possible** — Use native shapes (rounded rectangles, circles, lines) for simple graphics. SVG embeds render as images in PowerPoint and cannot be edited.
- **Speaker notes** — Add speaker notes to every content slide with talking points and presenter instructions.
- **Master slide layouts** — For template decks, define slide layouts so recipients can add new slides matching the style.

## Architecture Diagrams with Shapes

For technical presentations, build architecture diagrams using PptxGenJS native shapes rather than images:

- **Rectangles** for services/components: `slide.addShape('rect', { ... })`
- **Lines and arrows** for connections: `slide.addShape('line', { ... })`
- **Text labels** inside shapes for component names
- **Color coding**: Use accent colors for active/healthy components, red for failure indicators, gray for inactive
- **Progressive revelation**: Build the same diagram across 2-3 slides, adding complexity at each step (simple → production → failure points)

```javascript
// Adding speaker notes
slide.addNotes('Key talking points:\n- First point\n- Second point\n- Remember to demo the feature');
```

## Additional Resources

### Reference Files

- **`references/pptxgenjs-helpers.md`** — Full API reference for layout builders, text measurement, validation, and image helpers
- **`references/slide-patterns.md`** — Detailed slide type patterns with dimensions and positioning

### Script Files

- **`scripts/render-slides.py`** — Convert PPTX to PNG via LibreOffice + PDF pipeline
- **`scripts/validate-deck.py`** — Automated deck validation (slide count, font sizes, content density)
