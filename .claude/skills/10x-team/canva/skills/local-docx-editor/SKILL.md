---
name: local-docx-editor
description: |
  Edit Word documents (DOCX) locally without Canva API. Use this skill when user provides
  a DOCX file and wants to modify content, update formatting, or restructure document.
  Maintains original styles, fonts, spacing, and layout. Does NOT require Canva.
  Output goes to output/ folder. Use for: "edit this document", "update section 3", "change Word file".
---

# Local DOCX Editor Skill

Edit and manipulate Word documents locally without requiring Canva API.

---

## ⚠️ CRITICAL DESIGN PRESERVATION RULES (MANDATORY)

**These rules are NON-NEGOTIABLE. Violating them will break the document design.**

### 🚫 NEVER DO THESE THINGS:

1. **NEVER create new text boxes** - Word documents rarely use text boxes; only modify existing ones
2. **NEVER add new shapes or elements** - Only modify EXISTING elements
3. **NEVER add new sections from scratch** - COPY existing section structure
4. **NEVER change font sizes** - Unless user EXPLICITLY requests it
5. **NEVER change font styles/colors** - Unless user EXPLICITLY requests it
6. **NEVER change alignments** - Unless user EXPLICITLY requests it
7. **NEVER change margins or spacing** - Unless user EXPLICITLY requests it
8. **NEVER change headers/footers** - Unless user EXPLICITLY requests it
9. **NEVER modify templates/styles** - Unless user EXPLICITLY requests it
10. **NEVER add/remove table columns** - Unless user EXPLICITLY requests it

### ✅ ALWAYS DO THESE THINGS:

1. **ALWAYS replace text within existing paragraphs** only
2. **ALWAYS preserve all formatting** (font, size, color, style, alignment)
3. **ALWAYS copy existing paragraph/section structure** for new content
4. **ALWAYS analyze document structure first** before any modification
5. **ALWAYS identify body text vs headers/footers/decorative elements**
6. **ALWAYS maintain existing styles** when replacing content

### How to Add New Content (CORRECT WAY):

```python
# WRONG - Adds completely new paragraph with default formatting
doc.add_paragraph("New text")

# CORRECT - Find similar paragraph, copy its style, then modify
existing_para = doc.paragraphs[5]  # Find one with similar purpose
# Use its style for new content
```

### How to Update Content (CORRECT WAY):

```python
# WRONG - Might change formatting
paragraph.text = "New text"

# CORRECT - Replace text while preserving runs and formatting
for run in paragraph.runs:
    if "old text" in run.text:
        run.text = run.text.replace("old text", "new text")
```

---

## CRITICAL: Never Modify Original Files

1. **ALWAYS** copy the original to `output/working/` first
2. **ALL** edits happen on the copy
3. **SAVE** results to `output/docx/`
4. **ORIGINAL** file remains untouched

## When to Use This Skill

Use this skill when:
- User provides a DOCX/DOC file and wants modifications
- Need to update text while maintaining formatting
- Need to update tables
- Need to update content within existing structure
- **User has NOT explicitly asked to use Canva**

## Capabilities

### Read Operations (SAFE - No Risk)
- Extract all text content
- Get document structure (headings, paragraphs)
- Extract images and tables
- Get styles and formatting info
- Identify editable vs structural elements

### Write Operations (FOLLOW PRESERVATION RULES)
- **Replace text** in existing paragraphs (NOT add new paragraphs)
- **Update table cells** (NOT add/remove columns)
- **Replace images** in existing image placeholders
- **Bulk text replacement** across document

### ❌ Operations NOT Supported (To Preserve Design)
- Adding new text boxes
- Adding new shapes
- Changing fonts/colors/sizes (unless explicitly requested)
- Modifying headers/footers (unless explicitly requested)
- Changing margins or page layout
- Adding/removing table columns

### Conversion
- DOCX to PDF
- DOCX to plain text

## Running Python Scripts (Virtual Environment)

**IMPORTANT**: Always use the virtual environment Python:

```bash
# Windows
.venv\Scripts\python.exe scripts/local/script_name.py

# macOS/Linux
.venv/bin/python scripts/local/script_name.py
```

## Workflow

### Step 1: Create Safe Copy
```bash
.venv\Scripts\python.exe scripts/local/safe_copy.py --source "input/document.docx"
```

### Step 2: Analyze
```bash
.venv\Scripts\python.exe scripts/local/docx_utils.py "output/working/document_copy.docx"
```

### Step 3: Make Modifications

Use docx_utils.py for:
- Find and replace text
- Update specific paragraphs
- Modify table cells

### Step 4: Save Result
Save to `output/docx/document_modified.docx`

## 3-Mode Workflow

### MODE 1: PLAN
- Analyze document structure
- List sections and word counts
- Document proposed changes

### MODE 2: CLARIFY
- Confirm content to modify
- Verify formatting requirements
- Check word count targets

### MODE 3: IMPLEMENT
- Create working copy
- Apply modifications
- Save to output folder

## Maintaining Format Integrity

### Preservation Rules
1. **Styles** - Preserve all named styles
2. **Spacing** - Line and paragraph spacing
3. **Lists** - Bullet and numbering styles
4. **Tables** - Column widths and formatting

## Research Capabilities

This skill can:
- Search for Word document best practices
- Look up python-docx documentation
- Research document formatting standards
- Find solutions to specific challenges

## Available Scripts

- `docx_utils.py` - Core DOCX analysis and manipulation
- `safe_copy.py` - Create working copies safely

## Todo List Tracking (REQUIRED)

**ALWAYS use TodoWrite** to track progress:

```json
[
  {"content": "Create safe working copy", "status": "in_progress", "activeForm": "Creating safe copy"},
  {"content": "Analyze document structure", "status": "pending", "activeForm": "Analyzing document"},
  {"content": "Apply modifications", "status": "pending", "activeForm": "Applying changes"},
  {"content": "Save to output/docx/", "status": "pending", "activeForm": "Saving result"}
]
```

## Output Location

- `output/docx/` - Modified documents
- `output/working/` - Working copies
