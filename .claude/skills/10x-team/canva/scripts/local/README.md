# Local File Scripts

Python scripts for local file manipulation (PDF, PPTX, DOCX, XLSX).

## CRITICAL RULE: NEVER MODIFY ORIGINAL FILES

**This is a non-negotiable rule for all scripts in this folder:**

1. **NEVER** edit, modify, or overwrite user's original files
2. **ALWAYS** create a working copy first using `safe_copy.py`
3. **ALWAYS** work on the copy in `output/working/`
4. **ALWAYS** save results to appropriate `output/` subfolder
5. **ALWAYS** leave original files untouched

## Workflow

```
User's File (input/)     →     Working Copy (output/working/)     →     Final Result (output/[type]/)
   [PROTECTED]                        [EDITABLE]                            [SAVED HERE]
   Never touched                      All edits here                        User's result
```

## Using These Scripts

### Step 1: Always Create Safe Copy First

```bash
# ALWAYS run this first
python scripts/local/safe_copy.py --source "input/document.pdf"

# Output:
# ✅ Original file is PROTECTED and will NOT be modified:
#    input/document.pdf
# 📄 Working copy created at:
#    output/working/document_copy.pdf
```

### Step 2: Work on the Copy

```bash
# Pass the COPY path to utility scripts
python scripts/local/pdf_utils.py "output/working/document_copy.pdf"
```

### Step 3: Save to Output Folder

All scripts save final results to:
- `output/pdf/` - Modified PDFs
- `output/pptx/` - Modified PowerPoints
- `output/docx/` - Modified Word documents
- `output/xlsx/` - Modified Excel files

## Available Scripts

### Core Utilities
| Script | Description |
|--------|-------------|
| `safe_copy.py` | Creates working copies (USE THIS FIRST) |
| `pdf_utils.py` | PDF analysis and manipulation |
| `pptx_utils.py` | PowerPoint analysis and manipulation |
| `docx_utils.py` | Word document analysis and manipulation |
| `xlsx_utils.py` | Excel analysis and manipulation |

### Script Parameters

All scripts follow this pattern:
- `--file` or `-f`: Path to working copy (NOT original)
- `--output` or `-o`: Output path in output/ folder
- Other operation-specific parameters

### Example Usage

```bash
# PDF Operations
python scripts/local/pdf_utils.py "output/working/doc_copy.pdf"

# PPTX Operations
python scripts/local/pptx_utils.py "output/working/presentation_copy.pptx"

# DOCX Operations
python scripts/local/docx_utils.py "output/working/document_copy.docx"

# XLSX Operations
python scripts/local/xlsx_utils.py "output/working/spreadsheet_copy.xlsx"
```

## Operation Logging

All operations are logged to `output/logs/file_operations.json`:

```json
{
  "timestamp": "20240115_103000",
  "operation": "safe_copy",
  "original": "input/report.pdf",
  "copy": "output/working/report_copy.pdf",
  "file_type": "pdf",
  "original_modified": false
}
```

This creates an audit trail and proves the original was never touched.

## Dependencies

Install required packages:
```bash
pip install PyPDF2 pdfplumber reportlab python-pptx python-docx openpyxl Pillow
```

Or install all at once:
```bash
pip install -r requirements.txt
```

## Why This Matters

1. **User Trust**: Users trust us with their important documents
2. **Reversibility**: Mistakes can be undone by starting fresh
3. **Comparison**: Users can compare original vs. modified
4. **Audit Trail**: Clear record of what was changed
5. **No Regrets**: Original is always safe no matter what

## Error Handling

If something goes wrong:
1. Original file is ALWAYS safe in its original location
2. Delete the working copy: `rm output/working/*`
3. Start fresh with a new `safe_copy.py` call

## Script Authors Note

When creating new scripts for this folder:
1. NEVER accept `input/` paths for write operations
2. ALWAYS require output path to be in `output/` folder
3. ALWAYS validate paths before any write operation
4. ALWAYS log operations to the audit trail
