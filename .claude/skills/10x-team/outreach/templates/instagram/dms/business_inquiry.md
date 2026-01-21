---
name: Business Inquiry
type: dm
max_length: 1000
description: Professional business outreach
tags: [business, professional, partnership]
---
Hi {{ first_name | default("") }}! 👋

{{ intro | default("I represent " + (my_company | default("[company]")) + " and came across your incredible profile.") }}

{{ compliment | default("Your content and engagement are really impressive!") }} 🔥

{{ business_proposal | default("We're looking for creators like you to partner with and would love to discuss a potential opportunity.") }}

{{ cta | default("Would you be interested in learning more?") }}

Best,
{{ my_name }}
{{ my_company | default("") }}
