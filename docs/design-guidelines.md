# Design Guidelines

This document defines the visual design system for ClaudeKit Marketing.

## Color System

### Primary Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Primary | `#6366F1` | CTAs, links, interactive elements |
| Primary Dark | `#4F46E5` | Hover states, emphasis |
| Primary Light | `#A5B4FC` | Backgrounds, highlights |

### Neutral Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Gray 900 | `#111827` | Primary text |
| Gray 700 | `#374151` | Secondary text |
| Gray 500 | `#6B7280` | Tertiary text, icons |
| Gray 200 | `#E5E7EB` | Borders, dividers |
| Gray 50 | `#F9FAFB` | Backgrounds |

### Semantic Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Success | `#10B981` | Success states, positive indicators |
| Warning | `#F59E0B` | Warnings, attention needed |
| Error | `#EF4444` | Errors, destructive actions |
| Info | `#3B82F6` | Information, tips |

## Typography

### Font Stack

```css
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
```

### Type Scale

| Size | Class | Usage |
|------|-------|-------|
| 48px | `text-5xl` | Hero headlines |
| 36px | `text-4xl` | Page titles |
| 30px | `text-3xl` | Section headers |
| 24px | `text-2xl` | Subsection headers |
| 20px | `text-xl` | Card titles |
| 16px | `text-base` | Body text |
| 14px | `text-sm` | Secondary text |
| 12px | `text-xs` | Captions, labels |

### Line Heights

- Headlines: `1.2`
- Body text: `1.6`
- UI elements: `1.4`

## Spacing System

Based on 4px base unit:

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | 4px | Tight spacing |
| `space-2` | 8px | Default spacing |
| `space-3` | 12px | Component padding |
| `space-4` | 16px | Section padding |
| `space-6` | 24px | Group spacing |
| `space-8` | 32px | Section margins |
| `space-12` | 48px | Page sections |

## Component Patterns

### Buttons

```css
/* Primary Button */
.btn-primary {
  background: #6366F1;
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 500;
}

/* Secondary Button */
.btn-secondary {
  background: transparent;
  border: 1px solid #E5E7EB;
  color: #374151;
  padding: 12px 24px;
  border-radius: 8px;
}
```

### Cards

```css
.card {
  background: white;
  border: 1px solid #E5E7EB;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
```

### Inputs

```css
.input {
  border: 1px solid #E5E7EB;
  border-radius: 8px;
  padding: 12px 16px;
  font-size: 16px;
}

.input:focus {
  border-color: #6366F1;
  outline: none;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}
```

## Layout Grid

### Container Widths

| Breakpoint | Max Width |
|------------|-----------|
| Mobile | 100% - 32px padding |
| Tablet | 768px |
| Desktop | 1024px |
| Wide | 1280px |

### Grid System

12-column grid with:
- Gutter: 24px
- Column: Flexible

## Iconography

### Icon Style

- Style: Outline (2px stroke)
- Size: 24px default
- Corner radius: 2px
- Stroke linecap: Round

### Recommended Icon Libraries

1. Heroicons (primary)
2. Lucide Icons (alternative)

## Imagery

### Photography Style

- Clean, modern backgrounds
- Professional but approachable
- Diverse representation
- Natural lighting preferred

### Illustrations

- Flat design with subtle gradients
- Primary color palette
- Simple, abstract shapes
- Consistent stroke weight

## Motion

### Timing

| Type | Duration | Easing |
|------|----------|--------|
| Micro | 100ms | ease-out |
| Standard | 200ms | ease-in-out |
| Complex | 300ms | ease-in-out |
| Page | 400ms | ease-in-out |

### Transitions

```css
/* Default transition */
transition: all 200ms ease-in-out;

/* Button hover */
transition: background 100ms ease-out;

/* Modal/overlay */
transition: opacity 200ms ease-in-out, transform 200ms ease-in-out;
```

## Responsive Design

### Breakpoints

| Name | Width | Description |
|------|-------|-------------|
| sm | 640px | Small devices |
| md | 768px | Tablets |
| lg | 1024px | Desktops |
| xl | 1280px | Large screens |
| 2xl | 1536px | Wide screens |

### Mobile-First Approach

1. Design for mobile first
2. Add complexity for larger screens
3. Touch-friendly targets (min 44px)
4. Consider thumb zones

## Accessibility

### Requirements

- WCAG 2.1 AA compliance minimum
- Color contrast: 4.5:1 for text
- Focus indicators visible
- Alt text for all images
- Keyboard navigation support

### Color Contrast Examples

| Text Color | Background | Ratio | Pass |
|------------|------------|-------|------|
| Gray 900 | White | 16:1 | ✅ |
| Gray 700 | White | 9:1 | ✅ |
| Primary | White | 5:1 | ✅ |
| Gray 500 | White | 4.6:1 | ✅ |

## Dark Mode (Optional)

### Dark Palette

| Light | Dark |
|-------|------|
| Gray 50 | Gray 900 |
| Gray 900 | Gray 50 |
| White | Gray 800 |
| Primary | Primary (unchanged) |

## Usage with Agents

When agents reference design guidelines:

1. **Content Creator**: Follow typography and spacing
2. **Social Media Manager**: Use brand colors in graphics
3. **UI/UX Designer**: Apply full design system
4. **Campaign Manager**: Ensure visual consistency

## Updates

Review quarterly with brand team. Track design system usage and gather feedback for improvements.
