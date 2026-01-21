---
name: canva-asset-manager
description: |
  Upload and manage assets (images, videos, audio) in your Canva account. Use this skill
  when user wants to upload files to Canva, manage their asset library, or work with
  uploaded media. Handles image, video, and audio uploads. Follows 3-mode workflow.
  For organizing uploaded assets use canva-folder-organizer.
---

# Canva Asset Manager

Upload and manage media assets in your Canva account.

---

## Capabilities

1. **Upload Assets** - Upload images, videos, audio from files
2. **Upload from URL** - Import assets from web URLs
3. **Get Asset Info** - View asset metadata
4. **Update Assets** - Rename and tag assets
5. **Delete Assets** - Remove assets (moves to trash)

---

## Supported File Types

### Images (Max 50MB)
| Format | Extension | Notes |
|--------|-----------|-------|
| JPEG | `.jpg`, `.jpeg` | Best for photos |
| PNG | `.png` | Supports transparency |
| GIF | `.gif` | Static or animated |
| WebP | `.webp` | Modern format |
| HEIC/HEIF | `.heic`, `.heif` | Apple format |
| TIFF | `.tiff`, `.tif` | High quality |

### Videos (Max 500MB)
| Format | Extension | Notes |
|--------|-----------|-------|
| MP4 | `.mp4` | Most common |
| MOV | `.mov` | Apple format |
| AVI | `.avi` | Windows format |
| WebM | `.webm` | Web format |
| MKV | `.mkv` | Container format |
| M4V | `.m4v` | Apple format |
| MPEG | `.mpeg`, `.mpg` | Legacy format |

### Audio
| Format | Extension |
|--------|-----------|
| MP3 | `.mp3` |
| WAV | `.wav` |
| M4A | `.m4a` |
| OGG | `.ogg` |

---

## Available Scripts

### Upload from File
```bash
# Upload single file
.venv\Scripts\python.exe scripts/upload_asset.py "path/to/image.png"

# With custom name
.venv\Scripts\python.exe scripts/upload_asset.py "path/to/image.png" --name "My Asset"

# Wait for upload to complete
.venv\Scripts\python.exe scripts/upload_asset.py "path/to/video.mp4" --wait

# JSON output
.venv\Scripts\python.exe scripts/upload_asset.py "path/to/file.jpg" --json
```

### Upload from URL (Preview API)
```bash
# Upload from URL
.venv\Scripts\python.exe scripts/upload_asset_from_url.py "https://example.com/image.png" --name "Downloaded Image"

# With timeout
.venv\Scripts\python.exe scripts/upload_asset_from_url.py "https://example.com/video.mp4" --name "Video" --timeout 600
```

### Get Asset Info
```bash
# Get asset details
.venv\Scripts\python.exe scripts/get_asset.py "asset_id"

# JSON output
.venv\Scripts\python.exe scripts/get_asset.py "asset_id" --json
```

### Update Asset
```bash
# Rename asset
.venv\Scripts\python.exe scripts/update_asset.py "asset_id" --name "New Name"

# Set tags
.venv\Scripts\python.exe scripts/update_asset.py "asset_id" --tags "tag1" "tag2" "tag3"

# Add tags to existing
.venv\Scripts\python.exe scripts/update_asset.py "asset_id" --add-tags "new-tag"

# Rename and tag
.venv\Scripts\python.exe scripts/update_asset.py "asset_id" --name "My Logo" --tags "brand" "logo"
```

### Delete Asset
```bash
# Delete asset (moves to trash)
.venv\Scripts\python.exe scripts/delete_asset.py "asset_id"

# Force confirm
.venv\Scripts\python.exe scripts/delete_asset.py "asset_id" --confirm

# JSON output
.venv\Scripts\python.exe scripts/delete_asset.py "asset_id" --json
```

---

## 3-Mode Workflow

### MODE 1: PLAN
1. Verify file format is supported
2. Check file size limits
3. Determine naming and tagging strategy

### MODE 2: CLARIFY
Ask user:
- What should the asset be named?
- Any tags to add for organization?
- Should we wait for upload to complete?

### MODE 3: IMPLEMENT
```bash
# Execute upload
.venv\Scripts\python.exe scripts/upload_asset.py "input/images/logo.png" --name "Company Logo" --wait

# Output:
# Starting upload...
# Upload job started: job_xxx
# Waiting for upload to complete...
#
# Asset Uploaded Successfully!
# ==================================================
#   Asset ID: asset_xxx
#   Name: Company Logo
#   Type: image
```

---

## Use Cases

### Upload Brand Assets
```bash
# Upload logo
.venv\Scripts\python.exe scripts/upload_asset.py "brand/logo.png" --name "Primary Logo"

# Upload with brand tags
.venv\Scripts\python.exe scripts/upload_asset.py "brand/icon.png" --name "Brand Icon"
.venv\Scripts\python.exe scripts/update_asset.py "asset_xxx" --tags "brand" "logo" "icon"
```

### Upload Marketing Images
```bash
# Upload product photos
.venv\Scripts\python.exe scripts/upload_asset.py "products/product1.jpg" --name "Product 1"
.venv\Scripts\python.exe scripts/upload_asset.py "products/product2.jpg" --name "Product 2"
```

### Upload from Web
```bash
# Download and upload from URL
.venv\Scripts\python.exe scripts/upload_asset_from_url.py "https://example.com/photo.jpg" --name "Stock Photo"
```

---

## File Size Limits

| Type | Max Size |
|------|----------|
| Images | 50 MB |
| Videos | 500 MB |
| URL uploads | 100 MB |

---

## Rate Limits

| Operation | Limit |
|-----------|-------|
| Upload operations | 20-30 requests/user |
| Get asset | 100 requests/user |
| Update asset | 20-30 requests/user |
| Delete asset | 20-30 requests/user |

---

## Error Handling

### Unsupported Format
```
Error: File format not supported
```
**Solution**: Convert to supported format (JPG, PNG, MP4, etc.)

### File Too Large
```
Error: File exceeds size limit
```
**Solution**: Compress or resize the file

### Upload Failed
```
Error: Upload job failed
```
**Solution**: Check file integrity, try re-uploading

---

## Asset vs Design Import

| Operation | Use For | Script |
|-----------|---------|--------|
| **Asset Upload** | Images, Videos (become reusable assets) | `upload_asset.py` |
| **Design Import** | PPTX, PDF, AI, PSD (become editable designs) | `import_design.py` |

---

## Integration

Works with:
- **canva-folder-organizer**: Organize uploaded assets into folders
- **canva-image-editor**: Use assets in designs
- **canva-video**: Use video assets
