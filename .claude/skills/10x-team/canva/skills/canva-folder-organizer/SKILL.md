---
name: canva-folder-organizer
description: |
  Organize and manage folders in your Canva account. Use this skill when user wants to
  create folders, move designs between folders, rename folders, or organize their
  Canva project structure. Follows 3-mode workflow to prevent accidental moves or deletions.
  For viewing folder contents use canva-explorer first.
---

# Canva Folder Organizer

Manage and organize your Canva folder structure and move items between folders.

---

## Capabilities

1. **Create Folders** - Create new folders and subfolders
2. **Rename Folders** - Update folder names
3. **Delete Folders** - Remove folders (moves to trash)
4. **Get Folder Info** - View folder details
5. **List Contents** - View items in a folder
6. **Move Items** - Move designs and assets between folders

---

## Folder Structure

```
Canva Account
├── Projects (root)
│   ├── Folder 1
│   │   ├── Subfolder A
│   │   └── Subfolder B
│   └── Folder 2
├── Uploads (uploads)
│   └── [Uploaded assets]
└── Trash
    └── [Deleted items]
```

### Special Folder IDs
- `root` - Top level Projects folder
- `uploads` - User's Uploads folder

---

## Available Scripts

### Create Folder
```bash
# Create folder at root
.venv\Scripts\python.exe scripts/create_folder.py "Marketing"

# Create subfolder
.venv\Scripts\python.exe scripts/create_folder.py "Q1 Campaign" --parent "folder_id"

# JSON output
.venv\Scripts\python.exe scripts/create_folder.py "New Folder" --json
```

### Get Folder Info
```bash
# Get folder details
.venv\Scripts\python.exe scripts/get_folder.py "folder_id"

# Get root folder
.venv\Scripts\python.exe scripts/get_folder.py "root"

# JSON output
.venv\Scripts\python.exe scripts/get_folder.py "folder_id" --json
```

### List Folder Contents
```bash
# List all items in folder
.venv\Scripts\python.exe scripts/list_folder_contents.py "folder_id"

# Filter by type
.venv\Scripts\python.exe scripts/list_folder_contents.py "folder_id" --type design
.venv\Scripts\python.exe scripts/list_folder_contents.py "folder_id" --type folder
.venv\Scripts\python.exe scripts/list_folder_contents.py "folder_id" --type image

# Sort options
.venv\Scripts\python.exe scripts/list_folder_contents.py "folder_id" --sort modified_descending
.venv\Scripts\python.exe scripts/list_folder_contents.py "folder_id" --sort name_ascending

# Limit results
.venv\Scripts\python.exe scripts/list_folder_contents.py "folder_id" --limit 20

# JSON output
.venv\Scripts\python.exe scripts/list_folder_contents.py "folder_id" --json
```

### Rename Folder
```bash
# Rename folder
.venv\Scripts\python.exe scripts/update_folder.py "folder_id" "New Name"

# JSON output
.venv\Scripts\python.exe scripts/update_folder.py "folder_id" "New Name" --json
```

### Delete Folder
```bash
# Delete folder (moves to trash)
.venv\Scripts\python.exe scripts/delete_folder.py "folder_id"

# Force confirm
.venv\Scripts\python.exe scripts/delete_folder.py "folder_id" --confirm

# JSON output
.venv\Scripts\python.exe scripts/delete_folder.py "folder_id" --json
```

### Move Items
```bash
# Move single item
.venv\Scripts\python.exe scripts/move_items.py --items "item_id" --to "target_folder_id"

# Move multiple items
.venv\Scripts\python.exe scripts/move_items.py --items "id1" "id2" "id3" --to "target_folder_id"

# JSON output
.venv\Scripts\python.exe scripts/move_items.py --items "id1" "id2" --to "folder_id" --json
```

---

## 3-Mode Workflow

### MODE 1: PLAN
1. Map current folder structure
2. Identify items to organize
3. Determine target folders

### MODE 2: CLARIFY
Ask user:
- Where should the new folder be created?
- Which items should be moved?
- Confirm delete operations

### MODE 3: IMPLEMENT
```bash
# Create folder structure
.venv\Scripts\python.exe scripts/create_folder.py "2024"
.venv\Scripts\python.exe scripts/create_folder.py "Q1" --parent "folder_2024_id"
.venv\Scripts\python.exe scripts/create_folder.py "Q2" --parent "folder_2024_id"

# Move items
.venv\Scripts\python.exe scripts/move_items.py --items "design1" "design2" --to "folder_q1_id"
```

---

## Organization Strategies

### By Project
```
Projects/
├── Project Alpha/
│   ├── Designs/
│   └── Assets/
├── Project Beta/
│   ├── Designs/
│   └── Assets/
```

### By Date
```
Projects/
├── 2024/
│   ├── Q1/
│   ├── Q2/
│   ├── Q3/
│   └── Q4/
└── Archive/
```

### By Type
```
Projects/
├── Social Media/
│   ├── Instagram/
│   ├── Facebook/
│   └── LinkedIn/
├── Presentations/
├── Marketing/
└── Brand Assets/
```

### By Client
```
Projects/
├── Client A/
│   ├── Active/
│   └── Completed/
├── Client B/
└── Internal/
```

---

## Sort Options

| Option | Description |
|--------|-------------|
| `modified_descending` | Newest modified first |
| `modified_ascending` | Oldest modified first |
| `name_descending` | Z-A alphabetical |
| `name_ascending` | A-Z alphabetical |

---

## Item Types

| Type | Description |
|------|-------------|
| `design` | Canva designs |
| `folder` | Subfolders |
| `image` | Uploaded images |

---

## Rate Limits

| Operation | Limit |
|-----------|-------|
| Create folder | 20-30 requests/user |
| Update folder | 20-30 requests/user |
| Delete folder | 20-30 requests/user |
| List items | 100 requests/user |
| Move items | 20-30 requests/user |

---

## Error Handling

### Folder Not Found
```
Error: 404 - Folder does not exist
```
**Solution**: Verify folder ID

### Permission Denied
```
Error: 403 - Cannot modify this folder
```
**Solution**: Check folder ownership

### Item Not Found
```
Error: Item not found for move operation
```
**Solution**: Verify item IDs

---

## Safety Notes

1. **Deleted folders go to Trash** - Recoverable for 30 days
2. **Preview before bulk moves** - Verify items are correct
3. **Empty folders** - Can be deleted safely
4. **Shared folders** - May have restrictions

---

## Integration

Works with:
- **canva-explorer**: View folder contents first
- **canva-design**: Get design IDs to move
- **canva-asset-manager**: Organize uploaded assets
