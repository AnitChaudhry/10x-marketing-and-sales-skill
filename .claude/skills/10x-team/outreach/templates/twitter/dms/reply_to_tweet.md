---
name: DM After Tweet Reply
type: dm
max_length: 10000
description: Follow up in DM after replying to their tweet
tags: [warm, engagement, follow-up]
---
Hey {{ first_name | default("") }}!

Just replied to your tweet about {{ tweet_topic | default("that topic") }} - {{ follow_up | default("wanted to continue the conversation here") }}.

{{ custom_message | default("I've been thinking about this a lot and would love to hear more about your perspective.") }}

{{ question | default("Have you written more about this anywhere?") }}
