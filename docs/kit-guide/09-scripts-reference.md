# Scripts Reference & Utility Tools

## Overview

ClaudeKit includes utility scripts for brand management, asset handling, and automation. These scripts support the marketing workflow by handling repetitive tasks programmatically.

## Brand Guidelines Scripts

**Location:** `.claude/skills/brand-guidelines/scripts/`

### inject-brand-context.cjs
Extract brand context from guidelines for prompt injection

**Purpose:** Inject dynamic brand context into AI prompts for brand-aware content generation

**Usage:**
```bash
# Standard output (pretty-printed)
node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs

# JSON output for scripting
node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs --json

# Specific format
node .claude/skills/brand-guidelines/scripts/inject-brand-context.cjs --format json
```

**Output:**
```json
{
  "brandName": "Your Brand",
  "voice": {
    "tone": "Professional yet approachable",
    "personality": ["trait1", "trait2"]
  },
  "visual": {
    "colors": {
      "primary": "#6366F1",
      "secondary": "#EC4899"
    },
    "typography": {
      "headings": "Inter",
      "body": "Inter"
    }
  },
  "messaging": {
    "valueProposition": "...",
    "keyMessages": ["..."]
  }
}
```

**Integration Points:**
- Content commands automatically call this
- Email templates inject context
- Design commands use for brand-aware visuals
- Social posts reference for tone consistency

### validate-asset.cjs
Validate asset naming and compliance

**Purpose:** Ensure assets follow naming conventions and meet requirements

**Usage:**
```bash
# Validate single asset
node .claude/skills/brand-guidelines/scripts/validate-asset.cjs assets/images/banner.png

# JSON output
node .claude/skills/brand-guidelines/scripts/validate-asset.cjs assets/images/banner.png --json

# Validate entire directory
node .claude/skills/brand-guidelines/scripts/validate-asset.cjs assets/ --recursive
```

**Validation Checks:**
- File naming convention compliance
- File size optimization
- Image dimensions appropriateness
- Format compatibility (PNG, JPG, SVG)
- Color palette compliance
- Brand element presence (logo, colors)

**Output:**
```json
{
  "file": "banner_launch_hero_20251209_16-9.png",
  "valid": true,
  "warnings": [],
  "size": "245KB",
  "dimensions": "1920x1080",
  "optimization": "Good (< 300KB recommended)"
}
```

### extract-colors.cjs
Extract and compare colors from images

**Purpose:** Extract color palettes from images and compare against brand palette

**Usage:**
```bash
# Show brand palette
node .claude/skills/brand-guidelines/scripts/extract-colors.cjs --palette

# Extract from image
node .claude/skills/brand-guidelines/scripts/extract-colors.cjs assets/images/screenshot.png

# Compare with tolerance
node .claude/skills/brand-guidelines/scripts/extract-colors.cjs assets/images/screenshot.png --compare --tolerance 10

# JSON output
node .claude/skills/brand-guidelines/scripts/extract-colors.cjs assets/images/screenshot.png --json
```

**Output:**
```json
{
  "image": "screenshot.png",
  "colors": [
    {
      "hex": "#6366F1",
      "rgb": "99, 102, 241",
      "name": "Primary Blue",
      "match": "Exact match with brand primary"
    },
    {
      "hex": "#EC4899",
      "rgb": "236, 72, 153",
      "name": "Pink",
      "match": "Within 5% tolerance of secondary"
    }
  ]
}
```

### sync-brand-to-tokens.cjs
Sync brand guidelines to design tokens

**Purpose:** Convert brand guidelines to design tokens (JSON and CSS)

**Usage:**
```bash
# Sync brand to tokens
node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs

# Specify input and output
node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs \
  --input docs/brand-guidelines.md \
  --output assets/design-tokens.json

# Also generate CSS
node .claude/skills/brand-guidelines/scripts/sync-brand-to-tokens.cjs --css
```

**Input:** `docs/brand-guidelines.md`

**Output Files Created:**
- `assets/design-tokens.json` - Token definitions
- `assets/design-tokens.css` - CSS custom properties
- `.assets/manifest.json` - Asset registry (updated)

**CSS Tokens Generated:**
```css
:root {
  --color-primary: #6366F1;
  --color-secondary: #EC4899;
  --font-heading: "Inter", sans-serif;
  --font-body: "Inter", sans-serif;
  --spacing-base: 8px;
  --spacing-sm: 4px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
}
```

## Media Processing Scripts

**Location:** `.claude/skills/media-processing/scripts/`

### remove-background.sh
Remove background from images

**Purpose:** Remove background from product photos, screenshots, etc.

**Usage:**
```bash
# Remove background from PNG
./scripts/remove-background.sh input.png

# Specify output
./scripts/remove-background.sh input.png output.png

# Batch process
./scripts/remove-background.sh images/*.jpg --output ./processed/
```

**Requires:** ImageMagick or similar tool

### crop.sh
Crop image to specific dimensions

**Purpose:** Crop to exact dimensions for different platforms

**Usage:**
```bash
# Crop to width x height
./scripts/crop.sh image.png 1200x630

# Crop with center focus
./scripts/crop.sh image.png 1200x630 --gravity center

# Batch crop
./scripts/crop.sh *.png 1920x1080 --output ./cropped/
```

### resize.sh
Resize images for different formats

**Purpose:** Create multiple sizes for responsive images

**Usage:**
```bash
# Create standard sizes
./scripts/resize.sh image.png --standard

# Output: image-sm.png, image-md.png, image-lg.png

# Custom sizes
./scripts/resize.sh image.png 400 800 1200 --suffix ""

# For web optimization
./scripts/resize.sh image.png --web
```

### optimize.sh
Compress and optimize images for web

**Purpose:** Reduce file size while maintaining quality

**Usage:**
```bash
# Optimize single image
./scripts/optimize.sh image.png

# Batch optimize
./scripts/optimize.sh images/*.png --recursive

# Aggressive compression
./scripts/optimize.sh image.png --aggressive
```

## Asset Management Scripts

**Location:** `.claude/scripts/`

### manifest-update.cjs
Update asset manifest registry

**Purpose:** Track all assets in central registry

**Usage:**
```bash
# Add asset to manifest
node manifest-update.cjs add assets/images/hero.png \
  --title "Hero Image" \
  --campaign "launch" \
  --tags "hero,16-9"

# List all assets
node manifest-update.cjs list

# Search assets
node manifest-update.cjs search --campaign launch

# Remove asset
node manifest-update.cjs remove assets/images/old.png
```

**Manifest Structure:**
```json
{
  "assets": [
    {
      "id": "img-001",
      "path": "assets/images/hero.png",
      "title": "Hero Image",
      "type": "image",
      "campaign": "launch",
      "tags": ["hero", "16-9"],
      "created": "2025-12-09T10:30:00Z",
      "modified": "2025-12-09T10:30:00Z",
      "size": "245KB",
      "status": "approved"
    }
  ]
}
```

## Automation Scripts

### statusline.sh / statusline.ps1 / statusline.cjs
Display project status

**Purpose:** Show current project status and active work

**Location:** `.claude/`

**Usage:**
```bash
# Bash
source statusline.sh

# PowerShell
. statusline.ps1

# Node.js
node statusline.cjs
```

**Shows:**
- Current branch and status
- Active tasks/plans
- Brand context status
- Last sync time
- Current campaign

## Custom Scripts Location

Add custom scripts to:
```
.claude/scripts/custom/
```

**Template:**
```bash
#!/bin/bash
# Script name and purpose
# Usage: ./script-name.sh [arguments]

set -e  # Exit on error

# Your script code here
echo "Running custom script..."

# Log results
echo "✓ Script completed"
```

## Using Scripts in Commands

Scripts are automatically called by commands:

```bash
# /content:good automatically calls
node inject-brand-context.cjs

# /design:good automatically calls
node extract-colors.cjs

# /campaign create automatically calls
node manifest-update.cjs
```

## Script Development Guidelines

When creating new scripts:

1. **Input validation**
   ```bash
   if [ $# -eq 0 ]; then
     echo "Usage: script.sh <argument>"
     exit 1
   fi
   ```

2. **Error handling**
   ```bash
   if ! command -v required_tool &> /dev/null; then
     echo "Error: required_tool not found"
     exit 1
   fi
   ```

3. **Output formatting**
   ```bash
   # Success
   echo "✓ Operation completed"

   # Error
   echo "✗ Operation failed" >&2
   exit 1
   ```

4. **JSON output option**
   ```bash
   if [ "$1" = "--json" ]; then
     echo '{"status": "success"}'
   else
     echo "Operation completed successfully"
   fi
   ```

## Script Troubleshooting

**Script not found?**
- Verify path: `.claude/skills/[skill]/scripts/[script].cjs`
- Check permissions: `chmod +x script.sh`
- For Node scripts: verify Node.js installed

**"Permission denied" error?**
```bash
# Make executable
chmod +x .claude/scripts/script-name.sh
```

**Script produces no output?**
- Add debug flag: `--debug` or `--verbose`
- Check logs: `command 2>&1 | tee output.log`
- Verify input files exist

**Async script hanging?**
- Check for missing dependencies
- Verify API keys in `.env`
- Look for infinite loops or network timeouts

## Integration with Workflows

Scripts are triggered by:

1. **Commands:** `/content:good` → calls script
2. **Workflows:** Defined in `.claude/workflows/`
3. **Hooks:** Auto-triggered on events (see `.claude/hooks/`)
4. **Manual:** Run directly from terminal

**Examples:**
```bash
# When writing content
/content:good "..."
# Automatically runs: inject-brand-context.cjs

# When creating design
/design:good "..."
# Automatically runs: extract-colors.cjs, validate-asset.cjs

# When managing assets
/content:hub
# Automatically runs: manifest-update.cjs
```

## Performance Optimization

For batch operations:

```bash
# Process multiple files in parallel
for file in assets/images/*.png; do
  node extract-colors.cjs "$file" --json >> results.json &
done
wait

# Limit concurrent operations
for file in assets/images/*.png; do
  if [ $(jobs -r -p | wc -l) -ge 4 ]; then
    wait -n
  fi
  ./process.sh "$file" &
done
```

## Next Steps

1. Review relevant scripts for your workflow
2. Run `/seo` commands that use keyword research
3. Use brand injection for content: `inject-brand-context.cjs`
4. Validate assets: `validate-asset.cjs`
5. Extract colors: `extract-colors.cjs`
6. Create custom scripts as needed
