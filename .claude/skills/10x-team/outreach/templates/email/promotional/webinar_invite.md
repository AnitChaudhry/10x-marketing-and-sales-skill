---
name: Webinar Invite
type: promotional
subject: "{{ subject | default('You\\'re invited: ' + (webinar_title | default('[Webinar Title]'))) }}"
description: Invite to a webinar or event
tags: [promotional, webinar, event, invite]
---
Hi {{ first_name }},

{{ opening | default("I'd love to invite you to an upcoming event...") }}

**{{ webinar_title | default("[Webinar Title]") }}**

{{ description | default("[Brief description of what attendees will learn]") }}

**Details:**
- 📅 Date: {{ date | default("[Date]") }}
- 🕐 Time: {{ time | default("[Time]") }}
- 📍 Where: {{ location | default("Online (Zoom)") }}
- ⏱️ Duration: {{ duration | default("45 minutes") }}

**What you'll learn:**
{{ agenda | default("- [Topic 1]\n- [Topic 2]\n- [Topic 3]") }}

**Who should attend:**
{{ audience | default("[Target audience description]") }}

{{ bonus | default("") }}

{{ cta | default("[Save your spot →](" + (registration_link | default("[link]")) + ")") }}

{{ urgency | default("Seats are limited - register now to secure your spot!") }}

See you there!

{{ my_name }}
{{ my_title | default("") }}
