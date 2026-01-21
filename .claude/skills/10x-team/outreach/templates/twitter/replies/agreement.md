---
name: Agreement Reply
type: reply
max_length: 280
description: Agree and build on their point
tags: [agreement, engagement, support]
---
{{ agreement | default("100% agree") }} {{ first_name | default("") }}. {{ elaboration | default("This has been my experience too.") }}

{{ example | default("") }}
