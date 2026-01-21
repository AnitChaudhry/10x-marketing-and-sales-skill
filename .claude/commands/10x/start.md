# /10x/start - Launch Visual Workflow Canvas

---

## Description

Starts the 10x Outreach visual workflow canvas - a drag-and-drop interface for designing multi-platform outreach sequences.

---

## Usage

```
/10x/start
```

---

## Prompt

You are launching the 10x Team visual workflow canvas.

### Instructions

1. **Check Canvas Status**
   First, check if the canvas is already running:
   ```bash
   curl -s http://localhost:3000/api/canvas/status 2>/dev/null || echo "Canvas not running"
   ```

2. **Start Canvas if Needed**
   If not running, start the canvas:
   ```bash
   cd canvas && npm install && npm run dev -- --port 3000 &
   ```

3. **Open in Browser**
   The canvas will be available at: http://localhost:3000

4. **Verify Connection**
   Wait for startup and verify:
   ```bash
   sleep 3 && curl -s http://localhost:3000/api/canvas/status
   ```

### Canvas Features

Once running, the canvas provides:
- **Drag-and-drop nodes** for Discovery, LinkedIn, Twitter, Instagram, Email
- **Connection drawing** between nodes
- **Workflow export** to JSON
- **Pre-built templates** for B2B, Brand, Influencer outreach
- **Auto-save** to localStorage

### Node Types Available

| Node | Color | Purpose |
|------|-------|---------|
| Discovery | Purple | Find people with Exa AI |
| LinkedIn | Blue | Connect, message, engage |
| Twitter | Sky Blue | Follow, DM, reply, retweet |
| Instagram | Pink | Follow, DM, comment, stories |
| Email | Green | Send emails via Gmail |
| Delay | Gray | Wait between actions |
| Condition | Yellow | Branch based on response |

### Next Steps

After starting, suggest:
```
Canvas is running at http://localhost:3000

Next steps:
1. Design your workflow by adding nodes
2. Connect nodes by dragging from ▶ to ◀
3. Configure each node's settings
4. Click "Run" to export workflow JSON
5. Execute with: /10x workflow run
```

---

## Related Skills

- `10x-team/outreach/skills/canvas-workflow/SKILL.md`
- `10x-team/outreach/skills/workflow-engine/SKILL.md`
