---
name: linkedin-adapter
description: |
  LinkedIn automation adapter for the 100X Outreach System.
  Use this skill when performing LinkedIn actions like connecting, messaging, viewing profiles, liking posts, or commenting.
  This skill controls Browser-Use MCP to execute LinkedIn actions with templates.
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

# LinkedIn Adapter Skill

Automates LinkedIn actions using Browser-Use MCP with intelligent template rendering.

## Browser-Use MCP: Cloud-Hosted

**No local installation required!** Browser-Use MCP is cloud-hosted via Claude Code.
Tools available:
- `mcp__browser-use__browser_task` - Execute browser automation
- `mcp__browser-use__list_browser_profiles` - List profiles
- `mcp__browser-use__monitor_task` - Monitor progress

## IMPORTANT: You Control Browser-Use

**You are the brain that orchestrates Browser-Use.** This skill tells you exactly how to:
1. Load and render templates
2. Generate Browser-Use tasks
3. Execute actions via Browser-Use MCP
4. Monitor and report results

## When to Use This Skill

Use this skill when the user wants to:
- Send LinkedIn connection requests
- Message LinkedIn connections
- View LinkedIn profiles (warm-up)
- Like/comment on LinkedIn posts
- Send InMails

## Available LinkedIn Actions

| Action | Description | Max Steps |
|--------|-------------|-----------|
| `view_profile` | View someone's LinkedIn profile | 5 |
| `like_post` | Like a recent post | 8 |
| `comment` | Comment on a post | 10 |
| `connect` | Send connection request | 12 |
| `message` | Send a direct message | 12 |
| `inmail` | Send an InMail | 12 |

## Available Templates

### Connection Requests (`templates/linkedin/connection-requests/`)
- `cold_outreach.md` - General cold outreach
- `startup_founder.md` - Reach out to founders
- `thought_leader.md` - Connect with thought leaders
- `speaker_invitation.md` - Invite speakers
- `content_collaboration.md` - Content collab requests
- `alumni_connect.md` - Alumni connections
- `potential_client.md` - Sales outreach
- `mutual_connection.md` - Mutual connection intro
- `same_industry.md` - Same industry connection
- `recruiter.md` - Recruiter outreach
- `investor_outreach.md` - Investor connections
- `event_attendee.md` - Event attendee connections

### Messages (`templates/linkedin/messages/`)
- `intro_after_connect.md` - First message after connecting
- `follow_up_no_response.md` - Follow up on no response
- `meeting_request.md` - Request a meeting
- `collaboration_proposal.md` - Propose collaboration
- `value_offer.md` - Offer value
- `thank_you.md` - Thank you message
- `partnership_proposal.md` - Partnership proposals
- `sales_intro.md` - Sales introduction
- `referral_request.md` - Ask for referrals
- `expertise_request.md` - Ask for expert advice
- `podcast_invitation.md` - Podcast guest invitation

### InMails (`templates/linkedin/inmails/`)
- `cold_inmail.md` - Cold InMail
- `executive_outreach.md` - Executive outreach
- `job_opportunity.md` - Job opportunities

### Comments (`templates/linkedin/comments/`)
- `thoughtful_engagement.md` - Thoughtful comment
- `question_comment.md` - Ask a question
- `congratulations.md` - Congratulate them

## CRITICAL: Step-by-Step Execution Flow

### Step 1: Get Browser Profile

First, get the user's LinkedIn browser profile:

```
Use mcp__browser-use__list_browser_profiles to get available profiles.
Ask user which profile to use if multiple exist.
Save the profile_id for later use.
```

### Step 2: Load and Render Template

Read the template file and render with Jinja2:

```bash
# List available templates
python .claude/scripts/template_loader.py list --platform linkedin --category connection-requests

# Render a template with variables
python .claude/scripts/template_loader.py render --path linkedin/connection-requests/cold_outreach --var first_name "John" --var company "Acme Inc" --var industry "AI/ML" --var my_name "Your Name"
```

### Step 3: Generate Browser-Use Task

Use the LinkedIn adapter to generate a Browser-Use task:

```bash
# Generate task for connection request
python .claude/scripts/linkedin_adapter.py task --action connect --url "https://linkedin.com/in/username" --name "John Smith" --message "RENDERED_TEMPLATE_TEXT" --user default

# Generate task for messaging
python .claude/scripts/linkedin_adapter.py task --action message --url "https://linkedin.com/in/username" --name "John Smith" --message "RENDERED_TEMPLATE_TEXT" --user default

# Generate task for viewing profile
python .claude/scripts/linkedin_adapter.py task --action view_profile --url "https://linkedin.com/in/username" --name "John Smith" --user default

# Generate task for liking post
python .claude/scripts/linkedin_adapter.py task --action like_post --url "https://linkedin.com/in/username" --name "John Smith" --user default
```

The adapter returns JSON with:
- `task`: The Browser-Use task description
- `max_steps`: Recommended max steps
- `can_proceed`: Whether rate limits allow this action
- `message`: The rendered message

### Step 4: Execute via Browser-Use MCP

Use the generated task with Browser-Use:

```
Use mcp__browser-use__browser_task with:
- task: The task description from the adapter
- profile_id: The user's LinkedIn browser profile
- max_steps: The recommended max_steps from adapter
```

### Step 5: Monitor Task Progress

Poll the task until completion:

```
Use mcp__browser-use__monitor_task with the task_id.
Poll every few seconds until status is "completed" or "failed".
Report progress to user: "Step 2/5 complete - clicked Connect button"
```

### Step 6: Record Action and Get Delay

Record the action for rate limiting:

```bash
# Record successful action
python .claude/scripts/rate_limiter.py --user default --platform linkedin --action connect --record --success --target "linkedin.com/in/username"

# Get recommended delay before next action
python .claude/scripts/rate_limiter.py --user default --platform linkedin --action connect --delay
```

## Example: Send Connection Request

**User:** "Connect with John Smith on LinkedIn with a cold outreach message"

**You should:**

1. **Get profile:**
   ```
   Call mcp__browser-use__list_browser_profiles
   → Get LinkedIn profile_id
   ```

2. **Render template:**
   ```bash
   python .claude/scripts/template_loader.py render --path linkedin/connection-requests/cold_outreach --var first_name "John" --var company "UNKNOWN" --var my_name "Your Name"
   ```
   → Get rendered message

3. **Generate task:**
   ```bash
   python .claude/scripts/linkedin_adapter.py task --action connect --url "https://linkedin.com/in/johnsmith" --name "John Smith" --message "Hi John, I came across your profile..." --user default
   ```
   → Get Browser-Use task description

4. **Execute:**
   ```
   Call mcp__browser-use__browser_task with:
   - task: "Navigate to https://linkedin.com/in/johnsmith..."
   - profile_id: "abc123"
   - max_steps: 12
   ```

5. **Monitor:**
   ```
   Call mcp__browser-use__monitor_task(task_id)
   Report: "Connected with John Smith successfully!"
   ```

6. **Record:**
   ```bash
   python .claude/scripts/rate_limiter.py --user default --platform linkedin --action connect --record --success --target "linkedin.com/in/johnsmith"
   ```

## Example: Bulk Outreach (Single Approval)

**User:** "Connect with these 5 LinkedIn profiles"

**You should:**

1. Show preview:
   ```
   ═══════════════════════════════════════════
   LINKEDIN OUTREACH - 5 CONNECTIONS
   ═══════════════════════════════════════════

   Template: Cold Outreach

   Targets:
   1. John Smith (CEO at Acme)
   2. Jane Doe (CTO at TechCo)
   3. Bob Wilson (Founder at StartupX)
   4. Alice Chen (VP at BigCorp)
   5. Mike Brown (Director at MidCo)

   Estimated time: ~30 minutes
   ═══════════════════════════════════════════

   Proceed with all 5 connection requests?
   ```

2. After single approval, execute ALL actions autonomously:
   - Render template for each person
   - Execute via Browser-Use
   - Wait for rate-limited delay (2-10 minutes)
   - Report progress after each action
   - Final summary when complete

## Rate Limits

| Action | Daily Limit | Min Delay | Max Delay |
|--------|-------------|-----------|-----------|
| view_profile | 100 | 30s | 120s |
| like_post | 100 | 30s | 120s |
| comment | 25 | 120s | 600s |
| connect | 20 | 120s | 600s |
| message | 50 | 120s | 600s |
| inmail | 15 | 300s | 600s |

## Check Rate Limits

```bash
# Check remaining actions
python .claude/scripts/rate_limiter.py --user default --platform linkedin --remaining

# Check if specific action is allowed
python .claude/scripts/rate_limiter.py --user default --platform linkedin --action connect --check
```
