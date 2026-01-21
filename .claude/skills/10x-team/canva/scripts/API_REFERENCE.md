# Canva Connect API Reference

Complete reference for all Canva API endpoints implemented in `canva_client.py`.

## Base URL

```
https://api.canva.com/rest/v1/
```

## Authentication

All endpoints require OAuth 2.0 Bearer token authentication.

```python
from canva_client import get_client
client = get_client()  # Uses token from .env
```

---

## User Endpoints

### Get User Info
```python
client.get_user_info()
```
- **Endpoint**: `GET /v1/users/me`
- **Returns**: User ID, team ID

### Get User Profile
```python
client.get_user_profile()
```
- **Endpoint**: `GET /v1/users/me/profile`
- **Returns**: Display name

### Get User Capabilities
```python
client.get_user_capabilities()
```
- **Endpoint**: `GET /v1/users/me/capabilities`
- **Returns**: Available API features for user

---

## Design Endpoints

### List Designs
```python
client.list_designs(
    limit=50,           # Max 100
    continuation=None,  # Pagination token
    ownership=None,     # 'owned' or 'shared'
    sort_by=None,       # 'relevance', 'modified_descending', etc.
    query=None          # Search query (max 255 chars)
)
```
- **Endpoint**: `GET /v1/designs`

### Get Design
```python
client.get_design(design_id)
```
- **Endpoint**: `GET /v1/designs/{design_id}`

### Get Design Pages
```python
client.get_design_pages(design_id, offset=1, limit=50)
```
- **Endpoint**: `GET /v1/designs/{design_id}/pages`
- **Returns**: Page thumbnails and metadata

### Get Export Formats
```python
client.get_export_formats(design_id)
```
- **Endpoint**: `GET /v1/designs/{design_id}/export-formats`

### Create Design
```python
# By preset type
client.create_design(design_type='presentation', title='My Presentation')

# By custom dimensions
client.create_design(width=1920, height=1080, title='Custom Design')
```
- **Endpoint**: `POST /v1/designs`
- **Design types**: `instagram_post`, `instagram_story`, `facebook_post`, `presentation`, `doc`, `whiteboard`, `poster`, `flyer`, `a4_document`, `us_letter_document`

---

## Export Endpoints

### Create Export Job
```python
client.create_export(
    design_id='...',
    format_type='pdf',     # 'pdf', 'png', 'jpg', 'pptx', 'mp4', 'gif'
    pages=[1, 2, 3],       # Optional: specific pages (1-indexed)
    quality='standard',    # 'standard' or 'print' (PDF only)
    size='large',          # 'small', 'medium', 'large' (PNG/JPG)
    lossless=False,        # PNG only
    export_quality=85      # JPG quality 1-100
)
```
- **Endpoint**: `POST /v1/exports`
- **Rate limit**: 20 requests/user

### Get Export Status
```python
client.get_export(export_id)
```
- **Endpoint**: `GET /v1/exports/{export_id}`

### Wait for Export (Helper)
```python
result = client.wait_for_export(export_id, timeout=300, poll_interval=2)
```

### Export and Download (Helper)
```python
files = client.export_and_download(
    design_id='...',
    format_type='pptx',
    output_dir='output/exports',
    filename='my_presentation',  # Optional
    pages=[1, 2, 3],             # Optional
    quality='print',             # Optional
    timeout=300
)
```

---

## Import Endpoints

### Create Design Import Job
```python
client.create_design_import(file_path='presentation.pptx', title='My Import')
```
- **Endpoint**: `POST /v1/imports`
- **Supported formats**: `.pptx`, `.pdf`, `.ai`, `.psd`
- **Rate limit**: 20 requests/minute

### Get Import Status
```python
client.get_design_import_status(job_id)
```
- **Endpoint**: `GET /v1/imports/{job_id}`

### Create URL Import Job
```python
client.create_url_design_import(url='https://...', title='My Import')
```
- **Endpoint**: `POST /v1/url-imports`

### Get URL Import Status
```python
client.get_url_design_import_status(job_id)
```
- **Endpoint**: `GET /v1/url-imports/{job_id}`

### Import and Wait (Helper)
```python
result = client.import_and_wait(
    file_path='presentation.pptx',
    title='My Import',
    timeout=300
)
```

---

## Folder Endpoints

### Create Folder
```python
client.create_folder(name='My Folder', parent_folder_id='root')
```
- **Endpoint**: `POST /v1/folders`
- **Special IDs**: `root` (Projects), `uploads` (Uploads folder)

### Get Folder
```python
client.get_folder(folder_id)
```
- **Endpoint**: `GET /v1/folders/{folder_id}`

### Update Folder
```python
client.update_folder(folder_id, name='New Name')
```
- **Endpoint**: `PATCH /v1/folders/{folder_id}`

### Delete Folder
```python
client.delete_folder(folder_id)
```
- **Endpoint**: `DELETE /v1/folders/{folder_id}`
- **Note**: Moves to trash

### List Folder Items
```python
client.list_folder_items(
    folder_id='root',
    limit=50,
    continuation=None,
    item_types=['design', 'folder', 'image'],
    sort_by='modified_descending'
)
```
- **Endpoint**: `GET /v1/folders/{folder_id}/items`

### Move Items
```python
client.move_items(item_ids=['id1', 'id2'], target_folder_id='folder_id')
```
- **Endpoint**: `POST /v1/folders/move`

---

## Asset Endpoints

### Get Asset
```python
client.get_asset(asset_id)
```
- **Endpoint**: `GET /v1/assets/{asset_id}`

### Update Asset
```python
client.update_asset(asset_id, name='New Name', tags=['tag1', 'tag2'])
```
- **Endpoint**: `PATCH /v1/assets/{asset_id}`

### Delete Asset
```python
client.delete_asset(asset_id)
```
- **Endpoint**: `DELETE /v1/assets/{asset_id}`
- **Note**: Moves to trash

### Create Asset Upload Job
```python
client.create_asset_upload(name='My Image', file_path='image.png')
```
- **Endpoint**: `POST /v1/asset-uploads`
- **Supported images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.heic`, `.heif`, `.tiff` (max 50MB)
- **Supported videos**: `.mp4`, `.mov`, `.avi`, `.webm`, `.mkv`, `.m4v`, `.mpeg` (max 500MB)

### Get Asset Upload Status
```python
client.get_asset_upload_status(job_id)
```
- **Endpoint**: `GET /v1/asset-uploads/{job_id}`

### Create URL Asset Upload
```python
client.create_url_asset_upload(name='My Image', url='https://...')
```
- **Endpoint**: `POST /v1/url-asset-uploads`

### Get URL Asset Upload Status
```python
client.get_url_asset_upload_status(job_id)
```
- **Endpoint**: `GET /v1/url-asset-uploads/{job_id}`

### Upload Asset and Wait (Helper)
```python
result = client.upload_asset_and_wait(
    file_path='image.png',
    name='My Image',  # Optional
    timeout=300
)
```

---

## Brand Template Endpoints (Enterprise Only)

### List Brand Templates
```python
client.list_brand_templates(
    limit=25,
    continuation=None,
    query=None,
    ownership=None,
    sort_by=None
)
```
- **Endpoint**: `GET /v1/brand-templates`

### Get Brand Template
```python
client.get_brand_template(brand_template_id)
```
- **Endpoint**: `GET /v1/brand-templates/{brand_template_id}`

### Get Brand Template Dataset
```python
client.get_brand_template_dataset(brand_template_id)
```
- **Endpoint**: `GET /v1/brand-templates/{brand_template_id}/dataset`

---

## Autofill Endpoints (Enterprise Only)

### Create Autofill Job
```python
client.create_autofill(
    brand_template_id='...',
    data={'field1': 'value1', 'field2': 'value2'},
    title='My Autofilled Design'
)
```
- **Endpoint**: `POST /v1/autofills`

### Get Autofill Status
```python
client.get_autofill_status(job_id)
```
- **Endpoint**: `GET /v1/autofills/{job_id}`

### Wait for Autofill (Helper)
```python
result = client.wait_for_autofill(job_id, timeout=300, poll_interval=3)
```

---

## Comment Endpoints (Preview API)

### Create Comment Thread
```python
client.create_comment_thread(
    design_id='...',
    message='My comment',
    attached_to={'page_id': '...'},  # Optional
    assignee_id='...'                 # Optional
)
```
- **Endpoint**: `POST /v1/designs/{design_id}/comments`

### Get Comment Thread
```python
client.get_comment_thread(design_id, thread_id)
```
- **Endpoint**: `GET /v1/designs/{design_id}/comments/{thread_id}`

### Create Reply
```python
client.create_reply(design_id, thread_id, message='My reply')
```
- **Endpoint**: `POST /v1/designs/{design_id}/comments/{thread_id}/replies`

### List Replies
```python
client.list_replies(design_id, thread_id, limit=50, continuation=None)
```
- **Endpoint**: `GET /v1/designs/{design_id}/comments/{thread_id}/replies`

### Get Reply
```python
client.get_reply(design_id, thread_id, reply_id)
```
- **Endpoint**: `GET /v1/designs/{design_id}/comments/{thread_id}/replies/{reply_id}`

---

## Resize Endpoints (Premium Feature)

### Create Resize Job
```python
client.create_resize(
    design_id='...',
    width=1080,
    height=1920,
    title='Resized Design'  # Optional
)
```
- **Endpoint**: `POST /v1/resizes`
- **Note**: Max 25M total pixels

### Get Resize Status
```python
client.get_resize_status(job_id)
```
- **Endpoint**: `GET /v1/resizes/{job_id}`

### Wait for Resize (Helper)
```python
result = client.wait_for_resize(job_id, timeout=300, poll_interval=2)
```

---

## App Endpoints

### Get App JWKS
```python
client.get_app_jwks(app_id)
```
- **Endpoint**: `GET /v1/apps/{app_id}/jwks`
- **Returns**: JSON Web Key Set for JWT verification

---

## Connect Endpoints

### Get Signing Public Keys
```python
client.get_signing_public_keys()
```
- **Endpoint**: `GET /v1/connect/keys`
- **Returns**: JWKS for webhook signature verification

---

## OIDC Endpoints

### Get OIDC JWKS
```python
client.get_oidc_jwks()
```
- **Endpoint**: `GET /v1/oidc/jwks`

### Get User Info (OIDC)
```python
client.get_user_info_oidc()
```
- **Endpoint**: `GET /v1/oidc/userinfo`
- **Requires**: `openid` scope

---

## Rate Limits

| Operation Type | Limit |
|---------------|-------|
| List operations | 100 requests/user |
| Create/Update operations | 20-30 requests/user |
| Export operations | 20 requests/user |
| Import operations | 20 requests/minute |

---

## OAuth Endpoints (via requests, not client methods)

### Generate Access Token
```
POST /v1/oauth/token
```

### Introspect Token
```
POST /v1/oauth/introspect
```

### Revoke Token
```
POST /v1/oauth/revoke
```
