---
name: Congratulations
type: comment
max_length: 1250
description: Congratulate on achievement, new role, etc.
tags: [congratulations, celebration, positive]
---
Congratulations, {{ first_name | default("") }}! {{ specific_praise | default("This is well-deserved.") }}

{{ personal_note | default("I've always been impressed by your work and dedication.") }}

{{ well_wish | default("Wishing you continued success in this new chapter!") }} 🎉
