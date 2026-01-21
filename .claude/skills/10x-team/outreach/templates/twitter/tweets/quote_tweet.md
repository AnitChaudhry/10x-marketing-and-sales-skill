---
name: Quote Tweet
type: quote
max_length: 280
description: Quote tweet with added value
tags: [quote, engagement, amplify]
---
{{ your_take | default("This 👇") }}

{{ insight | default("Key takeaway: " + (point | default("[your insight]"))) }}

{{ hashtags | default("") }}
