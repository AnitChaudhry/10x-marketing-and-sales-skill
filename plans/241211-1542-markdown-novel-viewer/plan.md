# Plan: markdown-novel-viewer Skill

**Created:** 2024-12-11
**Status:** Completed
**Completed:** 2025-12-11 16:05 UTC
**Scope:** Project (.claude/skills/markdown-novel-viewer)

## Overview

Background HTTP server rendering markdown files with calm, book-like reading experience for ClaudeKit users reviewing plans, storyboards, and documentation.

## Goals

- Novel book aesthetic (warm colors, serif fonts, centered headings)
- Dark/light theme toggle with persistence
- Plan navigation sidebar for multi-phase plans
- Inline image rendering for storyboards
- Background server with auto-open browser option

## Architecture

```
.claude/skills/markdown-novel-viewer/
├── SKILL.md
├── scripts/
│   ├── server.cjs           # Main HTTP server
│   ├── markdown-renderer.cjs # MD→HTML conversion
│   ├── plan-navigator.cjs   # Multi-file plan handling
│   └── tests/
│       └── server.test.cjs
├── assets/
│   ├── template.html        # Base HTML template
│   ├── novel-theme.css      # Combined light/dark styles
│   └── reader.js            # Client-side theme toggle
└── references/
    └── customization.md
```

## Phases

| Phase | Name | Status | Link |
|-------|------|--------|------|
| 1 | Core Server Infrastructure | Completed | [phase-01-core-server.md](./phase-01-core-server.md) |
| 2 | Markdown Rendering Engine | Completed | [phase-02-markdown-renderer.md](./phase-02-markdown-renderer.md) |
| 3 | UI/UX Novel Theme | Completed | [phase-03-novel-theme.md](./phase-03-novel-theme.md) |
| 4 | Plan Navigation System | Completed | [phase-04-plan-navigation.md](./phase-04-plan-navigation.md) |
| 5 | Slash Command Integration | Completed | [phase-05-slash-command.md](./phase-05-slash-command.md) |

## Tech Stack

- **Runtime:** Node.js (native http module)
- **Markdown:** marked + highlight.js
- **Fonts:** Google Fonts (Libre Baskerville, Inter)
- **State:** JSON file for instance tracking

## Success Criteria

- [x] Server starts in <500ms
- [x] Renders markdown with images correctly
- [x] Theme toggle works and persists
- [x] Plan phases navigable via sidebar
- [x] `/preview` command works
- [x] Clean shutdown on SIGTERM

## Completion Notes

**All 5 phases successfully implemented:**
- Phase 1: Core Server (port-finder, process-mgr, http-server, server.cjs)
- Phase 2: Markdown Renderer (marked, highlight.js, gray-matter integration)
- Phase 3: Novel Theme (template.html, novel-theme.css, reader.js)
- Phase 4: Plan Navigation (plan-navigator.cjs with sidebar)
- Phase 5: Slash Command (/preview command created)

**Security enhancements applied:**
- Path traversal protection in file serving
- Sanitized error messages
- Updated marked library to v17 for XSS prevention
