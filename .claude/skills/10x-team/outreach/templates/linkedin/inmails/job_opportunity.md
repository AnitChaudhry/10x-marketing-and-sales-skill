---
name: Job Opportunity
type: inmail
max_length: 1900
subject_max_length: 200
description: Reach out about a job opening
tags: [recruiting, hiring, job, hr]
---
Subject: {{ subject | default("Exciting opportunity at " + (my_company | default("a growing company"))) }}

Hi {{ first_name }},

Your experience as {{ title | default("a professional") }} at {{ company }} caught my attention. {{ specific_reason | default("Your background aligns perfectly with what we're looking for.") }}

We're building something exciting at {{ my_company | default("our company") }} and are looking for {{ role_description | default("talented individuals like yourself") }}.

The role offers:
{{ benefits | default("- Competitive compensation\n- Growth opportunities\n- Great team culture") }}

Would you be open to a confidential conversation to learn more? Even if the timing isn't right, I'd love to connect for future opportunities.

Best,
{{ my_name }}
{{ my_title | default("Recruiter") }}
