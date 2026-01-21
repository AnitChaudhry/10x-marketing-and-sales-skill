# Image Generation & Design Commands

## Overview

Design commands create immersive, professional visual content using AI-powered image generation and design intelligence databases.

## Main Command: `/design:good`

**Description:** Create an immersive design

**Usage:**
```bash
/design:good <tasks>
```

**Example:**
```bash
/design:good "create landing page hero section with brand colors"
/design:good "design email header banner for product launch"
/design:good "create social media carousel covering features"
```

## Design Subcommands

### `/design:good`
Create professional, immersive designs with storytelling, micro-interactions, 3D effects.

**Workflow:**
1. Activate `ui-ux-pro-max` skill first (design intelligence database)
2. Run design intelligence searches for style/trends
3. Use `researcher` agents to study design patterns
4. Delegate to `ui-ux-designer` agent for implementation
5. Generate assets with `ai-multimodal` skill
6. Verify quality with asset analysis
7. Update `docs/design-guidelines.md` if needed

### `/design:generate`
Generate specific visual assets using Imagen 4 (ai-multimodal skill)

**Usage:**
```bash
/design:generate "hero image for SaaS landing page"
/design:generate "product mockup showing feature X"
```

### `/design:3d`
Create 3D visualizations and immersive designs

**Usage:**
```bash
/design:3d "3D product showcase"
/design:3d "interactive feature visualization"
```

### `/design:screenshot`
Capture screenshots of generated designs or websites

**Usage:**
```bash
/design:screenshot "/path/to/html/file"
/design:screenshot "https://example.com/page"
```

### `/slides:create`
Create presentation slides

**Usage:**
```bash
/slides:create "product pitch deck"
/slides:create "Q1 marketing strategy presentation"
```

### `/design:video`
Generate video content from design descriptions

**Usage:**
```bash
/design:video "product demo animation"
/design:video "customer testimonial video"
```

## AI Image Generation Flow

### Step 1: Design Intelligence Search

Before generating, gather intelligence:

```bash
# Search for product type (landing pages, dashboards, etc)
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "SaaS landing page" --domain product

# Search for visual styles (minimalism, glassmorphism, etc)
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "minimalism dark mode" --domain style

# Search for typography inspiration
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "bold headlines modern" --domain typography

# Search for color palettes
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "tech startup" --domain color
```

### Step 2: Image Generation

Generate images using `ai-multimodal` skill (Imagen 4):

**Capabilities:**
- Text-to-image generation (brand-aware)
- Image editing and manipulation
- Background removal
- Image analysis and description
- Video frame generation

**Integration Point:** Brand context auto-injected for on-brand visual generation

### Step 3: Asset Processing

Apply post-processing if needed:

```bash
# Remove background from generated image
.claude/skills/media-processing/scripts/remove-background.sh <image>

# Crop to specific dimensions
.claude/skills/media-processing/scripts/crop.sh <image> <width>x<height>

# Resize to multiple formats
.claude/skills/media-processing/scripts/resize.sh <image> <sizes>

# Compress for web
.claude/skills/media-processing/scripts/optimize.sh <image>
```

### Step 4: Quality Verification

Analyze generated assets:

```bash
# Verify image quality and compliance
node .claude/skills/brand-guidelines/scripts/validate-asset.cjs <image-path>

# Check colors against brand palette
node .claude/skills/brand-guidelines/scripts/extract-colors.cjs <image-path>
```

## Design Skills Used

### ui-ux-pro-max
Design intelligence database with:
- **50 design styles** (glassmorphism, brutalism, minimalism, etc.)
- **21 color palettes** (tech, SaaS, e-commerce, etc.)
- **50 font pairings** (Google Fonts)
- **20 chart types** (for dashboards)
- **8 tech stacks** (React, Vue, Svelte, SwiftUI, etc.)

### ai-multimodal
- Text-to-image generation (Imagen 4)
- Image editing (crops, resizes, background removal)
- Image analysis (color extraction, compliance checking)
- Video frame generation

### frontend-design-pro
- Production-ready HTML/CSS/JS
- Real photos (Unsplash/Pexels links)
- Zero AI-generated "slop"
- Component libraries (shadcn/ui, Tailwind)

### ui-styling
- Tailwind CSS utilities
- shadcn/ui components
- Responsive design
- Dark mode support
- Accessibility standards

## Design Workflow Example

### Scenario: Create Landing Page

```bash
# 1. Gather design intelligence
/design:good "research modern SaaS landing page designs"

# 2. Create wireframe
/design:good "create HTML wireframe for product landing page"

# 3. Generate hero image
/design:generate "hero image showing SaaS dashboard with user collaboration features"

# 4. Apply styling
/design:good "create Tailwind CSS styled landing page with brand colors"

# 5. Optimize images
# (Automatically handled by design commands)

# 6. Verify brand compliance
# (Content reviewer agent validates)
```

## Output Locations

All generated designs saved to:

```
assets/
├── designs/                    # Main design files
│   ├── landing-pages/
│   ├── email-templates/
│   └── social-media/
├── images/
│   ├── generated/             # AI-generated images
│   │   └── {timestamp}/
│   └── optimized/
├── banners/
│   ├── email/
│   ├── social/
│   └── web/
└── screenshots/               # Captured screenshots
```

**Naming Convention:**
```
{type}_{campaign}_{description}_{timestamp}_{variant}.{ext}

Examples:
- design_launch_landing-hero_20251209_desktop.html
- banner_promo_email-header_20251209_600w.png
- image_case-study_client-testimonial_20251209_16-9.jpg
```

## Design Guidelines Document

Maintain `docs/design-guidelines.md` with:

1. **Visual Style**
   - Color palette with hex/RGB values
   - Typography (fonts, sizes, weights)
   - Spacing and grid system
   - Border radius, shadows, effects

2. **Components**
   - Button styles
   - Form inputs
   - Cards and containers
   - Navigation patterns

3. **Layouts**
   - Hero section structure
   - Content sections
   - Footer design
   - Responsive breakpoints

4. **Imagery**
   - Photography style
   - Illustration style
   - Icon system
   - Video production guidelines

## Image Quality Checklist

When generating or approving images:

- [ ] Brand colors used correctly
- [ ] Typography matches guidelines
- [ ] Aspect ratio correct for platform
- [ ] File size optimized for web
- [ ] No AI artifacts or "slop"
- [ ] Accessibility considerations (alt text, contrast)
- [ ] Consistent with existing brand assets

## Common Design Commands

### Hero Images
```bash
/design:generate "hero image for [product] showing [key feature]"
```

### Product Mockups
```bash
/design:good "product mockup displaying feature [X]"
```

### Social Media Graphics
```bash
/design:generate "Instagram post design for [campaign]"
/design:generate "LinkedIn article cover image"
```

### Email Headers
```bash
/design:generate "email header banner for [campaign] in [brand-color]"
```

### Feature Illustrations
```bash
/design:good "create 5 feature illustrations showing [use cases]"
```

### Charts & Infographics
```bash
/design:good "create infographic showing [data/process]"
```

## Troubleshooting

**Generated image doesn't match brand colors?**
- Verify brand colors in `docs/brand-guidelines.md`
- Run `inject-brand-context.cjs` to ensure context available
- Try more specific color descriptions in prompt

**Image has AI artifacts or looks "fake"?**
- Use `frontend-design-pro` skill instead (real photos)
- Request screenshot of actual design instead of AI generation
- Specify style: "realistic photography" vs "illustration"

**Design not responsive?**
- Specify dimensions: "16:9", "1:1", "mobile (375px)"
- Ask for multiple formats: desktop/tablet/mobile
- Use `/design:screenshot` to verify on different viewports

**Colors extracted don't match palette?**
- Ensure image saved as PNG (JPEG may lose color accuracy)
- Export image from design tool at highest quality
- Verify palette defined correctly in brand guidelines

## Best Practices

1. **Always inject brand context** - Ensures on-brand visuals
2. **Use ui-ux-pro-max first** - Gathers design intelligence before generating
3. **Verify quality** - Run validation scripts after generation
4. **Maintain guidelines** - Update `docs/design-guidelines.md` as brand evolves
5. **Asset organization** - Use naming conventions strictly
6. **Real over AI** - Prefer real photos (Unsplash/Pexels) over AI generation when possible

## Next Steps

1. Define visual style in `docs/design-guidelines.md`
2. Try `/design:good "create [simple asset]"` to test
3. Run `/design:screenshot` on HTML output to verify
4. Organize assets in `assets/designs/` with naming convention
5. Set up brand color extraction workflow
