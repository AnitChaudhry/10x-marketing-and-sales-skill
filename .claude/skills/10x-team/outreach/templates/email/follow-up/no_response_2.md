---
name: Follow Up 2 - No Response
type: follow_up
subject: "{{ subject | default('Quick follow up') }}"
description: Second follow-up after no response
tags: [follow-up, persistence, brief]
delay_days: 5
sequence: 2
---
Hi {{ first_name }},

{{ opening | default("Bumping this to the top of your inbox.") }}

{{ value_add | default("Thought this might be helpful: " + (resource | default("[relevant resource or insight]")) + ".") }}

{{ cta | default("Worth a quick conversation?") }}

{{ my_name }}
