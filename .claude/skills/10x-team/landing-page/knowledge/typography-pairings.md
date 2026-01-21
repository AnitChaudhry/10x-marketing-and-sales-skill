# Typography Pairings & Guidelines

> **Used by**: Design Agent
> **When**: Selecting fonts based on brand personality

---

## Font Pairing Rules

1. **Contrast in style**: Pair serif with sans-serif OR different sans weights
2. **Similar x-height**: Fonts should feel related
3. **Maximum 2-3 fonts**: Headings, body, accent (optional)
4. **Match the mood**: Fonts carry personality

---

## Recommended Pairings by Brand Personality

### Professional / Corporate / SaaS
```
Headings: Inter (600-700)
Body: Inter (400)
Why: Clean, neutral, highly readable
Google Fonts: https://fonts.google.com/specimen/Inter
```

### Modern / Tech / Cutting-edge
```
Headings: Space Grotesk (600) or Satoshi (700)
Body: Inter (400) or DM Sans (400)
Why: Geometric, contemporary feel
```

### Friendly / Startup / Approachable
```
Headings: DM Sans (700) or Nunito (700)
Body: DM Sans (400)
Why: Rounded, welcoming, approachable
```

### Premium / Luxury / Sophisticated
```
Headings: Playfair Display (600) or Cormorant (600)
Body: Lato (400) or Source Sans (400)
Why: Elegant contrast between serif and sans
```

### Creative / Agency / Artistic
```
Headings: Fraunces (600) or Clash Display (600)
Body: DM Sans (400)
Why: Distinctive personality, memorable
```

### Minimal / Clean / Essential
```
Headings: System fonts or Inter (500)
Body: System fonts or Inter (400)
Why: No distraction, pure content focus
```

---

## Type Scale (Responsive)

```json
{
  "scale": {
    "h1": "clamp(2.5rem, 5vw, 4rem)",
    "h2": "clamp(2rem, 4vw, 3rem)",
    "h3": "clamp(1.5rem, 3vw, 2rem)",
    "h4": "clamp(1.25rem, 2vw, 1.5rem)",
    "body": "1rem",
    "bodyLarge": "1.125rem",
    "small": "0.875rem",
    "tiny": "0.75rem"
  },
  "lineHeight": {
    "headings": "1.2",
    "body": "1.6"
  },
  "letterSpacing": {
    "headings": "-0.02em",
    "body": "0",
    "uppercase": "0.05em"
  }
}
```

---

## Font Resources

### Free Fonts
- **Google Fonts**: fonts.google.com (largest free repository)
- **FontShare**: fontshare.com (high-quality free fonts)
- **Adobe Fonts**: Included with Creative Cloud subscription

### Identifying Fonts
- **WhatFont**: Chrome/Firefox plugin to identify fonts on websites

---

## Typography CSS Template

```css
:root {
  --font-heading: 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;

  --text-h1: clamp(2.5rem, 5vw, 4rem);
  --text-h2: clamp(2rem, 4vw, 3rem);
  --text-h3: clamp(1.5rem, 3vw, 2rem);
  --text-body: 1rem;

  --leading-tight: 1.2;
  --leading-normal: 1.6;
}

h1, h2, h3, h4 {
  font-family: var(--font-heading);
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
}

body {
  font-family: var(--font-body);
  font-size: var(--text-body);
  line-height: var(--leading-normal);
}
```

---

## Font Weight Guidelines

| Use Case | Weight |
|----------|--------|
| Hero headline | 700 (Bold) |
| Section headers | 600 (Semi-bold) |
| Subheads | 500 (Medium) |
| Body text | 400 (Regular) |
| Secondary text | 400 (Regular) |
| Buttons/CTAs | 600 (Semi-bold) |

---

## Accessibility Considerations

- Minimum body font size: 16px (1rem)
- Sufficient line-height: 1.5+ for body text
- Adequate contrast: Dark text on light, or vice versa
- Avoid all-caps for long text (harder to read)
- Don't rely on font style alone to convey meaning
