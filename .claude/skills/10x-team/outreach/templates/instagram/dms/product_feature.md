---
name: Product Feature Request
type: dm
max_length: 1000
description: Ask to feature a product
tags: [product, feature, marketing]
---
Hey {{ first_name | default("") }}!

Love your content! Your audience seems like the perfect fit for {{ product | default("our product") }}.

{{ product_description | default("We've built something special that your followers would love") }}.

{{ offer | default("We'd love to send you a sample to try - no strings attached") }}.

{{ cta | default("Interested?") }}

- {{ my_name }}
