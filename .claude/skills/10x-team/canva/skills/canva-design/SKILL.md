---
name: canva-design
description: |
  Comprehensive design operations skill for Canva. Handles all design CRUD operations:
  create, list, search, get details, get pages, check export formats. Use this skill
  for any design-related operations that don't involve editing content.
  For editing images use canva-image-editor, for presentations use canva-presentation.
---

# Canva Design Operations

Complete design management: create, list, search, and inspect designs.

---

## Capabilities

1. **Create Designs** - New designs with presets or custom dimensions
2. **List Designs** - Browse all designs with filtering
3. **Search Designs** - Find designs by query
4. **Get Design Details** - Metadata, URLs, thumbnails
5. **Get Design Pages** - Page thumbnails and information
6. **Check Export Formats** - Available export options

---

## Available Scripts

### Create Design
```bash
# By preset type
.venv\Scripts\python.exe scripts/create_design.py --type presentation --title "My Presentation"
.venv\Scripts\python.exe scripts/create_design.py --type instagram_post --title "My Post"
.venv\Scripts\python.exe scripts/create_design.py --type doc --title "My Document"

# By custom dimensions
.venv\Scripts\python.exe scripts/create_design.py --width 1080 --height 1350 --title "Instagram Portrait"
.venv\Scripts\python.exe scripts/create_design.py --width 1920 --height 1080 --title "HD Video"

# Smart create (by type name)
.venv\Scripts\python.exe scripts/smart_create_design.py instagram_post --title "My Post"
.venv\Scripts\python.exe scripts/smart_create_design.py linkedin_banner --title "Profile Banner"
.venv\Scripts\python.exe scripts/smart_create_design.py youtube_thumbnail --title "Video Thumbnail"

# List all available design types
.venv\Scripts\python.exe scripts/smart_create_design.py --list
```

### List Designs
```bash
# List all designs
.venv\Scripts\python.exe scripts/list_designs.py

# With limit
.venv\Scripts\python.exe scripts/list_designs.py --limit 20

# Filter by ownership
.venv\Scripts\python.exe scripts/list_designs.py --ownership owned
.venv\Scripts\python.exe scripts/list_designs.py --ownership shared

# Sort options
.venv\Scripts\python.exe scripts/list_designs.py --sort modified_descending
.venv\Scripts\python.exe scripts/list_designs.py --sort title_ascending

# JSON output
.venv\Scripts\python.exe scripts/list_designs.py --json
```

### Search Designs
```bash
# Search by query
.venv\Scripts\python.exe scripts/search_designs.py "marketing"
.venv\Scripts\python.exe scripts/search_designs.py "Q4 report"

# With filters
.venv\Scripts\python.exe scripts/search_designs.py "presentation" --ownership owned --limit 10

# Get all results with pagination
.venv\Scripts\python.exe scripts/search_designs.py "logo" --all

# JSON output
.venv\Scripts\python.exe scripts/search_designs.py "banner" --json
```

### Get Design Details
```bash
# Get design metadata
.venv\Scripts\python.exe scripts/get_design_details.py "DAFxxxxxxxxxx"

# JSON output
.venv\Scripts\python.exe scripts/get_design_details.py "DAFxxxxxxxxxx" --json
```

### Get Design Pages
```bash
# Get page thumbnails
.venv\Scripts\python.exe scripts/get_design_pages.py "DAFxxxxxxxxxx"

# With pagination
.venv\Scripts\python.exe scripts/get_design_pages.py "DAFxxxxxxxxxx" --offset 1 --limit 50

# Get all pages
.venv\Scripts\python.exe scripts/get_design_pages.py "DAFxxxxxxxxxx" --all

# JSON output
.venv\Scripts\python.exe scripts/get_design_pages.py "DAFxxxxxxxxxx" --json
```

### Get Export Formats
```bash
# Check available export formats for a design
.venv\Scripts\python.exe scripts/get_export_formats.py "DAFxxxxxxxxxx"
```

---

## Design Types (Presets)

### Canva Built-in Presets
| Preset | Description |
|--------|-------------|
| `presentation` | 16:9 presentation |
| `doc` | Canva Doc |
| `whiteboard` | Collaborative whiteboard |
| `instagram_post` | 1080x1080 square |
| `instagram_story` | 1080x1920 story |
| `facebook_post` | Facebook feed post |
| `poster` | Large format poster |
| `flyer` | Marketing flyer |
| `a4_document` | A4 size document |
| `us_letter_document` | US Letter document |

### Smart Create Types (50+)
Use `smart_create_design.py --list` to see all available types including:
- All social media formats (Instagram, Facebook, LinkedIn, Twitter, YouTube, Pinterest, TikTok)
- Business documents (presentations, reports, cards)
- Marketing materials (posters, flyers, banners)
- Ad formats (leaderboard, rectangle, skyscraper)

---

## 3-Mode Workflow

### MODE 1: PLAN
1. Understand what type of design is needed
2. Determine correct dimensions
3. Plan title and purpose

### MODE 2: CLARIFY
Ask user to confirm:
- Design type/dimensions
- Title
- Purpose (affects which skill to use next)

### MODE 3: IMPLEMENT
```bash
# Example: Create Instagram post
.venv\Scripts\python.exe scripts/smart_create_design.py instagram_post --title "Summer Sale Announcement"

# Output:
# Design Created Successfully!
# ==================================================
#   Type:        instagram_post
#   Dimensions:  1080 x 1080 px
#   Platform:    instagram
#   ID:          DAFxxxxxxxxxx
#   Title:       Summer Sale Announcement
#
#   Edit URL: https://www.canva.com/design/DAFxxxxxxxxxx/edit
```

---

## Design Information Returned

### Design Metadata
```json
{
  "id": "DAFxxxxxxxxxx",
  "title": "My Design",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T12:45:00Z",
  "urls": {
    "edit_url": "https://www.canva.com/design/.../edit",
    "view_url": "https://www.canva.com/design/.../view"
  }
}
```

### Page Information
```json
{
  "pages": [
    {
      "id": "page_id",
      "width": 1080,
      "height": 1080,
      "thumbnail": {
        "url": "https://..."
      }
    }
  ]
}
```

---

## Next Steps After Creating

1. **Edit in Canva**: Open the edit URL to add content
2. **Use Other Skills**:
   - `canva-image-editor` for image designs
   - `canva-presentation` for slide decks
   - `canva-video` for video content
3. **Export**: Use `canva-export` skill when done

---

## Rate Limits

| Operation | Limit |
|-----------|-------|
| List designs | 100 requests/user |
| Create design | 20 requests/user |
| Get design | 100 requests/user |

---

## Error Handling

### Design Not Found
```
Error: 404 Not Found - Design does not exist
```

### Invalid Dimensions
```
Error: Dimensions must be positive integers
```

### Rate Limited
```
Error: 429 Too Many Requests
```
Wait and retry.
