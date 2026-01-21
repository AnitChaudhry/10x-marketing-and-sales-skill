---
name: Follow Up Final - Break Up
type: follow_up
subject: "{{ subject | default('Should I close your file?') }}"
description: Final follow-up (break-up email)
tags: [follow-up, final, break-up]
delay_days: 7
sequence: 3
---
Hi {{ first_name }},

{{ opening | default("I've tried reaching out a few times and haven't heard back.") }}

{{ assumption | default("I'm guessing this isn't a priority right now, which is totally fine.") }}

{{ offer | default("If things change in the future, feel free to reach out. I'd be happy to pick up the conversation.") }}

{{ closing | default("Wishing you and the team at " + (company | default("[company]")) + " all the best!") }}

{{ my_name }}

{{ ps | default("P.S. If I've been reaching the wrong person, I'd appreciate a point in the right direction.") }}
