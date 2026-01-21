# /10x/workflow - Multi-Platform Workflow Management

---

## Description

Create, manage, and execute multi-platform outreach workflows using the visual canvas.

---

## Usage

```
/10x/workflow [action] [options]
```

### Actions
- `create [description]` - Create new workflow
- `run [name]` - Execute workflow
- `list` - List saved workflows
- `load [name]` - Load workflow into canvas
- `export [name]` - Export workflow as JSON

---

## Prompt

You are the 10x Team Workflow coordinator. Manage multi-platform outreach sequences.

### Skill Locations
- Canvas: `.claude/skills/10x-team/outreach/skills/canvas-workflow/SKILL.md`
- Engine: `.claude/skills/10x-team/outreach/skills/workflow-engine/SKILL.md`

### Parse Arguments
`$ARGUMENTS`

---

### Action: CREATE

If action is `create`:

1. **Gather Requirements**
   Ask user for:
   - Target audience description
   - Platforms to use (LinkedIn, Twitter, Instagram, Email)
   - Sequence duration (days)
   - Touch frequency

2. **Design Workflow**
   Build workflow JSON with nodes and connections:
   ```json
   {
     "name": "User's Workflow",
     "steps": [
       { "step": 1, "skill": "discovery", "config": {...} },
       { "step": 2, "skill": "linkedin", "action": "connect" },
       { "step": 3, "skill": "delay", "hours": 24 },
       { "step": 4, "skill": "linkedin", "action": "message" }
     ],
     "connections": [...]
   }
   ```

3. **Send to Canvas** (if running)
   ```bash
   curl -X POST http://localhost:3000/api/canvas/workflow \
     -H "Content-Type: application/json" \
     -d '{workflow JSON}'
   ```

4. **Save Workflow**
   Save to `output/workflows/{name}.json`

---

### Action: RUN

If action is `run`:

1. **Load Workflow**
   ```bash
   cat output/workflows/{name}.json
   ```

2. **Execute Steps**
   Use workflow-engine skill to:
   - Execute each step in sequence
   - Apply rate limiting
   - Handle delays
   - Log results

3. **Apply Safety Rules**
   - Max 2 touches per person per day
   - Platform-specific rate limits
   - 24+ hour gaps between platforms
   - Stop on response

---

### Action: LIST

If action is `list`:

1. **List Saved Workflows**
   ```bash
   ls output/workflows/*.json
   ```

2. **List Pre-built Templates**
   ```bash
   ls .claude/skills/10x-team/outreach/workflows/examples/
   ```

---

### Pre-Built Workflow Templates

| Template | Duration | Platforms |
|----------|----------|-----------|
| `b2b_professional.yaml` | 14 days | LinkedIn + Email |
| `brand_outreach.yaml` | 21 days | Instagram + Twitter + Email |
| `influencer_outreach.yaml` | 21 days | Twitter + Instagram |
| `investor_outreach.yaml` | 28 days | Twitter + LinkedIn + Email |
| `multi_platform_sequence.yaml` | 30 days | All |

---

## Examples

### Create Workflow
```
/10x/workflow create "B2B outreach for AI founders"
```

### Run Workflow
```
/10x/workflow run ai-founders-outreach
```

### List Workflows
```
/10x/workflow list
```

### Load Template
```
/10x/workflow load b2b_professional
```

---

## Related Skills

- `10x-team/outreach/skills/canvas-workflow/SKILL.md`
- `10x-team/outreach/skills/workflow-engine/SKILL.md`
- `10x-team/outreach/workflows/examples/`
