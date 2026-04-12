# PPTX Slide Patterns

Detailed slide type patterns with dimensions and positioning for PptxGenJS. All measurements in inches for a 16:9 widescreen layout (10" x 5.625").

## Common Dimensions

| Element | Position | Notes |
|---------|----------|-------|
| Safe margin | 0.5" from all edges | Minimum clearance |
| Content area | x:0.5, y:0.5, w:9, h:4.625 | Full usable space |
| Title area | x:0.5, y:0.3, w:9, h:0.8 | Standard heading position |
| Body area | x:0.5, y:1.3, w:9, h:3.8 | Below title |

## Title Slide

```javascript
const slide = pptx.addSlide();
slide.background = { color: '0a0a0a' };

// Main title
slide.addText(title, {
  x: 0.5, y: 1.2, w: 9, h: 1.8,
  fontSize: 44, fontFace: 'Clash Display',
  color: 'ffffff', bold: true, align: 'center',
  lineSpacing: 52
});

// Subtitle
slide.addText(subtitle, {
  x: 1.5, y: 3.2, w: 7, h: 0.8,
  fontSize: 22, fontFace: 'IBM Plex Sans',
  color: '999999', align: 'center'
});

// Speaker / event info
slide.addText(`${speaker} — ${event} — ${date}`, {
  x: 1, y: 4.5, w: 8, h: 0.5,
  fontSize: 14, fontFace: 'IBM Plex Sans',
  color: '666666', align: 'center'
});
```

## Content Slide with Bullets

```javascript
const slide = pptx.addSlide();

// Heading
slide.addText(heading, {
  x: 0.5, y: 0.3, w: 9, h: 0.8,
  fontSize: 32, fontFace: 'Clash Display',
  color: 'ffffff', bold: true
});

// Accent line under heading
slide.addShape(pptx.shapes.LINE, {
  x: 0.5, y: 1.05, w: 2, h: 0,
  line: { color: '4a9eff', width: 3 }
});

// Bullet list
const bulletItems = items.map(item => ({
  text: item,
  options: {
    fontSize: 20, fontFace: 'IBM Plex Sans',
    color: 'e0e0e0', bullet: { code: '2022' },
    breakLine: true, paraSpaceAfter: 8
  }
}));

slide.addText(bulletItems, {
  x: 0.7, y: 1.3, w: 8.5, h: 3.8,
  valign: 'top', lineSpacing: 28
});
```

## Two-Column: Image + Text

```javascript
const slide = pptx.addSlide();

// Heading (full width)
slide.addText(heading, {
  x: 0.5, y: 0.3, w: 9, h: 0.8,
  fontSize: 28, fontFace: 'Clash Display',
  color: 'ffffff', bold: true
});

// Left column: text content
slide.addText(textContent, {
  x: 0.5, y: 1.3, w: 4.2, h: 3.8,
  fontSize: 18, fontFace: 'IBM Plex Sans',
  color: 'e0e0e0', valign: 'top', lineSpacing: 26
});

// Right column: image
slide.addImage({
  path: imagePath,
  x: 5.2, y: 1.2, w: 4.3, h: 4.0,
  sizing: { type: 'contain', w: 4.3, h: 4.0 },
  rounding: true
});
```

## Quote Slide

```javascript
const slide = pptx.addSlide();
slide.background = { color: '4a9eff' };

// Quote mark
slide.addText('"', {
  x: 0.5, y: 0.5, w: 1, h: 1,
  fontSize: 80, fontFace: 'Georgia',
  color: 'ffffff', bold: true
});

// Quote text
slide.addText(quote, {
  x: 1.5, y: 1.2, w: 7, h: 2.5,
  fontSize: 24, fontFace: 'IBM Plex Sans',
  color: 'ffffff', italic: true,
  lineSpacing: 36, valign: 'middle'
});

// Attribution
slide.addText(`— ${author}, ${role}`, {
  x: 1.5, y: 4.0, w: 7, h: 0.5,
  fontSize: 16, fontFace: 'IBM Plex Sans',
  color: 'e0e0ff'
});
```

## Feature Grid (2x3)

```javascript
const slide = pptx.addSlide();

slide.addText(heading, {
  x: 0.5, y: 0.2, w: 9, h: 0.7,
  fontSize: 28, fontFace: 'Clash Display',
  color: 'ffffff', bold: true, align: 'center'
});

const cols = 3, rows = 2;
const cardW = 2.7, cardH = 1.8;
const gapX = 0.3, gapY = 0.3;
const startX = (10 - cols * cardW - (cols - 1) * gapX) / 2;
const startY = 1.2;

features.forEach((feat, i) => {
  const col = i % cols;
  const row = Math.floor(i / cols);
  const x = startX + col * (cardW + gapX);
  const y = startY + row * (cardH + gapY);

  // Card background
  slide.addShape(pptx.shapes.ROUNDED_RECTANGLE, {
    x, y, w: cardW, h: cardH,
    fill: { color: '1a1a2e' },
    rectRadius: 0.1
  });

  // Feature title
  slide.addText(feat.title, {
    x: x + 0.15, y: y + 0.15, w: cardW - 0.3, h: 0.4,
    fontSize: 16, fontFace: 'Clash Display',
    color: '4a9eff', bold: true
  });

  // Feature description
  slide.addText(feat.description, {
    x: x + 0.15, y: y + 0.6, w: cardW - 0.3, h: 1.0,
    fontSize: 12, fontFace: 'IBM Plex Sans',
    color: 'cccccc', valign: 'top'
  });
});
```

## Code Slide

```javascript
const slide = pptx.addSlide();

slide.addText(heading, {
  x: 0.5, y: 0.3, w: 9, h: 0.7,
  fontSize: 28, fontFace: 'Clash Display',
  color: 'ffffff', bold: true
});

// Code block background
slide.addShape(pptx.shapes.ROUNDED_RECTANGLE, {
  x: 0.5, y: 1.2, w: 9, h: 3.8,
  fill: { color: '1e1e2e' },
  rectRadius: 0.1
});

// Code text (monospace)
slide.addText(codeText, {
  x: 0.7, y: 1.4, w: 8.6, h: 3.4,
  fontSize: 14, fontFace: 'JetBrains Mono',
  color: 'e0e0e0', valign: 'top',
  lineSpacing: 20, paraSpaceAfter: 0
});
```

## Section Divider

```javascript
const slide = pptx.addSlide();
slide.background = { color: '4a9eff' };

slide.addText(sectionTitle, {
  x: 1, y: 1.5, w: 8, h: 2.5,
  fontSize: 48, fontFace: 'Clash Display',
  color: 'ffffff', bold: true,
  align: 'center', valign: 'middle'
});
```

## Metric Highlight

```javascript
const slide = pptx.addSlide();

slide.addText(heading, {
  x: 0.5, y: 0.3, w: 9, h: 0.7,
  fontSize: 28, fontFace: 'Clash Display',
  color: 'ffffff', bold: true, align: 'center'
});

const metricW = 2.8;
const startX = (10 - metrics.length * metricW - (metrics.length - 1) * 0.3) / 2;

metrics.forEach((m, i) => {
  const x = startX + i * (metricW + 0.3);

  // Large number
  slide.addText(m.value, {
    x, y: 1.5, w: metricW, h: 1.5,
    fontSize: 48, fontFace: 'Clash Display',
    color: '4a9eff', bold: true, align: 'center'
  });

  // Label
  slide.addText(m.label, {
    x, y: 3.0, w: metricW, h: 0.5,
    fontSize: 16, fontFace: 'IBM Plex Sans',
    color: '999999', align: 'center'
  });
});
```
