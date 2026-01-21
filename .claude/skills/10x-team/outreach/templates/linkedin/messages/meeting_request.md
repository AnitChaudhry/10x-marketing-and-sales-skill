---
name: Meeting Request
type: message
max_length: 8000
description: Ask for a call or meeting
tags: [meeting, call, calendar]
---
Hi {{ first_name }},

I hope you're doing well! I've really enjoyed our exchanges and would love to take the conversation further.

{{ custom_message | default("I think there's a lot we could learn from each other, and a quick chat might surface some interesting opportunities.") }}

Would you be open to a {{ meeting_type | default("15-minute call") }} sometime in the next week or two? Happy to work around your schedule.

Here's my calendar if that's easier: {{ calendar_link | default("[calendar link]") }}

Looking forward to it!

{{ my_name }}
