---
name: Introduction After Connection
type: message
max_length: 8000
description: First message after connection is accepted
tags: [intro, first-message, warm]
---
Hi {{ first_name }},

Thanks for connecting! I've been following {{ company }}'s journey and really admire {{ specific_interest | default("what you're building") }}.

{{ custom_message | default("I'm particularly interested in how you're approaching the challenges in this space.") }}

Would love to learn more about your work. What's the most exciting thing you're working on right now?

Best,
{{ my_name }}
