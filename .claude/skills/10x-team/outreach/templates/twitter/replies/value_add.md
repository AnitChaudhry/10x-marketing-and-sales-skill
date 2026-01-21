---
name: Value Add Reply
type: reply
max_length: 280
description: Reply that adds value to the conversation
tags: [value, engagement, helpful]
---
{{ acknowledgment | default("Great point!") }} {{ addition | default("I'd add:") }}

{{ insight | default("[Your valuable insight here]") }}

{{ question | default("") }}
