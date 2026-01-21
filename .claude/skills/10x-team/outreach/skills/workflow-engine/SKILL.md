---
name: workflow-engine
description: |
  Orchestrate multi-step, multi-platform outreach workflows.
  Supports discovery → warm-up → engagement → outreach sequences with intelligent rate limiting.
  Use this skill for complex campaigns that span multiple platforms and require phased execution.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Grep
  - TodoWrite
  - AskUserQuestion
  - mcp__browser-use__browser_task
  - mcp__browser-use__list_browser_profiles
  - mcp__browser-use__monitor_task
---

# Workflow Engine Skill

Orchestrates multi-step, multi-platform outreach workflows for the 100X Outreach System.

## IMPORTANT: Professional Outreach Principles

This system follows strict rules to ensure **professional, non-spammy outreach**:

### Touch Limits (Per Person)
| Target Type | Max/Day | Max/Week | Total Max | Cool-Off |
|-------------|---------|----------|-----------|----------|
| Person | 2 | 5 | 8 | 7 days |
| Brand | 1 | 3 | 6 | 14 days |
| Influencer | 1 | 2 | 5 | 14 days |
| Executive | 1 | 2 | 4 | 21 days |

### Platform Delays
| Platform | Between DMs | After Follow | Between Connections |
|----------|-------------|--------------|---------------------|
| LinkedIn | 24-48 hours | 24 hours | 4-8 hours |
| Twitter | 24-48 hours | 4-24 hours | 2-6 hours |
| Instagram | 48-72 hours | 24-48 hours | 4-12 hours |

### Key Rules
- **NEVER message the same person more than 2x per day**
- **NEVER DM without warm-up first (follow, like, engage)**
- **ALWAYS wait 24+ hours between platforms**
- **STOP immediately when response received**

## Pre-Built Intelligent Workflows

### 1. B2B Professional (`workflows/examples/b2b_professional.yaml`)
- Target: Business professionals, decision makers
- Duration: 14 days
- Platforms: LinkedIn + Email
- Pattern: View → Like → Connect → Message → Email → Follow-ups

### 2. Brand Outreach (`workflows/examples/brand_outreach.yaml`)
- Target: Brands, companies
- Duration: 21 days (slower)
- Platforms: Instagram + Email
- Pattern: Follow → Engage → Comment → Story → DM → Email

### 3. Influencer Outreach (`workflows/examples/influencer_outreach.yaml`)
- Target: Content creators, thought leaders
- Duration: 21 days
- Platforms: Twitter + Instagram + Email
- Pattern: Follow → Like → Reply → Reply → DM (only 1 DM!)

### 4. Investor Outreach (`workflows/examples/investor_outreach.yaml`)
- Target: VCs, Angels
- Duration: 28 days
- Platforms: Twitter + LinkedIn + Email
- Pattern: Twitter engage → LinkedIn connect → Email pitch

### 5. Multi-Platform (`workflows/examples/multi_platform_sequence.yaml`)
- Target: Any (adaptive)
- Duration: 30 days
- Platforms: All (routes to best platform)
- Pattern: Primary warm-up → Secondary follow → Connect → Cross-platform

## Outreach Rules Configuration

All rules are defined in `workflows/outreach_rules.yaml`:
- Touch limits by target type
- Platform-specific delays
- Escalation patterns
- Warm-up requirements
- Message quality rules
- Timing rules (active hours, best days)
- Response handling

## When to Use This Skill

Use this skill when the user:
- Says `/workflow create` - Create a workflow visually in the canvas
- Says `/workflow run` - Run workflow from Visual Canvas
- Wants to create a multi-step outreach campaign
- Needs to sequence actions across platforms (LinkedIn → Twitter → Email)
- Wants to set up automated warm-up sequences
- Needs to run daily/scheduled campaigns

## Visual Canvas Integration

Claude Code can now **create workflows visually** in the canvas web app in real-time!

### Creating Workflows Visually (`/workflow create`)

When user says `/workflow create`, follow this process:

#### Step 1: Check Canvas Status

```bash
python .claude/scripts/canvas_client.py status
```

If canvas is not running, inform the user:
```
The visual canvas is not running. Start it first:
  /start
Then try /workflow create again.
```

#### Step 2: Gather Requirements

Ask the user what kind of workflow they want:
- Target audience (e.g., "AI founders", "DevOps engineers")
- Platforms to use (LinkedIn, Twitter, Instagram, Email)
- Outreach goal (connect, pitch, collaborate)

#### Step 3: Build and Send Workflow to Canvas

Use the canvas client to create the workflow visually:

```bash
python .claude/scripts/canvas_client.py workflow '{"name": "My Workflow", "nodes": [...], "connections": [...]}'
```

Or use the pre-built templates:
```bash
python .claude/scripts/canvas_client.py b2b           # B2B Professional workflow
python .claude/scripts/canvas_client.py influencer    # Influencer outreach workflow
```

#### Step 4: Inform the User

```
I've created your workflow visually in the canvas!

Open http://localhost:3000 to see it being built in real-time.

The workflow includes:
- 8 nodes (Discovery → LinkedIn → Delay → Email...)
- 7 connections linking the steps

You can:
1. Watch the workflow appear on the canvas
2. Drag nodes to rearrange the layout
3. Click Run to save and execute
```

### Example: Creating a Custom Workflow

**User:** "Create a workflow to reach DevOps engineers on LinkedIn and Twitter"

**Claude Code builds this workflow visually:**

```python
# Claude Code sends this to the canvas API
workflow = {
    "name": "DevOps Outreach",
    "nodes": [
        {"id": "discover", "skill": "discovery", "label": "Find DevOps Engineers"},
        {"id": "linkedin-view", "skill": "linkedin", "label": "View LinkedIn Profile"},
        {"id": "linkedin-like", "skill": "linkedin", "label": "Like Recent Post"},
        {"id": "delay-1", "skill": "delay", "label": "Wait 24 Hours"},
        {"id": "linkedin-connect", "skill": "linkedin", "label": "Send Connection Request"},
        {"id": "twitter-follow", "skill": "twitter", "label": "Follow on Twitter"},
        {"id": "delay-2", "skill": "delay", "label": "Wait 48 Hours"},
        {"id": "linkedin-msg", "skill": "linkedin", "label": "Send Introduction Message"}
    ],
    "connections": [
        {"from": "discover", "to": "linkedin-view"},
        {"from": "linkedin-view", "to": "linkedin-like"},
        {"from": "linkedin-like", "to": "delay-1"},
        {"from": "delay-1", "to": "linkedin-connect"},
        {"from": "linkedin-connect", "to": "twitter-follow"},
        {"from": "twitter-follow", "to": "delay-2"},
        {"from": "delay-2", "to": "linkedin-msg"}
    ]
}

# Send to canvas
python .claude/scripts/canvas_client.py workflow '...'
```

The canvas will show each node appearing with a visual animation, followed by connections being drawn between them.

### Canvas API Endpoints

The canvas exposes these endpoints for Claude Code:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/canvas/status` | GET | Check if canvas is running |
| `/api/canvas/command` | POST | Send a single command |
| `/api/canvas/commands` | GET | Poll for pending commands |
| `/api/canvas/workflow` | POST | Create a complete workflow |
| `/api/canvas/clear-commands` | POST | Clear command queue |

### Command Types

| Command | Payload | Description |
|---------|---------|-------------|
| `clear` | `{}` | Clear all shapes |
| `add-node` | `{id, skillType, label, x, y}` | Add a node |
| `add-connection` | `{from, to}` | Connect two nodes |
| `run-simulation` | `{}` | Trigger simulation mode |

## Running Canvas Workflows (`/workflow run`)

When user says `/workflow run`, follow this process:

### Step 1: Read the Workflow Queue

```bash
# Check for workflow in queue
cat output/workflow-queue/latest.json
```

### Step 2: Parse and Display Workflow Summary

Show the user what will be executed:

```
═══════════════════════════════════════════════════════════════
                 CANVAS WORKFLOW READY TO RUN
═══════════════════════════════════════════════════════════════

📋 WORKFLOW: 10x-Team Workflow
📅 CREATED: 2024-01-21T...

📊 NODES (in execution order):
   1. 🔍 Discovery - Find Prospects
      Config: query="AI startup founders", maxResults=50

   2. 💼 LinkedIn - Connect
      Config: action=connect, template=professional_intro

   3. 📧 Gmail - Send Email
      Config: subject="Quick question...", template=b2b_intro

🔗 CONNECTIONS: 2 links

═══════════════════════════════════════════════════════════════
```

### Step 3: Execute Each Node

For each node in topological order (based on connections):

1. **Discovery Node** → Use `discovery-engine` skill
2. **LinkedIn Node** → Use `linkedin-adapter` skill
3. **Twitter Node** → Use `twitter-adapter` skill
4. **Instagram Node** → Use `instagram-adapter` skill
5. **Gmail Node** → Use `gmail-adapter` skill
6. **Template Node** → Load template from `.claude/templates/`
7. **Audience Node** → Define target filters
8. **Campaign Node** → Execute full campaign

### Step 4: Apply Rate Limiting

Between each action, respect the platform delays:
- LinkedIn: 24-48 hours between DMs
- Twitter: 24-48 hours between DMs
- Instagram: 48-72 hours between DMs

### Example Canvas Workflow Execution

```
User: /workflow run

Claude:
1. Reading workflow from output/workflow-queue/latest.json...
2. Found 3 nodes, 2 connections

   Executing Node 1: Discovery
   → Running discovery with query "AI startup founders"
   → Found 25 people

   Executing Node 2: LinkedIn (rate-limited)
   → Using linkedin-adapter for 25 people
   → Action: connect with template

   Executing Node 3: Gmail (rate-limited)
   → Using gmail-adapter for 25 people
   → Subject: "Quick question..."

3. Workflow complete! Results saved to campaigns/
```

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple single-platform outreach → use platform-specific skills
- Finding people → use `discovery-engine`
- Managing team → use `team-manager`
- Email-only campaigns → use `outreach-manager`

## Capabilities

1. **Workflow Creation** - Create multi-phase campaigns
2. **Phase Management** - Define action sequences with delays
3. **Multi-Platform** - Coordinate LinkedIn, Twitter, Instagram, Gmail
4. **Rate Limiting** - Intelligent delays to avoid detection
5. **Progress Tracking** - Track per-target, per-phase status
6. **Approval Flow** - Single approval before autonomous execution

## CRITICAL: Single Approval Workflow

### The user approves ONCE. After approval, the workflow runs AUTONOMOUSLY.

```
┌─────────────────────────────────────────────────────────────┐
│                     WORKFLOW OVERVIEW                        │
├─────────────────────────────────────────────────────────────┤
│  1. CREATE    → Define workflow and phases                   │
│  2. DISCOVER  → Find targets using Exa AI                   │
│  3. PREVIEW   → Show complete workflow summary              │
│  4. APPROVE   → User confirms ONCE (single approval)        │
│  5. EXECUTE   → Workflow runs autonomously (no interrupts)  │
│  6. REPORT    → Show final results when complete            │
└─────────────────────────────────────────────────────────────┘
```

## Workflow Definition

Workflows can be created from YAML files or programmatically.

### YAML Workflow Example

```yaml
# workflows/examples/ai_founders.yaml
name: "AI Founders Outreach"
description: "Connect with AI startup founders"

discovery:
  source: "exa"
  query: "AI startup founders Series A San Francisco"
  max_results: 10

phases:
  - name: "view_profile"
    platform: "linkedin"
    action: "view_profile"
    delay_after: "2-5 minutes"

  - name: "engage"
    platform: "linkedin"
    action: "like_post"
    delay_after: "1-3 hours"
    condition: "has_recent_posts"

  - name: "connect"
    platform: "linkedin"
    action: "connect"
    template: "templates/linkedin/connection_request.txt"
    delay_after: "24-48 hours"

  - name: "follow_twitter"
    platform: "twitter"
    action: "follow"
    condition: "has_twitter"
    delay_after: "2-4 hours"

  - name: "message"
    platform: "linkedin"
    action: "message"
    template: "templates/linkedin/intro_message.txt"
    condition: "connection_accepted"
    delay_after: "24-72 hours"

schedule:
  days: ["monday", "tuesday", "wednesday", "thursday", "friday"]
  hours:
    start: "09:00"
    end: "17:00"
  timezone: "America/Los_Angeles"
```

## Commands Reference

### Create Workflow

```bash
python .claude/scripts/workflow_engine.py create --name "My Campaign" --description "Outreach to developers" --user default --query "developers at startups"
```

### Load from YAML

```bash
python .claude/scripts/workflow_engine.py load --file workflows/examples/ai_founders.yaml --user default
```

### List Workflows

```bash
python .claude/scripts/workflow_engine.py list
python .claude/scripts/workflow_engine.py list --status running
```

### Get Workflow Details

```bash
python .claude/scripts/workflow_engine.py get --id WORKFLOW_ID
```

### Approve Workflow

```bash
python .claude/scripts/workflow_engine.py approve --id WORKFLOW_ID --user default
```

### Pause Workflow

```bash
python .claude/scripts/workflow_engine.py pause --id WORKFLOW_ID
```

### Cancel Workflow

```bash
python .claude/scripts/workflow_engine.py cancel --id WORKFLOW_ID
```

## Execution Flow

### Phase 1: Create Workflow

```json
[
  {"content": "Create workflow from user requirements", "status": "in_progress"},
  {"content": "Define phases and actions", "status": "pending"},
  {"content": "Run discovery for targets", "status": "pending"},
  {"content": "Show approval summary", "status": "pending"},
  {"content": "Execute workflow after approval", "status": "pending"}
]
```

### Phase 2: Discovery Integration

Use the discovery-engine skill to find targets:

1. Create discovery session
2. Search using Exa AI
3. Add discovered people to workflow

### Phase 3: Approval Summary

Present a complete summary for approval:

```
═══════════════════════════════════════════════════════════════
                 WORKFLOW READY FOR APPROVAL
═══════════════════════════════════════════════════════════════

📋 WORKFLOW: AI Founders Outreach
📝 DESCRIPTION: Connect with AI startup founders

🔍 DISCOVERY:
   Query: "AI startup founders Series A San Francisco"
   Found: 10 targets

👥 TARGETS (Sample):
   1. John Smith - CEO at AITech (LinkedIn, Twitter)
   2. Jane Doe - Founder at MLStartup (LinkedIn)
   3. Bob Wilson - CTO at DataCo (LinkedIn, Twitter, Email)
   ...

📊 PHASES:
   1. View Profile (LinkedIn) - 2-5 min delay
   2. Like Post (LinkedIn) - 1-3 hour delay
   3. Connect (LinkedIn) - 24-48 hour delay
   4. Follow (Twitter) - 2-4 hour delay
   5. Message (LinkedIn) - 24-72 hour delay

⏰ SCHEDULE:
   Days: Mon-Fri
   Hours: 9:00 AM - 5:00 PM PST

⏳ ESTIMATED DURATION: ~5 days

═══════════════════════════════════════════════════════════════
⚠️  Once approved, workflow will run AUTOMATICALLY.
    No further approvals needed.
═══════════════════════════════════════════════════════════════

Do you approve this workflow? (yes/no)
```

### Phase 4: Autonomous Execution

After approval, use Browser-Use MCP to execute actions:

1. Get next action from workflow
2. Execute via `mcp__browser-use__browser_task`
3. Monitor with `mcp__browser-use__monitor_task`
4. Record result
5. Wait for rate-limited delay
6. Repeat until complete

### Phase 5: Report

```
═══════════════════════════════════════════════════════════════
                    WORKFLOW COMPLETE
═══════════════════════════════════════════════════════════════

✅ COMPLETED: 8/10 targets
❌ FAILED: 2 targets

📊 ACTIONS:
   LinkedIn Profile Views: 10/10
   LinkedIn Post Likes: 7/10
   LinkedIn Connections: 8/10
   Twitter Follows: 6/10
   LinkedIn Messages: 5/8 (awaiting acceptance)

⏱️  DURATION: 5 days 3 hours

📁 LOG: campaigns/completed/abc123.json

═══════════════════════════════════════════════════════════════
```

## Rate Limiting Integration

The workflow engine integrates with the rate limiter:

```bash
# Check rate limits before action
python .claude/scripts/rate_limiter.py --user USER_ID --platform linkedin --action connect --check

# Record action after execution
python .claude/scripts/rate_limiter.py --user USER_ID --platform linkedin --action connect --record --target "linkedin.com/in/target"
```

## Platform Actions

### LinkedIn Actions
- `view_profile` - View target's profile (warm-up)
- `like_post` - Like a recent post (engagement)
- `comment` - Comment on a post (engagement)
- `connect` - Send connection request
- `message` - Send InMail/message

### Twitter Actions
- `follow` - Follow target
- `like_tweet` - Like a tweet
- `retweet` - Retweet
- `reply` - Reply to tweet
- `dm` - Send direct message

### Instagram Actions
- `follow` - Follow target
- `like_post` - Like a post
- `comment` - Comment on post
- `dm` - Send direct message

### Gmail Actions
- `send` - Send email (via gmail_client.py)

## Browser-Use MCP Execution

**Browser-Use MCP is cloud-hosted via Claude Code** - no local installation required!

### For LinkedIn/Twitter/Instagram Actions:

Use the platform adapters to generate Browser-Use tasks:

```bash
# Generate LinkedIn task
python .claude/scripts/linkedin_adapter.py task --action connect --url "https://linkedin.com/in/username" --name "John Smith" --message "Hi John..." --user default

# Generate Twitter task
python .claude/scripts/twitter_adapter.py task --action dm --handle "@username" --name "John" --message "Hey John..." --user default

# Generate Instagram task
python .claude/scripts/instagram_adapter.py task --action dm --handle "@username" --name "John" --message "Hey John..." --user default
```

### Execute with Browser-Use MCP:

```
1. Get browser profile:
   Call mcp__browser-use__list_browser_profiles
   → Select appropriate profile for the platform

2. Execute task:
   Call mcp__browser-use__browser_task with:
   - task: The task description from adapter
   - profile_id: The browser profile UUID
   - max_steps: Recommended max_steps from adapter

3. Monitor progress:
   Call mcp__browser-use__monitor_task(task_id)
   Poll until completed or failed
```

### For Gmail Actions:

Gmail uses direct API (not Browser-Use):

```bash
python .claude/scripts/gmail_client.py send --to "email@example.com" --subject "Subject" --body "Body"
```

## Data Storage

- `campaigns/active/` - Running workflows
- `campaigns/completed/` - Finished workflows
- `campaigns/logs/` - Execution logs
- `workflows/examples/` - Example YAML files
- `workflows/custom/` - User-created workflows

## Example Conversation

**User:** "Create a workflow to reach out to 10 DevOps engineers"

**Assistant:**

1. "I'll create a multi-platform outreach workflow. Let me gather some details:"
   - What's your search criteria? (e.g., location, company size)
   - Which platforms? (LinkedIn, Twitter, Instagram)
   - What's your outreach goal? (connect, message, etc.)

2. Create workflow with phases

3. Run discovery to find targets

4. Show approval summary

5. After approval, execute autonomously

6. Report results when complete
