# Phase 3b: Content Hub / Assets Management

## Context Links

- [Plan Overview](./plan.md)
- [Phase 3: Marketing Skills](./phase-03-marketing-skills.md)
- [Research: Content Hub](../reports/researcher-20251209-content-hub-assets-management.md)
- [Source: ClaudeKit Marketing Overview](../../docs/overall/ClaudeKit-Marketing-Claude-Code-for-Sales-and-Marketing.md#L243-271)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 21-24, 2025 (parallel with Phase 3) |
| **Priority** | High |
| **Implementation Status** | ✅ DONE |
| **Review Status** | ✅ DONE |
| **Description** | Implement asset management system with brand guidelines + Imagen 4 integration |
| **Estimated Hours** | 28-36 hours |
| **Actual Hours** | ~18 hours (cloud/database deferred) |

---

## Architecture

### System Components

```
Content Hub System
├── Asset Storage (Local + Cloud)
│   ├── File system organization
│   ├── Cloudflare R2 integration
│   └── Google Drive sync (optional)
├── Brand Guidelines System
│   ├── Markdown-based guidelines
│   ├── Context injection hooks
│   └── Version management
├── Image Generation (Imagen 4)
│   ├── Marketing visual generation
│   ├── Image editing/refinement
│   └── Brand-aware prompting
├── Asset Metadata (PostgreSQL/SQLite)
│   ├── Asset registry
│   ├── Version history
│   └── Tagging/search
└── CLI Commands
    ├── /asset create|list|search|generate
    └── /brand guidelines|validate|inject
```

### Directory Structure

```
project-root/
├── .assets/                          # Git-tracked metadata
│   ├── manifest.json                 # Central asset registry
│   ├── versions/                     # Version history
│   │   └── {asset-id}/
│   │       ├── v1.json
│   │       └── changelog.md
│   ├── tags.json                     # Tagging system
│   └── metadata/                     # Asset metadata by type
│       ├── designs.json
│       ├── banners.json
│       ├── logos.json
│       └── videos.json
├── assets/                           # Raw files (.gitignore for large files)
│   ├── designs/
│   │   ├── campaigns/
│   │   ├── web/
│   │   └── print/
│   ├── banners/
│   │   ├── social-media/
│   │   ├── email-headers/
│   │   └── landing-pages/
│   ├── logos/
│   │   ├── full-horizontal/
│   │   ├── icon-only/
│   │   ├── monochrome/
│   │   └── variations/
│   ├── videos/
│   │   ├── ads/
│   │   ├── tutorials/
│   │   └── testimonials/
│   ├── infographics/
│   └── generated/                    # AI-generated assets
│       └── {timestamp}/
└── docs/
    └── brand-guidelines.md           # Central brand guidelines
```

---

## Skill

### Important
Use the existing `/skill:create <prompt>` slash command to create new skills.

### Structure
```
.claude/skills/brand-guidelines/
├── SKILL.md                          # Main skill definition
├── references/
│   ├── brand-guideline-template.md   # Template for creating guidelines
│   ├── voice-tone-guide.md           # Voice/tone documentation
│   ├── asset-organization.md         # Directory structure guide
│   ├── color-palette-management.md   # Color system documentation
│   ├── typography-specifications.md  # Font/sizing rules
│   ├── logo-usage-rules.md           # Logo guidelines
│   └── approval-checklist.md         # QA checklist
├── scripts/
│   ├── inject-brand-context.cjs      # Brand injection hook
│   ├── validate-asset.cjs            # Brand compliance checker
│   └── extract-colors.cjs            # Color palette extractor
└── templates/
    └── brand-guidelines-starter.md   # Starter template
```

---

## Brand Guidelines System

### 2.1 Document Format (Markdown)

**Location:** `docs/brand-guidelines.md`

**Required Sections:**

```markdown
# Brand Guidelines v{X.Y}

## Color Palette
### Primary Colors
- **Color Name:** #HEX (RGB: R, G, B)
  - Usage: {use cases}
  - Contrast Ratio: {ratio}:1

### Secondary Colors
### Neutral Palette

## Typography
### Font Stack
- Primary: {font-family}
- Body: {font-family}
- Monospace: {font-family}

### Sizing Scale
- H1: {size}px / {mobile-size}px
- H2-H6: {sizes}
- Body: {size}px
- Small/Caption: {sizes}

## Logo Usage
### Variants
- Horizontal full color
- Icon only
- Monochrome (dark/light)

### Rules
- Minimum size
- Clear space
- Don't do

## Voice & Tone
### Brand Personality
### Tone Guidelines
### Prohibited Terms

## Design System Components
### Buttons
### Spacing Scale
### Border Radius

## Approval Checklist
- [ ] Colors match palette
- [ ] Typography approved
- [ ] Logo placement correct
- [ ] Accessibility verified
```

### 2.2 Brand Context Injection

**Hook Implementation:** `.claude/hooks/brand-context-injector.cjs`

```javascript
// Runs before content generation commands
// Injects brand context into system prompt

module.exports = {
  event: 'pre:content',

  async handler(context) {
    const brandGuidelines = await loadBrandGuidelines();
    const extractedContext = extractBrandContext(brandGuidelines);

    return {
      systemPromptAddition: `
BRAND CONTEXT:
- Primary Color: ${extractedContext.colors.primary}
- Secondary Colors: ${extractedContext.colors.secondary.join(', ')}
- Font: ${extractedContext.typography.primary}
- Voice: ${extractedContext.voice.personality}
- Prohibited Terms: ${extractedContext.voice.prohibited.join(', ')}

Apply these brand guidelines to all generated content.
      `
    };
  }
};
```

### 2.3 Brand Validation

**Asset Validation Checklist:**

| Check | Method | Threshold |
|-------|--------|-----------|
| Color compliance | Extract colors, compare to palette | 80% match |
| Typography | Font detection (if embedded) | Exact match |
| Logo presence | Image recognition | Required for marketing |
| Contrast ratio | WCAG calculation | AA minimum (4.5:1) |
| File naming | Regex pattern match | 100% compliance |

---

## Imagen 4 Integration

### 3.1 API Specifications

| Model | Use Case | Cost | Speed |
|-------|----------|------|-------|
| imagen-4.0-fast-001 | Quick iterations | $0.02/image | Fast |
| imagen-4.0-generate-001 | Standard quality | $0.04/image | Medium |
| imagen-4.0-ultra-001 | High quality | $0.08/image | Slow |

### 3.2 Generation Capabilities

**Marketing Visual Types:**
- Banners (social media, email headers, landing pages)
- Product mockups
- Infographics (with Gemini text overlay)
- Background images
- Ad creatives
- Social media posts

**Prompt Template with Brand Injection:**

```
Create a professional marketing {asset_type} for {brand_name}:

Visual: {detailed_description}
Style: {brand_style} - {adjectives}
Mood: {mood}

BRAND REQUIREMENTS:
- Primary Color: {primary_color}
- Accent Color: {accent_color}
- Style: Professional, polished, {brand_adjectives}
- Target audience: {audience}

Technical: High quality, {aspect_ratio}, optimized for {platform}
Do not include: {prohibited_elements}
```

### 3.3 Image Editing Features

| Feature | Capability | Use Case |
|---------|-----------|----------|
| Inpainting | Modify specific regions | Logo replacement, text editing |
| Style transfer | Apply artistic styles | Brand consistency |
| Upscaling | Up to 17MP | Print-ready assets |
| Background removal | Subject isolation | Product photography |
| Color adjustment | Palette modification | Brand alignment |

---

## Database Schema

### Assets Table

```sql
CREATE TABLE assets (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT NOT NULL,  -- design|banner|logo|video|infographic
  description TEXT,
  file_path TEXT NOT NULL UNIQUE,
  file_size BIGINT,
  mime_type TEXT,

  -- Cloud storage
  r2_key TEXT,
  gdrive_id TEXT,

  -- Metadata
  width INTEGER,
  height INTEGER,
  duration_seconds DECIMAL,
  color_palette TEXT[],
  tags TEXT[],

  -- Versioning
  version INT DEFAULT 1,
  parent_asset_id TEXT REFERENCES assets(id),
  source_model TEXT,  -- imagen-4|user-upload|canva
  source_prompt TEXT,

  -- Lifecycle
  created_by TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  approved_by TEXT,
  approved_at TIMESTAMP,
  status TEXT DEFAULT 'draft',  -- draft|approved|archived

  -- Relationships
  campaign_id TEXT REFERENCES campaigns(id),
  brand_guideline_version INT,

  -- Search
  search_vector tsvector
);

-- Indexes
CREATE INDEX idx_assets_type ON assets(type);
CREATE INDEX idx_assets_status ON assets(status);
CREATE INDEX idx_assets_tags ON assets USING GIN(tags);
CREATE INDEX idx_assets_search ON assets USING GIN(search_vector);
```

### Brand Guidelines Table

```sql
CREATE TABLE brand_guidelines (
  version INT PRIMARY KEY,
  content TEXT NOT NULL,  -- markdown
  colors_json JSONB,      -- extracted color data
  typography_json JSONB,  -- extracted typography
  voice_json JSONB,       -- extracted voice/tone
  created_by TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  is_active BOOLEAN DEFAULT FALSE
);
```

### Asset Versions Table

```sql
CREATE TABLE asset_versions (
  id SERIAL PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES assets(id),
  version INT NOT NULL,
  file_path TEXT NOT NULL,
  r2_key TEXT,
  changes_summary TEXT,
  created_by TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(asset_id, version)
);
```

---

## Naming Conventions

### Asset File Naming

```
{type}_{campaign}_{description}_{timestamp}_{variant}.{ext}

Examples:
banner_claude-launch_hero-image_20251209_16-9.png
logo_brand-refresh_horizontal-full-color_20251209.svg
design_holiday-campaign_email-hero_20251209_dark-mode.psd
video_product-demo_feature-walkthrough_20251209.mp4
```

### Components

| Component | Format | Example |
|-----------|--------|---------|
| type | lowercase | banner, logo, design |
| campaign | kebab-case | claude-launch, q1-promo |
| description | kebab-case | hero-image, email-header |
| timestamp | YYYYMMDD | 20251209 |
| variant | kebab-case (optional) | dark-mode, 1x1, mobile |

---

## Cloud Storage Integration

### Cloudflare R2 Setup

**Benefits:**
- S3-compatible API
- No egress fees
- 10GB free storage/month
- Global CDN

**Configuration:**

```typescript
// .claude/skills/brand-guidelines/scripts/r2-client.cjs

const { S3Client, PutObjectCommand, GetObjectCommand } = require('@aws-sdk/client-s3');

const r2Client = new S3Client({
  region: 'auto',
  endpoint: `https://${process.env.R2_ACCOUNT_ID}.r2.cloudflarestorage.com`,
  credentials: {
    accessKeyId: process.env.R2_ACCESS_KEY_ID,
    secretAccessKey: process.env.R2_SECRET_ACCESS_KEY
  }
});

async function uploadAsset(filePath, key, metadata) {
  const command = new PutObjectCommand({
    Bucket: process.env.R2_BUCKET_NAME,
    Key: `assets/${key}`,
    Body: fs.readFileSync(filePath),
    Metadata: metadata
  });
  return r2Client.send(command);
}
```

### Google Drive Integration (Optional)

**Use Cases:**
- Collaborative review workflows
- Client access
- Backup storage

**MCP Server:** Use existing Google Drive MCP

---

## Commands (Phase 4)

### Asset Commands

```
/asset create [type] [name]
  Create new asset entry, open for upload

/asset list [type] [--campaign] [--status]
  List assets with filtering

/asset search [query]
  Full-text search across assets

/asset generate [type] [prompt]
  Generate new asset with Imagen 4

/asset edit [asset-id] [prompt]
  Edit existing asset (inpainting)

/asset approve [asset-id]
  Mark asset as approved

/asset version [asset-id]
  Create new version of asset

/asset export [asset-id] [format]
  Export asset for specific use

/asset sync [--r2] [--gdrive]
  Sync assets to cloud storage
```

### Brand Commands

```
/brand guidelines
  Display current brand guidelines

/brand validate [asset-path]
  Validate asset against brand guidelines

/brand context
  Show extracted brand context for injection

/brand colors
  Display color palette with usage

/brand version [new-version]
  Create new brand guidelines version

/brand compare [v1] [v2]
  Compare two guideline versions
```

---

## Implementation Steps

### Day 1: Core Infrastructure

1. Create skill directory structure
2. Write SKILL.md main definition
3. Create brand-guideline-template.md
4. Create asset-organization.md
5. Set up database schema (PostgreSQL/SQLite)

### Day 2: Brand System

6. Write voice-tone-guide.md
7. Write color-palette-management.md
8. Write typography-specifications.md
9. Implement inject-brand-context.cjs hook
10. Implement validate-asset.cjs script

### Day 3: Imagen 4 Integration

11. Create Imagen 4 client wrapper
12. Implement brand-aware prompt builder
13. Create generation templates
14. Implement image editing capabilities
15. Test generation pipeline

### Day 4: Storage & Polish

16. Implement R2 upload/download
17. Implement versioning system
18. Create approval workflow
19. Integration testing
20. Documentation updates

---

## Todo List

### Completed ✅
- [x] Create brand-guidelines skill directory
- [x] Write `SKILL.md` main definition
- [x] Create brand-guideline-template.md reference
- [x] Create voice-tone-guide.md reference
- [x] Create asset-organization.md reference
- [x] Create color-palette-management.md reference
- [x] Create typography-specifications.md reference
- [x] Create approval-checklist.md reference
- [x] Implement inject-brand-context.cjs script
- [x] Implement validate-asset.cjs script
- [x] Implement extract-colors.cjs script
- [x] Set up asset directory structure (.assets/ and assets/)
- [x] Create brand-guidelines-starter.md template
- [x] Update skill-catalog.md

### Deferred to Phase 4
- [ ] Set up database schema (using JSON manifests for now)
- [ ] Implement Imagen 4 client (via ai-multimodal skill)
- [ ] Implement R2 integration (cloud storage deferred)
- [ ] Automated test suite

---

## Success Criteria

1. Brand guidelines skill loads correctly
2. Brand context injects into content workflows
3. Asset validation identifies compliance issues
4. Imagen 4 generates brand-aligned visuals
5. Versioning tracks asset history
6. Cloud storage sync works reliably
7. CLI commands functional
8. Database queries performant

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Imagen 4 inconsistent | Medium | Medium | Multiple generations, selection |
| Brand extraction accuracy | Medium | Medium | Manual review, structured markdown |
| Storage cost overrun | Low | Low | R2 free tier, monitoring |
| Database migration | Low | Medium | Schema versioning |
| Color compliance detection | Medium | Low | Tolerance thresholds |

---

## Security Considerations

- Store API keys in environment variables
- R2 credentials never committed
- Signed URLs for cloud access (expiring)
- Asset approval before publishing
- Audit logging for changes
- PII handling in metadata

---

## Cost Estimation

| Component | Cost |
|-----------|------|
| Imagen 4 (100 images/month) | $2-8 |
| Cloudflare R2 (10GB) | Free |
| PostgreSQL (hosted) | $5-15/month |
| Google Drive | Free (15GB) |
| **Total/month** | **$7-23** |

---

## Integration Points

### Campaign System

- Assets linked to campaigns via `campaign_id`
- Campaign dashboard shows asset status
- Approval workflow integrated

### Content Creation

- Brand context auto-injected
- Generated assets stored automatically
- Versioning for iterations

### Analytics

- Asset usage tracking
- Performance by asset type
- A/B test results storage

---

## Next Steps

After Phase 3b completion:
1. Create /asset and /brand commands in Phase 4
2. Integrate with campaign workflows
3. Add Canva MCP for advanced editing
4. Build web UI for asset browsing (future)

---

## Unresolved Questions

1. Web UI requirements for asset management?
2. Real-time collaboration needs?
3. Watermarking strategy for drafts?
4. Multi-tenant support (multiple brands)?
5. Image format optimization (WebP, AVIF)?
6. Version retention policy (how many versions to keep)?
