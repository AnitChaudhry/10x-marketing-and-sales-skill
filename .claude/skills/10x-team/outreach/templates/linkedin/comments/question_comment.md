---
name: Question Comment
type: comment
max_length: 1250
description: Ask a thoughtful question on a post
tags: [engagement, question, comment]
---
{{ acknowledgment | default("Really interesting perspective") }}! {{ context | default("This got me thinking about") }} {{ topic | default("the broader implications") }}.

{{ question | default("How do you see this evolving in the next few years?") }}

Would love to hear more about {{ specific_aspect | default("your experience with this") }}.
