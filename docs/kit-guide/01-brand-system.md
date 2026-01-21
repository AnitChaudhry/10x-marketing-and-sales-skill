# Brand System & Guidelines

## Overview

The brand-guidelines skill manages brand identity, voice, messaging, and asset management. All marketing content is validated against your brand standards.

## Commands

### `/brand`
Brand management commands: `/brand:update`, `/brand:audit` (future)

### `/brand:update`

Update brand identity and automatically sync to all design system files.

**Usage:**
```bash
# Interactive mode
/brand:update

# With theme hint
/brand:update "Ocean Professional"

# Quick preset
/brand:update "midnight purple"
```

**What it does:**
- Collects brand input (theme name, colors, mood keywords)
- Updates `docs/brand-guidelines.md` with new identity
- Syncs changes to `assets/design-tokens.json` (token definitions)
- Regenerates `assets/design-tokens.css` (CSS variables)
- Verifies all files are synchronized

**Workflow:**

1. **Gather Input** - Interactive prompts for:
   - Theme name (e.g., "Ocean Professional", "Electric Creative")
   - Primary color name & hex code (e.g., "Ocean Blue", #3B82F6)
   - Secondary color name & hex code (e.g., "Golden Amber", #F59E0B)
   - Accent color name & hex code (e.g., "Emerald", #10B981)
   - Brand mood keywords (e.g., "professional, trustworthy, premium")

2. **Update Brand Guidelines** - Modifies `docs/brand-guidelines.md`:
   - Quick Reference color table
   - Brand Concept section with theme name
   - Color Palette section (Primary, Secondary, Accent with shades)
   - AI Image Generation prompts & keywords

3. **Sync to Design Tokens** - Runs `sync-brand-to-tokens.cjs`:
   ```bash
   node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs
   ```
   - Updates `assets/design-tokens.json` with color names/values
   - Regenerates `assets/design-tokens.css` with CSS variables

4. **Verify Sync** - Confirmation checks:
   ```bash
   # Extract brand context as JSON
   node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs --json

   # Verify CSS variables exist
   grep "primary" assets/design-tokens.css
   ```

**The sync-brand-to-tokens.cjs Script**

**Location:** `.claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs`

**Purpose:** Synchronizes changes from `docs/brand-guidelines.md` to design token files.

**What it syncs:**
- Color names and hex codes
- Color shade variations
- Typography settings
- Brand mood/keywords for AI generation

**Input:** Parses `docs/brand-guidelines.md`
**Output:**
- `assets/design-tokens.json` (structured token definitions)
- `assets/design-tokens.css` (CSS custom properties/variables)

**Run manually:**
```bash
node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs
```

**Example Usage**

**Scenario 1: Interactive Update**
```bash
/brand:update
# Prompts:
# → Theme name? "Sunset Warm"
# → Primary color? "Orange" #F97316
# → Secondary color? "Red" #DC2626
# → Accent color? "Yellow" #FACC15
# → Brand mood? "energetic, warm, inspiring"
#
# Updates brand-guidelines.md, syncs to tokens
# Output: Theme updated to Sunset Warm
```

**Scenario 2: Quick Preset**
```bash
/brand:update "ocean-professional"
# Uses preset values:
# Primary: #3B82F6 Ocean Blue
# Secondary: #F59E0B Golden Amber
# Accent: #10B981 Emerald
#
# Syncs immediately, confirms: "Ocean Professional applied"
```

**Preset Options**
| Preset | Primary | Secondary | Accent |
|--------|---------|-----------|--------|
| ocean-professional | #3B82F6 Ocean Blue | #F59E0B Golden Amber | #10B981 Emerald |
| electric-creative | #FF6B6B Coral | #9B5DE5 Electric Purple | #00F5D4 Neon Mint |
| forest-calm | #059669 Forest Green | #92400E Warm Brown | #FBBF24 Sunlight |
| midnight-purple | #7C3AED Violet | #EC4899 Pink | #06B6D4 Cyan |
| sunset-warm | #F97316 Orange | #DC2626 Red | #FACC15 Yellow |

## Skill: brand-guidelines

**Location:** `.claude/skills/brand-guidelines/`

### When to Use
- Establish brand voice and tone
- Define visual identity (logos, colors, fonts)
- Create messaging frameworks
- Ensure brand consistency across content
- Manage and organize marketing assets
- Validate brand compliance

### Quick Start

**Inject brand context into prompts:**
```bash
# Shell/Bash
node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs

# JSON output for scripting
node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs --json
```

**Validate an asset:**
```bash
# Check naming, size, format compliance
node .claude/skills/brand-guidelines/scripts/validate-asset.cjs <asset-path>

# JSON output
node .claude/skills/brand-guidelines/scripts/validate-asset.cjs <asset-path> --json
```

**Extract and compare colors:**
```bash
# Show palette from brand guidelines
node .claude/skills/brand-guidelines/scripts/extract-colors.cjs --palette

# Extract colors from an image
node .claude/skills/brand-guidelines/scripts/extract-colors.cjs <image-path>
```

**Sync brand to design tokens:**
```bash
# Update docs/brand-guidelines.md, then sync to token files
node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs
```

## Brand Files Structure

### Source of Truth
- **`docs/brand-guidelines.md`** - Main brand document (human-readable)
  - Brand voice & tone
  - Visual identity guidelines
  - Messaging framework
  - Color palette
  - Typography specifications
  - Logo usage rules
  - Asset organization

### Synced Output
- **`assets/design-tokens.json`** - Token definitions (auto-synced from brand doc)
- **`assets/design-tokens.css`** - CSS variables (auto-synced)
- **`.assets/manifest.json`** - Central asset registry
- **`.assets/tags.json`** - Asset tagging system
- **`.assets/metadata/`** - Type-specific metadata
- **`.assets/versions/`** - Version history

## Brand Components

### Voice Dimensions
Define your brand voice on these spectrums:
- **Tone:** Formal ↔ Casual
- **Language:** Simple ↔ Complex
- **Character:** Serious ↔ Playful
- **Emotion:** Reserved ↔ Expressive

### Visual Elements
Document these visual assets:
- **Logo:** Primary, secondary, icon variants
- **Colors:** Primary, secondary, accent (with hex/RGB)
- **Typography:** Header fonts, body fonts, sizes
- **Imagery Style:** Photography, illustration, pattern styles

## Asset Directory Structure

```
.assets/                    # Git-tracked metadata
├── manifest.json          # Asset registry
├── tags.json             # Tagging system
├── versions/             # Version history
└── metadata/             # Type-specific metadata

assets/                    # Raw files
├── designs/              # Campaign, web, print designs
├── banners/              # Social, email, landing page banners
├── logos/                # Full logos, icons, monochrome
├── videos/               # Ads, tutorials, testimonials
├── infographics/
├── photos/
└── generated/            # AI-generated (timestamped)
```

## Asset Naming Convention

```
{type}_{campaign}_{description}_{timestamp}_{variant}.{ext}

Examples:
- banner_claude-launch_hero-image_20251209_16-9.png
- logo_brand-refresh_horizontal_20251209.svg
- email_promo_call-to-action_20251209_mobile.png
- social_product-launch_instagram-reel_20251209_square.mp4
```

Breaking down: `banner_claude-launch_hero-image_20251209_16-9.png`
- **type:** banner
- **campaign:** claude-launch
- **description:** hero-image
- **timestamp:** 20251209 (YYYYMMDD)
- **variant:** 16-9 (aspect ratio)
- **ext:** png

## Brand Sync Workflow

When updating brand identity, always sync all files:

1. **Edit source document**
   ```bash
   # Update your brand guidelines
   vim docs/brand-guidelines.md
   ```

2. **Sync to design tokens**
   ```bash
   node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs
   ```

3. **Verify sync succeeded**
   ```bash
   node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs --json | head -20
   ```

**Files auto-synced:**
- `docs/brand-guidelines.md` → Source
- `assets/design-tokens.json` → Token definitions
- `assets/design-tokens.css` → CSS variables

## Reference Templates

The skill includes reference guides:

| Topic | File | Purpose |
|-------|------|---------|
| Voice Framework | `references/voice-framework.md` | Brand voice development & testing |
| Visual Identity | `references/visual-identity.md` | Core visual elements |
| Messaging | `references/messaging-framework.md` | Value props & messaging |
| Consistency | `references/consistency-checklist.md` | Audit checklist |
| Guidelines Template | `references/brand-guideline-template.md` | Comprehensive starter |
| Asset Organization | `references/asset-organization.md` | Directory & naming |
| Color Management | `references/color-palette-management.md` | Color systems |
| Typography | `references/typography-specifications.md` | Fonts & scales |
| Logo Usage | `references/logo-usage-rules.md` | Logo variants & placement |
| Approval Checklist | `references/approval-checklist.md` | Review process |

## Brand Consistency Workflow

### Asset Approval Process
1. Create asset following naming convention
2. Run `validate-asset.cjs` for compliance check
3. Extract colors, compare to palette
4. Complete approval checklist
5. Register in `.assets/manifest.json`

### Brand Audit (Quarterly)
1. Collect all marketing materials
2. Assess consistency across channels
3. Identify gaps and misalignments
4. Prioritize fixes
5. Update `docs/brand-guidelines.md`

## Voice Examples

When defining voice, provide examples:

**Do's:**
- [List 3-5 good example phrases/content]

**Don'ts:**
- [List 3-5 things to avoid]

**Example Use Cases:**
- Email subject line: "..."
- Social post: "..."
- Product description: "..."

## Integration with Content Creation

When using content commands (e.g., `/content:good`):

1. Brand context auto-injected via `inject-brand-context.cjs`
2. Content reviewed for brand compliance
3. Colors/typography verified against palette
4. Voice tone checked against messaging framework

## Best Practices

1. **Consistency > Perfection** - Apply voice consistently, not perfectly
2. **Voice Adapts** - Tone shifts by context, personality stays constant
3. **Show Examples** - Provide sample content, not just rules
4. **Evolve Guidelines** - Update as brand grows
5. **Audit Quarterly** - Regular consistency checks
6. **Register All Assets** - Maintain manifest.json
7. **Use Conventions Strictly** - Standard naming prevents chaos

## Troubleshooting

**Scripts not working?**
- Ensure `docs/brand-guidelines.md` exists
- Check Node.js version compatibility
- Verify `.claude/skills/brand-guidelines/scripts/` path

**Colors not matching?**
- Export images as PNG for accurate extraction
- Verify color format in `docs/brand-guidelines.md`
- Run `validate-asset.cjs` to identify format issues

**Brand context not injecting?**
- Check `docs/brand-guidelines.md` format
- Run with `--json` flag to debug output
- Verify file exists at expected path

## Next Steps

1. Create/update `docs/brand-guidelines.md` with your brand
2. Run brand sync scripts to generate tokens
3. Use `/content:good` and verify brand context appears
4. Set up asset organization in `assets/` with naming convention
5. Run quarterly audits to maintain consistency
