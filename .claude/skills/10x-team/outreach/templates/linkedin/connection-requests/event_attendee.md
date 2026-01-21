---
name: Event Attendee
type: connection_request
max_length: 300
description: Connect after meeting at an event
tags: [event, conference, networking, warm]
---
Hi {{ first_name }},

Great connecting at {{ event_name | default("the event") }}! Really enjoyed our conversation about {{ topic | default("the industry") }}. Let's stay in touch.

{{ my_name }}
