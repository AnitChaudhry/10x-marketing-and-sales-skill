---
name: local-pptx-editor
description: |
  Edit PowerPoint (PPTX) files locally without Canva API. Use this skill when user provides
  a PPTX file and wants to modify slides, update text, change images, or restructure content.
  Maintains original formatting, themes, animations, and layout. Does NOT require Canva.
  Output goes to output/ folder. Use for: "edit this presentation", "update slide 5", "change PPT text".
---

# Local PPTX Editor Skill

Edit and manipulate PowerPoint files locally without requiring Canva API.

---

## ⚠️ CRITICAL DESIGN PRESERVATION RULES (MANDATORY)

**These rules are NON-NEGOTIABLE. Violating them will break the presentation design.**

### 🚫 NEVER DO THESE THINGS:

1. **NEVER create new text boxes** - Only modify text in EXISTING placeholders
2. **NEVER add new shapes or elements** - Only modify EXISTING elements
3. **NEVER create blank slides** - ALWAYS duplicate an existing slide
4. **NEVER change font sizes** - Unless user EXPLICITLY requests it
5. **NEVER change font colors** - Unless user EXPLICITLY requests it
6. **NEVER change alignments** - Unless user EXPLICITLY requests it
7. **NEVER change positions** - Unless user EXPLICITLY requests it
8. **NEVER change backgrounds** - Unless user EXPLICITLY requests it
9. **NEVER change the theme** - Unless user EXPLICITLY requests it
10. **NEVER modify decorative elements** - Logos, lines, shapes must stay intact

### ✅ ALWAYS DO THESE THINGS:

1. **ALWAYS duplicate existing slides** to create new ones (preserves theme)
2. **ALWAYS replace text within existing placeholders** only
3. **ALWAYS preserve all formatting** when replacing text
4. **ALWAYS analyze slide structure FIRST** before any modification
5. **ALWAYS identify placeholders vs decorative elements** before editing

---

## CRITICAL: Never Modify Original Files

1. **ALWAYS** copy the original to `output/working/` first (scripts do this automatically)
2. **ALL** edits happen on the copy
3. **SAVE** results to `output/pptx/`
4. **ORIGINAL** file remains untouched

## When to Use This Skill

Use this skill when:
- User provides a PPTX file and wants modifications
- Need to update slide content while maintaining design
- Need to add/remove/reorder slides
- Need to modify speaker notes
- **User has NOT explicitly asked to use Canva**

## Available CLI Scripts

All scripts are in `scripts/local/` and must be run with the virtual environment:

```bash
# Windows
.venv\Scripts\python.exe scripts/local/<script_name>.py

# macOS/Linux
.venv/bin/python scripts/local/<script_name>.py
```

### Analysis Scripts (ALWAYS RUN FIRST)

#### pptx_analyze.py - Analyze presentation for safe editing
```bash
# Full analysis
.venv\Scripts\python.exe scripts/local/pptx_analyze.py "path/to/presentation.pptx"

# Analyze specific slide
.venv\Scripts\python.exe scripts/local/pptx_analyze.py "path/to/presentation.pptx" --slide 3

# JSON output
.venv\Scripts\python.exe scripts/local/pptx_analyze.py "path/to/presentation.pptx" --json
```

### Text Modification Scripts

#### pptx_replace_text.py - Find and replace text (preserves formatting)
```bash
# Replace text across all slides
.venv\Scripts\python.exe scripts/local/pptx_replace_text.py "presentation.pptx" \
    --find "Old Text" --replace "New Text"

# Replace on specific slide only
.venv\Scripts\python.exe scripts/local/pptx_replace_text.py "presentation.pptx" \
    --find "Q3" --replace "Q4" --slide 5

# Dry run (preview changes)
.venv\Scripts\python.exe scripts/local/pptx_replace_text.py "presentation.pptx" \
    --find "2023" --replace "2024" --dry-run
```

#### pptx_update_content.py - Update slide title/content
```bash
# Update slide title
.venv\Scripts\python.exe scripts/local/pptx_update_content.py "presentation.pptx" \
    --slide 3 --title "New Title Here"

# Update slide content
.venv\Scripts\python.exe scripts/local/pptx_update_content.py "presentation.pptx" \
    --slide 3 --content "New content paragraph"

# Update with bullet points
.venv\Scripts\python.exe scripts/local/pptx_update_content.py "presentation.pptx" \
    --slide 3 --bullets "Point 1" "Point 2" "Point 3"

# Update both title and content
.venv\Scripts\python.exe scripts/local/pptx_update_content.py "presentation.pptx" \
    --slide 3 --title "New Title" --content "New content"
```

### Slide Structure Scripts

#### pptx_duplicate_slide.py - Duplicate a slide (THE CORRECT WAY to add slides)
```bash
# Duplicate slide 2
.venv\Scripts\python.exe scripts/local/pptx_duplicate_slide.py "presentation.pptx" \
    --source 2

# Duplicate and insert at specific position
.venv\Scripts\python.exe scripts/local/pptx_duplicate_slide.py "presentation.pptx" \
    --source 2 --position 5

# Duplicate with new content
.venv\Scripts\python.exe scripts/local/pptx_duplicate_slide.py "presentation.pptx" \
    --source 2 --title "New Slide Title" --content "New content here"
```

#### pptx_add_slides_from_template.py - Add multiple slides from template
```bash
# Add slides from JSON file
.venv\Scripts\python.exe scripts/local/pptx_add_slides_from_template.py "presentation.pptx" \
    --template 2 --content "slides_content.json"

# Add slides from inline JSON
.venv\Scripts\python.exe scripts/local/pptx_add_slides_from_template.py "presentation.pptx" \
    --template 2 --content '[{"title":"Slide 1","content":"Content"},{"title":"Slide 2","content_items":["A","B"]}]'
```

#### pptx_delete_slide.py - Delete slides
```bash
# Delete slide 5
.venv\Scripts\python.exe scripts/local/pptx_delete_slide.py "presentation.pptx" \
    --slides 5 --confirm

# Delete multiple slides
.venv\Scripts\python.exe scripts/local/pptx_delete_slide.py "presentation.pptx" \
    --slides 3 5 7 --confirm
```

#### pptx_reorder_slides.py - Reorder slides
```bash
# Move slide 3 to position 1
.venv\Scripts\python.exe scripts/local/pptx_reorder_slides.py "presentation.pptx" \
    --order 3 1 2 4 5
```

#### pptx_batch_update.py - Batch update multiple slides
```bash
# From JSON file
.venv\Scripts\python.exe scripts/local/pptx_batch_update.py "presentation.pptx" \
    --updates "updates.json"
```

Updates JSON format:
```json
[
    {"slide_num": 1, "title": "New Title 1"},
    {"slide_num": 2, "content": "New content"},
    {"slide_num": 3, "content_items": ["Bullet 1", "Bullet 2"]},
    {"slide_num": 4, "replacements": {"old": "new", "2023": "2024"}}
]
```

### Utility Scripts

#### safe_copy.py - Create safe working copy
```bash
.venv\Scripts\python.exe scripts/local/safe_copy.py --source "input/presentation.pptx"
```

---

## 3-Mode Workflow

### MODE 1: PLAN

**MANDATORY: Run analysis FIRST**

```bash
.venv\Scripts\python.exe scripts/local/pptx_analyze.py "presentation.pptx"
```

This shows:
- All slides with layout types
- Editable elements (titles, content)
- Decorative elements (DO NOT TOUCH)
- Warnings about what to avoid

### MODE 2: CLARIFY

Ask user to confirm:
- Which slides to modify
- Exact text replacements
- Whether content length is acceptable
- Any specific formatting needs (rarely - should preserve existing)

### MODE 3: IMPLEMENT

Run the appropriate script(s):
1. For text changes: `pptx_replace_text.py` or `pptx_update_content.py`
2. For new slides: `pptx_duplicate_slide.py` or `pptx_add_slides_from_template.py`
3. For deletions: `pptx_delete_slide.py`
4. For reordering: `pptx_reorder_slides.py`

All scripts automatically:
- Create safe copies
- Preserve all formatting
- Save to `output/pptx/`

---

## Example Workflows

### Example 1: Update text on a slide
```bash
# 1. Analyze
.venv\Scripts\python.exe scripts/local/pptx_analyze.py "report.pptx" --slide 3

# 2. Update title
.venv\Scripts\python.exe scripts/local/pptx_update_content.py "report.pptx" \
    --slide 3 --title "Q4 2024 Results"
```

### Example 2: Replace text across presentation
```bash
# 1. Dry run to see what will change
.venv\Scripts\python.exe scripts/local/pptx_replace_text.py "report.pptx" \
    --find "2023" --replace "2024" --dry-run

# 2. Apply changes
.venv\Scripts\python.exe scripts/local/pptx_replace_text.py "report.pptx" \
    --find "2023" --replace "2024"
```

### Example 3: Add new slides from template
```bash
# 1. Analyze to find good template slide
.venv\Scripts\python.exe scripts/local/pptx_analyze.py "report.pptx"

# 2. Add new slides using slide 2 as template
.venv\Scripts\python.exe scripts/local/pptx_add_slides_from_template.py "report.pptx" \
    --template 2 \
    --content '[{"title":"New Section","content":"Introduction to new topic"}]'
```

---

## Output Locations

- `output/pptx/` - Modified presentations
- `output/working/` - Temporary working copies (auto-cleaned)

---

## Supported File Types

- `.pptx` - PowerPoint 2007+ (primary format)
- `.ppt` - Legacy PowerPoint (limited support)

---

## Todo List Tracking (REQUIRED)

**ALWAYS use TodoWrite** to track progress:

```json
[
  {"content": "Analyze presentation structure", "status": "in_progress", "activeForm": "Analyzing slides"},
  {"content": "Identify editable elements", "status": "pending", "activeForm": "Identifying elements"},
  {"content": "Apply text modifications", "status": "pending", "activeForm": "Applying changes"},
  {"content": "Verify output file", "status": "pending", "activeForm": "Verifying output"}
]
```
