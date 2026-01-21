---
name: Follow Up 1 - No Response
type: follow_up
subject: "{{ subject | default('Re: ' + (original_subject | default('My previous email'))) }}"
description: First follow-up after no response
tags: [follow-up, reminder, gentle]
delay_days: 3
sequence: 1
---
Hi {{ first_name }},

{{ opening | default("Just wanted to follow up on my previous email.") }}

{{ brief_reminder | default("I reached out about " + (topic | default("[topic]")) + " and thought it might be valuable for " + (company | default("you")) + ".") }}

{{ new_value | default("Since then, " + (update | default("[new relevant update or value add]")) + ".") }}

{{ cta | default("Would you have a few minutes to chat this week?") }}

{{ closing | default("No worries if the timing isn't right - just let me know either way.") }}

Best,
{{ my_name }}
