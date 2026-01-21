# 100X Outreach Templates

This folder contains all message templates for the 100X Outreach System, organized by platform.

## Directory Structure

```
templates/
├── linkedin/                    # LinkedIn templates
│   ├── README.md               # LinkedIn-specific documentation
│   ├── connection-requests/    # Connection request notes (300 chars max)
│   ├── messages/               # Direct messages after connection
│   ├── inmails/                # InMail templates (premium)
│   └── comments/               # Post comment templates
│
├── twitter/                     # Twitter/X templates
│   ├── README.md               # Twitter-specific documentation
│   ├── dms/                    # Direct messages
│   ├── tweets/                 # Tweet and quote tweet templates
│   └── replies/                # Reply templates
│
├── instagram/                   # Instagram templates
│   ├── README.md               # Instagram-specific documentation
│   ├── dms/                    # Direct messages
│   ├── comments/               # Post comment templates
│   └── stories/                # Story reply templates
│
└── email/                       # Email templates
    ├── README.md               # Email-specific documentation
    ├── outreach/               # Cold/warm outreach emails
    ├── follow-up/              # Follow-up sequences
    ├── promotional/            # Promotional emails
    └── newsletters/            # Newsletter templates
```

## Quick Start

### 1. List All Templates

```bash
python scripts/template_loader.py list
```

### 2. List Templates by Platform

```bash
python scripts/template_loader.py list --platform linkedin
python scripts/template_loader.py list --platform twitter
python scripts/template_loader.py list --platform instagram
python scripts/template_loader.py list --platform email
```

### 3. View a Template

```bash
python scripts/template_loader.py get linkedin/connection-requests/cold_outreach
```

### 4. Render a Template

```bash
python scripts/template_loader.py render linkedin/messages/intro_after_connect \
  --var first_name "John" \
  --var company "Acme Inc" \
  --var my_name "Sarah"
```

### 5. Search Templates

```bash
python scripts/template_loader.py search "cold"
python scripts/template_loader.py search "follow-up"
```

## Template Format

All templates use **Jinja2** syntax with **YAML frontmatter**:

```markdown
---
name: Template Name
type: dm | message | email | comment
max_length: 300
subject: "Email subject line (for emails only)"
description: What this template is for
tags: [cold, warm, b2b]
---

Hi {{ first_name }},

Your message here with {{ variables }}.

Best,
{{ my_name }}
```

## Available Variables

### Common Variables (All Platforms)

| Variable | Description |
|----------|-------------|
| `{{ first_name }}` | Recipient's first name |
| `{{ last_name }}` | Recipient's last name |
| `{{ name }}` | Full name |
| `{{ company }}` | Their company |
| `{{ title }}` | Their job title |
| `{{ my_name }}` | Your name |
| `{{ my_company }}` | Your company |
| `{{ custom_message }}` | Custom personalization |

### Platform-Specific Variables

| Platform | Variable | Description |
|----------|----------|-------------|
| LinkedIn | `{{ linkedin_url }}` | Their LinkedIn URL |
| LinkedIn | `{{ mutual_connection }}` | Shared connection |
| Twitter | `{{ handle }}` | Their @handle |
| Twitter | `{{ recent_tweet }}` | Topic of recent tweet |
| Instagram | `{{ handle }}` | Their @handle |
| Instagram | `{{ story_content }}` | What their story showed |
| Email | `{{ email }}` | Their email address |
| Email | `{{ calendar_link }}` | Your scheduling link |

## Character Limits

| Platform | Type | Max Length |
|----------|------|------------|
| LinkedIn | Connection Request | 300 |
| LinkedIn | Message | 8,000 |
| LinkedIn | InMail | 1,900 |
| LinkedIn | Comment | 1,250 |
| Twitter | Tweet/Reply | 280 |
| Twitter | DM | 10,000 |
| Instagram | DM | 1,000 |
| Instagram | Comment | 2,200 |
| Email | Subject | ~50 recommended |
| Email | Body | No limit |

## Adding Custom Templates

1. **Create a file** in the appropriate folder:
   ```
   templates/linkedin/messages/my_custom_template.md
   ```

2. **Add frontmatter** with metadata:
   ```yaml
   ---
   name: My Custom Template
   type: message
   max_length: 8000
   description: My custom outreach template
   tags: [custom, b2b, saas]
   ---
   ```

3. **Write your template** using Jinja2 variables:
   ```
   Hi {{ first_name }},

   {{ custom_message }}

   Best,
   {{ my_name }}
   ```

4. **Test your template**:
   ```bash
   python scripts/template_loader.py render linkedin/messages/my_custom_template \
     --var first_name "Test" --var my_name "Me"
   ```

## Best Practices

### General

- **Personalize**: Use at least 2-3 personalized elements
- **Be Concise**: Shorter messages get better response rates
- **Value First**: Lead with value, not asks
- **Clear CTA**: One specific ask per message

### Platform-Specific

**LinkedIn:**
- Keep connection requests under 300 characters
- Reference their work or company specifically
- Avoid salesy language

**Twitter:**
- Match the casual, conversational tone
- Use 1-2 emojis maximum
- Keep it brief - under 280 characters

**Instagram:**
- Be authentic and match the platform vibe
- Emojis are expected (2-4 is fine)
- Story replies are great ice breakers

**Email:**
- Short subject lines (under 50 chars)
- Mobile-friendly formatting
- Avoid spam trigger words

## Template Categories

### Outreach Templates
- Cold outreach to strangers
- Warm intros via mutual connections
- Referral-based introductions

### Engagement Templates
- Post comments
- Tweet replies
- Story reactions

### Follow-Up Templates
- No response sequences
- Post-meeting follow-ups
- Check-ins

### Promotional Templates
- Product launches
- Feature announcements
- Webinar invites

## Integration with Workflows

Templates are automatically loaded by the workflow engine:

```yaml
# In your workflow YAML
phases:
  - name: "connect"
    platform: "linkedin"
    action: "connect"
    template: "linkedin/connection-requests/cold_outreach"
```

The template loader will:
1. Load the template
2. Render with discovered person's data
3. Validate character limits
4. Pass to the platform adapter for sending

## Exporting Template List

Generate a markdown list of all templates:

```bash
python scripts/template_loader.py export --output TEMPLATE_LIST.md
```
