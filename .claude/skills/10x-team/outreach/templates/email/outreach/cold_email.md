---
name: Cold Email
type: cold_email
subject: "{{ subject | default('Quick question about ' + (company | default('your work'))) }}"
description: General cold outreach email
tags: [cold, b2b, outreach]
---
Hi {{ first_name }},

{{ opening | default("I came across " + (company | default("your work")) + " and was impressed by " + (impressive_thing | default("what you're building")) + ".") }}

{{ connection | default("I'm reaching out because I believe there might be an interesting opportunity to connect.") }}

{{ value_proposition | default("At " + (my_company | default("[my company]")) + ", we help companies like yours " + (value | default("[solve X problem]")) + ".") }}

{{ social_proof | default("") }}

{{ cta | default("Would you be open to a quick 15-minute call to explore if there's a fit?") }}

Best regards,
{{ my_name }}
{{ my_title | default("") }}
{{ my_company | default("") }}

{{ ps | default("") }}
