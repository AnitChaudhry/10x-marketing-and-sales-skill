# Visual Interest Techniques

> **Used by**: Design Agent, Build Agent
> **When**: Adding visual polish and differentiation

---

## Text Effects

### Handwritten Annotation
Circles, arrows, underlines with hand-drawn feel.
```css
/* Use SVG assets or custom brush strokes */
```

### Gradient Text
Colorful gradient fill on headings.
```css
.gradient-text {
  background: linear-gradient(90deg, #3b82f6, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

### Non-standard Bullet Points
Icons instead of standard bullets.
```html
<ul class="custom-bullets">
  <li>✓ Feature one</li>
  <li>✓ Feature two</li>
</ul>
```

### Font-change as Highlight
Different font/style for emphasis words.
```html
<h1>The <em class="highlight-font">fastest</em> way to ship</h1>
```

### Bold Stats
Large numbers with smaller labels.
```html
<div class="stat">
  <span class="stat-number">10K+</span>
  <span class="stat-label">Happy customers</span>
</div>
```

---

## UI Depth Effects

### Card Shadows
Layered shadow for depth.
```css
.card {
  box-shadow:
    0 1px 2px rgba(0,0,0,0.05),
    0 4px 6px rgba(0,0,0,0.05),
    0 10px 20px rgba(0,0,0,0.1);
}
```

### Glassmorphism
Frosted glass effect.
```css
.glass {
  background: rgba(255,255,255,0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.2);
}
```

### Border Sheen
Gradient border for premium feel.
```css
.sheen-border {
  border: 1px solid transparent;
  background: linear-gradient(white, white) padding-box,
              linear-gradient(135deg, #ddd, #fff, #ddd) border-box;
}
```

### 3D / Mockups
Product screenshots in device frames or perspective.

---

## Background Techniques

### Subtle Gradient
Barely noticeable color shift.
```css
body {
  background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
}
```

### Mesh Gradient
Organic, multi-point gradient blobs.

### Dot Grid
Subtle repeating dot pattern.
```css
.dot-grid {
  background-image: radial-gradient(#e5e7eb 1px, transparent 1px);
  background-size: 20px 20px;
}
```

### Visible Grid
Light lines creating structure.
```css
.line-grid {
  background-image:
    linear-gradient(rgba(0,0,0,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,0,0,0.03) 1px, transparent 1px);
  background-size: 40px 40px;
}
```

### Noise Texture
Subtle grain for warmth.
```css
.noise {
  background-image: url('noise.png');
  opacity: 0.03;
}
```

---

## Decorative Elements

### Icon Decoration
Geometric shapes behind/around icons.

### Blob Backgrounds
Organic shapes as section backgrounds.

### XL Text
Oversized typography as visual element.

### XL Shape
Large, low-opacity geometric shape.

---

## Image Techniques

### Frame Break
Image element extends beyond its container.

### Background Removal
Subject on transparent/solid background.

### Duotone
Two-color treatment of photos.

### Shape Masking
Image clipped to blob or geometric shape.

### Gradient Masking
Image fades to transparent at edges.

---

## Interactive Effects

### Hover Lift
```css
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.15);
}
```

### Scroll Animations
Elements fade/slide in on scroll.
```css
.animate-on-scroll {
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.5s ease;
}
.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Button Styles
Various button treatments:
- Gradient fill
- Border with hover fill
- Shadow lift on hover
- Icon animation

---

## When to Use What

| Brand Feel | Recommended Techniques |
|------------|----------------------|
| Professional | Subtle shadows, clean grids, minimal decoration |
| Modern/Tech | Gradients, glassmorphism, dark backgrounds |
| Friendly | Rounded shapes, warm colors, illustrations |
| Premium | Large whitespace, thin borders, subtle animations |
| Creative | Bold colors, custom shapes, unique typography |
| Minimal | Maximum whitespace, no decoration, system fonts |

---

## Warning: Don't Overdo It

- Pick 3-5 techniques maximum
- Ensure they match brand personality
- Visual interest should enhance, not distract
- Test on multiple devices
- Consider page load performance
