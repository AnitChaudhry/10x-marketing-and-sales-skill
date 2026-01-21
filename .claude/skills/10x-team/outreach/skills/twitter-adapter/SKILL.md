---
name: twitter-adapter
description: |
  Twitter/X automation adapter for the 100X Outreach System.
  Use this skill when performing Twitter actions like following, DMing, liking tweets, replying, or retweeting.
  This skill controls Browser-Use MCP to execute Twitter actions with templates.
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

# Twitter/X Adapter Skill

Automates Twitter/X actions using Browser-Use MCP with intelligent template rendering.

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
- Follow Twitter accounts
- Send Twitter DMs
- Like tweets
- Reply to tweets
- Retweet or quote tweet
- Engage with Twitter content

## Available Twitter Actions

| Action | Description | Max Steps |
|--------|-------------|-----------|
| `follow` | Follow a Twitter user | 6 |
| `like_tweet` | Like a specific tweet | 5 |
| `retweet` | Retweet a tweet | 5 |
| `reply` | Reply to a tweet | 8 |
| `dm` | Send a direct message | 10 |
| `quote_tweet` | Quote tweet with comment | 8 |

## Available Templates

### DMs (`templates/twitter/dms/`)
- `cold_dm.md` - Cold outreach DM
- `after_follow.md` - DM after following
- `mutual_follower.md` - Mutual follower intro
- `reply_to_tweet.md` - DM after tweet interaction
- `collaboration.md` - Collaboration request
- `thank_you.md` - Thank you message
- `founder_outreach.md` - Founder outreach
- `thought_leader_outreach.md` - Thought leader outreach
- `influencer_outreach.md` - Influencer collaboration
- `expert_consultation.md` - Expert consultation request
- `podcast_guest.md` - Podcast guest invitation
- `investor_intro.md` - Investor introduction

### Tweets (`templates/twitter/tweets/`)
- `engagement_reply.md` - Engagement reply
- `quote_tweet.md` - Quote tweet template
- `mention.md` - Mention someone
- `thread_starter.md` - Start a thread

### Replies (`templates/twitter/replies/`)
- `value_add.md` - Add value to conversation
- `question.md` - Ask a question
- `agreement.md` - Agree with insight
- `insight.md` - Share an insight
- `build_in_public.md` - Build in public engagement
- `milestone_congrats.md` - Congratulate milestones

## CRITICAL: Step-by-Step Execution Flow

### Step 1: Get Browser Profile

First, get the user's Twitter browser profile:

```
Use mcp__browser-use__list_browser_profiles to get available profiles.
Ask user which profile to use if multiple exist.
Save the profile_id for later use.
```

### Step 2: Load and Render Template

Read the template file and render with Jinja2:

```bash
# List available templates
python .claude/scripts/template_loader.py list --platform twitter --category dms

# Render a template with variables
python .claude/scripts/template_loader.py render --path twitter/dms/cold_dm --var first_name "John" --var topic "AI" --var my_name "Your Name"
```

### Step 3: Generate Browser-Use Task

Use the Twitter adapter to generate a Browser-Use task:

```bash
# Generate task for follow
python .claude/scripts/twitter_adapter.py task --action follow --handle "@username" --name "John Smith" --user default

# Generate task for DM
python .claude/scripts/twitter_adapter.py task --action dm --handle "@username" --name "John Smith" --message "RENDERED_TEMPLATE_TEXT" --user default

# Generate task for reply
python .claude/scripts/twitter_adapter.py task --action reply --handle "@username" --name "John Smith" --tweet-url "https://x.com/user/status/123" --message "RENDERED_TEMPLATE_TEXT" --user default

# Generate task for like
python .claude/scripts/twitter_adapter.py task --action like_tweet --handle "@username" --name "John Smith" --tweet-url "https://x.com/user/status/123" --user default
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
- profile_id: The user's Twitter browser profile
- max_steps: The recommended max_steps from adapter
```

### Step 5: Monitor Task Progress

Poll the task until completion:

```
Use mcp__browser-use__monitor_task with the task_id.
Poll every few seconds until status is "completed" or "failed".
Report progress to user: "Step 3/6 complete - sending DM..."
```

### Step 6: Record Action and Get Delay

Record the action for rate limiting:

```bash
# Record successful action
python .claude/scripts/rate_limiter.py --user default --platform twitter --action dm --record --success --target "@username"

# Get recommended delay before next action
python .claude/scripts/rate_limiter.py --user default --platform twitter --action dm --delay
```

## Example: Send Twitter DM

**User:** "DM @founder123 about a collaboration"

**You should:**

1. **Get profile:**
   ```
   Call mcp__browser-use__list_browser_profiles
   → Get Twitter profile_id
   ```

2. **Render template:**
   ```bash
   python .claude/scripts/template_loader.py render --path twitter/dms/collaboration --var first_name "Founder" --var my_name "Your Name" --var topic "AI tools"
   ```
   → Get rendered message

3. **Generate task:**
   ```bash
   python .claude/scripts/twitter_adapter.py task --action dm --handle "@founder123" --name "Founder" --message "Hey Founder! Love your content..." --user default
   ```
   → Get Browser-Use task description

4. **Execute:**
   ```
   Call mcp__browser-use__browser_task with:
   - task: "Send a direct message to Founder (@founder123) on Twitter/X..."
   - profile_id: "abc123"
   - max_steps: 10
   ```

5. **Monitor:**
   ```
   Call mcp__browser-use__monitor_task(task_id)
   Report: "DM sent to @founder123 successfully!"
   ```

6. **Record:**
   ```bash
   python .claude/scripts/rate_limiter.py --user default --platform twitter --action dm --record --success --target "@founder123"
   ```

## Example: Follow and Engage Sequence

**User:** "Follow @techguru and like their latest tweet"

**You should:**

1. Show preview:
   ```
   ═══════════════════════════════════════════
   TWITTER ENGAGEMENT - @techguru
   ═══════════════════════════════════════════

   Actions:
   1. Follow @techguru
   2. Like their latest tweet

   Estimated time: ~3 minutes (with delay)
   ═══════════════════════════════════════════

   Proceed?
   ```

2. After approval, execute sequentially:
   - Follow user
   - Wait for rate-limited delay (1-5 minutes)
   - Like their latest tweet
   - Report completion

## Example: Bulk DM Outreach (Single Approval)

**User:** "DM these 5 founders about my product"

**You should:**

1. Show preview:
   ```
   ═══════════════════════════════════════════
   TWITTER DM OUTREACH - 5 MESSAGES
   ═══════════════════════════════════════════

   Template: Founder Outreach

   Targets:
   1. @founder1 - John (CEO at StartupA)
   2. @founder2 - Jane (Founder at TechB)
   3. @founder3 - Bob (CTO at ProductC)
   4. @founder4 - Alice (Founder at AppD)
   5. @founder5 - Mike (CEO at PlatformE)

   Estimated time: ~25 minutes
   ═══════════════════════════════════════════

   Proceed with all 5 DMs?
   ```

2. After single approval, execute ALL autonomously:
   - Render template for each person
   - Execute via Browser-Use
   - Wait for rate-limited delay (1-5 minutes)
   - Report progress after each DM
   - Final summary when complete

## Rate Limits

| Action | Daily Limit | Min Delay | Max Delay |
|--------|-------------|-----------|-----------|
| follow | 50 | 60s | 300s |
| like_tweet | 100 | 30s | 120s |
| retweet | 50 | 60s | 300s |
| reply | 75 | 60s | 300s |
| dm | 50 | 60s | 300s |
| quote_tweet | 50 | 60s | 300s |

## Check Rate Limits

```bash
# Check remaining actions
python .claude/scripts/rate_limiter.py --user default --platform twitter --remaining

# Check if specific action is allowed
python .claude/scripts/rate_limiter.py --user default --platform twitter --action dm --check
```

## Special Considerations

### DMs Require Mutual Following or Open DMs
- If you can't DM someone, try following them first
- Some users have DMs open to everyone
- Some require mutual following

### Tweet Character Limits
- Tweets/replies: 280 characters max
- DMs: 10,000 characters max
- Adapter automatically truncates if needed

### Rate Limit Sensitivity
Twitter is very sensitive to automation. The delays are designed to mimic human behavior:
- Random delays between actions
- No actions during unusual hours
- Burst detection and cooldown
