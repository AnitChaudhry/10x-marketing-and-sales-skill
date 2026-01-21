---
name: After Follow DM
type: dm
max_length: 1000
description: Message after following someone
tags: [warm, follow-up, introduction]
delay_after_follow: 2-4 hours
---
Hey {{ first_name | default("") }}! 👋

Just followed you - {{ reason | default("your content is amazing") }}! 🔥

{{ specific_praise | default("Really love " + (recent_post | default("what you're sharing")) + ".") }}

{{ question | default("How long have you been creating content?") }}
