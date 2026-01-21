# Twitter/X Templates

This folder contains all Twitter/X message templates for the 100X Outreach System.

## Folder Structure

```
twitter/
├── dms/                   # Direct Messages
│   ├── cold_dm.md
│   ├── after_follow.md
│   ├── mutual_follower.md
│   ├── reply_to_tweet.md
│   ├── collaboration.md
│   └── thank_you.md
│
├── tweets/                # Public tweets and quote tweets
│   ├── engagement_reply.md
│   ├── quote_tweet.md
│   ├── mention.md
│   └── thread_starter.md
│
└── replies/               # Reply templates
    ├── value_add.md
    ├── question.md
    ├── agreement.md
    └── insight.md
```

## Template Format

All templates use **Jinja2** syntax with YAML frontmatter:

```markdown
---
name: Template Name
type: dm | tweet | reply | quote
max_length: 280
description: What this template is for
tags: [cold, warm, engagement]
---

Hey {{ first_name }}! 👋

Your message here with {{ variables }}.

{{ my_handle }}
```

## Available Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{ first_name }}` | Recipient's first name | John |
| `{{ name }}` | Display name | John Smith |
| `{{ handle }}` | Their Twitter handle | @johnsmith |
| `{{ company }}` | Their company | Acme Inc |
| `{{ recent_tweet }}` | Topic of recent tweet | AI trends |
| `{{ tweet_url }}` | URL of specific tweet | https://x.com/... |
| `{{ my_name }}` | Your name | Your Name |
| `{{ my_handle }}` | Your Twitter handle | @yourhandle |
| `{{ custom_message }}` | Custom personalization | - |

## Character Limits

| Type | Max Length |
|------|------------|
| Tweet | 280 characters |
| DM | 10,000 characters |
| Reply | 280 characters |
| Quote Tweet | 280 characters (+ quoted tweet) |

## Best Practices

1. **Keep it Short**: Twitter favors brevity
2. **Use Emojis Sparingly**: 1-2 max, match the platform tone
3. **Be Conversational**: Twitter is casual
4. **Add Value**: Don't just say "great tweet"
5. **Avoid Links in DMs**: Can trigger spam filters

## Rate Limits (Conservative)

| Action | Daily Limit | Min Delay |
|--------|-------------|-----------|
| Follow | 50 | 60 seconds |
| DM | 50 | 60 seconds |
| Tweet | 20 | - |
| Like | 100 | - |

## Adding Custom Templates

1. Create a new `.md` file in the appropriate folder
2. Add the YAML frontmatter with metadata
3. Keep it under character limits
4. Test before using in campaigns
