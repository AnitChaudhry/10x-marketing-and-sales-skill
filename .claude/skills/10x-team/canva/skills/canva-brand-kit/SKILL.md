---
name: canva-brand-kit
description: |
  Manage and apply brand kits in Canva. Use this skill when user wants to work with
  brand colors, fonts, logos, or maintain brand consistency across designs. Helps
  define brand guidelines and ensures designs follow brand standards.
  Requires Canva Pro/Enterprise for full brand kit features.
---

# Canva Brand Kit & Templates

Manage brand identity and use brand templates with autofill functionality.

---

## Capabilities

1. **List Brand Templates** - View available brand templates (Enterprise)
2. **Get Template Details** - View template metadata and dataset
3. **Create Autofill** - Generate designs from templates with data (Enterprise)
4. **Brand Guidelines** - Document and manage brand standards

---

## Enterprise Features

### Brand Templates
Brand templates are pre-designed layouts that can be filled with custom data.

### Autofill
Automatically populate brand templates with your data to create personalized designs.

---

## Available Scripts

### List Brand Templates (Enterprise)
```bash
# List all brand templates
.venv\Scripts\python.exe scripts/list_brand_templates.py

# Search templates
.venv\Scripts\python.exe scripts/list_brand_templates.py --query "social media"

# Filter by ownership
.venv\Scripts\python.exe scripts/list_brand_templates.py --ownership owned

# Limit results
.venv\Scripts\python.exe scripts/list_brand_templates.py --limit 10

# JSON output
.venv\Scripts\python.exe scripts/list_brand_templates.py --json
```

### Get Brand Template (Enterprise)
```bash
# Get template details
.venv\Scripts\python.exe scripts/get_brand_template.py "template_id"

# Include dataset (fields for autofill)
.venv\Scripts\python.exe scripts/get_brand_template.py "template_id" --dataset

# JSON output
.venv\Scripts\python.exe scripts/get_brand_template.py "template_id" --json
```

### Create Autofill Design (Enterprise)
```bash
# Create design from template with data
.venv\Scripts\python.exe scripts/create_autofill.py "template_id" --data '{"headline": "Summer Sale", "price": "$99"}'

# With title for the new design
.venv\Scripts\python.exe scripts/create_autofill.py "template_id" --data '{"field1": "value1"}' --title "My Design"

# From data file
.venv\Scripts\python.exe scripts/create_autofill.py "template_id" --data-file "data/campaign.json" --title "Campaign Design"

# Wait for completion
.venv\Scripts\python.exe scripts/create_autofill.py "template_id" --data '{"name": "John"}' --wait

# JSON output
.venv\Scripts\python.exe scripts/create_autofill.py "template_id" --data '{"field": "value"}' --json
```

---

## Autofill Workflow

### Step 1: Find a Template
```bash
.venv\Scripts\python.exe scripts/list_brand_templates.py --query "social post"
```

### Step 2: Get Template Dataset
```bash
.venv\Scripts\python.exe scripts/get_brand_template.py "template_id" --dataset

# Output shows available fields:
# Dataset Fields (3):
#   - headline: text (required)
#   - subtext: text
#   - image_url: image
```

### Step 3: Create Autofill
```bash
.venv\Scripts\python.exe scripts/create_autofill.py "template_id" \
    --data '{"headline": "New Product Launch", "subtext": "Available now!"}' \
    --title "Product Launch Post"
```

---

## Data File Format

Create a JSON file for autofill data:

```json
{
  "headline": "Summer Sale",
  "subtext": "Up to 50% off everything",
  "price": "$99",
  "cta": "Shop Now",
  "date": "July 15-20"
}
```

Then use:
```bash
.venv\Scripts\python.exe scripts/create_autofill.py "template_id" --data-file "data/sale.json"
```

---

## 3-Mode Workflow

### MODE 1: PLAN
1. Identify available brand templates
2. Get template dataset fields
3. Prepare autofill data

### MODE 2: CLARIFY
Ask user:
- Which template to use?
- What data to fill in?
- Title for the generated design?

### MODE 3: IMPLEMENT
```bash
# Create personalized design
.venv\Scripts\python.exe scripts/create_autofill.py "template_id" \
    --data '{"headline": "Welcome Back", "name": "John"}' \
    --title "Personalized Welcome"

# Output:
# Starting autofill job...
# Autofill job started: job_xxx
# Waiting for autofill to complete...
#
# Autofill Job Status: SUCCESS
# ==================================================
#   Design ID: DAFxxxxxxxxxx
#   Title: Personalized Welcome
#
#   Edit URL: https://www.canva.com/design/DAFxxxxxxxxxx/edit
```

---

## Use Cases

### Personalized Marketing
```bash
# Create personalized emails for different segments
.venv\Scripts\python.exe scripts/create_autofill.py "email_template" \
    --data '{"recipient": "VIP Customer", "offer": "Exclusive 30% off"}' \
    --title "VIP Email"
```

### Social Media Campaigns
```bash
# Generate multiple posts from template
for city in "New York" "Los Angeles" "Chicago"; do
    .venv\Scripts\python.exe scripts/create_autofill.py "local_post_template" \
        --data "{\"city\": \"$city\"}" \
        --title "Post - $city"
done
```

### Event Materials
```bash
# Create event flyer
.venv\Scripts\python.exe scripts/create_autofill.py "event_flyer" \
    --data-file "events/conference.json" \
    --title "Tech Conference 2024"
```

---

## Brand Guidelines Documentation

Store brand guidelines in `samples/brand-kits/`:

```
samples/brand-kits/
├── brand-config.json       # Colors, fonts, spacing
├── colors.json             # Detailed color palette
├── typography.json         # Font specifications
├── logos/                  # Logo files
│   ├── primary.png
│   ├── secondary.png
│   └── icon.png
└── guidelines.md           # Brand guidelines document
```

### Example brand-config.json
```json
{
  "brand_name": "Your Brand",
  "colors": {
    "primary": "#2E86AB",
    "secondary": "#F4D35E",
    "accent": "#EE6352",
    "text_primary": "#1A1A1A"
  },
  "fonts": {
    "heading": "Montserrat",
    "body": "Open Sans"
  }
}
```

---

## Feature Requirements

| Feature | Required Plan |
|---------|---------------|
| Brand Templates | Enterprise |
| Autofill | Enterprise |
| List Templates | Enterprise |
| Brand Kit (colors, fonts, logos) | Pro |

---

## Rate Limits

| Operation | Limit |
|-----------|-------|
| List templates | 100 requests/user |
| Get template | 100 requests/user |
| Create autofill | 20-30 requests/user |

---

## Error Handling

### Enterprise Required
```
Error: 403 Forbidden
Note: Brand templates require Canva Enterprise plan
```

### Template Not Found
```
Error: 404 - Template does not exist
```

### Invalid Data
```
Error: Missing required field 'headline'
```
**Solution**: Check template dataset for required fields

---

## Integration

Works with:
- **canva-export**: Export autofill-generated designs
- **canva-design**: Manage created designs
- **canva-folder-organizer**: Organize generated designs
