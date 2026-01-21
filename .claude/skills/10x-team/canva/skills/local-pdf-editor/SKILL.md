---
name: local-pdf-editor
description: |
  Edit PDF files locally without Canva API. Use this skill when user provides a PDF file
  and wants to modify content, extract text, merge/split pages, or update specific sections.
  Maintains original formatting, spacing, fonts, and layout. Does NOT require Canva.
  Output goes to the output/ folder. Use for: "edit this PDF", "change page 15", "update text in PDF".
---

# Local PDF Editor Skill

Edit and manipulate PDF files locally without requiring Canva API.

---

## ⚠️ CRITICAL DESIGN PRESERVATION RULES (MANDATORY)

**These rules are NON-NEGOTIABLE. Violating them will break the PDF layout.**

### 🚫 NEVER DO THESE THINGS:

1. **NEVER add new text boxes** - Only modify text in EXISTING locations
2. **NEVER add new elements** - Only modify EXISTING elements
3. **NEVER change font sizes** - Unless user EXPLICITLY requests it
4. **NEVER change font styles** - Unless user EXPLICITLY requests it
5. **NEVER change text positions** - Unless user EXPLICITLY requests it
6. **NEVER change margins/spacing** - Unless user EXPLICITLY requests it
7. **NEVER change page layouts** - Unless user EXPLICITLY requests it
8. **NEVER modify headers/footers** - Unless user EXPLICITLY requests it
9. **NEVER add/remove pages** - Unless user EXPLICITLY requests it
10. **NEVER modify form fields structure** - Only update values

### ✅ ALWAYS DO THESE THINGS:

1. **ALWAYS replace text in existing locations** only
2. **ALWAYS preserve all formatting** (font, size, color, position)
3. **ALWAYS analyze PDF structure first** before any modification
4. **ALWAYS identify editable text vs fixed graphics**
5. **ALWAYS convert to DOCX for complex edits, then back to PDF**
6. **ALWAYS verify layout is preserved** after modifications

### PDF Editing Limitations:

PDFs are designed for viewing, not editing. Direct text editing is LIMITED:
- Can replace text in form fields easily
- Can replace text in simple text blocks
- Complex layouts may require DOCX conversion approach

### How to Update Content (CORRECT WAY):

```
1. Convert PDF to DOCX (preserves layout better)
2. Edit text in DOCX (using docx preservation rules)
3. Convert back to PDF
4. Verify layout is preserved
```

---

## CRITICAL: Never Modify Original Files

1. **ALWAYS** copy the original to `output/working/` first
2. **ALL** edits happen on the copy
3. **SAVE** results to `output/pdf/`
4. **ORIGINAL** file remains untouched

## When to Use This Skill

Use this skill when:
- User provides a PDF file and wants modifications
- Need to extract text from PDF
- Need to merge or split PDF pages (with explicit permission)
- Need to update specific content while maintaining layout
- **User has NOT explicitly asked to use Canva**

## Capabilities

### Read Operations (SAFE - No Risk)
- Extract text from PDF (all pages or specific)
- Extract images from PDF
- Get PDF metadata (pages, size, fonts)
- Analyze PDF structure
- Identify editable vs fixed elements

### Write Operations (FOLLOW PRESERVATION RULES)
- **Replace text** in existing locations (NOT add new text)
- **Update form field values** (NOT add new fields)
- Merge multiple PDFs (with explicit permission)
- Split PDF into separate files (with explicit permission)

### ❌ Operations NOT Supported (To Preserve Design)
- Adding new text boxes
- Adding new elements
- Changing fonts/colors/sizes (unless explicitly requested)
- Changing layout or margins
- Adding/removing pages (unless explicitly requested)

### Conversion
- PDF to DOCX (for easier editing, recommended approach)
- PDF to images (PNG/JPG)
- PDF to text
- DOCX back to PDF

## Running Python Scripts (Virtual Environment)

**IMPORTANT**: Always use the virtual environment Python:

```bash
# Windows
.venv\Scripts\python.exe scripts/local/script_name.py

# macOS/Linux
.venv/bin/python scripts/local/script_name.py
```

## Workflow for Content Modification

### Step 1: Create Safe Copy
```bash
.venv\Scripts\python.exe scripts/local/safe_copy.py --source "input/document.pdf"
```

### Step 2: Analyze the PDF
```bash
.venv\Scripts\python.exe scripts/local/pdf_utils.py "output/working/document_copy.pdf"
```

### Step 3: For Text Modifications
```bash
# Convert to DOCX for easier editing
.venv\Scripts\python.exe scripts/local/pdf_to_docx.py --file "output/working/document_copy.pdf"

# Make modifications to the DOCX

# Convert back to PDF
.venv\Scripts\python.exe scripts/local/docx_to_pdf.py --file "output/working/document_copy.docx" --output "output/pdf/document_modified.pdf"
```

## 3-Mode Workflow

### MODE 1: PLAN
- Analyze the PDF structure
- Document current state (pages, content)
- List proposed changes
- Identify what will NOT change

### MODE 2: CLARIFY
- Confirm which content to modify
- Ask about formatting preferences
- Verify output requirements

### MODE 3: IMPLEMENT
- Create working copy
- Make modifications
- Save to output folder
- Report results

## Research Capabilities

This skill can:
- Search the web for PDF manipulation techniques
- Look up PDF format specifications
- Research best practices for maintaining formatting
- Find solutions to specific PDF challenges

## Available Scripts

- `pdf_utils.py` - Core PDF analysis and manipulation
- `safe_copy.py` - Create working copies safely

## Todo List Tracking (REQUIRED)

**ALWAYS use TodoWrite** to track progress:

```json
[
  {"content": "Create safe working copy", "status": "in_progress", "activeForm": "Creating safe copy"},
  {"content": "Analyze PDF structure", "status": "pending", "activeForm": "Analyzing PDF"},
  {"content": "Apply modifications", "status": "pending", "activeForm": "Applying changes"},
  {"content": "Save to output/pdf/", "status": "pending", "activeForm": "Saving result"}
]
```

## Output Location

All modified files saved to:
- `output/pdf/` - Modified PDFs
- `output/working/` - Intermediate files
