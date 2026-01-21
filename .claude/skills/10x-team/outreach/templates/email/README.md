# Email Templates

This folder contains all email templates for the 100X Outreach System.

## Folder Structure

```
email/
├── outreach/              # Cold/warm outreach emails
│   ├── cold_email.md
│   ├── warm_intro.md
│   ├── referral_intro.md
│   ├── partnership.md
│   └── investor_pitch.md
│
├── follow-up/             # Follow-up emails
│   ├── no_response_1.md
│   ├── no_response_2.md
│   ├── no_response_final.md
│   ├── after_meeting.md
│   ├── after_call.md
│   └── check_in.md
│
├── promotional/           # Promotional emails
│   ├── product_launch.md
│   ├── feature_announcement.md
│   ├── discount_offer.md
│   └── webinar_invite.md
│
└── newsletters/           # Newsletter templates
    ├── weekly_digest.md
    ├── monthly_update.md
    └── announcement.md
```

## Template Format

All templates use **Jinja2** syntax with YAML frontmatter:

```markdown
---
name: Template Name
type: cold_email | follow_up | promotional | newsletter
subject: "Email subject with {{ variables }}"
description: What this template is for
tags: [cold, b2b, saas]
---

Hi {{ first_name }},

Your email body here with {{ variables }}.

Best regards,
{{ my_name }}
{{ my_title }}
{{ my_company }}
```

## Available Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{ first_name }}` | Recipient's first name | John |
| `{{ last_name }}` | Recipient's last name | Smith |
| `{{ name }}` | Full name | John Smith |
| `{{ email }}` | Their email | john@company.com |
| `{{ company }}` | Their company | Acme Inc |
| `{{ title }}` | Their job title | CEO |
| `{{ industry }}` | Their industry | SaaS |
| `{{ website }}` | Their website | acme.com |
| `{{ my_name }}` | Your name | Your Name |
| `{{ my_email }}` | Your email | you@company.com |
| `{{ my_title }}` | Your job title | Founder |
| `{{ my_company }}` | Your company | Your Company |
| `{{ custom_message }}` | Custom personalization | - |
| `{{ calendar_link }}` | Your scheduling link | calendly.com/you |

## Subject Line Variables

Subjects are defined in the frontmatter and can use the same variables:

```yaml
subject: "Quick question about {{ company }}"
subject: "{{ first_name }}, thought you'd find this useful"
subject: "Following up on {{ topic }}"
```

## Best Practices

1. **Personalize**: Use at least 2-3 personalized elements
2. **Short Subject Lines**: Under 50 characters
3. **Clear CTA**: One specific ask per email
4. **Value First**: Lead with what's in it for them
5. **Mobile Friendly**: Many read on phones - keep it scannable
6. **No Attachments**: In cold emails, avoid attachments

## Email Deliverability Tips

1. **Warm Up**: New email accounts need warming
2. **Avoid Spam Words**: "Free", "Act now", etc.
3. **Plain Text**: Consider plain text for cold emails
4. **Unsubscribe**: Include opt-out for bulk emails
5. **Throttle**: Use rate limiting (60+ seconds between)

## Adding Custom Templates

1. Create a new `.md` file in the appropriate folder
2. Add the YAML frontmatter with `subject` field
3. Write your template using Jinja2 variables
4. Test with a dry run before live campaigns
