# Style Presets

12 curated visual style presets for professional presentations. Each preset defines a complete design language: typography pair, color palette, and signature visual elements.

## How to Use

Present 3 presets to the user as visual options. Select based on audience and context:
- **Technical talks**: Dark Monospace, Neon Cyber, Terminal Green
- **Corporate/pitch**: Swiss Modern, Clean Corporate, Warm Minimal
- **Creative/editorial**: Vintage Editorial, Dark Botanical, Paper & Ink
- **Conference/bold**: Bold Signal, Gradient Wave, Midnight Blue

---

## 1. Dark Monospace

**Audience**: Developers, technical conferences
**Personality**: Hacker aesthetic, terminal-inspired

```css
:root {
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --accent: #58a6ff;
  --accent-secondary: #3fb950;
  --font-heading: 'JetBrains Mono', monospace;
  --font-body: 'IBM Plex Mono', monospace;
}
```

**Signature elements**: Faint grid background, blinking cursor animation on title, code-block-style content containers with left border accent.

---

## 2. Swiss Modern

**Audience**: Design-aware professionals, product teams
**Personality**: Bauhaus rigor, precise geometry

```css
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f5f5f5;
  --text-primary: #1a1a1a;
  --text-secondary: #666666;
  --accent: #ff3300;
  --accent-secondary: #0066ff;
  --font-heading: 'Clash Display', sans-serif;
  --font-body: 'IBM Plex Sans', sans-serif;
}
```

**Signature elements**: Visible grid lines, asymmetric layouts, red accent bars, generous white space, numbered sections.

---

## 3. Bold Signal

**Audience**: Startups, product launches, pitch decks
**Personality**: High-energy, confident, attention-grabbing

```css
:root {
  --bg-primary: #0a0a0a;
  --bg-secondary: #1a1a1a;
  --text-primary: #ffffff;
  --text-secondary: #999999;
  --accent: #ff6b35;
  --accent-secondary: #ffd700;
  --font-heading: 'Cabinet Grotesk', sans-serif;
  --font-body: 'General Sans', sans-serif;
}
```

**Signature elements**: Large numbers as navigation, gradient accent cards, bold oversized headings, orange-to-gold gradient accents.

---

## 4. Dark Botanical

**Audience**: Creative agencies, brand presentations
**Personality**: Warm sophistication, editorial elegance

```css
:root {
  --bg-primary: #1a1a1a;
  --bg-secondary: #2a2a2a;
  --text-primary: #f0ebe3;
  --text-secondary: #c9b896;
  --accent: #c9b896;
  --accent-secondary: #e8b4b8;
  --font-heading: 'Cormorant Garamond', serif;
  --font-body: 'IBM Plex Sans', sans-serif;
}
```

**Signature elements**: Soft gradient circles (radial gradients), serif/sans pairing, muted gold and pink accents, organic shapes in background.

---

## 5. Clean Corporate

**Audience**: Enterprise, B2B, internal presentations
**Personality**: Professional, trustworthy, clean

```css
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --text-primary: #212529;
  --text-secondary: #6c757d;
  --accent: #4361ee;
  --accent-secondary: #3a0ca3;
  --font-heading: 'Plus Jakarta Sans', sans-serif;
  --font-body: 'Source Sans 3', sans-serif;
}
```

**Signature elements**: Thin colored top bar, subtle diagonal background shapes, blue gradient accents, card-based layouts with soft shadows.

---

## 6. Neon Cyber

**Audience**: Tech startups, AI/ML demos, hackathons
**Personality**: Futuristic, cutting-edge, electric

```css
:root {
  --bg-primary: #0a0a1a;
  --bg-secondary: #12122a;
  --text-primary: #e0e0ff;
  --text-secondary: #8080b0;
  --accent: #00f0ff;
  --accent-secondary: #ff00aa;
  --font-heading: 'Orbitron', sans-serif;
  --font-body: 'Exo 2', sans-serif;
}
```

**Signature elements**: Neon glow effects (text-shadow), dark gradient backgrounds with subtle noise, animated scan lines, cyan/magenta accents.

---

## 7. Warm Minimal

**Audience**: Education, non-profit, wellness
**Personality**: Approachable, calm, human

```css
:root {
  --bg-primary: #faf8f5;
  --bg-secondary: #f0ece6;
  --text-primary: #2d2d2d;
  --text-secondary: #6b6b6b;
  --accent: #c05c3c;
  --accent-secondary: #4a7c6f;
  --font-heading: 'Fraunces', serif;
  --font-body: 'Outfit', sans-serif;
}
```

**Signature elements**: Warm beige tones, rounded corners, hand-drawn-style dividers, terracotta and sage accents, generous padding.

---

## 8. Vintage Editorial

**Audience**: Media, publishing, content marketing
**Personality**: Magazine-quality, storytelling

```css
:root {
  --bg-primary: #f5f0e8;
  --bg-secondary: #ebe5d9;
  --text-primary: #1a1a1a;
  --text-secondary: #555555;
  --accent: #c41e3a;
  --accent-secondary: #1a3a5c;
  --font-heading: 'Playfair Display', serif;
  --font-body: 'Lora', serif;
}
```

**Signature elements**: Drop caps, pull quotes with decorative borders, classic serif pairing, crimson accents, sepia-toned images.

---

## 9. Terminal Green

**Audience**: Security talks, DevOps, infrastructure
**Personality**: Retro terminal, matrix-inspired

```css
:root {
  --bg-primary: #0a0a0a;
  --bg-secondary: #111111;
  --text-primary: #33ff33;
  --text-secondary: #1a991a;
  --accent: #33ff33;
  --accent-secondary: #00ccff;
  --font-heading: 'Share Tech Mono', monospace;
  --font-body: 'Fira Code', monospace;
}
```

**Signature elements**: Scanline overlay, typewriter text animation, green-on-black palette, CRT curve effect (subtle border-radius on slides), blinking cursor.

---

## 10. Gradient Wave

**Audience**: SaaS demos, product showcases
**Personality**: Modern, dynamic, polished

```css
:root {
  --bg-primary: #0f0c29;
  --bg-secondary: #302b63;
  --text-primary: #ffffff;
  --text-secondary: #b8b8d0;
  --accent: #24c6dc;
  --accent-secondary: #514a9d;
  --font-heading: 'Sora', sans-serif;
  --font-body: 'Nunito Sans', sans-serif;
}
```

**Signature elements**: Animated gradient backgrounds (CSS `@keyframes`), wave SVG dividers, glass-morphism cards (backdrop-blur), purple-to-teal gradients.

---

## 11. Midnight Blue

**Audience**: Finance, enterprise, data-heavy talks
**Personality**: Authoritative, data-driven, serious

```css
:root {
  --bg-primary: #1a1f36;
  --bg-secondary: #252b48;
  --text-primary: #e0e4f0;
  --text-secondary: #8892b0;
  --accent: #6366f1;
  --accent-secondary: #22d3ee;
  --font-heading: 'Manrope', sans-serif;
  --font-body: 'DM Sans', sans-serif;
}
```

**Signature elements**: Data cards with subtle borders, chart-friendly color scheme, indigo/cyan accents, metric highlight boxes, clean grids.

---

## 12. Paper & Ink

**Audience**: Academic, research, thought leadership
**Personality**: Scholarly, thoughtful, refined

```css
:root {
  --bg-primary: #fefdfb;
  --bg-secondary: #f5f3ef;
  --text-primary: #2c2c2c;
  --text-secondary: #666666;
  --accent: #1a5276;
  --accent-secondary: #7d3c98;
  --font-heading: 'EB Garamond', serif;
  --font-body: 'Crimson Pro', serif;
}
```

**Signature elements**: Thin horizontal rules, footnote-style citations, serif-heavy typography, navy/purple accents, margin annotations, paper texture background.

---

## Atmospheric Background Recipes

Advanced CSS recipes for adding depth and texture to slide backgrounds. Mix and match with any preset for distinctive visual polish.

### Noise Texture Overlay

Adds subtle film grain for tactile, analog feel.

```css
.slide::after {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 1;
}
```

**Good for**: Dark Monospace, Terminal Green, Neon Cyber

---

### Gradient Mesh Background

Layered radial gradients create organic depth and movement.

```css
.slide {
  background:
    radial-gradient(ellipse at 20% 50%, rgba(var(--accent-rgb), 0.15) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(var(--accent2-rgb), 0.1) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 80%, rgba(var(--accent-rgb), 0.08) 0%, transparent 50%),
    var(--bg-primary);
}
```

**Good for**: Dark Botanical, Gradient Wave, Midnight Blue

---

### Geometric Grid Pattern

Clean structural lines reinforce precision and order.

```css
.slide {
  background-image: 
    linear-gradient(rgba(var(--accent-rgb), 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(var(--accent-rgb), 0.05) 1px, transparent 1px);
  background-size: 60px 60px;
}
```

**Good for**: Swiss Modern, Clean Corporate

---

### Grain Overlay (Film Effect)

Conic gradient creates photographic grain at 0.03 opacity.

```css
.slide::before {
  content: '';
  position: absolute;
  inset: 0;
  opacity: 0.03;
  background: repeating-conic-gradient(#000 0.00015%, transparent 0.0005%) 50% / 200px;
  pointer-events: none;
  mix-blend-mode: multiply;
}
```

**Good for**: Vintage Editorial, Paper & Ink, Warm Minimal

---

## Custom Preset Creation Guide

Build memorable, on-brand presets tailored to your audience.

### Step 1: Choose a Foundation
Start with the closest existing preset from the 12 above. This gives you proven color harmony, typography pairing, and signature elements to iterate from.

### Step 2: Override CSS Variables
Only modify the `:root` variables you need:
- `--bg-primary`, `--bg-secondary` for depth
- `--text-primary`, `--text-secondary` for legibility
- `--accent`, `--accent-secondary` for brand consistency
- `--font-heading`, `--font-body` for personality

Keep all other styles from the foundation preset intact.

### Step 3: Pick Distinctive Fonts
Choose from these curated free sources:
- **Fontshare** (fontshare.com) — High-quality India Type Foundry fonts, zero licensing overhead
  - Headlines: Fraunces, Clash Display, Cabinet Grotesk
  - Body: General Sans, DM Sans, Outfit
- **Google Fonts** (fonts.google.com) — Vetted open-source fonts with global support
  - Headlines: Playfair Display, Cormorant Garamond, Sora
  - Body: Lora, Source Sans 3, Nunito Sans

Avoid Inter, Space Grotesk, and Exo 2 unless they're core to your identity — they're widely used and read as generic "AI slop."

### Step 4: Test WCAG Contrast
Verify all text pairs meet **WCAG AA** (4.5:1 for body, 3:1 for large text) using:
- WebAIM Contrast Checker (webaim.org/resources/contrastchecker/)
- Chrome DevTools Lighthouse Accessibility audit
- Reference the WCAG guidelines in design-principles.md

### Step 5: Add One Atmospheric Recipe
Pick one recipe from "Atmospheric Background Recipes" above and include its CSS in your preset. This adds visual signature and prevents flat, generic designs:
- Noise Texture + dark preset = tactile sophistication
- Gradient Mesh + gradient preset = flowing elegance
- Grid Pattern + modern preset = structured precision
- Grain Overlay + editorial preset = vintage storytelling

### Step 6: Define Signature Elements
List 2–3 unique visual markers that make your preset instantly recognizable:
- Example: "Oversized pull quotes with left border accent, wavy dividers, color-field backgrounds"
- Example: "Bold section numbers, floating accent cards, animated gradient underlines"
- These become the memorable "brand" of your preset across all slides.

### Template

```css
/* MyPreset */
:root {
  --bg-primary: #...;
  --bg-secondary: #...;
  --text-primary: #...;
  --text-secondary: #...;
  --accent: #...;
  --accent-secondary: #...;
  --font-heading: '...', ...;
  --font-body: '...', ...;
}

/* Then add one atmospheric recipe CSS here */
.slide {
  /* Mix in Noise, Gradient Mesh, Grid, or Grain */
}
```

**Signature elements**: [Your 2–3 distinctive markers]
