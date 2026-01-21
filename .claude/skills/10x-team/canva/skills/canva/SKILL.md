---
name: canva
description: |
  Main command for Canva operations. Routes to appropriate skill based on request.
user-invocable: true
---

# Canva Skills Hub

Main orchestrator for all Canva API operations. Routes requests to specialized skills.

---

## All Available Canva Skills

### Core Operations
| Skill | Use When | Key Capabilities |
|-------|----------|-----------------|
| **canva-design** | Creating or managing designs | Create, list, search, get details |
| **canva-export** | Downloading designs | PDF, PNG, JPG, PPTX, MP4, GIF |
| **canva-import** | Uploading documents | Import PPTX, PDF, AI, PSD |
| **canva-asset-manager** | Managing media files | Upload images, videos, audio |
| **canva-folder-organizer** | Organizing content | Create folders, move items |

### Specialized Operations
| Skill | Use When | Key Capabilities |
|-------|----------|-----------------|
| **canva-resize** | Adapting for platforms | Resize designs (Pro/Enterprise) |
| **canva-comments** | Collaboration | Add comments, replies |
| **canva-brand-kit** | Brand consistency | Templates, autofill (Enterprise) |
| **canva-creative** | Creating from scratch | Social media, presentations |

### Exploration & Info
| Skill | Use When | Key Capabilities |
|-------|----------|-----------------|
| **canva-explorer** | Browsing account | View designs, folders |
| **canva-user** | Account info | User profile, capabilities |

### Content Editing
| Skill | Use When | Key Capabilities |
|-------|----------|-----------------|
| **canva-image-editor** | Editing images | Modify existing designs |
| **canva-presentation** | Editing slides | Presentation modifications |
| **canva-video** | Video designs | Video creation/editing |

### Local File Editing
| Skill | Use When | Key Capabilities |
|-------|----------|-----------------|
| **local-pptx-editor** | Edit PPTX locally | PowerPoint text updates |
| **local-pdf-editor** | Edit PDF locally | PDF modifications |
| **local-docx-editor** | Edit DOCX locally | Word document updates |
| **local-xlsx-editor** | Edit XLSX locally | Excel modifications |

---

## Quick Start Commands

### Check Account
```bash
.venv\Scripts\python.exe scripts/get_user.py --all
```

### List Designs
```bash
.venv\Scripts\python.exe scripts/list_designs.py
```

### Create Design
```bash
# By preset
.venv\Scripts\python.exe scripts/create_design.py --type presentation --title "My Deck"

# By dimensions
.venv\Scripts\python.exe scripts/create_design.py --width 1080 --height 1080 --title "Square Post"

# Smart create by type name
.venv\Scripts\python.exe scripts/smart_create_design.py instagram_post --title "My Post"
```

### Export Design
```bash
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" --format pdf
```

### Import File
```bash
.venv\Scripts\python.exe scripts/import_design.py "path/to/file.pptx"
```

### Upload Asset
```bash
.venv\Scripts\python.exe scripts/upload_asset.py "path/to/image.png"
```

---

## Complete API Coverage

This skills system covers ALL 48 Canva Connect API endpoints:

### User Endpoints (3)
- GET /v1/users/me
- GET /v1/users/me/profile
- GET /v1/users/me/capabilities

### Design Operations (5)
- GET /v1/designs
- POST /v1/designs
- GET /v1/designs/{id}
- GET /v1/designs/{id}/pages
- GET /v1/designs/{id}/export-formats

### Export Operations (2)
- POST /v1/exports
- GET /v1/exports/{id}

### Import Operations (4)
- POST /v1/imports
- GET /v1/imports/{id}
- POST /v1/url-imports
- GET /v1/url-imports/{id}

### Folder Operations (6)
- POST /v1/folders
- GET /v1/folders/{id}
- PATCH /v1/folders/{id}
- DELETE /v1/folders/{id}
- GET /v1/folders/{id}/items
- POST /v1/folders/move

### Asset Operations (7)
- GET /v1/assets/{id}
- PATCH /v1/assets/{id}
- DELETE /v1/assets/{id}
- POST /v1/asset-uploads
- GET /v1/asset-uploads/{id}
- POST /v1/url-asset-uploads
- GET /v1/url-asset-uploads/{id}

### Brand Templates (3) - Enterprise
- GET /v1/brand-templates
- GET /v1/brand-templates/{id}
- GET /v1/brand-templates/{id}/dataset

### Autofill (2) - Enterprise
- POST /v1/autofills
- GET /v1/autofills/{id}

### Comments (5) - Preview API
- POST /v1/designs/{id}/comments
- GET /v1/designs/{id}/comments/{thread_id}
- POST /v1/designs/{id}/comments/{thread_id}/replies
- GET /v1/designs/{id}/comments/{thread_id}/replies
- GET /v1/designs/{id}/comments/{thread_id}/replies/{reply_id}

### Resize (2) - Premium
- POST /v1/resizes
- GET /v1/resizes/{id}

### Security (3)
- GET /v1/apps/{id}/jwks
- GET /v1/connect/keys
- GET /v1/oidc/jwks

### OIDC (1)
- GET /v1/oidc/userinfo

---

## All CLI Scripts

### User & Auth
- `get_user.py` - User info, profile, capabilities
- `auth_check.py` - Verify authentication
- `oauth_flow.py` - OAuth authorization

### Design Operations
- `create_design.py` - Create by preset/dimensions
- `smart_create_design.py` - Create by type name (50+ types)
- `list_designs.py` - List all designs
- `search_designs.py` - Search designs
- `get_design_details.py` - Get design metadata
- `get_design_pages.py` - Get page thumbnails
- `get_export_formats.py` - Check available formats

### Export Operations
- `export_design.py` - Export single design
- `batch_export.py` - Export multiple designs
- `download_export.py` - Download completed export

### Import Operations
- `import_design.py` - Import from file
- `import_from_url.py` - Import from URL
- `get_import_status.py` - Check import job

### Asset Operations
- `upload_asset.py` - Upload from file
- `upload_asset_from_url.py` - Upload from URL
- `get_asset.py` - Get asset details
- `update_asset.py` - Update name/tags
- `delete_asset.py` - Delete asset

### Folder Operations
- `create_folder.py` - Create folder
- `get_folder.py` - Get folder details
- `update_folder.py` - Rename folder
- `delete_folder.py` - Delete folder
- `list_folder_contents.py` - List folder items
- `list_folders.py` - List all folders
- `move_items.py` - Move items between folders

### Brand Templates (Enterprise)
- `list_brand_templates.py` - List templates
- `get_brand_template.py` - Get template details
- `create_autofill.py` - Create autofill design

### Resize (Premium)
- `resize_design.py` - Resize design

### Comments
- `create_comment.py` - Create comment thread
- `reply_to_comment.py` - Reply to comment
- `list_comments.py` - List replies

### Security
- `get_signing_keys.py` - Get signing keys

### Design Types
- `design_types.py` - 50+ design type configurations
- `integration_helper.py` - Cross-skill integration

---

## Skill Routing Guide

| User Request | Route To |
|--------------|----------|
| "Create a design" | canva-design |
| "Make an Instagram post" | canva-creative |
| "Export to PDF" | canva-export |
| "Upload my logo" | canva-asset-manager |
| "Import my PowerPoint" | canva-import |
| "Create a folder" | canva-folder-organizer |
| "Move designs" | canva-folder-organizer |
| "Resize for LinkedIn" | canva-resize |
| "Add a comment" | canva-comments |
| "Use brand template" | canva-brand-kit |
| "Edit local PPTX" | local-pptx-editor |
| "What designs do I have?" | canva-explorer |
| "Check my account" | canva-user |

---

## Output Locations

```
output/
├── exports/      # Exported design files
├── designs/      # Downloaded designs
├── integration/  # Cross-skill integration files
└── logs/         # Operation logs
```

---

## Rate Limits Summary

| Operation Type | Limit |
|----------------|-------|
| List operations | 100 requests/user |
| Create/Update | 20-30 requests/user |
| Export | 20 requests/user |
| Import | 20 requests/minute |

---

## Feature Requirements by Plan

| Feature | Free | Pro | Enterprise |
|---------|------|-----|------------|
| Create/Export designs | Yes | Yes | Yes |
| Upload assets | Yes | Yes | Yes |
| Folder management | Yes | Yes | Yes |
| Comments | Yes | Yes | Yes |
| Resize | No | Yes | Yes |
| Brand templates | No | No | Yes |
| Autofill | No | No | Yes |
