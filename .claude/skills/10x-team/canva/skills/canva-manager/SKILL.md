---
name: canva-manager
description: |
  Comprehensive Canva API integration skill for managing designs, folders, assets, and exports.
  Uses a 3-mode workflow: PLAN (analyze what needs to be done), CLARIFY (ask user questions),
  and IMPLEMENT (execute changes via Python scripts). Ensures safe operations by always
  confirming changes before execution. Use this skill when the user wants to work with their
  Canva account, manage designs, organize folders, upload assets, or export designs.
---

# Canva Manager Skill

A comprehensive skill for managing Canva designs, folders, and assets through the Canva Connect API. This skill operates in a **3-mode workflow** to ensure safe and accurate operations on your Canva account.

## Overview

This skill provides full control over your Canva account including:
- **Designs**: List, view, create, import (PPTX/PDF/AI/PSD), export, and manage designs
- **Folders**: Create, organize, move items, and manage your project structure
- **Assets**: Upload images/videos, manage asset library
- **Exports**: Export designs to various formats (PDF, PNG, JPG, PPTX, MP4, GIF)

## 3-Mode Workflow

**CRITICAL: Always follow this workflow. Never skip to implementation without completing Plan and Clarify modes.**

### Mode 1: PLAN

Before making ANY changes to Canva, you MUST:

1. **Analyze the Request**
   - What exactly does the user want to accomplish?
   - Which Canva resources are involved (designs, folders, assets)?
   - What API operations will be needed?

2. **Gather Current State**
   - Run the discovery scripts to understand current Canva account state
   - List relevant designs, folders, or assets
   - Identify exactly which items will be affected

3. **Create Detailed Plan**
   - Document every action that will be taken
   - List which designs/folders/assets will be modified
   - Specify the exact changes (names, exports, moves, etc.)
   - Identify potential risks or irreversible actions

4. **Present Plan to User**

### Mode 2: CLARIFY

After presenting the plan, you MUST ask clarifying questions:

1. **Required Questions**
   - "Does this plan accurately reflect what you want to do?"
   - "Are there any items I should exclude from this operation?"

2. **Context-Specific Questions**
   - For exports: "What format and quality do you prefer?"
   - For folder operations: "Should I create backups first?"
   - For design modifications: "Should I work on copies instead of originals?"

3. **Confirmation Requirements**
   - Get explicit "yes" or confirmation before proceeding
   - If user has concerns, return to PLAN mode with modifications

### Mode 3: IMPLEMENT

Only after explicit user approval:

1. **Execute with Logging**
   - Run the appropriate Python scripts
   - Log every API call and response
   - Save results to the output folder

2. **Report Results**
   - Show exactly what was changed
   - Provide links/IDs of affected items
   - Note any errors or partial completions

## Environment Setup

Ensure the `.env` file is configured:

```bash
# Required - Get from https://www.canva.com/developers/
CANVA_CLIENT_ID=your_client_id
CANVA_CLIENT_SECRET=your_client_secret

# OAuth tokens (obtained after authorization)
CANVA_ACCESS_TOKEN=your_access_token
CANVA_REFRESH_TOKEN=your_refresh_token

# Optional
CANVA_REDIRECT_URI=http://127.0.0.1:3001/oauth/redirect
```

## Running Python Scripts (Virtual Environment)

**IMPORTANT**: Always use the virtual environment Python:

```bash
# Windows
.venv\Scripts\python.exe scripts/<script_name>.py

# macOS/Linux
.venv/bin/python scripts/<script_name>.py
```

## Available Scripts

All scripts are in `scripts/`:

### Discovery Scripts (Safe - Read Only)

#### auth_check.py - Verify credentials and get user info
```bash
.venv\Scripts\python.exe scripts/auth_check.py
```

#### list_designs.py - List all designs with metadata
```bash
.venv\Scripts\python.exe scripts/list_designs.py
.venv\Scripts\python.exe scripts/list_designs.py --query "presentation" --limit 10
.venv\Scripts\python.exe scripts/list_designs.py --json
```

#### list_folders.py - List folder structure
```bash
.venv\Scripts\python.exe scripts/list_folders.py
.venv\Scripts\python.exe scripts/list_folders.py --json
```

#### get_design_details.py - Get detailed info about a specific design
```bash
.venv\Scripts\python.exe scripts/get_design_details.py "DESIGN_ID"
.venv\Scripts\python.exe scripts/get_design_details.py "DESIGN_ID" --pages --formats
```

#### list_folder_contents.py - List items in a specific folder
```bash
.venv\Scripts\python.exe scripts/list_folder_contents.py "FOLDER_ID"
.venv\Scripts\python.exe scripts/list_folder_contents.py "root" --types design folder
.venv\Scripts\python.exe scripts/list_folder_contents.py "uploads"
```

### Export Scripts

#### export_design.py - Export a design to specified format
```bash
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" --format pdf
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" --format pptx --output output/exports
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" --format png --pages 1 2 3
```

#### download_export.py - Download a completed export by job ID
```bash
.venv\Scripts\python.exe scripts/download_export.py "EXPORT_JOB_ID"
.venv\Scripts\python.exe scripts/download_export.py "EXPORT_JOB_ID" --output output/myfile
```

#### batch_export.py - Export multiple designs at once
```bash
.venv\Scripts\python.exe scripts/batch_export.py --designs "ID1" "ID2" "ID3" --format pdf
.venv\Scripts\python.exe scripts/batch_export.py --designs "ID1" "ID2" --format pptx --output output/exports
```

### Import Scripts

#### import_design.py - Import PPTX, PDF, AI, or PSD files into Canva
```bash
# Import a PPTX file
.venv\Scripts\python.exe scripts/import_design.py "presentation.pptx"

# Import with custom title
.venv\Scripts\python.exe scripts/import_design.py "presentation.pptx" --title "My Imported Presentation"

# Import a PDF
.venv\Scripts\python.exe scripts/import_design.py "document.pdf" --title "My PDF"

# Start import without waiting
.venv\Scripts\python.exe scripts/import_design.py "presentation.pptx" --no-wait
```

Supported import formats:
- `.pptx` - PowerPoint presentations
- `.pdf` - PDF documents
- `.ai` - Adobe Illustrator files
- `.psd` - Photoshop files

#### get_import_status.py - Check status of import job
```bash
.venv\Scripts\python.exe scripts/get_import_status.py "JOB_ID"
.venv\Scripts\python.exe scripts/get_import_status.py "JOB_ID" --wait
```

### Asset Upload Scripts

#### upload_asset.py - Upload images/videos to Canva
```bash
# Upload an image
.venv\Scripts\python.exe scripts/upload_asset.py "image.png"

# Upload with custom name
.venv\Scripts\python.exe scripts/upload_asset.py "photo.jpg" --name "Product Photo"

# Upload a video
.venv\Scripts\python.exe scripts/upload_asset.py "video.mp4"
```

Supported upload formats:
- Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.heic`, `.heif`, `.tiff`, `.tif` (max 50MB)
- Videos: `.mp4`, `.mov`, `.avi`, `.webm`, `.mkv`, `.m4v`, `.mpeg`, `.mpg` (max 500MB)

### Folder Management Scripts

#### create_folder.py - Create a new folder
```bash
.venv\Scripts\python.exe scripts/create_folder.py --name "My Project"
.venv\Scripts\python.exe scripts/create_folder.py --name "Subfolder" --parent "PARENT_FOLDER_ID"
```

#### move_items.py - Move items between folders
```bash
.venv\Scripts\python.exe scripts/move_items.py --items "ITEM_ID1" "ITEM_ID2" --folder "TARGET_FOLDER_ID"
.venv\Scripts\python.exe scripts/move_items.py --items "DESIGN_ID" --folder "root"
```

#### delete_folder.py - Delete a folder (moves to trash)
```bash
.venv\Scripts\python.exe scripts/delete_folder.py "FOLDER_ID" --confirm
```

### Design Creation Scripts

#### create_design.py - Create a new blank design
```bash
# Create by preset type
.venv\Scripts\python.exe scripts/create_design.py --type presentation --title "My Presentation"
.venv\Scripts\python.exe scripts/create_design.py --type instagram_post

# Create with custom dimensions
.venv\Scripts\python.exe scripts/create_design.py --width 1920 --height 1080 --title "Custom Design"

# List available types
.venv\Scripts\python.exe scripts/create_design.py --list-types
```

Available design types:
- `instagram_post`, `instagram_story`
- `facebook_post`
- `presentation`
- `doc`
- `whiteboard`
- `poster`, `flyer`
- `a4`, `letter`

### Asset Management Scripts

#### delete_asset.py - Delete an asset (moves to trash)
```bash
.venv\Scripts\python.exe scripts/delete_asset.py "ASSET_ID" --confirm
```

## API Rate Limits

Be aware of Canva API rate limits:
- List operations: 100 requests/user
- Create/Update operations: 20-30 requests/user
- Export operations: 20 requests/user
- Import operations: 20 requests/minute

For bulk operations, scripts automatically implement delays between requests.

## Usage Examples

### Example 1: Explore Canva Account
```bash
# Check authentication
.venv\Scripts\python.exe scripts/auth_check.py

# List all designs
.venv\Scripts\python.exe scripts/list_designs.py

# List folder structure
.venv\Scripts\python.exe scripts/list_folders.py
```

### Example 2: Export Presentation to PPTX
```bash
# Find the design
.venv\Scripts\python.exe scripts/list_designs.py --query "Q4 Report"

# Export it
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" --format pptx --output output/exports
```

### Example 3: Import PPTX to Canva
```bash
# Import the file
.venv\Scripts\python.exe scripts/import_design.py "presentation.pptx" --title "Imported Presentation"
```

### Example 4: Organize Designs into Folders
```bash
# Create a folder
.venv\Scripts\python.exe scripts/create_folder.py --name "2024 Projects"

# Move designs to the folder
.venv\Scripts\python.exe scripts/move_items.py --items "DESIGN_ID1" "DESIGN_ID2" --folder "NEW_FOLDER_ID"
```

### Example 5: Upload Assets
```bash
# Upload images
.venv\Scripts\python.exe scripts/upload_asset.py "logo.png" --name "Company Logo"
.venv\Scripts\python.exe scripts/upload_asset.py "photo.jpg" --name "Product Photo"
```

## Safety Guidelines

1. **Never modify without confirmation** - Always get explicit approval
2. **Prefer copies over originals** - For risky operations, suggest working on copies
3. **Batch operations need extra care** - Show sample of items before bulk changes
4. **Export originals before deletion** - If user wants to delete, export first
5. **Log everything** - All operations are logged to output folder
6. **Rate limit awareness** - Don't exceed API limits; scripts implement delays

## Troubleshooting

### Authentication Issues
```bash
.venv\Scripts\python.exe scripts/auth_check.py
```
If this fails, re-run OAuth flow or refresh tokens.

### Design Not Found
- Check exact spelling and case
- Try listing all designs to find the correct name
- Designs may be in trash or shared with you

### Export Failures
- Some formats require Canva Pro
- Very large designs may timeout
- Check design isn't corrupted

### Import Failures
- Ensure file format is supported (.pptx, .pdf, .ai, .psd)
- Check file size limits
- Verify file isn't corrupted

## Resources

- [Canva Connect API Docs](https://www.canva.dev/docs/connect/)
- [Canva Developer Portal](https://www.canva.com/developers/)
- [API Rate Limits](https://www.canva.dev/docs/connect/rate-limits/)

## Todo List Tracking (REQUIRED)

**ALWAYS use TodoWrite** to track progress for Canva operations:

```json
[
  {"content": "Check API authentication", "status": "in_progress", "activeForm": "Checking authentication"},
  {"content": "List user's designs", "status": "pending", "activeForm": "Listing designs"},
  {"content": "Export requested design", "status": "pending", "activeForm": "Exporting design"},
  {"content": "Confirm completion", "status": "pending", "activeForm": "Confirming completion"}
]
```

## File Outputs

All outputs are saved to the `output/` folder:
- `output/exports/` - Exported files (PDFs, images, PPTX, etc.)
- `output/logs/` - Operation logs with timestamps
- `output/auth/` - Authentication info
