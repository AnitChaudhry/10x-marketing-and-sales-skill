---
name: Speaker Invitation
type: connection_request
max_length: 300
description: Invite someone to speak at an event
tags: [speaker, event, invitation]
---
Hi {{ first_name }},

I'm organizing {{ event_name | default("an upcoming event") }} focused on {{ topic | default("industry insights") }}. Your expertise would be perfect for our audience.

Would love to connect and share more details about a potential speaking opportunity.

{{ my_name }}
