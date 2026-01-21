# Phase 3: UI/UX Novel Theme

**Status:** Pending
**Priority:** High
**Depends on:** Phase 2

## Context

- [plan.md](./plan.md) - Main plan overview
- [phase-02-markdown-renderer.md](./phase-02-markdown-renderer.md) - Renderer

## Overview

Create calm, book-like reading experience with warm colors, serif typography, and dark/light theme toggle.

## Design Specifications

### Light Theme (Default)
```css
--bg-primary: #faf8f3;      /* Warm cream paper */
--bg-secondary: #f5f2eb;    /* Slightly darker cream */
--text-primary: #2c2c2c;    /* Soft black */
--text-secondary: #5c5c5c;  /* Muted gray */
--accent: #8b4513;          /* Saddle brown */
--border: #e8e4db;          /* Warm gray border */
```

### Dark Theme
```css
--bg-primary: #1a1a1a;      /* Near black */
--bg-secondary: #252525;    /* Dark gray */
--text-primary: #e8e4db;    /* Warm white */
--text-secondary: #a0a0a0;  /* Muted gray */
--accent: #d4a574;          /* Warm gold */
--border: #3a3a3a;          /* Dark border */
```

### Typography
- **Headings:** Libre Baskerville (serif), centered
- **Body:** Inter or system-ui (readable sans)
- **Code:** JetBrains Mono or monospace
- **Base size:** 18px, line-height 1.7

## Requirements

1. Warm, paper-like background
2. Serif headings, centered alignment
3. Comfortable reading width (max 720px)
4. Dark/light toggle button (top-right)
5. Theme persisted in localStorage
6. Smooth transition between themes
7. Font size adjustment (S/M/L)
8. Print-friendly styles

## Architecture

```
assets/
├── template.html     # Base HTML structure
├── novel-theme.css   # All styles (light + dark)
└── reader.js         # Theme toggle, font controls
```

## Implementation Steps

### 3.1 Create template.html
```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{title}}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Inter:wght@400;500&family=JetBrains+Mono&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/novel-theme.css">
</head>
<body>
  <header class="reader-controls">
    <button id="theme-toggle" aria-label="Toggle theme">
    <div class="font-controls"><!-- S M L buttons --></div>
  </header>
  <aside class="sidebar">{{toc}}</aside>
  <main class="content">{{content}}</main>
  <script src="/assets/reader.js"></script>
</body>
</html>
```

### 3.2 Implement novel-theme.css
- CSS custom properties for theming
- `.content` max-width 720px, centered
- `h1, h2, h3` centered, serif font
- Code blocks with subtle background
- Image styling (max-width, border-radius)
- Table styling (clean borders)
- Print media query

### 3.3 Implement reader.js
```javascript
// Theme toggle
const toggle = document.getElementById('theme-toggle');
const html = document.documentElement;
const stored = localStorage.getItem('novel-theme') || 'light';
html.dataset.theme = stored;

toggle.addEventListener('click', () => {
  const next = html.dataset.theme === 'light' ? 'dark' : 'light';
  html.dataset.theme = next;
  localStorage.setItem('novel-theme', next);
});

// Font size
const sizes = { S: '16px', M: '18px', L: '20px' };
```

### 3.4 Style code blocks
- Use highlight.js theme matching novel aesthetic
- Light: github-like
- Dark: custom warm dark

### 3.5 Responsive design
- Sidebar collapses on mobile
- Content full-width on small screens
- Touch-friendly controls

## Todo

- [ ] 3.1 Create template.html
- [ ] 3.2 Implement novel-theme.css
- [ ] 3.3 Implement reader.js
- [ ] 3.4 Style code blocks
- [ ] 3.5 Responsive design

## Success Criteria

- Page feels calm and book-like
- Theme toggle works immediately
- Theme persists across refreshes
- Readable on all screen sizes
- Code blocks properly styled
- Images display inline correctly

## Visual Reference

```
┌─────────────────────────────────────────────────┐
│  [TOC]                    [S] [M] [L]  [🌙]    │
├─────────────────────────────────────────────────┤
│                                                 │
│         Phase 1: Core Server                    │
│         ────────────────────                    │
│                                                 │
│    Lorem ipsum dolor sit amet, consectetur      │
│    adipiscing elit. Sed do eiusmod tempor...   │
│                                                 │
│    ┌──────────────────────────────────────┐    │
│    │ const server = http.createServer()  │    │
│    └──────────────────────────────────────┘    │
│                                                 │
│    [image.png - storyboard frame]              │
│                                                 │
└─────────────────────────────────────────────────┘
```
