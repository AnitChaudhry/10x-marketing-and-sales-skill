# /10x/linkedin - LinkedIn Automation

---

## Description

Automate LinkedIn actions: connect, message, like, comment, view profiles.

---

## Usage

```
/10x/linkedin [action] [target/options]
```

### Actions
- `connect [query/name]` - Send connection request
- `message [name] [text]` - Send message to connection
- `like [url]` - Like a post
- `comment [url] [text]` - Comment on a post
- `view [profile-url]` - View a profile

---

## Prompt

Activate the LinkedIn adapter skill: `.claude/skills/10x-team/outreach/skills/linkedin-adapter/SKILL.md`

Parse arguments: `$ARGUMENTS`

### Rate Limits (Built-in)
| Action | Daily Limit | Delay |
|--------|-------------|-------|
| Connections | 20 | 2-10 min |
| Messages | 50 | 2-10 min |
| Profile Views | 100 | 1-3 min |

### Browser-Use MCP Integration
Uses `mcp__browser-use__browser_task` for automation.

1. First, check for authenticated profile:
   ```
   mcp__browser-use__list_browser_profiles
   ```

2. Execute action with appropriate profile

---

## Examples

```
/10x/linkedin connect "Product managers at tech startups"
/10x/linkedin message "John Doe" "Hi, loved your recent post on AI!"
/10x/linkedin like https://linkedin.com/posts/...
/10x/linkedin comment https://linkedin.com/posts/... "Great insights!"
```

---

## Templates

Available in `.claude/skills/10x-team/outreach/templates/linkedin/`:
- Connection requests (12 templates)
- Messages (11 templates)
- InMails (3 templates)
- Comments (3 templates)
