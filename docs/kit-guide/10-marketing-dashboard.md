# Marketing Dashboard - Skill Guide

**Status:** Foundation Phase (Phase 1 Complete)
**Type:** Mini App (Vue 3 + Hono)
**Path:** `.claude/skills/marketing-dashboard/`

## Overview

Local-first marketing command center for solopreneurs. Unified dashboard to manage campaigns, assets, brand identity, and AI automation recipes with Claude Code.

**Architecture:**
- Frontend: Vue 3 + Vite + Tailwind CSS (localhost:5173)
- Backend: Hono (Node.js) + SQLite (localhost:3457)
- Database: better-sqlite3 with schema for campaigns, content, assets, automations

## Quick Start

### Development Mode (Two Terminals Required)

**Terminal 1 - API Server:**
```bash
cd .claude/skills/marketing-dashboard/server
npm install  # First time only
npm run dev
```
Output: `Server: http://localhost:3457`

**Terminal 2 - Vue Frontend:**
```bash
cd .claude/skills/marketing-dashboard/app
npm install  # First time only
npm run dev
```
Output: `http://localhost:5173` (auto-opens in browser)

### Production Mode

```bash
# Build frontend
cd .claude/skills/marketing-dashboard/app
npm run build

# Start server (serves API + built frontend)
cd ../server
npm start
```
Server runs at `http://localhost:3457` with combined API + static assets.

## Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Frontend | Vue 3 | ^3.5.24 |
| Build Tool | Vite | ^7.2.4 |
| Styling | Tailwind CSS + PostCSS | ^4.1.18 |
| Backend Framework | Hono | ^4.0.0 |
| Node Runtime | @hono/node-server | ^1.8.0 |
| Database | SQLite (better-sqlite3) | ^9.4.0 |
| State Management | Pinia | ^3.0.4 |
| Routing | Vue Router | ^4.6.4 |
| Testing | Vitest | ^4.0.16 |

## URLs

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend App | `http://localhost:5173` | Vue dashboard UI |
| API Server | `http://localhost:3457` | REST API endpoints |
| Health Check | `http://localhost:3457/health` | Server status (JSON) |
| Logos (Static) | `http://localhost:3457/static/logos/*` | Logo file serving |

## Features

### Brand Center (BrandView.vue)

Manage visual design system and brand guidelines. Displays:

**Sub-Components:**
- **ColorPalette** - Design token colors from `design-tokens.json`
- **TypographyPreview** - Font families, weights, sizes from tokens
- **SpacingScale** - Margin/padding token scale visualization
- **ComponentShowcase** - Pre-built UI component examples with token styling
- **LogoGallery** - Browsable logo collection with upload capability
- **VoiceSummary** - Brand voice/messaging guidelines parsed from `docs/brand-guidelines.md`

**Data Flow:**
1. Vue mounts → `brandStore.fetchAll()`
2. Store requests: `/api/brand/tokens`, `/api/brand/voice`, `/api/brand/logos`
3. Components render token data + logos + brand voice

### Asset Management

File browser + scanner integration. Browse, filter, and manage marketing assets (images, documents, videos).

**Capabilities:**
- Live asset scanning from `assets/` folder
- Database persistence with metadata (category, format, size, upload status)
- Asset content preview for text files (max 10MB)
- Safe file serving with path traversal prevention

### Logo Management

**Upload:** POST `/api/brand/logos` with form-data file
**Restrictions:**
- Types: PNG, JPG, SVG, WebP only
- Max size: 5MB
- Filename sanitization (removes path separators, dangerous chars)
- Stored in: `assets/logos/`

**Browse:** GET `/api/brand/logos` lists all logos with metadata + serving URL

## API Endpoints

### Brand Routes (`/api/brand`)

#### GET `/api/brand/tokens`
Returns design tokens from `assets/design-tokens.json`

**Response (200):**
```json
{
  "colors": { "primary": "#3B82F6", ... },
  "typography": { "fontFamily": {...}, "fontSize": {...} },
  "spacing": { "1": "0.25rem", ... }
}
```

**Error (404):** Design tokens file not found

---

#### GET `/api/brand/voice`
Parses brand guidelines via `inject-brand-context.cjs` script
Reads: `docs/brand-guidelines.md`

**Response (200):**
```json
{
  "tone": "Professional, approachable",
  "messaging": ["Core value 1", "Core value 2"],
  "guidelines": "..."
}
```

**Error (404):** Script or guidelines file not found
**Error (500):** Script execution failed

---

#### GET `/api/brand/logos`
Lists all logos from `assets/logos/` recursively

**Response (200):**
```json
[
  {
    "name": "logo.svg",
    "path": "logo.svg",
    "category": ".",
    "url": "http://localhost:3457/static/logos/logo.svg"
  },
  {
    "name": "icon.png",
    "path": "variants/icon.png",
    "category": "variants",
    "url": "http://localhost:3457/static/logos/variants/icon.png"
  }
]
```

**Response (200 - Empty):** `[]` (creates dir if missing)

---

#### POST `/api/brand/logos`
Upload new logo file

**Request:** multipart/form-data with `file` field

**Validation:**
- MIME type: image/png, image/jpeg, image/svg+xml, image/webp
- Max size: 5MB
- Filename: alphanumeric + underscore/dash/dot only

**Response (200):**
```json
{
  "success": true,
  "name": "my_logo.svg",
  "path": "my_logo.svg"
}
```

**Error (400):** Invalid type, too large, bad filename
**Error (500):** Upload failed

---

### Assets Routes (`/api/assets`)

#### GET `/api/assets`
List assets from database + live folder scan

**Response (200):**
```json
{
  "assets": [
    {
      "id": "uuid",
      "path": "images/banner.png",
      "name": "banner.png",
      "category": "images",
      "format": "png",
      "formatType": "image",
      "size": 102400,
      "modified_at": "2025-12-24T10:30:00Z",
      "ai_prompt": null,
      "r2_status": null,
      "r2_url": null
    }
  ],
  "total": 5,
  "fromDatabase": 3,
  "fromScan": 2
}
```

---

#### GET `/api/assets/:id`
Fetch single asset by ID

**Response (200):**
```json
{
  "asset": { /* asset object */ }
}
```

**Error (404):** Asset not found

---

#### POST `/api/assets/scan`
Rescan `assets/` folder and sync database

**Response (200):**
```json
{
  "success": true,
  "scanned": 10,
  "inserted": 2,
  "updated": 3,
  "message": "Scanned 10 assets: 2 new, 3 updated"
}
```

---

#### PUT `/api/assets/:id`
Update asset metadata (AI prompt, R2 status/URL)

**Request Body:**
```json
{
  "ai_prompt": "Create marketing banner for product X",
  "r2_status": "uploaded",
  "r2_url": "https://cdn.example.com/asset.png"
}
```

**Response (200):** Updated asset object

**Error (404):** Asset not found

---

#### GET `/api/assets/:id/content`
Get raw file content (text files only, max 10MB)

**Response (200):**
```json
{
  "content": "file contents as string",
  "format": "md",
  "size": 1024
}
```

**Error (403):** Path traversal detected, access denied
**Error (404):** File not found
**Error (413):** File too large (>10MB)

---

#### GET `/api/assets/file/*`
Serve asset files directly with path traversal security

**Path Format:** `/api/assets/file/path/to/asset.png`

**Security Checks:**
1. URL decode validation
2. Backslash normalization (Windows)
3. Absolute path blocking
4. Parent directory (`..`) blocking
5. Path resolution within `assets/` only
6. Boundary check before file read

**Response (200):** File binary content
**Error (403):** Access denied (path traversal)
**Error (404):** File not found

---

## Database Schema

Initialized by `server/db/database.js` (better-sqlite3)

**Tables:**

### assets
```sql
CREATE TABLE assets (
  id TEXT PRIMARY KEY,
  path TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  category TEXT,
  format TEXT,
  format_type TEXT,
  size INTEGER,
  modified_at TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  ai_prompt TEXT,
  r2_status TEXT,
  r2_url TEXT
)
```

### campaigns
```sql
CREATE TABLE campaigns (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  status TEXT DEFAULT 'draft',
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT DEFAULT CURRENT_TIMESTAMP
)
```

### content
```sql
CREATE TABLE content (
  id TEXT PRIMARY KEY,
  campaign_id TEXT,
  type TEXT,
  title TEXT NOT NULL,
  body TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
)
```

### automations
```sql
CREATE TABLE automations (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  trigger TEXT,
  action TEXT,
  enabled BOOLEAN DEFAULT true,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
```

Foreign key enforcement: Enabled (`PRAGMA foreign_keys = ON`)

## Frontend Structure

```
app/src/
├── views/
│   ├── BrandView.vue       ← Brand Center (main dashboard)
│   └── ...
├── components/
│   ├── brand/
│   │   ├── ColorPalette.vue
│   │   ├── TypographyPreview.vue
│   │   ├── SpacingScale.vue
│   │   ├── ComponentShowcase.vue
│   │   ├── LogoGallery.vue
│   │   └── VoiceSummary.vue
│   └── ...
├── stores/
│   ├── brand.js            ← Pinia store (API integration)
│   └── ...
├── App.vue
└── main.js
```

### Brand Store (Pinia)

**State:**
- `tokens` - Design tokens from `/api/brand/tokens`
- `logos` - Logo list from `/api/brand/logos`
- `voice` - Brand voice from `/api/brand/voice`
- `loading` - Request status
- `error` - Error message if any

**Actions:**
- `fetchAll()` - Load tokens + logos + voice in parallel
- `uploadLogo(file)` - POST to `/api/brand/logos`

## Security

### File Upload (Logo)
- Whitelist MIME types (PNG, JPG, SVG, WebP)
- Enforce max size (5MB)
- Sanitize filenames (remove path separators, parent refs, non-alphanumeric)
- Store in safe directory (`assets/logos/`)

### File Serving (Assets)
- URL decode validation
- Backslash normalization (cross-platform)
- Absolute path rejection
- Parent directory (`..`) rejection
- Boundary check: file must be within `assets/` directory
- Safe file read with size limit (10MB for preview)

### API
- CORS restricted to localhost:5173 (configurable via `ALLOWED_ORIGINS` env var)
- No authentication required for local development (commented out in index.js)
- Error handling: development mode shows error details, production hides them

## Environment Variables

**Server (`.claude/skills/marketing-dashboard/server`):**

```bash
PORT=3457                                    # API server port
ALLOWED_ORIGINS=http://localhost:5173       # CORS allowed origins (comma-separated)
NODE_ENV=development                        # development or production
API_BASE_URL=http://localhost:3457          # For logo URLs (brand.js)
```

## Development Commands

**Server:**
```bash
npm run dev          # Watch mode (auto-restart on changes)
npm start            # Production mode
npm test             # Run tests
npm test:watch       # Test watch mode
npm test:ui          # Test UI dashboard
```

**Frontend:**
```bash
npm run dev          # Dev server with HMR
npm run build        # Production build → dist/
npm run preview      # Preview built app locally
```

## File Paths

All paths relative to project root (`/Applications/MAMP/htdocs/claudekit-marketing/claudekit-marketing/`):

| Path | Purpose |
|------|---------|
| `.claude/skills/marketing-dashboard/` | Skill root |
| `.claude/skills/marketing-dashboard/server/` | Hono API |
| `.claude/skills/marketing-dashboard/app/` | Vue frontend |
| `.claude/skills/marketing-dashboard/server/db/` | Database module |
| `.claude/skills/marketing-dashboard/server/routes/` | API routes |
| `.claude/skills/marketing-dashboard/server/middleware/` | Auth + middleware |
| `.claude/skills/marketing-dashboard/app/src/views/` | Vue page components |
| `.claude/skills/marketing-dashboard/app/src/components/` | Vue UI components |
| `.claude/skills/marketing-dashboard/app/src/stores/` | Pinia state stores |
| `assets/design-tokens.json` | Design token data (read by `/api/brand/tokens`) |
| `assets/logos/` | Logo storage (read/write by `/api/brand/logos`) |
| `docs/brand-guidelines.md` | Brand voice guidelines (read by `/api/brand/voice`) |

## Health Check

```bash
curl http://localhost:3457/health
```

**Response (200):**
```json
{
  "status": "ok",
  "timestamp": "2025-12-24T16:30:00.000Z",
  "environment": "development"
}
```

## Troubleshooting

**Issue:** Frontend can't connect to API
**Fix:** Ensure server running on 3457, check CORS in `ALLOWED_ORIGINS`

**Issue:** Logo upload fails
**Fix:** Check file type (PNG/JPG/SVG/WebP), size (<5MB), filename has valid chars

**Issue:** Design tokens not loading
**Fix:** Verify `assets/design-tokens.json` exists and is valid JSON

**Issue:** Brand voice returns 404
**Fix:** Ensure `docs/brand-guidelines.md` exists; check brand-guidelines script path

**Issue:** Database locked error
**Fix:** Restart server (kill process, `npm run dev` again)

## Next Phases

- **Phase 2:** Full CRUD API routes (campaigns, content, automations)
- **Phase 3:** Additional Vue components + stores for campaigns/content
- **Phase 4:** Dashboard features (charts, filters, bulk actions)
- **Phase 5:** Integration with Claude Code AI automation + deployment options
