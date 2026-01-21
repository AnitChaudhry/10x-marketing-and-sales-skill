---
name: Story Mention
type: story_mention
max_length: 1000
description: When you mention them in your story
tags: [mention, shoutout, collaboration]
---
Shoutout to {{ handle }} {{ emoji | default("🙌") }}

{{ reason | default("Go follow them for amazing content!") }} {{ emoji2 | default("✨") }}
