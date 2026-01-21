---
name: Compliment Comment
type: comment
max_length: 2200
description: Genuine compliment on their content
tags: [compliment, positive, engagement]
---
{{ compliment | default("Absolutely stunning") }} {{ emoji | default("😍") }} {{ specific_detail | default("The composition is perfect!") }}

{{ encouragement | default("Keep creating!") }} {{ emoji2 | default("✨") }}
