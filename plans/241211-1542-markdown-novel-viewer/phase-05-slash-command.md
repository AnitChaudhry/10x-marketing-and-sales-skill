# Phase 5: Slash Command Integration

**Status:** Pending
**Priority:** Medium
**Depends on:** Phase 4

## Context

- [plan.md](./plan.md) - Main plan overview
- [phase-04-plan-navigation.md](./phase-04-plan-navigation.md) - Navigation

## Overview

Create `/preview` slash command for easy invocation from Claude Code.

## Requirements

1. `/preview <file>` - Preview single markdown file
2. `/preview <plan-dir>` - Preview plan with navigation
3. Auto-detect if argument is file or directory
4. Support relative and absolute paths
5. Show URL after server starts
6. `--stop` flag to kill running server

## Command Design

```bash
# Preview single file
/preview docs/readme.md

# Preview plan directory (opens plan.md)
/preview plans/241211-feature-x/

# Preview with specific port
/preview docs/readme.md --port 4000

# Stop running server
/preview --stop
```

## Architecture

```
.claude/commands/
└── preview.md          # Slash command definition

.claude/skills/markdown-novel-viewer/
└── scripts/
    └── server.cjs      # Called by slash command
```

## Implementation Steps

### 5.1 Create slash command file

`.claude/commands/preview.md`:
```markdown
---
name: preview
description: Preview markdown files in novel-reader UI
arguments:
  - name: file
    description: Path to markdown file or plan directory
    required: true
  - name: port
    description: Server port (default: 3456)
    required: false
  - name: stop
    description: Stop running server
    required: false
---

Preview markdown file in novel-reader UI.

## Usage
- `/preview <file.md>` - Preview single markdown file
- `/preview <plan-dir>/` - Preview plan with navigation
- `/preview --stop` - Stop running server

## Execution
Run the markdown-novel-viewer server script:

\`\`\`bash
node .claude/skills/markdown-novel-viewer/scripts/server.cjs \
  --file "{{file}}" \
  {{#if port}}--port {{port}}{{/if}} \
  {{#if stop}}--stop{{/if}} \
  --open
\`\`\`

Report the URL to the user.
```

### 5.2 Update server.cjs for command integration
- Accept `--file` as file or directory
- If directory, look for `plan.md`
- Return clean JSON output for command parsing

```javascript
// Output format for slash command
if (process.env.CLAUDE_COMMAND) {
  console.log(JSON.stringify({
    success: true,
    url: `http://localhost:${port}`,
    file: resolvedPath
  }));
}
```

### 5.3 Handle path resolution
```javascript
function resolvePath(input, cwd) {
  // Handle relative paths from current working directory
  if (!path.isAbsolute(input)) {
    return path.resolve(cwd, input);
  }
  return input;
}
```

### 5.4 Add --stop implementation
```javascript
if (args.stop) {
  const pids = glob.sync('/tmp/md-novel-viewer-*.pid');
  pids.forEach(pidFile => {
    const pid = fs.readFileSync(pidFile, 'utf8').trim();
    try {
      process.kill(parseInt(pid));
      fs.unlinkSync(pidFile);
      console.log(`Stopped server (PID: ${pid})`);
    } catch (e) {
      fs.unlinkSync(pidFile); // Clean stale PID file
    }
  });
  process.exit(0);
}
```

### 5.5 SKILL.md documentation

Add usage section to SKILL.md:
```markdown
## Slash Command

Use `/preview` to quickly preview markdown:

\`\`\`bash
/preview plans/my-plan/plan.md    # Preview plan
/preview docs/readme.md           # Preview doc
/preview --stop                   # Stop server
\`\`\`
```

### 5.6 Test integration
- Test with various path formats
- Test directory auto-detection
- Test stop command
- Verify URL output format

## Todo

- [ ] 5.1 Create slash command file
- [ ] 5.2 Update server.cjs for command integration
- [ ] 5.3 Handle path resolution
- [ ] 5.4 Add --stop implementation
- [ ] 5.5 Update SKILL.md documentation
- [ ] 5.6 Test integration

## Success Criteria

- `/preview file.md` starts server and opens browser
- `/preview plan-dir/` opens plan.md with navigation
- `/preview --stop` kills running server
- URL displayed clearly in Claude Code output
- Relative paths work correctly

## Error Handling

| Error | Message |
|-------|---------|
| File not found | `Error: File not found: {path}` |
| Not markdown | `Error: Not a markdown file: {path}` |
| Port in use | `Using alternative port: {port}` |
| No server running | `No server running to stop` |
