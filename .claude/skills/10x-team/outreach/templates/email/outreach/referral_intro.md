---
name: Referral Introduction
type: warm_email
subject: "{{ subject | default((referrer_name | default('Your colleague')) + ' recommended I connect with you') }}"
description: Email when referred by someone
tags: [referral, warm, trusted]
---
Hi {{ first_name }},

{{ referrer_name | default("[Referrer]") }} from {{ referrer_company | default("[company]") }} recommended I get in touch with you. {{ referrer_context | default("They spoke highly of your work at " + (company | default("[company]")) + ".") }}

{{ why_reaching_out | default("I'm reaching out because " + (reason | default("[reason]")) + ".") }}

{{ about_us | default("A bit about us: " + (company_description | default("[brief company description]")) + ".") }}

{{ value_for_them | default("I believe we could help you with " + (value | default("[specific value]")) + ".") }}

{{ cta | default("Would you be open to a brief conversation to explore this further?") }}

{{ referrer_name | default("[Referrer]") }} cc'd so they can make a warm intro if preferred.

Best regards,
{{ my_name }}
{{ my_title | default("") }}
