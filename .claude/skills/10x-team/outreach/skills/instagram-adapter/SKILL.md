---
name: instagram-adapter
description: |
  Instagram automation adapter for the 100X Outreach System.
  Use this skill when performing Instagram actions like following, DMing, liking posts, commenting, or replying to stories.
  This skill controls Browser-Use MCP to execute Instagram actions with templates.
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

# Instagram Adapter Skill

Automates Instagram actions using Browser-Use MCP with intelligent template rendering.

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
- Follow Instagram accounts
- Send Instagram DMs
- Like Instagram posts
- Comment on posts
- Reply to stories
- Engage with Instagram content

## Available Instagram Actions

| Action | Description | Max Steps |
|--------|-------------|-----------|
| `follow` | Follow an Instagram user | 6 |
| `like_post` | Like a post | 6 |
| `comment` | Comment on a post | 8 |
| `dm` | Send a direct message | 10 |
| `story_reply` | Reply to a story | 10 |

## Available Templates

### DMs (`templates/instagram/dms/`)
- `cold_dm.md` - Cold outreach DM
- `after_follow.md` - DM after following
- `story_reply.md` - Reply to story
- `mutual_follower.md` - Mutual follower intro
- `collaboration.md` - Collaboration request
- `business_inquiry.md` - Business inquiry
- `thank_you.md` - Thank you message
- `influencer_outreach.md` - Influencer outreach
- `brand_collaboration.md` - Brand collaboration
- `creator_partnership.md` - Creator partnership
- `expert_connect.md` - Expert connection
- `product_feature.md` - Product feature request
- `founder_connect.md` - Founder connection

### Comments (`templates/instagram/comments/`)
- `engagement.md` - General engagement
- `compliment.md` - Compliment their content
- `question.md` - Ask a question
- `support.md` - Show support
- `value_add.md` - Add value
- `appreciation.md` - Show appreciation

### Stories (`templates/instagram/stories/`)
- `story_reply.md` - Reply to story
- `story_mention.md` - Mention in story
- `story_reaction.md` - React to story

## CRITICAL: Step-by-Step Execution Flow

### Step 1: Get Browser Profile

First, get the user's Instagram browser profile:

```
Use mcp__browser-use__list_browser_profiles to get available profiles.
Ask user which profile to use if multiple exist.
Save the profile_id for later use.
```

### Step 2: Load and Render Template

Read the template file and render with Jinja2:

```bash
# List available templates
python .claude/scripts/template_loader.py list --platform instagram --category dms

# Render a template with variables
python .claude/scripts/template_loader.py render --path instagram/dms/cold_dm --var first_name "John" --var what_you_like "your content" --var my_name "Your Name"
```

### Step 3: Generate Browser-Use Task

Use the Instagram adapter to generate a Browser-Use task:

```bash
# Generate task for follow
python .claude/scripts/instagram_adapter.py task --action follow --handle "@username" --name "John Smith" --user default

# Generate task for DM
python .claude/scripts/instagram_adapter.py task --action dm --handle "@username" --name "John Smith" --message "RENDERED_TEMPLATE_TEXT" --user default

# Generate task for comment
python .claude/scripts/instagram_adapter.py task --action comment --handle "@username" --name "John Smith" --post-url "https://instagram.com/p/ABC123" --message "RENDERED_TEMPLATE_TEXT" --user default

# Generate task for like
python .claude/scripts/instagram_adapter.py task --action like_post --handle "@username" --name "John Smith" --post-url "https://instagram.com/p/ABC123" --user default

# Generate task for story reply
python .claude/scripts/instagram_adapter.py task --action story_reply --handle "@username" --name "John Smith" --message "RENDERED_TEMPLATE_TEXT" --user default
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
- profile_id: The user's Instagram browser profile
- max_steps: The recommended max_steps from adapter
```

### Step 5: Monitor Task Progress

Poll the task until completion:

```
Use mcp__browser-use__monitor_task with the task_id.
Poll every few seconds until status is "completed" or "failed".
Report progress to user: "Step 4/10 complete - sending DM..."
```

### Step 6: Record Action and Get Delay

Record the action for rate limiting:

```bash
# Record successful action
python .claude/scripts/rate_limiter.py --user default --platform instagram --action dm --record --success --target "@username"

# Get recommended delay before next action
python .claude/scripts/rate_limiter.py --user default --platform instagram --action dm --delay
```

## Example: Send Instagram DM

**User:** "DM @influencer about a brand collaboration"

**You should:**

1. **Get profile:**
   ```
   Call mcp__browser-use__list_browser_profiles
   → Get Instagram profile_id
   ```

2. **Render template:**
   ```bash
   python .claude/scripts/template_loader.py render --path instagram/dms/brand_collaboration --var first_name "Influencer" --var company "My Brand" --var my_name "Your Name"
   ```
   → Get rendered message

3. **Generate task:**
   ```bash
   python .claude/scripts/instagram_adapter.py task --action dm --handle "@influencer" --name "Influencer" --message "Hi! Your brand aesthetic is amazing..." --user default
   ```
   → Get Browser-Use task description

4. **Execute:**
   ```
   Call mcp__browser-use__browser_task with:
   - task: "Send a direct message to Influencer (@influencer) on Instagram..."
   - profile_id: "abc123"
   - max_steps: 10
   ```

5. **Monitor:**
   ```
   Call mcp__browser-use__monitor_task(task_id)
   Report: "DM sent to @influencer successfully!"
   ```

6. **Record:**
   ```bash
   python .claude/scripts/rate_limiter.py --user default --platform instagram --action dm --record --success --target "@influencer"
   ```

## Example: Warm-Up Engagement Sequence

**User:** "Engage with @creator - like their post and leave a comment"

**You should:**

1. Show preview:
   ```
   ═══════════════════════════════════════════
   INSTAGRAM ENGAGEMENT - @creator
   ═══════════════════════════════════════════

   Actions:
   1. Like their most recent post
   2. Leave an engaging comment

   Template: Engagement comment

   Estimated time: ~5 minutes (with delay)
   ═══════════════════════════════════════════

   Proceed?
   ```

2. After approval, execute sequentially:
   - Like post
   - Wait for rate-limited delay (1.5-7 minutes)
   - Post comment
   - Report completion

## Example: Bulk Influencer Outreach (Single Approval)

**User:** "Reach out to these 5 influencers about a collaboration"

**You should:**

1. Show preview:
   ```
   ═══════════════════════════════════════════
   INSTAGRAM INFLUENCER OUTREACH - 5 DMS
   ═══════════════════════════════════════════

   Template: Influencer Outreach

   Targets:
   1. @influencer1 - Sarah (50K followers)
   2. @influencer2 - Mike (75K followers)
   3. @influencer3 - Emma (120K followers)
   4. @influencer4 - David (45K followers)
   5. @influencer5 - Lisa (90K followers)

   Estimated time: ~35 minutes
   ═══════════════════════════════════════════

   Proceed with all 5 DMs?
   ```

2. After single approval, execute ALL autonomously:
   - Render template for each influencer
   - Execute via Browser-Use
   - Wait for rate-limited delay (1.5-7 minutes)
   - Report progress after each DM
   - Final summary when complete

## Rate Limits

| Action | Daily Limit | Min Delay | Max Delay |
|--------|-------------|-----------|-----------|
| follow | 30 | 90s | 420s |
| like_post | 60 | 30s | 180s |
| comment | 20 | 90s | 420s |
| dm | 30 | 90s | 420s |
| story_reply | 30 | 90s | 420s |

## Check Rate Limits

```bash
# Check remaining actions
python .claude/scripts/rate_limiter.py --user default --platform instagram --remaining

# Check if specific action is allowed
python .claude/scripts/rate_limiter.py --user default --platform instagram --action dm --check
```

## Special Considerations

### DMs May Require Following
- Some accounts have DMs restricted to followers only
- Consider following first, then DMing later

### Comment Character Limits
- Comments: 2,200 characters max
- But shorter comments (under 150 chars) look more natural

### Story Replies
- Story replies go to their DMs
- Stories expire after 24 hours
- Good way to start conversations naturally

### Instagram is Very Sensitive
Instagram is the most aggressive at detecting automation:
- Longer delays than other platforms
- Random patterns are essential
- Avoid bulk actions in short periods
- The rate limiter has extra safety margins built in
