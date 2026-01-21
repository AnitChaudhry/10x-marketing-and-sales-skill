---
name: After Call Follow Up
type: follow_up
subject: "{{ subject | default('Following up on our call') }}"
description: Follow up after a phone/video call
tags: [follow-up, post-call, summary]
delay_days: 0
---
Hi {{ first_name }},

{{ opening | default("Thanks for taking the time to chat today!") }}

{{ summary | default("To recap our conversation:") }}

{{ key_points | default("- [Key point 1]\n- [Key point 2]\n- [Key point 3]") }}

{{ next_steps | default("**Next Steps:**\n- [Your action item]\n- [Their action item]") }}

{{ resources | default("As promised, here are the resources I mentioned:") }}
{{ resource_links | default("- [Resource 1]\n- [Resource 2]") }}

{{ cta | default("Let me know if you have any questions or need anything else.") }}

{{ closing | default("Looking forward to " + (next_meeting | default("our next conversation")) + "!") }}

Best,
{{ my_name }}
