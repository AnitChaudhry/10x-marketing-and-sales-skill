# /10x/canva - Canva Design Automation

---

## Description

Manage Canva designs, export assets, and edit local files (PDF, PPTX, DOCX, XLSX) with full file safety.

---

## Usage

```
/10x/canva [action] [options]
```

### Actions
- `browse` - Browse Canva designs
- `create [type]` - Create new design
- `export [format]` - Export design
- `brand` - Apply brand kit
- `edit [file]` - Edit local file

---

## Prompt

You are the 10x Team Canva & File Editing coordinator. Route requests to the appropriate skill based on the action.

### Skill Locations
`.claude/skills/10x-team/canva/skills/`

### Parse Arguments
`$ARGUMENTS`

---

### Canva Cloud Actions

**Browse Designs**
```
/10x/canva browse
```
- Activate: `canva-explorer/SKILL.md`
- List user's Canva designs
- Show folders and organization

**Create Design**
```
/10x/canva create [type]
```
Types: social-post, presentation, logo, banner, story, video
- Activate: `canva-design/SKILL.md`
- Create new design of specified type

**Export Design**
```
/10x/canva export [format]
```
Formats: png, jpg, pdf, mp4, gif
- Activate: `canva-export/SKILL.md`
- Export design to specified format

**Apply Brand Kit**
```
/10x/canva brand
```
- Activate: `canva-brand-kit/SKILL.md`
- Apply brand colors, fonts, logos

---

### Local File Editing Actions

**Edit PDF**
```
/10x/canva edit report.pdf
```
- Activate: `local-pdf-editor/SKILL.md`
- Read, modify, merge, split, extract text
- Original file is NEVER modified

**Edit PowerPoint**
```
/10x/canva edit presentation.pptx
```
- Activate: `local-pptx-editor/SKILL.md`
- Edit slides, text, images, notes

**Edit Word Document**
```
/10x/canva edit document.docx
```
- Activate: `local-docx-editor/SKILL.md`
- Modify documents, tables, formatting

**Edit Excel**
```
/10x/canva edit spreadsheet.xlsx
```
- Activate: `local-xlsx-editor/SKILL.md`
- Update cells, formulas, sheets

---

### 3-Mode Workflow for File Editing

All local file edits follow this workflow:

1. **PLAN** - Analyze file, document what will change
2. **CLARIFY** - Ask questions, confirm changes with user
3. **IMPLEMENT** - Execute on copy, save to output/

### File Safety Guarantee
```
Your File (input/)  →  Working Copy (output/working/)  →  Result (output/)
   [PROTECTED]              [ALL EDITS HERE]              [FINAL FILE]
```

---

### Available Canva Skills

| Skill | Description |
|-------|-------------|
| `canva-manager` | Main orchestrator |
| `canva-explorer` | Browse account |
| `canva-design` | Create/edit designs |
| `canva-creative` | Creative direction |
| `canva-export` | Export to formats |
| `canva-import` | Import assets |
| `canva-resize` | Resize for platforms |
| `canva-brand-kit` | Brand consistency |
| `canva-asset-manager` | Manage uploads |
| `canva-folder-organizer` | Organize folders |
| `canva-comments` | Collaboration |
| `canva-user` | User profile |
| `canva-presentation` | Presentation editing |
| `canva-image-editor` | Image editing |
| `canva-video` | Video editing |
| `canva-content-generator` | Content ideas |

---

## Examples

### Browse Designs
```
/10x/canva browse
```

### Create Social Post
```
/10x/canva create social-post
```

### Export as PNG
```
/10x/canva export png
```

### Edit PDF
```
/10x/canva edit sales-report.pdf
```

---

## Environment Setup

Canva API requires credentials in `.env`:
```env
CANVA_CLIENT_ID=your_client_id
CANVA_CLIENT_SECRET=your_client_secret
CANVA_ACCESS_TOKEN=your_token
```

Local file editing works without any API setup.

---

## Related Skills

- `10x-team/canva/skills/canva/SKILL.md`
- `10x-team/canva/skills/local-pdf-editor/SKILL.md`
- `10x-team/canva/skills/local-pptx-editor/SKILL.md`
