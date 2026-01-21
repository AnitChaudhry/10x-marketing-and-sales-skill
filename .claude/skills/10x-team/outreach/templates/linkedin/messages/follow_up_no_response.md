---
name: Follow Up - No Response
type: message
max_length: 8000
description: Follow up when someone hasn't responded
tags: [follow-up, reminder, persistence]
delay_days: 5
---
Hi {{ first_name }},

Just wanted to follow up on my previous message. I know you're busy, so I'll keep this brief.

{{ custom_message | default("I genuinely think there could be some interesting synergies between what we're both working on.") }}

If now isn't a good time, no worries at all. Would be happy to reconnect whenever works better for you.

{{ my_name }}
