# /10x/instagram - Instagram Automation

---

## Description

Automate Instagram actions: follow, DM, like, comment, story reply.

---

## Usage

```
/10x/instagram [action] [target/options]
```

### Actions
- `follow [@username]` - Follow user
- `dm [@username] [text]` - Send direct message
- `like [url]` - Like a post
- `comment [url] [text]` - Comment on post
- `story [username] [text]` - Reply to story

---

## Prompt

Activate the Instagram adapter skill: `.claude/skills/10x-team/outreach/skills/instagram-adapter/SKILL.md`

Parse arguments: `$ARGUMENTS`

### Rate Limits (Built-in)
| Action | Daily Limit | Delay |
|--------|-------------|-------|
| Follows | 30 | 1.5-7 min |
| DMs | 30 | 1.5-7 min |
| Likes | 60 | 1-3 min |
| Comments | 30 | 1.5-7 min |

### Browser-Use MCP Integration
Uses `mcp__browser-use__browser_task` for automation.

---

## Examples

```
/10x/instagram follow @creator
/10x/instagram dm @founder "Loved your recent post!"
/10x/instagram like https://instagram.com/p/...
/10x/instagram comment https://instagram.com/p/... "Amazing content!"
/10x/instagram story creator "That was helpful!"
```

---

## Templates

Available in `.claude/skills/10x-team/outreach/templates/instagram/`:
- DMs (14 templates)
- Comments (6 templates)
- Story replies (3 templates)
