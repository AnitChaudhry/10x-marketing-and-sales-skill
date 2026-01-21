---
name: Value Offer
type: message
max_length: 8000
description: Offer something valuable without asking for anything
tags: [value, giving, relationship]
---
Hi {{ first_name }},

I came across {{ resource | default("something") }} that made me think of you and {{ company }}.

{{ value_description | default("Given your focus on this space, I thought you might find it useful.") }}

{{ resource_link | default("[Link to resource]") }}

No strings attached - just thought it might be helpful. Let me know what you think!

{{ my_name }}
