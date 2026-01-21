---
name: start-app
description: Start the 10x-Team Visual Workflow Canvas application. Use this skill when the user wants to start, launch, or run the app.
user_invocable: true
command_name: start
---

# Start 10x-Team Canvas

This skill starts the visual workflow canvas application.

## Instructions

When invoked, perform these steps:

### Step 1: Navigate and Check Installation
First, check if dependencies are installed:
```bash
cd canvas && ls node_modules 2>/dev/null || echo "NEEDS_INSTALL"
```

### Step 2: Install if Needed
If node_modules doesn't exist or "NEEDS_INSTALL" was echoed:
```bash
cd canvas && npm install
```

### Step 3: Start Development Server
Start the Vite dev server on port 3000:
```bash
cd canvas && npm run dev -- --port 3000
```

Run this command in the background so the user can continue interacting.

### Step 4: Report Success
Tell the user:
```
10x-Team Canvas is starting on http://localhost:3000

Features:
• Drag-to-connect: Drag from green ▶ to blue ◀
• Auto-save: Your work is automatically preserved
• Export: PNG, SVG, or save as .10x file
• Simulate: Watch your workflow execute step-by-step
• Run: Save workflow and execute via "/workflow run"

Open http://localhost:3000 in your browser to start designing workflows!
```

## Trigger Phrases
- "start my app"
- "start the app"
- "start canvas"
- "launch the app"
- "run the app"
- "open canvas"
- "/start"
