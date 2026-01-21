---
name: canva-import
description: |
  Import files into Canva (PPTX, PDF, AI, PSD). Use this skill when user wants to
  upload documents for editing in Canva. Supports file upload and URL import.
  Follows 3-mode workflow for safe operations. For uploading images/videos use canva-asset-manager.
---

# Canva Import Operations

Import documents and design files into Canva for editing.

---

## Capabilities

1. **Import from File** - Upload PPTX, PDF, AI, PSD files
2. **Import from URL** - Import files from web URLs
3. **Check Import Status** - Monitor async import jobs
4. **Supported Formats** - PPTX, PDF, AI, PSD

---

## Supported File Formats

| Format | Extension | Description | Max Size |
|--------|-----------|-------------|----------|
| PowerPoint | `.pptx` | Presentations | Varies |
| PDF | `.pdf` | Documents | Varies |
| Illustrator | `.ai` | Vector graphics | Varies |
| Photoshop | `.psd` | Layered images | Varies |

**Note**: `.ppt` (old PowerPoint format) is NOT supported. Convert to `.pptx` first.

---

## Available Scripts

### Import from File
```bash
# Import PPTX file
.venv\Scripts\python.exe scripts/import_design.py "path/to/presentation.pptx"

# Import with custom title
.venv\Scripts\python.exe scripts/import_design.py "path/to/document.pdf" --title "My Document"

# Import and wait for completion
.venv\Scripts\python.exe scripts/import_design.py "path/to/design.psd" --wait

# Custom timeout
.venv\Scripts\python.exe scripts/import_design.py "path/to/large_file.pptx" --timeout 600

# JSON output
.venv\Scripts\python.exe scripts/import_design.py "path/to/file.pdf" --json
```

### Import from URL
```bash
# Import from URL
.venv\Scripts\python.exe scripts/import_from_url.py "https://example.com/presentation.pptx"

# With title
.venv\Scripts\python.exe scripts/import_from_url.py "https://example.com/document.pdf" --title "Imported Document"

# Custom timeout
.venv\Scripts\python.exe scripts/import_from_url.py "https://example.com/file.pptx" --timeout 600
```

### Check Import Status
```bash
# Check status of import job
.venv\Scripts\python.exe scripts/get_import_status.py "import_job_id"

# JSON output
.venv\Scripts\python.exe scripts/get_import_status.py "import_job_id" --json
```

---

## 3-Mode Workflow

### MODE 1: PLAN
1. Verify file format is supported (PPTX, PDF, AI, PSD)
2. Check file exists and is accessible
3. Determine if title override is needed

### MODE 2: CLARIFY
Ask user:
- Is the file in a supported format?
- What title should the imported design have?
- Should we wait for import to complete?

### MODE 3: IMPLEMENT
```bash
# Execute import
.venv\Scripts\python.exe scripts/import_design.py "C:/path/to/presentation.pptx" --title "My Presentation"

# Output:
# Starting import job...
# Import job started: import_abc123
# Waiting for import to complete...
#
# Import Complete!
# ==================================================
#   Design ID: DAFxxxxxxxxxx
#   Title: My Presentation
#
#   Edit URL: https://www.canva.com/design/DAFxxxxxxxxxx/edit
```

---

## Use Cases

### Import PowerPoint Presentation
```bash
# Import existing PPTX
.venv\Scripts\python.exe scripts/import_design.py "presentations/quarterly_report.pptx" --title "Q4 Report"

# After import, edit in Canva or export to different format
```

### Import PDF Document
```bash
# Import PDF for editing
.venv\Scripts\python.exe scripts/import_design.py "documents/brochure.pdf" --title "Company Brochure"
```

### Import from Cloud Storage
```bash
# Import from URL (e.g., cloud storage link)
.venv\Scripts\python.exe scripts/import_from_url.py "https://storage.example.com/files/design.pptx" --title "Cloud Design"
```

### Import Illustrator/Photoshop
```bash
# Import AI file
.venv\Scripts\python.exe scripts/import_design.py "designs/logo.ai" --title "Logo Design"

# Import PSD file
.venv\Scripts\python.exe scripts/import_design.py "designs/banner.psd" --title "Banner Design"
```

---

## Import Process

Canva imports are **asynchronous**:

1. **Upload File** - Send file to Canva, get job ID
2. **Process** - Canva converts file to Canva format
3. **Complete** - Design is ready for editing

```
Status Flow:
  in_progress → success
             → failed (with error)
```

---

## Import vs Asset Upload

| Operation | Use For | Script |
|-----------|---------|--------|
| **Import** | PPTX, PDF, AI, PSD (become designs) | `import_design.py` |
| **Asset Upload** | Images, Videos (become assets) | `upload_asset.py` |

---

## Error Handling

### Unsupported Format
```
Error: File format not supported
```
**Solution**: Convert to PPTX, PDF, AI, or PSD

### File Too Large
```
Error: File exceeds size limit
```
**Solution**: Compress or split the file

### Import Failed
```
Error: Import job failed - {error message}
```
**Solution**: Check file integrity, try re-uploading

### Invalid URL
```
Error: Could not fetch file from URL
```
**Solution**: Verify URL is accessible and points to a supported file type

---

## Rate Limits

| Operation | Limit |
|-----------|-------|
| Create import | 20 requests/minute |
| Get import status | 100 requests/user |

---

## Best Practices

1. **Use PPTX Format** - For presentations, always use `.pptx` (not `.ppt`)
2. **Check File Size** - Large files take longer to import
3. **Verify Format** - Only PPTX, PDF, AI, PSD are supported
4. **Wait for Completion** - Use `--wait` flag for scripts
5. **Preserve Titles** - Use `--title` to set meaningful names

---

## After Import

Once imported, you can:
1. **Edit in Canva** - Open the edit URL
2. **Export to different format** - Use `canva-export` skill
3. **Resize** - Use `canva-resize` skill
4. **Organize** - Use `canva-folder-organizer` to move to folder

---

## Integration

Works with other skills:
- **canva-export**: Export imported designs to different formats
- **canva-presentation**: Edit imported presentations
- **local-pptx-editor**: Edit PPTX locally before importing
