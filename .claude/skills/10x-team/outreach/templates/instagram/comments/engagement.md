---
name: Engagement Comment
type: comment
max_length: 2200
description: General engagement comment on posts
tags: [engagement, visibility, warm]
---
{{ reaction | default("This is amazing") }} {{ emoji | default("🔥") }} {{ specific_praise | default("Love the creativity here!") }}

{{ question_or_add | default("") }}
