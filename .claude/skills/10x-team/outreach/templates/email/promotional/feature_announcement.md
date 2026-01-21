---
name: Feature Announcement
type: promotional
subject: "{{ subject | default('New: ' + (feature_name | default('[Feature]')) + ' is here') }}"
description: Announce a new feature
tags: [promotional, feature, update]
---
Hi {{ first_name }},

{{ opening | default("Quick update on something you asked for...") }}

**New Feature: {{ feature_name | default("[Feature Name]") }}**

{{ description | default("[What the feature does]") }}

**How it works:**
{{ how_it_works | default("1. [Step 1]\n2. [Step 2]\n3. [Step 3]") }}

**Why you'll love it:**
{{ benefits | default("- [Benefit 1]\n- [Benefit 2]") }}

{{ availability | default("This is now available in your account.") }}

{{ cta | default("[Try it now →](" + (link | default("[link]")) + ")") }}

{{ closing | default("As always, let us know what you think!") }}

{{ my_name }}
