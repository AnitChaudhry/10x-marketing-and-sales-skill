---
name: Mutual Follower
type: dm
max_length: 1000
description: Message someone who follows you back
tags: [warm, mutual, networking]
---
Hey {{ first_name | default("") }}! 👋

Thanks for the follow back! {{ observation | default("Looks like we're into similar things.") }}

{{ custom_message | default("I've been loving your content, especially " + (recent_post | default("your recent posts")) + ".") }}

{{ question | default("What inspired you to start creating?") }} 💫
