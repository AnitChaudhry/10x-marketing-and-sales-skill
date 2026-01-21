# Instagram Templates

This folder contains all Instagram message templates for the 100X Outreach System.

## Folder Structure

```
instagram/
├── dms/                   # Direct Messages
│   ├── cold_dm.md
│   ├── after_follow.md
│   ├── story_reply.md
│   ├── mutual_follower.md
│   ├── collaboration.md
│   ├── business_inquiry.md
│   └── thank_you.md
│
├── comments/              # Post comments
│   ├── engagement.md
│   ├── compliment.md
│   ├── question.md
│   └── support.md
│
└── stories/               # Story replies and mentions
    ├── story_reply.md
    ├── story_mention.md
    └── story_reaction.md
```

## Template Format

All templates use **Jinja2** syntax with YAML frontmatter:

```markdown
---
name: Template Name
type: dm | comment | story_reply
max_length: 1000
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
| `{{ handle }}` | Their Instagram handle | @johnsmith |
| `{{ company }}` | Their company/brand | Acme Inc |
| `{{ recent_post }}` | Topic of recent post | travel photos |
| `{{ story_content }}` | What their story showed | your latest project |
| `{{ my_name }}` | Your name | Your Name |
| `{{ my_handle }}` | Your Instagram handle | @yourhandle |
| `{{ custom_message }}` | Custom personalization | - |

## Character Limits

| Type | Max Length |
|------|------------|
| DM | 1,000 characters |
| Comment | 2,200 characters |
| Story Reply | 1,000 characters |
| Bio | 150 characters |

## Best Practices

1. **Be Authentic**: Instagram is personal - match the vibe
2. **Use Emojis**: Expected on Instagram, but don't overdo it (2-4 max)
3. **Keep it Visual**: Reference their content specifically
4. **Be Casual**: Less formal than LinkedIn
5. **Avoid Links in First DM**: Can seem spammy
6. **Reply to Stories**: Great ice breaker

## Rate Limits (Conservative)

| Action | Daily Limit | Min Delay |
|--------|-------------|-----------|
| Follow | 30 | 90 seconds |
| DM | 30 | 90 seconds |
| Like | 100 | - |
| Comment | 30 | - |

## Adding Custom Templates

1. Create a new `.md` file in the appropriate folder
2. Add the YAML frontmatter with metadata
3. Keep the tone casual and authentic
4. Test before using in campaigns
