# LinkedIn Templates

This folder contains all LinkedIn message templates for the 100X Outreach System.

## Folder Structure

```
linkedin/
├── connection-requests/    # Connection request notes (max 300 chars)
│   ├── cold_outreach.md
│   ├── mutual_connection.md
│   ├── same_industry.md
│   ├── recruiter.md
│   ├── investor_outreach.md
│   └── event_attendee.md
│
├── messages/               # Direct messages after connection
│   ├── intro_after_connect.md
│   ├── follow_up_no_response.md
│   ├── meeting_request.md
│   ├── collaboration_proposal.md
│   ├── value_offer.md
│   └── thank_you.md
│
├── inmails/               # LinkedIn InMail (premium feature)
│   ├── cold_inmail.md
│   ├── executive_outreach.md
│   └── job_opportunity.md
│
└── comments/              # Post comments for engagement
    ├── thoughtful_engagement.md
    ├── question_comment.md
    └── congratulations.md
```

## Template Format

All templates use **Jinja2** syntax with YAML frontmatter:

```markdown
---
name: Template Name
type: connection_request | message | inmail | comment
max_length: 300
description: What this template is for
tags: [cold, warm, b2b, saas]
---

Hi {{ first_name }},

Your message here with {{ variables }}.

{{ my_name }}
```

## Available Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{ first_name }}` | Recipient's first name | John |
| `{{ last_name }}` | Recipient's last name | Smith |
| `{{ name }}` | Full name | John Smith |
| `{{ company }}` | Their company | Acme Inc |
| `{{ title }}` | Their job title | CEO |
| `{{ industry }}` | Their industry | SaaS |
| `{{ location }}` | Their location | San Francisco |
| `{{ mutual_connection }}` | Shared connection name | Sarah |
| `{{ recent_post }}` | Topic of recent post | AI trends |
| `{{ my_name }}` | Your name (from .env) | Your Name |
| `{{ my_company }}` | Your company | Your Company |
| `{{ my_title }}` | Your job title | Founder |
| `{{ custom_message }}` | Custom personalization | - |

## Character Limits

| Type | Max Length |
|------|------------|
| Connection Request Note | 300 characters |
| Regular Message | 8,000 characters |
| InMail | 1,900 characters (subject: 200) |
| Comment | 1,250 characters |

## Best Practices

1. **Personalize**: Always include at least one personalized element
2. **Be Concise**: Shorter messages get better response rates
3. **Value First**: Lead with value, not asks
4. **No Spam**: Avoid salesy language
5. **Call to Action**: End with a clear, low-commitment CTA

## Adding Custom Templates

1. Create a new `.md` file in the appropriate folder
2. Add the YAML frontmatter with metadata
3. Write your template using Jinja2 variables
4. Test with a dry run before live campaigns
