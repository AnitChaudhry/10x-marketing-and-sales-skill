---
name: Executive Outreach
type: inmail
max_length: 1900
subject_max_length: 200
description: Reach out to C-level executives
tags: [executive, c-level, premium, formal]
---
Subject: {{ subject | default("Idea for " + (company | default("your organization"))) }}

Dear {{ first_name }},

I've been following {{ company }}'s growth and your leadership in {{ industry | default("the industry") }}. {{ specific_observation | default("Your recent initiatives have been particularly impressive.") }}

{{ value_proposition | default("I'm reaching out because I believe I can help with a challenge that many organizations in your space face.") }}

Specifically:
{{ key_points | default("- [Key point 1]\n- [Key point 2]\n- [Key point 3]") }}

I understand your time is valuable. Would a brief {{ meeting_type | default("15-minute call") }} be possible to explore if there's a fit?

Respectfully,
{{ my_name }}
{{ my_title | default("") }}
{{ my_company | default("") }}
