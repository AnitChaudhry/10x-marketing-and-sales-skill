---
name: Collaboration Proposal
type: message
max_length: 8000
description: Propose a collaboration or partnership
tags: [collaboration, partnership, business]
---
Hi {{ first_name }},

I've been thinking about how {{ company }} and {{ my_company | default("what I'm working on") }} might complement each other.

{{ collaboration_idea | default("There seems to be a natural fit between our audiences and offerings that could benefit both sides.") }}

Here's what I had in mind:
{{ proposal_details | default("- A joint piece of content or webinar\n- Cross-promotion to each other's networks\n- Exploring a deeper partnership") }}

Would you be interested in exploring this further? I'm flexible on the format and open to your ideas.

{{ my_name }}
