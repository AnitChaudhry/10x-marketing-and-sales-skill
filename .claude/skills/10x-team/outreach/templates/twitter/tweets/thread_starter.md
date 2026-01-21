---
name: Thread Starter
type: tweet
max_length: 280
description: Start a thread (first tweet)
tags: [thread, content, engagement]
---
{{ hook | default("Here's what I learned about " + (topic | default("[topic]")) + ":") }}

{{ teaser | default("A thread 🧵👇") }}
