---
name: Podcast Guest Invitation
type: message
max_length: 8000
description: Invite someone to be a podcast guest
tags: [podcast, invitation, content]
---
Hi {{ first_name }},

I host {{ podcast_name | default("a podcast") }} focused on {{ podcast_topic | default("industry insights and founder stories") }}. We've had guests like {{ previous_guests | default("other thought leaders in the space") }}.

Your expertise on {{ their_expertise | default("this topic") }} would be perfect for our audience of {{ audience | default("professionals and entrepreneurs") }}.

The format is casual - {{ format | default("about 45 minutes, conversational style") }}.

Would you be interested in being a guest? I can send over more details if so.

Best,
{{ my_name }}
