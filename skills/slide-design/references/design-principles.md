# Slide Design Principles

Comprehensive guidelines for professional presentation design covering typography, color, layout, accessibility, and data visualization.

## Typography

### Hierarchy

| Element | Size Range | Weight | Purpose |
|---------|-----------|--------|---------|
| Title | 36–44pt | Bold/Black | Slide heading, immediate attention |
| Subtitle | 24–28pt | Medium | Supporting context |
| Body | 18–24pt | Regular | Main content |
| Caption | 14–16pt | Light/Regular | Annotations, sources |
| Footnote | 12pt minimum | Light | Legal, citations |

### Font Pairing Rules

- Pair a distinctive heading font with a neutral body font
- Sans-serif headings + sans-serif body: Modern, clean
- Serif headings + sans-serif body: Editorial, sophisticated
- Monospace headings + sans-serif body: Technical, developer-focused
- Never use more than 2 font families per presentation
- Ensure heading font has Bold/Black weights for impact

### Readability

- Line length: 45-75 characters per line
- Line spacing: 1.3-1.6x font size
- Paragraph spacing: 0.5-1x font size
- Left-align body text (never justify on slides)
- Center-align only titles, quotes, and short phrases

## Color

### Contrast Requirements

Follow WCAG guidelines:
- **AA standard**: 4.5:1 ratio for body text, 3:1 for large text (>18pt bold or >24pt)
- **AAA standard**: 7:1 ratio for body text (target for maximum readability)
- Test all color combinations with a contrast checker

### Color-Blind Safe Palettes

**Wong palette** (8 colors, distinguishable by all forms of color blindness):
`#000000, #E69F00, #56B4E9, #009E73, #F0E442, #0072B2, #D55E00, #CC79A7`

**IBM palette** (5 colors):
`#648FFF, #785EF0, #DC267F, #FE6100, #FFB000`

### Color Application

- **60-30-10 rule**: 60% background, 30% secondary, 10% accent
- Limit accent colors to 1-2 per presentation
- Use color consistently (same meaning throughout)
- Dark backgrounds: Light text (#e0e0e0 minimum, not pure white #ffffff)
- Light backgrounds: Dark text (#333333 minimum, not pure black #000000)

## Layout

### Grid System

- Use a 12-column grid mentally for element placement
- Maintain consistent margins (0.5" or 5% from edges)
- Align elements to an invisible grid — nothing should float randomly

### White Space

- Target 40-50% empty space per slide
- More white space = more professional
- White space guides the eye and creates breathing room
- Never fill every corner of a slide

### Visual Hierarchy

1. **Size**: Larger elements draw attention first
2. **Contrast**: High-contrast elements stand out
3. **Position**: Top-left and center attract eyes first
4. **Isolation**: Elements with surrounding space appear important
5. **Color**: Bright/saturated colors against neutral backgrounds

### Common Layouts

**Center stage**: Single centered element (title slides, quotes, key metrics)
**Split screen**: Two equal halves (comparisons, image + text)
**Asymmetric split**: 60/40 or 70/30 (content + supporting visual)
**Grid**: 2x2 or 3x2 cards (features, team members, products)
**Full bleed**: Edge-to-edge image with text overlay

## Accessibility

### Visual Accessibility

- Never rely on color alone to convey information
- Add labels, patterns, or icons alongside color coding
- Ensure sufficient contrast on all text elements
- Test with grayscale to verify information survives

### Motion Accessibility

- Respect `prefers-reduced-motion` media query
- Provide static alternatives for all animated content
- Avoid rapid flashing (no more than 3 flashes per second)
- Keep animations purposeful — enhance understanding, not decorate

### Structural Accessibility

- Use semantic HTML elements (headings, lists, figures)
- Add alt text to all images
- Ensure keyboard navigation works fully
- Maintain logical reading order

## Data Visualization

### Chart Selection

| Data Type | Best Chart | Avoid |
|-----------|-----------|-------|
| Comparison | Bar chart | Pie chart (>5 items) |
| Trend over time | Line chart | Bar chart (>10 periods) |
| Part of whole | Stacked bar, treemap | Pie (>5 slices) |
| Distribution | Histogram, box plot | Line chart |
| Relationship | Scatter plot | Bar chart |

### Simplification Rules

When adapting charts for slides:
1. Remove gridlines or make them very subtle
2. Remove axis lines if labels are present
3. Limit data series to 3-4 maximum
4. Use direct labeling instead of legends
5. Highlight the key insight with color or annotation
6. Use the largest font size possible for labels

### Progressive Disclosure

For complex data, split across multiple slides:
1. **Overview slide**: High-level chart with key takeaway
2. **Detail slide(s)**: Zoomed sections or supporting data
3. **Insight slide**: Written interpretation and implications

## Professional Polish Checklist

Before finalizing any presentation:

- [ ] Consistent font family across all slides
- [ ] Consistent color usage (accent means the same thing everywhere)
- [ ] All text meets minimum size requirements (14pt+)
- [ ] All text has sufficient contrast against background
- [ ] White space is generous and consistent
- [ ] Images are high-resolution and properly sized
- [ ] No orphaned words or awkward line breaks in headings
- [ ] Slide numbers or progress indicator present
- [ ] Speaker notes added for every content slide
- [ ] Animation timing is consistent throughout
- [ ] Tested at presentation resolution (1920x1080)
