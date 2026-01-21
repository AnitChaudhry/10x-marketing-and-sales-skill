---
name: canva-image-editor
description: |
  Edit and modify image-based designs in Canva (social media posts, posters, flyers, etc.).
  Use this skill when user wants to modify existing image designs or create new ones.
  Follows 3-mode workflow: PLAN changes, CLARIFY with user, then IMPLEMENT.
  For presentations use canva-presentation skill. For videos use canva-video skill.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# Canva Image Editor Skill

Edit and modify image-based designs in Canva including social media posts, posters, flyers, logos, and other static graphics.

---

## ⚠️ CRITICAL DESIGN PRESERVATION RULES (MANDATORY)

**These rules are NON-NEGOTIABLE. Violating them will break the design.**

### 🚫 NEVER DO THESE THINGS:

1. **NEVER create new text elements** - Only modify text in EXISTING elements
2. **NEVER add new shapes or elements** - Only modify EXISTING elements
3. **NEVER change font sizes** - Unless user EXPLICITLY requests it
4. **NEVER change font styles/colors** - Unless user EXPLICITLY requests it
5. **NEVER change element positions** - Unless user EXPLICITLY requests it
6. **NEVER change element sizes** - Unless user EXPLICITLY requests it
7. **NEVER change backgrounds** - Unless user EXPLICITLY requests it
8. **NEVER modify decorative elements** - Logos, frames, borders must stay intact
9. **NEVER add new layers** - Only modify existing layers
10. **NEVER change the template structure** - Unless user EXPLICITLY requests it

### ✅ ALWAYS DO THESE THINGS:

1. **ALWAYS replace text within existing elements** only
2. **ALWAYS replace images in existing image placeholders** only
3. **ALWAYS preserve all formatting** (font, size, color, position, alignment)
4. **ALWAYS analyze design structure first** before any modification
5. **ALWAYS identify content elements vs decorative elements** before editing
6. **ALWAYS duplicate the design first** before making changes

### Updating Content - THE CORRECT WAY:

```python
# WRONG - Creates new text element
create_text.py --design "ID" --text "New text"

# CORRECT - Updates existing text element
update_text.py --design "ID" --element "EXISTING_ELEMENT_ID" --text "New text"
```

### Replacing Images - THE CORRECT WAY:

```python
# WRONG - Adds new image layer
add_image.py --design "ID" --image "new_image.jpg"

# CORRECT - Replaces image in existing placeholder
replace_image.py --design "ID" --element "EXISTING_IMAGE_ID" --new-image "new_image.jpg"
```

---

## Scope of This Skill

**This skill handles:**
- Instagram Posts/Stories
- Facebook Posts/Covers
- Twitter/X Posts
- LinkedIn Posts/Banners
- Posters & Flyers
- Logos
- Business Cards
- Invitations
- Infographics
- Thumbnails
- Any static image design

**NOT handled by this skill:**
- Presentations/Slideshows → Use `canva-presentation`
- Videos/Animations → Use `canva-video`
- Document editing → Use `canva-document`
- Bulk exports → Use `canva-export`

## 3-Mode Workflow

### MODE 1: PLAN

Before any edits, analyze and document:

1. **Identify the Target Design**
   ```python
   # Use canva-explorer first to find the design
   python skills/canva-explorer/scripts/get_design.py --id "DESIGN_ID" --include-pages
   ```

2. **Analyze Current State**
   - Design dimensions
   - Number of elements (text, images, shapes)
   - Current colors and fonts
   - Background type

3. **Document Proposed Changes**
   ```
   ## Edit Plan for "[Design Name]"

   ### Current State
   - Type: Instagram Post (1080x1080)
   - Elements: 3 text layers, 2 images, 1 background
   - Primary colors: #FF5733, #FFFFFF

   ### Proposed Changes
   1. Update headline text from "X" to "Y"
   2. Replace main image with new uploaded asset
   3. Change background color to #2E86AB

   ### Elements NOT Being Changed
   - Logo placement (top-right)
   - Footer text
   - Secondary image

   ### Risks
   - Text may overflow if new headline is longer
   - New image aspect ratio may need adjustment
   ```

### MODE 2: CLARIFY

Ask user to confirm:

1. **Verify Changes**
   - "The headline will change from 'Summer Sale' to 'Winter Sale'. Correct?"
   - "Should I resize the new image to fit, or crop it?"

2. **Offer Options**
   - "Should I work on the original or create a copy first?"
   - "Do you want to preview the changes before finalizing?"

3. **Handle Ambiguity**
   - "I found 3 text elements. Which one should I modify?"
   - "The new color doesn't meet contrast guidelines. Proceed anyway?"

### MODE 3: IMPLEMENT

Execute approved changes:

```python
# Example: Update text element
python skills/canva-image-editor/scripts/update_text.py \
  --design "DESIGN_ID" \
  --element "ELEMENT_ID" \
  --text "New headline text"

# Example: Replace image
python skills/canva-image-editor/scripts/replace_image.py \
  --design "DESIGN_ID" \
  --element "ELEMENT_ID" \
  --new-image "path/to/image.jpg"

# Example: Update colors
python skills/canva-image-editor/scripts/update_colors.py \
  --design "DESIGN_ID" \
  --primary "#2E86AB" \
  --secondary "#F4D35E"
```

## Available Scripts

### Analysis Scripts
- `analyze_design.py` - Deep analysis of design elements
- `extract_colors.py` - Get color palette from design
- `extract_text.py` - Get all text content
- `check_dimensions.py` - Verify size and aspect ratio

### Edit Scripts
- `update_text.py` - Modify text content
- `replace_image.py` - Swap images in design
- `update_colors.py` - Change color scheme
- `resize_design.py` - Change dimensions
- `duplicate_design.py` - Create a copy before editing

### Creation Scripts
- `create_from_template.py` - New design from Canva template
- `create_blank.py` - New blank design with dimensions

## Design Types and Dimensions

| Type | Dimensions | Aspect Ratio |
|------|------------|--------------|
| Instagram Post | 1080x1080 | 1:1 |
| Instagram Story | 1080x1920 | 9:16 |
| Facebook Post | 1200x630 | 1.91:1 |
| Facebook Cover | 820x312 | 2.63:1 |
| Twitter Post | 1600x900 | 16:9 |
| LinkedIn Post | 1200x1200 | 1:1 |
| LinkedIn Banner | 1584x396 | 4:1 |
| Pinterest Pin | 1000x1500 | 2:3 |
| YouTube Thumbnail | 1280x720 | 16:9 |
| Poster | 18x24 inches | 3:4 |
| A4 Document | 210x297mm | 1:1.41 |

## Element Types

When working with design elements:

- **Text Elements**: Headlines, body text, captions
- **Image Elements**: Photos, graphics, icons
- **Shape Elements**: Rectangles, circles, lines
- **Frame Elements**: Image frames, masks
- **Background**: Solid color, gradient, image

## Safety Guidelines

1. **Always duplicate first** for major changes
2. **Check text overflow** when changing content
3. **Verify image quality** after replacement
4. **Test color contrast** for accessibility
5. **Log all changes** to output folder

## Example Interactions

### "Change the headline in my Instagram post"
```
[PLAN]
- Found design "Summer Promo" (1080x1080)
- Contains headline: "SUMMER SALE 50% OFF"
- Proposed: Change to user's new text

[CLARIFY]
- What should the new headline say?
- Keep same font and size?

[IMPLEMENT]
- Update text element with new content
- Verify no overflow
- Confirm change complete
```

### "Update the colors to match my brand"
```
[PLAN]
- Analyze current colors: #FF5733, #FFFFFF, #333333
- User's brand colors: #2E86AB, #F4D35E, #1A1A1A
- Map old → new colors

[CLARIFY]
- Confirm color mapping is correct
- Should background also change?
- Keep or update any accent colors?

[IMPLEMENT]
- Apply color changes to all elements
- Verify readability
- Export preview
```

## Output Files

Changes are logged to:
- `output/edits/` - Before/after comparisons
- `output/logs/edit_history.json` - All modifications
- `output/previews/` - Preview exports
