---
name: local-xlsx-editor
description: |
  Edit Excel spreadsheets (XLSX) locally without Canva API. Use this skill when user provides
  an XLSX file and wants to modify data, update formulas, or change formatting.
  Maintains original formulas, formatting, and structure. Does NOT require Canva.
  Output goes to output/ folder. Use for: "edit this spreadsheet", "update cell A5", "change Excel data".
---

# Local XLSX Editor Skill

Edit and manipulate Excel spreadsheets locally without requiring Canva API.

---

## ⚠️ CRITICAL DESIGN PRESERVATION RULES (MANDATORY)

**These rules are NON-NEGOTIABLE. Violating them will break the spreadsheet structure.**

### 🚫 NEVER DO THESE THINGS:

1. **NEVER add new columns** - Unless user EXPLICITLY requests it
2. **NEVER delete columns** - Unless user EXPLICITLY requests it
3. **NEVER change column widths** - Unless user EXPLICITLY requests it
4. **NEVER change cell formatting** - Unless user EXPLICITLY requests it
5. **NEVER change fonts/colors** - Unless user EXPLICITLY requests it
6. **NEVER change number formats** - Unless user EXPLICITLY requests it
7. **NEVER change cell borders** - Unless user EXPLICITLY requests it
8. **NEVER modify merged cells** - Unless user EXPLICITLY requests it
9. **NEVER change conditional formatting** - Unless user EXPLICITLY requests it
10. **NEVER modify data validation rules** - Unless user EXPLICITLY requests it

### ✅ ALWAYS DO THESE THINGS:

1. **ALWAYS update cell values** in existing cells only
2. **ALWAYS preserve formulas** when updating referenced cells
3. **ALWAYS preserve cell formatting** when updating values
4. **ALWAYS analyze spreadsheet structure first** before any modification
5. **ALWAYS identify data cells vs header/label cells** before editing
6. **ALWAYS preserve named ranges and tables**

### How to Update Data (CORRECT WAY):

```python
# WRONG - Might break formatting
cell.value = "new value"

# CORRECT - Update value while preserving format
# Read current formatting first
cell_format = cell.number_format
cell.value = "new value"
cell.number_format = cell_format  # Restore formatting
```

### Adding Rows (ONLY IF EXPLICITLY REQUESTED):

```python
# If user explicitly asks to add rows:
# - Add within existing data range, not outside
# - Copy formatting from adjacent row
# - Ensure formulas adjust correctly
```

---

## CRITICAL: Never Modify Original Files

1. **ALWAYS** copy the original to `output/working/` first
2. **ALL** edits happen on the copy
3. **SAVE** results to `output/xlsx/`
4. **ORIGINAL** file remains untouched

## When to Use This Skill

Use this skill when:
- User provides an XLSX/XLS file and wants modifications
- Need to update cell values or formulas
- Need to update data within existing structure
- **User has NOT explicitly asked to use Canva**

## Capabilities

### Read Operations (SAFE - No Risk)
- Read cell values and formulas
- Get sheet names and structure
- Extract data ranges
- Analyze formulas
- Identify data tables vs formatting

### Write Operations (FOLLOW PRESERVATION RULES)
- **Update cell values** (preserving formatting)
- **Update formulas** (preserving structure)
- Find and replace values

### ❌ Operations NOT Supported (To Preserve Design)
- Adding/removing columns (unless explicitly requested)
- Changing formatting (unless explicitly requested)
- Changing fonts/colors/borders (unless explicitly requested)
- Modifying merged cells (unless explicitly requested)
- Changing conditional formatting

### Conversion
- XLSX to CSV
- CSV to XLSX

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
.venv\Scripts\python.exe scripts/local/safe_copy.py --source "input/data.xlsx"
```

### Step 2: Analyze
```bash
.venv\Scripts\python.exe scripts/local/xlsx_utils.py "output/working/data_copy.xlsx"
```

### Step 3: Make Modifications

Use xlsx_utils.py for:
- Update specific cells
- Find and replace
- Modify ranges

### Step 4: Save Result
Save to `output/xlsx/data_modified.xlsx`

## 3-Mode Workflow

### MODE 1: PLAN
- Analyze spreadsheet structure
- List sheets and data ranges
- Document proposed changes

### MODE 2: CLARIFY
- Confirm cells to modify
- Verify formula handling
- Check formatting requirements

### MODE 3: IMPLEMENT
- Create working copy
- Apply modifications
- Save to output folder

## Formula Handling

- Formulas automatically recalculate when referenced cells change
- Relative references adjust when rows/columns added
- Named ranges maintained

## Research Capabilities

This skill can:
- Search for Excel best practices
- Look up openpyxl documentation
- Research spreadsheet formulas
- Find solutions to specific challenges

## Available Scripts

- `xlsx_utils.py` - Core XLSX analysis and manipulation
- `safe_copy.py` - Create working copies safely

## Todo List Tracking (REQUIRED)

**ALWAYS use TodoWrite** to track progress:

```json
[
  {"content": "Create safe working copy", "status": "in_progress", "activeForm": "Creating safe copy"},
  {"content": "Analyze spreadsheet structure", "status": "pending", "activeForm": "Analyzing spreadsheet"},
  {"content": "Apply modifications", "status": "pending", "activeForm": "Applying changes"},
  {"content": "Save to output/xlsx/", "status": "pending", "activeForm": "Saving result"}
]
```

## Output Location

- `output/xlsx/` - Modified spreadsheets
- `output/working/` - Working copies
