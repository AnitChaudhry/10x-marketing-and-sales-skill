# Phase 1: Core Server Infrastructure

**Status:** Pending
**Priority:** High
**Depends on:** None

## Context

- [plan.md](./plan.md) - Main plan overview

## Overview

Implement background HTTP server with process management, port allocation, and static file serving.

## Requirements

1. Start server in background (detached process)
2. Dynamic port allocation (default 3456, fallback to available)
3. PID file for process tracking
4. Graceful shutdown on SIGTERM/SIGINT
5. Serve static files (CSS, JS, images)
6. Auto-open browser option
7. Return URL to stdout

## Architecture

```
scripts/
├── server.cjs          # Main entry point
├── lib/
│   ├── http-server.cjs # Core HTTP handling
│   ├── port-finder.cjs # Dynamic port allocation
│   └── process-mgr.cjs # PID file, cleanup
```

## Implementation Steps

### 1.1 Create project structure
```bash
mkdir -p .claude/skills/markdown-novel-viewer/{scripts/lib,assets,references}
```

### 1.2 Implement port-finder.cjs
- Check if port available using net.createServer
- Return first available port in range 3456-3500

### 1.3 Implement process-mgr.cjs
- Write PID to `/tmp/md-novel-viewer-{port}.pid`
- Cleanup function to kill orphan processes
- `--stop` flag to kill running instance

### 1.4 Implement http-server.cjs
- Native `http.createServer`
- Route: `/` → serve rendered markdown
- Route: `/assets/*` → serve static files
- Route: `/file/*` → serve local images (relative to markdown file)
- MIME type detection for images/css/js

### 1.5 Implement server.cjs (main entry)
```javascript
// Usage:
// node server.cjs --file ./plan.md [--port 3456] [--open] [--stop]
```

- Parse args with minimist or manual parsing
- Find available port
- Start server in background (child_process.spawn with detached: true)
- Write PID file
- Print URL to stdout
- Auto-open browser if --open flag

### 1.6 Write tests
- Port finder returns available port
- Server starts and responds
- Static files served correctly
- Shutdown cleans up PID file

## Todo

- [ ] 1.1 Create project structure
- [ ] 1.2 Implement port-finder.cjs
- [ ] 1.3 Implement process-mgr.cjs
- [ ] 1.4 Implement http-server.cjs
- [ ] 1.5 Implement server.cjs
- [ ] 1.6 Write tests

## Success Criteria

- Server starts in background
- URL printed to stdout
- Browser opens when --open flag used
- Server stops cleanly with --stop
- Images from markdown directory accessible

## Risk Assessment

| Risk | Mitigation |
|------|------------|
| Port conflicts | Dynamic allocation with range |
| Orphan processes | PID file + cleanup on start |
| Permission issues | Use /tmp for PID files |

## Code Snippets

### Port finder pattern
```javascript
const net = require('net');
function isPortAvailable(port) {
  return new Promise((resolve) => {
    const server = net.createServer();
    server.once('error', () => resolve(false));
    server.once('listening', () => {
      server.close();
      resolve(true);
    });
    server.listen(port);
  });
}
```

### Background spawn pattern
```javascript
const { spawn } = require('child_process');
const child = spawn(process.execPath, [scriptPath, ...args], {
  detached: true,
  stdio: 'ignore'
});
child.unref();
```
