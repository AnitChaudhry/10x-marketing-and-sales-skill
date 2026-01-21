---
name: canva-creative
description: |
  Creative design generation skill for creating visual content from scratch. Use this skill when
  user wants to CREATE new designs for social media, presentations, marketing materials, etc.
  Integrates web search for inspiration, generates content ideas, and creates designs using Canva.
  Supports all platforms: Instagram, LinkedIn, Facebook, Twitter, YouTube, and more.
  Can be integrated with other skills for automated workflows (e.g., outreach campaigns).
---

# Canva Creative Design Generator

Create stunning visual content from scratch for any platform or purpose.

---

## Capabilities

This skill can:

1. **Research & Inspire** - Search for design trends, competitor examples, best practices
2. **Generate Content** - Create headlines, copy, and messaging for designs
3. **Create Designs** - Build designs using Canva API with correct dimensions
4. **Export Assets** - Download in any format (PNG, JPG, PDF, PPTX, etc.)
5. **Integrate** - Provide designs for other skills (outreach, automation, etc.)

---

## Supported Design Types

### Social Media
| Platform | Type | Dimensions | Use `create_design.py` with |
|----------|------|------------|------------------------------|
| Instagram Post (Square) | 1080x1080 | `--width 1080 --height 1080` |
| Instagram Post (Portrait) | 1080x1350 | `--width 1080 --height 1350` |
| Instagram Story/Reel | 1080x1920 | `--width 1080 --height 1920` |
| Facebook Post | 1080x1080 | `--width 1080 --height 1080` |
| Facebook Cover | 820x312 | `--width 820 --height 312` |
| LinkedIn Post | 1200x628 | `--width 1200 --height 628` |
| LinkedIn Banner | 1584x396 | `--width 1584 --height 396` |
| Twitter Post | 1200x675 | `--width 1200 --height 675` |
| Twitter Header | 1500x500 | `--width 1500 --height 500` |
| YouTube Thumbnail | 1280x720 | `--width 1280 --height 720` |
| Pinterest Pin | 1000x1500 | `--width 1000 --height 1500` |

### Business
| Type | Dimensions | Command |
|------|------------|---------|
| Presentation (16:9) | `--type presentation` | Built-in preset |
| Document | `--type doc` | Built-in preset |
| Business Card | 1050x600 | `--width 1050 --height 600` |
| Email Header | 600x200 | `--width 600 --height 200` |
| Poster (A3) | 1191x1684 | `--width 1191 --height 1684` |
| Flyer (A5) | 420x595 | `--width 420 --height 595` |

### Ads & Banners
| Type | Dimensions | Command |
|------|------------|---------|
| Leaderboard | 728x90 | `--width 728 --height 90` |
| Medium Rectangle | 300x250 | `--width 300 --height 250` |
| Skyscraper | 160x600 | `--width 160 --height 600` |
| Square Ad | 250x250 | `--width 250 --height 250` |

---

## 3-Mode Workflow

### MODE 1: RESEARCH & PLAN

**Step 1: Understand Requirements**
```
- What platform is this for?
- What is the purpose? (awareness, engagement, sales)
- What is the brand style? (colors, fonts, tone)
- What content/message needs to be conveyed?
- Are there any reference designs or competitors to research?
```

**Step 2: Research (if needed)**
```bash
# Use web search to find:
# - Design trends for the platform
# - Competitor examples
# - Best practices
# - Color schemes and inspiration
```

**Step 3: Content Generation**
```
- Generate headline options (3-5 variations)
- Create body copy (concise, action-oriented)
- Suggest imagery style
- Define call-to-action
```

**Step 4: Present Plan**
```markdown
## Design Plan

### Platform: Instagram Post
### Dimensions: 1080 x 1350 (Portrait)

### Content:
- Headline: "Transform Your Business in 30 Days"
- Subtext: "Join 10,000+ entrepreneurs who've scaled with our proven system"
- CTA: "Link in bio"

### Visual Direction:
- Style: Modern, minimalist
- Colors: Brand blue (#2563EB), White, Light gray
- Imagery: Abstract gradient background
- Typography: Bold sans-serif headline, clean body text

### Design Elements:
1. Background gradient (brand colors)
2. Headline text (center, large)
3. Supporting text (below headline)
4. Logo (bottom corner)
5. CTA (bottom)
```

### MODE 2: CLARIFY

Ask user to confirm:
- Content accuracy
- Visual direction
- Any specific requirements
- Brand guidelines to follow

### MODE 3: IMPLEMENT

**Step 1: Create Design in Canva**
```bash
# For social media (custom dimensions)
.venv\Scripts\python.exe scripts/create_design.py \
    --width 1080 --height 1350 \
    --title "Instagram Post - Transform Your Business"

# For presentations (preset)
.venv\Scripts\python.exe scripts/create_design.py \
    --type presentation \
    --title "Q4 Business Review"
```

**Step 2: Get Design URL**
The script returns the design ID and edit URL. Share with user for:
- Adding text and elements in Canva editor
- Using brand kit and templates
- Final adjustments

**Step 3: Export Design**
```bash
# Export as PNG (for social media)
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" \
    --format png --output output/designs

# Export as PDF (for documents)
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" \
    --format pdf --quality print

# Export as PPTX (for presentations)
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" \
    --format pptx
```

---

## Content Generation Templates

### Quote Graphics
```
Platform: [Platform]
Dimensions: [From reference]

Quote: "[Inspiring quote]"
Attribution: "- [Name], [Title]"
Background: [Color/gradient/image]
Logo placement: Bottom right
```

### Announcement Posts
```
Platform: [Platform]
Dimensions: [From reference]

Headline: [Attention-grabbing text]
Date/Details: [What, when, where]
CTA: [Action button text]
Urgency element: [Limited time/spots]
```

### Product Showcases
```
Platform: [Platform]
Dimensions: [From reference]

Product name: [Name]
Key benefit: [One-liner]
Features: [2-3 bullet points]
Price: [If applicable]
CTA: [Shop now/Learn more]
```

### Educational Content
```
Platform: [Platform]
Dimensions: [From reference]

Title: [How to / X Tips for / Guide to]
Content type: [Carousel/Single/Infographic]
Points: [3-7 key takeaways]
CTA: [Save/Share/Follow for more]
```

### Testimonials
```
Platform: [Platform]
Dimensions: [From reference]

Quote: "[Customer testimonial]"
Customer: [Name, Company]
Photo: [Headshot if available]
Rating: [Stars if applicable]
Logo: [Brand logo]
```

---

## Integration with Other Skills

### Outreach Integration

This skill can create designs that are then used by outreach skills:

```
Workflow: Create marketing email with custom graphic

1. USER: "Create a promotional graphic and send to our mailing list"

2. CANVA CREATIVE:
   - Creates design (1200 x 628 for email)
   - Exports as PNG
   - Saves to output/designs/

3. OUTREACH SKILL (10x-Outreach-Skill):
   - Reads design from output/designs/
   - Attaches to email
   - Sends to recipients
```

### Output for Integration

When creating designs for integration:
```bash
# Always export to standard location
.venv\Scripts\python.exe scripts/export_design.py "DESIGN_ID" \
    --format png \
    --output output/designs \
    --filename "campaign_graphic"

# Output path: output/designs/campaign_graphic.png
```

### Cross-Skill Data Format

For integration with other skills, provide:
```json
{
  "design_id": "DAFxxxxxxxxxxxx",
  "title": "Campaign Graphic",
  "platform": "email",
  "dimensions": {"width": 600, "height": 200},
  "exported_file": "output/designs/campaign_graphic.png",
  "exported_format": "png",
  "created_at": "2024-01-15T10:30:00Z"
}
```

---

## Design Best Practices

### For Engagement

1. **Use faces** - Increases engagement by 38%
2. **Bold colors** - Stand out in feeds
3. **Minimal text** - 20% rule for ads
4. **Clear hierarchy** - Guide the eye
5. **Strong CTA** - Tell people what to do

### For Brand Consistency

1. **Use brand colors** - Every time
2. **Consistent fonts** - Max 2 per design
3. **Logo placement** - Same corner always
4. **Style guide** - Follow brand guidelines
5. **Templates** - Create and reuse

### Platform-Specific

**Instagram:**
- Bright, vibrant colors
- Lifestyle imagery
- Carousel for education
- Stories for urgency

**LinkedIn:**
- Professional, clean
- Data and statistics
- Thought leadership
- Blue tones work well

**Facebook:**
- Community-focused
- Video performs best
- Emotional content
- Local/personal stories

**Twitter/X:**
- Timely, trending
- Humor works well
- Infographics
- News-jacking

---

## Example Workflows

### Example 1: Create Instagram Post

```
User: "Create an Instagram post announcing our Black Friday sale"

[PLAN]
Platform: Instagram
Dimensions: 1080 x 1350 (Portrait - best engagement)

Content:
- Headline: "BLACK FRIDAY SALE"
- Subtext: "Up to 50% off everything"
- Dates: "Nov 24-27"
- CTA: "Shop link in bio"

Visual:
- Bold black background
- Gold/yellow text accents
- Large typography
- Minimal, high-impact design

[IMPLEMENT]
.venv\Scripts\python.exe scripts/create_design.py \
    --width 1080 --height 1350 \
    --title "Black Friday Sale Post"
```

### Example 2: Create LinkedIn Banner

```
User: "Create a LinkedIn banner for my profile"

[PLAN]
Platform: LinkedIn Personal Banner
Dimensions: 1584 x 396

Content:
- Name/Title: "John Smith | Digital Marketing Expert"
- Value prop: "Helping brands grow with data-driven strategies"
- Contact: "john@example.com"

Visual:
- Professional gradient background
- Clean typography
- Subtle personal branding
- No face (profile picture overlaps)

[IMPLEMENT]
.venv\Scripts\python.exe scripts/create_design.py \
    --width 1584 --height 396 \
    --title "LinkedIn Banner - John Smith"
```

### Example 3: Create Presentation

```
User: "Create a pitch deck for our startup"

[PLAN]
Platform: Presentation
Dimensions: 16:9 (1920 x 1080)

Structure:
1. Title slide
2. Problem
3. Solution
4. Market size
5. Business model
6. Traction
7. Team
8. Ask

[IMPLEMENT]
.venv\Scripts\python.exe scripts/create_design.py \
    --type presentation \
    --title "Startup Pitch Deck"
```

---

## Available Scripts

### Creation
```bash
# Create by preset
.venv\Scripts\python.exe scripts/create_design.py --type presentation

# Create by dimensions
.venv\Scripts\python.exe scripts/create_design.py --width 1080 --height 1080

# With title
.venv\Scripts\python.exe scripts/create_design.py \
    --width 1080 --height 1350 \
    --title "My Instagram Post"
```

### Export
```bash
# Export as PNG
.venv\Scripts\python.exe scripts/export_design.py "ID" --format png

# Export as PDF (print quality)
.venv\Scripts\python.exe scripts/export_design.py "ID" --format pdf --quality print

# Export as PPTX
.venv\Scripts\python.exe scripts/export_design.py "ID" --format pptx

# Batch export
.venv\Scripts\python.exe scripts/batch_export.py \
    --designs "ID1" "ID2" "ID3" \
    --format png \
    --output output/campaign
```

---

## Todo List Tracking

**ALWAYS use TodoWrite** for creative workflows:

```json
[
  {"content": "Research design trends and best practices", "status": "in_progress", "activeForm": "Researching trends"},
  {"content": "Generate content and messaging", "status": "pending", "activeForm": "Generating content"},
  {"content": "Create design plan for user approval", "status": "pending", "activeForm": "Creating plan"},
  {"content": "Build design in Canva", "status": "pending", "activeForm": "Building design"},
  {"content": "Export and deliver final asset", "status": "pending", "activeForm": "Exporting design"}
]
```

---

## Output Locations

- `output/designs/` - Exported design files
- `output/exports/` - Batch exports

---

## Reference Documents

- `DESIGN_REFERENCE.md` - Full dimension guide and best practices
- `scripts/API_REFERENCE.md` - Canva API documentation
