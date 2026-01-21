---
name: canva-export
description: |
  Export Canva designs to various formats (PDF, PNG, JPG, PPTX, MP4, GIF). Use this skill
  when user wants to download, export, or save their designs. Handles single and bulk
  exports with format options. Follows 3-mode workflow for confirmation.
  For editing designs use other specialized skills (canva-image-editor, canva-presentation).
---

# Canva Export Operations

Export designs to all available formats with full control over quality and options.

---

## Capabilities

1. **Export to PDF** - Standard or print quality
2. **Export to PNG** - With size and compression options
3. **Export to JPG** - With quality control
4. **Export to PPTX** - PowerPoint presentation
5. **Export to MP4** - Video format
6. **Export to GIF** - Animated GIF
7. **Batch Export** - Multiple designs at once
8. **Check Export Formats** - See available options per design
9. **Download Exports** - Retrieve exported files

---

## Available Scripts

### Check Available Formats
```bash
# See what formats are available for a design
.venv\Scripts\python.exe scripts/get_export_formats.py "DAFxxxxxxxxxx"
```

### Export Design
```bash
# Export as PNG (default)
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx"
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format png

# Export as JPG
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format jpg

# Export as PDF (standard quality)
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format pdf

# Export as PDF (print quality - high resolution)
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format pdf --quality print

# Export as PPTX (PowerPoint)
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format pptx

# Export as MP4 (video)
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format mp4

# Export as GIF
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format gif

# Custom output directory and filename
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format png --output output/designs --filename "my_design"

# Export specific pages only (1-indexed)
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" --format png --pages 1 2 3
```

### Batch Export
```bash
# Export multiple designs
.venv\Scripts\python.exe scripts/batch_export.py --designs "DAF1" "DAF2" "DAF3" --format png --output output/batch

# Export with specific format
.venv\Scripts\python.exe scripts/batch_export.py --designs "DAF1" "DAF2" --format pdf --quality print

# From file (one design ID per line)
.venv\Scripts\python.exe scripts/batch_export.py --file design_ids.txt --format png
```

### Download Export (if job ID known)
```bash
# Download completed export
.venv\Scripts\python.exe scripts/download_export.py "export_job_id" --output output/downloads
```

---

## Export Formats

| Format | Best For | Supports |
|--------|----------|----------|
| **PDF** | Documents, Print | Multi-page, High quality |
| **PNG** | Web, Transparency | Single/Multi-page, Lossless |
| **JPG** | Photos, Social | Single/Multi-page, Compressed |
| **PPTX** | Presentations | Multi-page, Editable |
| **MP4** | Videos | Animation, Audio |
| **GIF** | Animations | No audio, Looping |

---

## Export Format Options

### PDF Options
| Option | Values | Description |
|--------|--------|-------------|
| `--quality` | `standard`, `print` | Print = higher DPI for printing |

### PNG Options
| Option | Values | Description |
|--------|--------|-------------|
| `--size` | `small`, `medium`, `large` | Image resolution |
| `--lossless` | flag | Lossless compression |

### JPG Options
| Option | Values | Description |
|--------|--------|-------------|
| `--size` | `small`, `medium`, `large` | Image resolution |
| `--export-quality` | 1-100 | Compression quality |

### Video Options (MP4/GIF)
No additional options - exports as configured in design.

---

## Size Reference

### PNG/JPG Sizes
| Size | Approximate Resolution |
|------|----------------------|
| small | ~500px max dimension |
| medium | ~1000px max dimension |
| large | Original resolution |

---

## 3-Mode Workflow

### MODE 1: PLAN
1. Get design ID
2. Check available export formats
3. Determine required format and quality

### MODE 2: CLARIFY
Ask user:
- Which format? (PDF, PNG, JPG, PPTX, MP4, GIF)
- Quality/size requirements?
- Output location?
- Specific pages?

### MODE 3: IMPLEMENT
```bash
# Execute export
.venv\Scripts\python.exe scripts/export_design.py "DAFxxxxxxxxxx" \
    --format pdf \
    --quality print \
    --output output/exports \
    --filename "final_design"

# Output:
# Starting export job...
# Export job started: export_abc123
# Waiting for export to complete...
# Downloaded: output/exports/final_design.pdf
#
# Export Complete!
# ==================================================
#   Format: PDF (print quality)
#   Files:  output/exports/final_design.pdf
```

---

## Use Cases

### Social Media Export
```bash
# Instagram Post (PNG, large)
.venv\Scripts\python.exe scripts/export_design.py "DAFinstagram" --format png --size large

# Multiple platforms
.venv\Scripts\python.exe scripts/batch_export.py \
    --designs "DAFinstagram" "DAFlinkedin" "DAFtwitter" \
    --format png --size large --output output/social
```

### Print Materials
```bash
# High-quality PDF for printing
.venv\Scripts\python.exe scripts/export_design.py "DAFbrochure" --format pdf --quality print

# Poster
.venv\Scripts\python.exe scripts/export_design.py "DAFposter" --format pdf --quality print
```

### Presentations
```bash
# Export to PowerPoint
.venv\Scripts\python.exe scripts/export_design.py "DAFpresentation" --format pptx --output output/presentations

# Export specific slides as images
.venv\Scripts\python.exe scripts/export_design.py "DAFpresentation" --format png --pages 1 5 10
```

### Video Content
```bash
# Export video design
.venv\Scripts\python.exe scripts/export_design.py "DAFvideo" --format mp4

# Export as GIF
.venv\Scripts\python.exe scripts/export_design.py "DAFanimation" --format gif
```

---

## Export Process

Canva exports are **asynchronous**:

1. **Initiate Export** - Request export, get job ID
2. **Poll Status** - Check if export is ready
3. **Download** - Get file from temporary URL

The export scripts handle this automatically. Download URLs are valid for 24 hours.

---

## Output Structure

Default output directory: `output/exports/`

```
output/
├── exports/
│   ├── design_name.pdf
│   ├── design_name.png
│   └── design_name.pptx
├── social/
│   ├── instagram.png
│   └── linkedin.png
└── batch/
    ├── design1.png
    ├── design2.png
    └── design3.png
```

---

## Rate Limits

| Operation | Limit |
|-----------|-------|
| Create export | 20 requests/user |
| Get export status | 100 requests/user |

**Note**: Download URLs are valid for 24 hours.

---

## Error Handling

### Unsupported Format
```
Error: Format 'xyz' is not available for this design
```
**Solution**: Check available formats with `get_export_formats.py`

### Export Failed
```
Error: Export job failed
```
**Solution**: Check design for issues, try different format

### Download Expired
```
Error: Download URL expired
```
**Solution**: Create new export job

---

## Integration

Exports can be used with:
- **10x-Outreach-Skill**: Attach exported images to emails
- **Local editing**: Download PPTX for local PowerPoint editing
- **Social posting**: Use exported PNG/JPG for social media
