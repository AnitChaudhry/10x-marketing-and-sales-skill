---
name: Collaboration Request
type: dm
max_length: 1000
description: Propose collaboration via DM
tags: [collaboration, partnership, business, creator]
---
Hey {{ first_name | default("") }}! 👋

I've been following your content for a while and absolutely love {{ what_you_love | default("your style") }}! ✨

{{ proposal_intro | default("I had an idea for a potential collab:") }}

{{ collaboration_idea | default("Would love to explore doing something together - maybe a joint post, reel, or story takeover?") }}

{{ cta | default("Would you be open to chatting about it?") }} 🙌

- {{ my_name }}
