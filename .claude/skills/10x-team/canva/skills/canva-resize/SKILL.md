---
name: canva-resize
description: |
  Resize designs to different dimensions. Use this skill when user wants to adapt
  a design for different platforms or sizes. Creates a new resized copy without
  modifying the original. Premium feature - requires Canva Pro or higher.
---

# Canva Design Resize

Create resized copies of designs for different platforms and dimensions.

---

## Capabilities

1. **Resize Designs** - Create resized copies with new dimensions
2. **Cross-Platform Adaptation** - Adapt designs for different social platforms
3. **Batch Resizing** - Resize one design to multiple formats

---

## Available Scripts

### Resize Design
```bash
# Basic resize
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" --width 1080 --height 1920

# With new title
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" --width 1200 --height 628 --title "LinkedIn Version"

# Custom timeout
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" --width 1080 --height 1350 --timeout 600

# JSON output
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" --width 1080 --height 1080 --json
```

---

## Common Resize Scenarios

### Instagram Post to Story
```bash
# Original: 1080x1080 (post)
# Target: 1080x1920 (story)
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" --width 1080 --height 1920 --title "Story Version"
```

### Facebook to LinkedIn
```bash
# Original: 1080x1080 (Facebook)
# Target: 1200x628 (LinkedIn)
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" --width 1200 --height 628 --title "LinkedIn Version"
```

### Social to YouTube Thumbnail
```bash
# Original: any
# Target: 1280x720 (YouTube)
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" --width 1280 --height 720 --title "YouTube Thumbnail"
```

### Presentation to Document
```bash
# Original: 1920x1080 (16:9)
# Target: 1920x1440 (4:3)
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" --width 1920 --height 1440 --title "4:3 Version"
```

---

## Platform Dimension Reference

### Social Media
| Platform | Type | Dimensions |
|----------|------|------------|
| Instagram | Post Square | 1080 x 1080 |
| Instagram | Post Portrait | 1080 x 1350 |
| Instagram | Story/Reel | 1080 x 1920 |
| Facebook | Post | 1080 x 1080 |
| Facebook | Cover | 820 x 312 |
| LinkedIn | Post | 1200 x 628 |
| LinkedIn | Banner | 1584 x 396 |
| Twitter | Post | 1200 x 675 |
| Twitter | Header | 1500 x 500 |
| YouTube | Thumbnail | 1280 x 720 |
| Pinterest | Pin | 1000 x 1500 |

### Business
| Type | Dimensions |
|------|------------|
| Presentation 16:9 | 1920 x 1080 |
| Presentation 4:3 | 1024 x 768 |
| A4 Document | 595 x 842 |
| US Letter | 612 x 792 |
| Business Card | 1050 x 600 |

---

## Constraints

### Maximum Pixels
- **Total limit**: 25,000,000 pixels (width × height)
- Example: 5000 × 5000 = 25M (maximum)
- Example: 6000 × 5000 = 30M (exceeds limit)

### Feature Availability
- **Requires**: Canva Pro, Teams, or Enterprise
- **Free accounts**: Will receive 403 error

---

## 3-Mode Workflow

### MODE 1: PLAN
1. Get current design dimensions
2. Determine target platform/size
3. Check pixel limit (25M max)

### MODE 2: CLARIFY
Ask user to confirm:
- Target dimensions
- New title for resized version
- Which platforms to target

### MODE 3: IMPLEMENT
```bash
# Execute resize
.venv\Scripts\python.exe scripts/resize_design.py "DAFxxxxxxxxxx" \
    --width 1080 --height 1920 \
    --title "Instagram Story Version"

# Output:
# Starting resize job...
# Resize job started: job_xxx
# Waiting for resize to complete...
#
# Resize Job Status: SUCCESS
# ==================================================
#   New Design ID: DAFyyyyyyyyyy
#   Title: Instagram Story Version
#   Dimensions: 1080 x 1920
#
#   Edit URL: https://www.canva.com/design/DAFyyyyyyyyyy/edit
```

---

## Batch Resizing Workflow

To resize one design to multiple formats:

```bash
# 1. Instagram Post (Square)
.venv\Scripts\python.exe scripts/resize_design.py "DAForiginal" --width 1080 --height 1080 --title "Instagram Post"

# 2. Instagram Story
.venv\Scripts\python.exe scripts/resize_design.py "DAForiginal" --width 1080 --height 1920 --title "Instagram Story"

# 3. Facebook Post
.venv\Scripts\python.exe scripts/resize_design.py "DAForiginal" --width 1200 --height 630 --title "Facebook Post"

# 4. LinkedIn Post
.venv\Scripts\python.exe scripts/resize_design.py "DAForiginal" --width 1200 --height 628 --title "LinkedIn Post"

# 5. Twitter Post
.venv\Scripts\python.exe scripts/resize_design.py "DAForiginal" --width 1200 --height 675 --title "Twitter Post"
```

---

## Error Handling

### Premium Required
```
Error: 403 Forbidden
Note: Resize requires Canva Pro or higher
```
**Solution**: Upgrade Canva plan or manually create new designs

### Pixel Limit Exceeded
```
Error: Total pixels (30,000,000) exceeds maximum (25,000,000)
```
**Solution**: Use smaller dimensions

### Design Not Found
```
Error: 404 Not Found
```
**Solution**: Verify design ID exists

---

## Tips

1. **Content Reflow**: Canva intelligently repositions elements when resizing
2. **Review After Resize**: Always check the resized design - some manual adjustments may be needed
3. **Keep Originals**: Resize creates a copy, original is preserved
4. **Title Convention**: Use descriptive titles like "Campaign - Instagram" for easy identification
