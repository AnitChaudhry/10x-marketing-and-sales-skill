# /10x/twitter - Twitter/X Automation

---

## Description

Automate Twitter/X actions: follow, DM, like, reply, retweet, quote tweet.

---

## Usage

```
/10x/twitter [action] [target/options]
```

### Actions
- `follow [@username]` - Follow user
- `dm [@username] [text]` - Send direct message
- `like [url]` - Like a tweet
- `reply [url] [text]` - Reply to a tweet
- `retweet [url]` - Retweet
- `quote [url] [text]` - Quote tweet

---

## Prompt

Activate the Twitter adapter skill: `.claude/skills/10x-team/outreach/skills/twitter-adapter/SKILL.md`

Parse arguments: `$ARGUMENTS`

### Rate Limits (Built-in)
| Action | Daily Limit | Delay |
|--------|-------------|-------|
| Follows | 50 | 1-5 min |
| DMs | 50 | 1-5 min |
| Likes | 100 | 30s-2 min |
| Replies | 50 | 1-5 min |

### Browser-Use MCP Integration
Uses `mcp__browser-use__browser_task` for automation.

---

## Examples

```
/10x/twitter follow @elonmusk
/10x/twitter dm @founder "Hey, loved your thread on startups!"
/10x/twitter like https://x.com/user/status/123
/10x/twitter reply https://x.com/user/status/123 "Great point!"
/10x/twitter quote https://x.com/user/status/123 "This is so true!"
```

---

## Templates

Available in `.claude/skills/10x-team/outreach/templates/twitter/`:
- DMs (12 templates)
- Replies (6 templates)
- Tweets (4 templates)
