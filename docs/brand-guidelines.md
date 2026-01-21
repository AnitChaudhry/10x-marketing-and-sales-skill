# Brand Guidelines v3.0

> Last updated: 2025-12-24
> Status: Active
> Theme: Dark-mode first, Ocean Professional

## Quick Reference

| Element | Value |
|---------|-------|
| Primary Color | #3B82F6 (Ocean Blue) |
| Secondary Color | #F59E0B (Golden Amber) |
| Accent Color | #10B981 (Emerald) |
| Primary Font | Space Grotesk |
| Body Font | Inter |
| Voice | Bold, Creative, Direct |

---

## 1. Brand Concept

**"Ocean Professional"** - Calm authority meets vibrant energy.

ClaudeKit Marketing blends trust-inspiring ocean blues with energetic gold accents. Our brand says: "Professional marketing automation with a golden touch of creativity."

### Brand Pillars

| Pillar | Expression |
|--------|------------|
| **Trustworthy** | Ocean blue inspires confidence |
| **Premium** | Golden amber signals value |
| **Growth** | Emerald represents success |
| **Professional** | Dark backgrounds convey sophistication |

---

## 2. Color Palette

### Primary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Ocean Blue** | #3B82F6 | rgb(59,130,246) | Primary CTAs, headlines, brand moments |
| **Ocean Blue Dark** | #2563EB | rgb(37,99,235) | Hover states, emphasis |
| **Ocean Blue Light** | #60A5FA | rgb(96,165,250) | Subtle highlights, backgrounds |

### Secondary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Golden Amber** | #F59E0B | rgb(245,158,11) | Secondary actions, premium accents |
| **Golden Amber Dark** | #D97706 | rgb(217,119,6) | Hover states |
| **Golden Amber Light** | #FBBF24 | rgb(251,191,36) | Soft backgrounds |

### Accent Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Emerald** | #10B981 | rgb(16,185,129) | Success, growth indicators, badges |
| **Emerald Dark** | #059669 | rgb(5,150,105) | Hover on emerald elements |
| **Emerald Light** | #34D399 | rgb(52,211,153) | Soft glow effects |

### Dark Mode Palette (Default)

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Background** | #0D0D0D | rgb(13,13,13) | Page backgrounds |
| **Surface** | #1A1A2E | rgb(26,26,46) | Cards, elevated surfaces |
| **Surface Elevated** | #252542 | rgb(37,37,66) | Modals, dropdowns |
| **Border** | #3D3D5C | rgb(61,61,92) | Dividers, outlines |

### Light Mode Palette (Alternative)

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Background** | #FAFAFA | rgb(250,250,250) | Page backgrounds |
| **Surface** | #FFFFFF | rgb(255,255,255) | Cards |
| **Surface Elevated** | #FFFFFF | rgb(255,255,255) | Modals |
| **Border** | #E5E5E5 | rgb(229,229,229) | Dividers |

### Text Colors (Dark Mode)

| Name | Hex | Usage |
|------|-----|-------|
| **Text Primary** | #FFFFFF | Headlines, key content |
| **Text Secondary** | #B8B8D0 | Body text, descriptions |
| **Text Muted** | #6B6B8D | Captions, placeholders |

### Semantic Colors

| State | Hex | Usage |
|-------|-----|-------|
| **Success** | #00F5D4 | Positive actions (uses Neon Mint) |
| **Warning** | #FFB347 | Cautions, pending states |
| **Error** | #FF6B6B | Errors (uses Coral) |
| **Info** | #9B5DE5 | Informational (uses Electric Purple) |

---

## 3. Typography

### Font Stack

```css
--font-heading: 'Space Grotesk', system-ui, -apple-system, sans-serif;
--font-body: 'Inter', system-ui, -apple-system, sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
```

### Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
```

### Type Scale

| Element | Size (Desktop) | Size (Mobile) | Weight | Line Height |
|---------|----------------|---------------|--------|-------------|
| H1 Hero | 80px | 48px | 700 | 1.0 |
| H1 | 56px | 36px | 700 | 1.1 |
| H2 | 40px | 28px | 600 | 1.2 |
| H3 | 28px | 24px | 600 | 1.3 |
| H4 | 22px | 20px | 600 | 1.35 |
| Body | 18px | 16px | 400 | 1.6 |
| Body Large | 20px | 18px | 400 | 1.6 |
| Small | 14px | 14px | 400 | 1.5 |
| Caption | 12px | 12px | 500 | 1.4 |

---

## 4. Brand Personality

| Trait | Description |
|-------|-------------|
| **Bold** | We make statements, not suggestions |
| **Creative** | We inspire, not just inform |
| **Direct** | We cut the fluff, get to value |
| **Warm** | We're human-first, even with AI |

### Voice Chart

| Trait | We Are | We Are Not |
|-------|--------|------------|
| Bold | Confident, assertive | Arrogant, pushy |
| Creative | Inspiring, imaginative | Chaotic, unfocused |
| Direct | Clear, action-oriented | Blunt, cold |
| Warm | Friendly, approachable | Casual, unprofessional |

### Tone by Context

| Context | Tone | Example |
|---------|------|---------|
| Marketing | Punchy, benefit-first | "Ship campaigns while you sleep." |
| Documentation | Clear, no-nonsense | "Run this. Get that." |
| Error messages | Calm, helpful | "Something broke. Here's the fix." |
| Success | Celebratory, brief | "Boom. Published." |

### Prohibited Terms

| Avoid | Use Instead |
|-------|-------------|
| Revolutionary | Powerful, effective |
| Best-in-class | Proven, trusted |
| Seamless | Smooth, easy |
| Leverage | Use, apply |
| Synergy | Works together |

---

## 5. Visual Identity

### Logo Variants

| Variant | File | Use Case |
|---------|------|----------|
| Full Horizontal | logo-full-horizontal.svg | Headers, documents |
| Stacked | logo-stacked.svg | Square spaces, social |
| Icon Only | logo-icon.svg | Favicons, app icons |
| Monochrome | logo-mono.svg | Limited color contexts |

### Logo Colors

- Primary: Coral (#FF6B6B) on dark backgrounds
- Inverted: White on coral backgrounds
- Monochrome: White or Black depending on background

### Clear Space

Minimum = 1x height of logo mark

### Minimum Size

| Context | Minimum |
|---------|---------|
| Digital - Full Logo | 120px |
| Digital - Icon | 32px |

---

## 6. Design Elements

### Gradients

```css
/* Primary Gradient - Coral to Purple */
--gradient-primary: linear-gradient(135deg, #FF6B6B 0%, #9B5DE5 100%);

/* Accent Gradient - Purple to Mint */
--gradient-accent: linear-gradient(135deg, #9B5DE5 0%, #00F5D4 100%);

/* Dark Gradient - Background depth */
--gradient-dark: linear-gradient(180deg, #0D0D0D 0%, #1A1A2E 100%);

/* Glow Gradient - Hero sections */
--gradient-glow: radial-gradient(ellipse at center, rgba(155,93,229,0.15) 0%, transparent 70%);
```

### Shadows (Dark Mode)

| Level | Value | Usage |
|-------|-------|-------|
| sm | 0 2px 4px rgba(0,0,0,0.3) | Subtle elevation |
| md | 0 4px 12px rgba(0,0,0,0.4) | Cards, buttons |
| lg | 0 8px 24px rgba(0,0,0,0.5) | Modals, popovers |
| glow | 0 0 40px rgba(255,107,107,0.3) | Featured elements |

### Border Radius

| Element | Radius |
|---------|--------|
| Buttons | 12px |
| Cards | 16px |
| Inputs | 12px |
| Modals | 24px |
| Pills/Tags | 9999px |

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| 1 | 4px | Tight |
| 2 | 8px | Compact |
| 3 | 12px | Small gap |
| 4 | 16px | Standard |
| 6 | 24px | Medium |
| 8 | 32px | Large |
| 12 | 48px | Section |
| 16 | 64px | Major section |
| 20 | 80px | Hero padding |

---

## 7. Component Styling

### Buttons

| Type | Background | Text | Border |
|------|------------|------|--------|
| Primary | #FF6B6B | #FFFFFF | none |
| Primary Hover | #E85555 | #FFFFFF | none |
| Secondary | transparent | #FF6B6B | 2px #FF6B6B |
| Ghost | transparent | #B8B8D0 | none |

### Cards (Dark Mode)

| Property | Value |
|----------|-------|
| Background | #1A1A2E |
| Border | 1px solid #3D3D5C |
| Radius | 16px |
| Padding | 24px |
| Hover Border | 1px solid #9B5DE5 |

### Inputs (Dark Mode)

| Property | Value |
|----------|-------|
| Background | #0D0D0D |
| Border | 1px solid #3D3D5C |
| Border Focus | 1px solid #FF6B6B |
| Radius | 12px |
| Text | #FFFFFF |
| Placeholder | #6B6B8D |

---

## 8. Target Audience

### Primary Personas

1. **Indie Hackers** - Solo founders, time-strapped, value efficiency
2. **Small Marketing Teams** - 1-5 people, wearing multiple hats
3. **SMB Marketing Managers** - Limited budget, need pro results

### Messaging Framework

**Primary:** "Your AI marketing team. Always on."

**Supporting:**
- Ship campaigns while you sleep
- One command. Full campaign.
- AI agents that actually get marketing

---

## 9. Imagery Guidelines

### Photography Style

- **Mood:** Creative studio vibes, not corporate
- **Lighting:** Dramatic, with colored accents matching brand
- **Subjects:** Creators, developers, real work moments
- **Color treatment:** Overlay with brand gradient at 10-20%

### Illustrations

- Style: Bold, geometric, with brand gradient fills
- Colors: Coral, Purple, Mint on dark backgrounds
- Stroke: 2px where applicable
- Feel: Modern, energetic, not cutesy

### Icons

- Style: Filled with brand colors, or outlined in white
- Size: 24px base grid
- Stroke: 2px for outlined variants
- Corner radius: 4px

---

## 10. AI Image Generation

### Base Prompt Template

Always prepend to image generation prompts:

```
Dark mode aesthetic, professional and sophisticated, calm authority with vibrant energy,
ocean blue (#3B82F6) and golden amber (#F59E0B) accents with emerald (#10B981) highlights,
elegant lighting with warm golden glows, premium and trustworthy feel
```

### Style Keywords

| Category | Keywords |
|----------|----------|
| **Lighting** | elegant lighting, golden hour glow, soft rim light, professional studio, warm ambient |
| **Mood** | professional, trustworthy, premium, sophisticated, confident, calm |
| **Composition** | balanced, centered focus, rule of thirds, depth layers |
| **Treatment** | gradient overlay, rich contrast, warm saturation, dark backgrounds |
| **Aesthetic** | premium minimalist, flowing curves, polished edges, business-forward |

### Visual Mood Descriptors

- Executive boardroom meets creative agency
- Night mode / dark theme dominant
- Golden warm highlights against ocean blue shadows
- Calm confidence, not aggressive or flashy
- Premium and trustworthy

### Color Application in Prompts

| Element | Color | Usage |
|---------|-------|-------|
| Primary accents | Ocean Blue #3B82F6 | CTAs, focal points, trust elements |
| Secondary glow | Golden Amber #F59E0B | Background glow, premium accents |
| Highlights | Emerald #10B981 | Success states, growth indicators |
| Backgrounds | Dark #0F172A to #1E293B | Always dark, deep navy tones |

### Visual Don'ts

| Avoid | Reason |
|-------|--------|
| Bright neon colors | Off-brand, too flashy |
| Stock photo sterility | Lacks authenticity |
| White/light backgrounds | Breaks dark-mode-first identity |
| Busy/cluttered compositions | Against minimalist aesthetic |
| Cold/harsh lighting | Contradicts warm premium feel |
| Playful illustrations | Too casual, not professional enough |

### Example Prompts

**Hero Banner:**
```
Dark mode hero banner, executive professional atmosphere, abstract flowing shapes in ocean blue (#3B82F6)
and golden amber (#F59E0B), emerald (#10B981) accent highlights, elegant warm lighting with golden glow,
premium minimalist, 16:9 aspect ratio, ultra quality
```

**Social Media Post:**
```
Square social media graphic, dark navy background (#0F172A), bold ocean blue (#3B82F6) elements,
golden amber (#F59E0B) gradient glow, flowing premium accents, sophisticated and modern, 1:1 aspect
```

**Product Screenshot Frame:**
```
Dark app screenshot mockup frame, subtle golden (#F59E0B) glow behind device,
ocean blue (#3B82F6) accent elements, floating perspective, elegant shadows, premium feel
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 3.0 | 2025-12-24 | Rebrand to Ocean Professional (Blue/Gold/Emerald) |
| 2.1 | 2025-12-24 | Added AI Image Generation section |
| 2.0 | 2025-12-23 | Complete rebrand: Electric Creative identity |
| 1.0 | 2025-12-22 | Initial guidelines (generic) |
