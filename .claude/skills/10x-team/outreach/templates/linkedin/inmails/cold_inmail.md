---
name: Cold InMail
type: inmail
max_length: 1900
subject_max_length: 200
description: Cold outreach via LinkedIn InMail (premium)
tags: [cold, premium, inmail]
---
Subject: {{ subject | default("Quick question about " + (company | default("your work"))) }}

Hi {{ first_name }},

I know we're not connected, but I came across your profile while researching {{ industry | default("leaders in this space") }} and was impressed by {{ impressive_thing | default("your background and what you've built at " + (company | default("your company"))) }}.

{{ custom_message | default("I'm reaching out because I believe there might be an interesting opportunity for us to connect.") }}

{{ value_proposition | default("I'd love to share some insights that might be relevant to what you're working on.") }}

Would you be open to a brief conversation? I promise to keep it focused and valuable for you.

Best regards,
{{ my_name }}
{{ my_title | default("") }}
