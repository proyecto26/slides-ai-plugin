# PptxGenJS Helper Functions Reference

API reference for the PptxGenJS helper library used in programmatic PowerPoint generation.

## Setup

```javascript
const pptxgen = require('pptxgenjs');
const pptx = new pptxgen();

// Set defaults
pptx.defineSection({ title: 'Main' });
pptx.layout = 'LAYOUT_WIDE'; // 13.33" x 7.5" (or use LAYOUT_16x9 for 10" x 5.625")
```

## Slide Dimensions

```javascript
function getSlideDimensions(slide, pptx) {
  // Returns { width, height } in inches
  // Handles EMU to inch conversion
  const layout = pptx.layout;
  if (layout === 'LAYOUT_WIDE') return { width: 13.33, height: 7.5 };
  if (layout === 'LAYOUT_16x9') return { width: 10, height: 5.625 };
  if (layout === 'LAYOUT_4x3') return { width: 10, height: 7.5 };
  return { width: 10, height: 5.625 }; // default
}
```

## Text Measurement

### measureText

Measure text dimensions using skia-canvas for font-aware precision:

```javascript
const { Canvas } = require('skia-canvas');

function measureText(text, fontFamily, fontSize) {
  const canvas = new Canvas(1, 1);
  const ctx = canvas.getContext('2d');
  ctx.font = `${fontSize}pt ${fontFamily}`;
  const metrics = ctx.measureText(text);
  return {
    width: metrics.width / 72, // Convert to inches
    height: fontSize / 72      // Approximate height
  };
}
```

### autoFontSize

Binary search for optimal font size to fit text in a box:

```javascript
function autoFontSize(text, box, fontFamily, options = {}) {
  const { minSize = 10, maxSize = 72, mode = 'shrink' } = options;
  let low = minSize;
  let high = maxSize;

  while (high - low > 0.5) {
    const mid = (low + high) / 2;
    const measured = measureText(text, fontFamily, mid);
    if (measured.width <= box.width && measured.height <= box.height) {
      low = mid; // Can go bigger
    } else {
      high = mid; // Too big
    }
  }

  return mode === 'shrink' ? Math.min(low, maxSize) : low;
}
```

### calcTextBoxHeightSimple

Analytical height calculation for a text box:

```javascript
function calcTextBoxHeightSimple(text, widthInches, fontSize, leading = 1.2) {
  const charsPerLine = Math.floor(widthInches * 72 / (fontSize * 0.6)); // Approximate
  const lines = Math.ceil(text.length / charsPerLine);
  const lineHeight = (fontSize / 72) * leading;
  return lines * lineHeight;
}
```

## Layout Builders

### addImageTextCard

Create an image + caption card component:

```javascript
function addImageTextCard(slide, options) {
  const { x, y, w, h, imagePath, title, description, imageHeight = 0.6 } = options;
  const imgH = h * imageHeight;
  const textH = h - imgH - 0.1;

  slide.addImage({ path: imagePath, x, y, w, h: imgH, sizing: { type: 'contain' } });
  slide.addText(title, {
    x, y: y + imgH + 0.05, w, h: 0.4,
    fontSize: 14, bold: true, align: 'center'
  });
  if (description) {
    slide.addText(description, {
      x, y: y + imgH + 0.45, w, h: textH - 0.45,
      fontSize: 11, color: '666666', align: 'center'
    });
  }
}
```

### addCardRow

Row of cards with auto-spacing:

```javascript
function addCardRow(slide, cards, region, options = {}) {
  const { gap = 0.2, align = 'center' } = options;
  const cardWidth = (region.w - gap * (cards.length - 1)) / cards.length;

  cards.forEach((card, i) => {
    const x = region.x + i * (cardWidth + gap);
    addImageTextCard(slide, {
      x, y: region.y, w: cardWidth, h: region.h,
      ...card
    });
  });
}
```

### addTimeline

Horizontal timeline with markers:

```javascript
function addTimeline(slide, milestones, region) {
  const { x, y, w, h } = region;
  const lineY = y + h * 0.4;
  const spacing = w / (milestones.length - 1 || 1);

  // Draw horizontal line
  slide.addShape(pptx.shapes.LINE, {
    x, y: lineY, w, h: 0,
    line: { color: '4a9eff', width: 2 }
  });

  milestones.forEach((m, i) => {
    const mx = x + i * spacing;

    // Marker circle
    slide.addShape(pptx.shapes.OVAL, {
      x: mx - 0.08, y: lineY - 0.08, w: 0.16, h: 0.16,
      fill: { color: '4a9eff' }
    });

    // Year/label above
    slide.addText(m.label, {
      x: mx - 0.5, y: lineY - 0.5, w: 1, h: 0.35,
      fontSize: 12, bold: true, align: 'center'
    });

    // Description below
    slide.addText(m.description, {
      x: mx - 0.6, y: lineY + 0.15, w: 1.2, h: 0.5,
      fontSize: 10, color: '666666', align: 'center'
    });
  });
}
```

## Validation Functions

### warnIfSlideHasOverlaps

Detect overlapping elements with geometry analysis:

```javascript
function warnIfSlideHasOverlaps(slide) {
  const elements = slide._slideObjects || [];
  const warnings = [];

  for (let i = 0; i < elements.length; i++) {
    for (let j = i + 1; j < elements.length; j++) {
      const a = elements[i].options;
      const b = elements[j].options;
      if (!a || !b) continue;

      const overlap = !(
        a.x + a.w <= b.x ||
        b.x + b.w <= a.x ||
        a.y + a.h <= b.y ||
        b.y + b.h <= a.y
      );

      if (overlap) {
        warnings.push({
          elementA: i,
          elementB: j,
          message: `Elements ${i} and ${j} overlap at (${a.x},${a.y}) and (${b.x},${b.y})`
        });
      }
    }
  }

  return warnings;
}
```

### warnIfSlideElementsOutOfBounds

Check elements stay within slide boundaries:

```javascript
function warnIfSlideElementsOutOfBounds(slide, pptx) {
  const dims = getSlideDimensions(slide, pptx);
  const elements = slide._slideObjects || [];
  const warnings = [];

  elements.forEach((el, i) => {
    const o = el.options;
    if (!o || o.x === undefined) return;

    if (o.x < 0 || o.y < 0 || o.x + o.w > dims.width || o.y + o.h > dims.height) {
      warnings.push({
        element: i,
        message: `Element ${i} extends beyond slide bounds: (${o.x}, ${o.y}, ${o.w}x${o.h}) vs slide (${dims.width}x${dims.height})`
      });
    }
  });

  return warnings;
}
```

## Image Helpers

### imageSizingContain

Contain image within bounds preserving aspect ratio:

```javascript
function imageSizingContain(maxWidth, maxHeight, imgWidth, imgHeight) {
  const ratio = Math.min(maxWidth / imgWidth, maxHeight / imgHeight);
  return {
    w: imgWidth * ratio,
    h: imgHeight * ratio,
    type: 'contain'
  };
}
```

### imageSizingCrop

Crop image to fill bounds:

```javascript
function imageSizingCrop(targetWidth, targetHeight) {
  return {
    w: targetWidth,
    h: targetHeight,
    type: 'cover'
  };
}
```

## Alignment Utilities

```javascript
function alignSlideElements(elements, axis, alignment) {
  if (axis === 'x') {
    const ref = alignment === 'left' ? Math.min(...elements.map(e => e.x))
              : alignment === 'right' ? Math.max(...elements.map(e => e.x + e.w))
              : elements.reduce((s, e) => s + e.x + e.w / 2, 0) / elements.length;

    elements.forEach(e => {
      if (alignment === 'left') e.x = ref;
      else if (alignment === 'right') e.x = ref - e.w;
      else e.x = ref - e.w / 2;
    });
  }
  // Similar for y axis
}

function distributeSlideElements(elements, axis) {
  if (elements.length < 3) return;
  const sorted = [...elements].sort((a, b) => a[axis] - b[axis]);
  const totalSpan = sorted[sorted.length - 1][axis] - sorted[0][axis];
  const spacing = totalSpan / (elements.length - 1);

  sorted.forEach((el, i) => {
    el[axis] = sorted[0][axis] + i * spacing;
  });
}
```
