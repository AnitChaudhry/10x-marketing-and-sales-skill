---
name: Podcast Guest Invitation
type: dm
max_length: 10000
description: Invite someone to your podcast
tags: [podcast, invitation, content]
---
Hey {{ first_name }}!

I host {{ podcast_name | default("a podcast") }} about {{ podcast_topic | default("industry insights") }} and your perspective would be perfect for our audience.

{{ why_them | default("Your takes on building in public and the creator economy are exactly what our listeners want to hear.") }}

Format: {{ format | default("45-60 min conversation, remote recording") }}

Would you be interested?
