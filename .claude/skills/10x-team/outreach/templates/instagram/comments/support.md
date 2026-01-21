---
name: Support Comment
type: comment
max_length: 2200
description: Show support and encouragement
tags: [support, encouragement, community]
---
{{ support | default("So proud of you!") }} {{ emoji | default("🙌") }} {{ specific | default("You've been crushing it lately!") }}

{{ encouragement | default("Can't wait to see what's next!") }} {{ emoji2 | default("💪") }}
