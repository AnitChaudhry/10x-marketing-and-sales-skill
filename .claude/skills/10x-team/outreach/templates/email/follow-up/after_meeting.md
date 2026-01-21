---
name: After Meeting Follow Up
type: follow_up
subject: "{{ subject | default('Great meeting you' + (' at ' + event_name if event_name else '')) }}"
description: Follow up after meeting someone
tags: [follow-up, post-meeting, warm]
delay_days: 1
---
Hi {{ first_name }},

{{ opening | default("It was great meeting you" + (" at " + (event_name | default("[event]")) if event_name else "") + "!") }}

{{ reference | default("I really enjoyed our conversation about " + (topic | default("[topic]")) + ".") }}

{{ next_step | default("As discussed, I wanted to " + (action | default("[share resource/schedule call/send proposal]")) + ".") }}

{{ resource | default("") }}

{{ cta | default("Let me know if you'd like to continue the conversation. I'm happy to " + (offer | default("[specific next step]")) + ".") }}

Looking forward to staying in touch!

Best,
{{ my_name }}
{{ my_title | default("") }}
