# Phase 2: Markdown Rendering Engine

**Status:** Pending
**Priority:** High
**Depends on:** Phase 1

## Context

- [plan.md](./plan.md) - Main plan overview
- [phase-01-core-server.md](./phase-01-core-server.md) - Server infrastructure

## Overview

Convert markdown files to styled HTML with syntax highlighting, image handling, and GFM support.

## Requirements

1. Parse GFM markdown (tables, task lists, fenced code)
2. Syntax highlight code blocks
3. Resolve relative image paths
4. Support frontmatter metadata
5. Generate table of contents

## Dependencies

```json
{
  "marked": "^12.0.0",
  "highlight.js": "^11.9.0",
  "gray-matter": "^4.0.3"
}
```

## Architecture

```
scripts/
├── markdown-renderer.cjs
└── lib/
    ├── marked-config.cjs    # marked extensions
    └── image-resolver.cjs   # Relative path handling
```

## Implementation Steps

### 2.1 Setup marked with extensions
```javascript
const { marked } = require('marked');
const hljs = require('highlight.js');

marked.setOptions({
  gfm: true,
  breaks: true,
  highlight: (code, lang) => {
    if (lang && hljs.getLanguage(lang)) {
      return hljs.highlight(code, { language: lang }).value;
    }
    return hljs.highlightAuto(code).value;
  }
});
```

### 2.2 Implement image resolver
- Parse markdown for image references `![alt](path)`
- If path is relative, convert to `/file/` route
- Handle both `./image.png` and `image.png` formats

### 2.3 Implement frontmatter parsing
```javascript
const matter = require('gray-matter');
const { data, content } = matter(markdownContent);
// data = { title, date, status }
// content = markdown without frontmatter
```

### 2.4 Generate table of contents
- Extract h1-h3 headings
- Generate anchor links
- Return as HTML sidebar content

### 2.5 Implement markdown-renderer.cjs
```javascript
// Usage:
// const { render } = require('./markdown-renderer.cjs');
// const html = render(markdownContent, { basePath: '/path/to/file' });
```

### 2.6 Write tests
- Basic markdown renders correctly
- Code blocks highlighted
- Images resolved to /file/ routes
- Frontmatter extracted
- TOC generated for headings

## Todo

- [ ] 2.1 Setup marked with highlight.js
- [ ] 2.2 Implement image-resolver.cjs
- [ ] 2.3 Implement frontmatter parsing
- [ ] 2.4 Generate TOC from headings
- [ ] 2.5 Implement markdown-renderer.cjs
- [ ] 2.6 Write tests

## Success Criteria

- All GFM features render correctly
- Code blocks have syntax highlighting
- Local images display in browser
- Frontmatter extracted for page title
- TOC links work for navigation

## Code Snippets

### Image resolver regex
```javascript
const imgRegex = /!\[([^\]]*)\]\(([^)]+)\)/g;
function resolveImages(markdown, basePath) {
  return markdown.replace(imgRegex, (match, alt, src) => {
    if (src.startsWith('http')) return match;
    const resolved = path.resolve(basePath, src);
    return `![${alt}](/file${resolved})`;
  });
}
```

### TOC generator
```javascript
function generateTOC(html) {
  const headings = [];
  const regex = /<h([1-3])[^>]*id="([^"]+)"[^>]*>([^<]+)<\/h\1>/g;
  let match;
  while ((match = regex.exec(html))) {
    headings.push({ level: match[1], id: match[2], text: match[3] });
  }
  return headings;
}
```
