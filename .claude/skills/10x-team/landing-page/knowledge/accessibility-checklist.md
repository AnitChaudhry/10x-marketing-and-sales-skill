# Accessibility Checklist (WCAG AA)

> **Used by**: Build Agent
> **When**: Final accessibility pass before completion

---

## Semantic HTML

- [ ] Use `<header>`, `<main>`, `<section>`, `<footer>`, `<nav>` appropriately
- [ ] Proper heading hierarchy (h1 → h2 → h3, no skipping levels)
- [ ] Only ONE `<h1>` per page
- [ ] Use `<button>` for actions, `<a>` for navigation
- [ ] Lists use `<ul>`, `<ol>`, `<li>` elements
- [ ] Forms use `<form>`, `<label>`, `<input>` with proper associations

---

## Color & Contrast

- [ ] **Normal text**: 4.5:1 contrast ratio minimum
- [ ] **Large text** (18px+ or 14px bold): 3:1 contrast ratio minimum
- [ ] Color is NOT the only way to convey information
- [ ] Links are distinguishable from surrounding text (not just color)
- [ ] Focus states are clearly visible

### Testing Tools
- WebAIM Contrast Checker
- Chrome DevTools → Rendering → Emulate vision deficiencies

---

## Images & Media

- [ ] All `<img>` elements have `alt` attributes
- [ ] Decorative images use `alt=""`
- [ ] Informative images have descriptive alt text
- [ ] Complex images (charts, infographics) have detailed descriptions
- [ ] Videos have captions or transcripts
- [ ] No auto-playing media with sound

### Alt Text Guidelines
```html
<!-- Informative -->
<img src="chart.png" alt="Sales increased 40% from Q1 to Q4 2024">

<!-- Decorative -->
<img src="divider.svg" alt="">

<!-- Functional (in links/buttons) -->
<a href="/"><img src="logo.png" alt="Company Name - Home"></a>
```

---

## Keyboard Navigation

- [ ] All interactive elements reachable via Tab key
- [ ] Tab order follows visual/logical order
- [ ] No keyboard traps (can always Tab out)
- [ ] Skip link at top: "Skip to main content"
- [ ] Focus indicator visible on all elements
- [ ] Dropdown menus accessible via keyboard

### Skip Link Implementation
```html
<a href="#main" class="skip-link">Skip to content</a>
<!-- ... navigation ... -->
<main id="main">
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 1rem;
  padding: 0.5rem 1rem;
  background: var(--color-primary);
  color: white;
  z-index: 100;
}
.skip-link:focus {
  top: 1rem;
}
```

---

## Focus States

- [ ] All interactive elements have visible focus styles
- [ ] Focus styles have sufficient contrast
- [ ] Focus styles are consistent across the site

```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Remove default, add custom */
button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.5);
}
```

---

## Forms

- [ ] All inputs have associated `<label>` elements
- [ ] Required fields are indicated (not just by color)
- [ ] Error messages are clear and specific
- [ ] Error messages are associated with inputs via `aria-describedby`
- [ ] Form validation errors announced to screen readers

```html
<label for="email">Email (required)</label>
<input
  type="email"
  id="email"
  name="email"
  required
  aria-describedby="email-error"
>
<span id="email-error" class="error">Please enter a valid email</span>
```

---

## Touch Targets

- [ ] Touch targets at least 44x44 pixels
- [ ] Adequate spacing between touch targets
- [ ] No tiny links or buttons

```css
.btn {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 24px;
}
```

---

## Content & Readability

- [ ] Content readable at 200% zoom
- [ ] No horizontal scrolling at 320px width
- [ ] Line length: 45-75 characters optimal
- [ ] Adequate line spacing (1.5+ for body text)
- [ ] Paragraphs not justified (left-aligned preferred)
- [ ] No blinking/flashing content

---

## ARIA Usage

Use ARIA only when native HTML isn't sufficient:

```html
<!-- Navigation landmarks -->
<nav aria-label="Main navigation">

<!-- Expandable content -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
<div id="menu" hidden>...</div>

<!-- Live regions for dynamic content -->
<div aria-live="polite" aria-atomic="true">
  <!-- Notifications appear here -->
</div>

<!-- Loading states -->
<button aria-busy="true">Loading...</button>
```

---

## Testing Checklist

### Manual Testing
- [ ] Navigate entire page using only keyboard
- [ ] Test with screen reader (VoiceOver, NVDA)
- [ ] Zoom to 200% and verify usability
- [ ] Test on mobile devices
- [ ] Check with browser reading mode

### Automated Testing
- [ ] Run Lighthouse accessibility audit
- [ ] Use axe DevTools browser extension
- [ ] Validate HTML (validator.w3.org)

---

## Common Issues to Avoid

| Issue | Fix |
|-------|-----|
| Missing alt text | Add descriptive alt to all images |
| Low contrast | Increase to 4.5:1 minimum |
| No focus styles | Add visible outline on :focus |
| Empty links/buttons | Add text or aria-label |
| Missing form labels | Associate labels with inputs |
| Auto-playing video | Add controls, don't autoplay |
| Tiny tap targets | Minimum 44x44px |
