---
name: Check In
type: follow_up
subject: "{{ subject | default('Checking in') }}"
description: General check-in with existing contact
tags: [check-in, relationship, nurture]
delay_days: 30
---
Hi {{ first_name }},

{{ opening | default("Hope you're doing well! Wanted to check in and see how things are going at " + (company | default("[company]")) + ".") }}

{{ context | default("It's been a while since we last connected and I've been thinking about " + (topic | default("our conversation")) + ".") }}

{{ value_add | default("Thought you might find this interesting: " + (resource | default("[relevant resource or insight]")) + ".") }}

{{ question | default("How's everything going on your end? Any exciting updates?") }}

{{ offer | default("If there's ever anything I can help with, don't hesitate to reach out.") }}

Best,
{{ my_name }}
