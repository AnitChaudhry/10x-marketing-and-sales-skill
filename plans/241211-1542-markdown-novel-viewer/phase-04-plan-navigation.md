# Phase 4: Plan Navigation System

**Status:** Pending
**Priority:** Medium
**Depends on:** Phase 3

## Context

- [plan.md](./plan.md) - Main plan overview
- [phase-03-novel-theme.md](./phase-03-novel-theme.md) - Theme system

## Overview

Enable navigation between plan phases via sidebar. Auto-detect related files in plan directory.

## Requirements

1. Detect plan directory structure
2. List all phase files in sidebar
3. Show current file as active
4. Next/Previous navigation buttons
5. Breadcrumb showing plan name
6. Parse plan.md for phase metadata

## Plan Directory Pattern

```
plans/241211-plan-name/
├── plan.md              # Overview with phase table
├── phase-01-name.md
├── phase-02-name.md
├── phase-03-name.md
└── reports/
    └── ...
```

## Architecture

```
scripts/
├── plan-navigator.cjs
└── lib/
    └── plan-detector.cjs  # Detect plan structure
```

## Implementation Steps

### 4.1 Implement plan-detector.cjs
```javascript
// Given a file path, detect if it's part of a plan
function detectPlan(filePath) {
  const dir = path.dirname(filePath);
  const planFile = path.join(dir, 'plan.md');

  if (fs.existsSync(planFile)) {
    return {
      isPlan: true,
      planDir: dir,
      planFile: planFile,
      phases: glob.sync('phase-*.md', { cwd: dir })
    };
  }
  return { isPlan: false };
}
```

### 4.2 Parse plan.md for phase info
- Extract phase table from plan.md
- Get phase names, statuses, links
- Return structured metadata

```javascript
function parsePlanTable(planContent) {
  // Parse markdown table: | Phase | Name | Status | Link |
  const phases = [];
  const tableRegex = /\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*\[([^\]]+)\]\(([^)]+)\)/g;
  // ...
  return phases;
}
```

### 4.3 Generate navigation sidebar
```html
<nav class="plan-nav">
  <div class="plan-title">
    <a href="/file/{{planDir}}/plan.md">Plan Overview</a>
  </div>
  <ul class="phase-list">
    {{#each phases}}
    <li class="{{#if active}}active{{/if}}">
      <a href="/file/{{path}}">
        <span class="status {{status}}"></span>
        {{name}}
      </a>
    </li>
    {{/each}}
  </ul>
</nav>
```

### 4.4 Add prev/next buttons
```html
<footer class="nav-footer">
  {{#if prev}}
  <a href="/file/{{prev.path}}" class="nav-prev">
    ← {{prev.name}}
  </a>
  {{/if}}
  {{#if next}}
  <a href="/file/{{next.path}}" class="nav-next">
    {{next.name}} →
  </a>
  {{/if}}
</footer>
```

### 4.5 Handle non-plan files
- If file not in plan directory, show simple TOC only
- No phase navigation for standalone files

### 4.6 Keyboard navigation
```javascript
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowLeft' && prev) location.href = prev;
  if (e.key === 'ArrowRight' && next) location.href = next;
});
```

## Todo

- [ ] 4.1 Implement plan-detector.cjs
- [ ] 4.2 Parse plan.md for phase info
- [ ] 4.3 Generate navigation sidebar
- [ ] 4.4 Add prev/next buttons
- [ ] 4.5 Handle non-plan files
- [ ] 4.6 Keyboard navigation

## Success Criteria

- Sidebar shows all phases when viewing plan file
- Current phase highlighted
- Click phase to navigate
- Prev/Next buttons work
- Arrow keys navigate phases
- Works correctly for non-plan files

## Code Snippets

### Status indicator
```css
.status {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  display: inline-block;
  margin-right: 8px;
}
.status.pending { background: #d4a574; }
.status.in-progress { background: #4a90d9; }
.status.completed { background: #5cb85c; }
```
