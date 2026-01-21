# Color Psychology & Palette Creation

> **Used by**: Design Agent
> **When**: Selecting colors based on brand personality

---

## Color Meanings

| Color | Associations | Best For |
|-------|-------------|----------|
| **Blue** | Trust, stability, professionalism, calm | Finance, tech, healthcare, corporate |
| **Green** | Growth, health, money, success, nature | Finance, health, eco, startups |
| **Purple** | Luxury, creativity, wisdom, royalty | Premium brands, creative, beauty |
| **Red** | Energy, urgency, passion, excitement | Sales, food, entertainment |
| **Orange** | Friendly, energetic, affordable, warm | Startups, e-commerce, youth brands |
| **Yellow** | Optimism, clarity, warmth, attention | Caution, highlights, cheerful brands |
| **Black** | Sophistication, power, elegance, luxury | Premium, fashion, tech |
| **White** | Clean, simple, modern, pure | Minimal brands, tech, healthcare |

---

## Brand Personality → Color Mapping

### Trustworthy / Professional / Authoritative
```
Primary: Blues, navys (#1e40af, #1e3a8a)
Secondary: Grays, whites
Accent: Subtle green or gold
```

### Modern / Sleek / Cutting-edge
```
Primary: Dark backgrounds (#0f172a, #18181b)
Secondary: Gradients, neon accents
Accent: Electric blue, purple, cyan
```

### Friendly / Warm / Approachable
```
Primary: Warm blues (#3b82f6), soft greens
Secondary: Warm neutrals, cream
Accent: Orange, coral, yellow
```

### Premium / Luxury / Sophisticated
```
Primary: Black, deep navy, burgundy
Secondary: Gold, cream, white
Accent: Metallic tones, subtle gradients
```

### Simple / Clean / Minimal
```
Primary: White, light grays
Secondary: One accent color only
Accent: Bold single color (blue, black)
```

### Creative / Playful / Quirky
```
Primary: Unexpected combinations
Secondary: Brights, pastels
Accent: Multiple bold colors
```

---

## Palette Structure

```json
{
  "brand": {
    "primary": "#____",      // Main brand color
    "primaryLight": "#____", // Hover states, backgrounds
    "primaryDark": "#____",  // Active states, text on light
    "secondary": "#____",    // Supporting color
    "accent": "#____"        // Highlights, CTAs
  },
  "neutral": {
    "white": "#FFFFFF",
    "background": "#____",   // Page background
    "surface": "#____",      // Card backgrounds
    "border": "#____",       // Dividers, borders
    "textPrimary": "#____",  // Main text
    "textSecondary": "#____",// Secondary text
    "textMuted": "#____"     // Hints, placeholders
  },
  "semantic": {
    "success": "#22c55e",
    "warning": "#f59e0b",
    "error": "#ef4444",
    "info": "#3b82f6"
  }
}
```

---

## Accessibility Requirements

### Contrast Ratios (WCAG AA)
- **Normal text**: 4.5:1 minimum
- **Large text** (18px+ or 14px bold): 3:1 minimum
- **Interactive elements**: Must be distinguishable

### Tools for Checking
- WebAIM Contrast Checker
- Figma Contrast plugin
- Chrome DevTools

---

## Gradient Guidelines

### When to Use Gradients
- Modern/tech brands
- Hero backgrounds
- CTAs for emphasis
- Accent elements

### Creating Good Gradients
- Span 30-60° on the color wheel for vibrant
- Use analogous colors for subtle
- Avoid muddy middle tones
- Test at different screen sizes

---

## Color Variation Tips

### Creating Tints (Lighter)
- Add white, increase lightness
- Use for backgrounds, hover states

### Creating Shades (Darker)
- Add black, decrease lightness
- Use for text, active states, depth

### Creating Tones (Muted)
- Add gray, reduce saturation
- Use for secondary elements, disabled states
