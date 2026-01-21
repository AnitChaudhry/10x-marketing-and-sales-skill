# Video Production & Scripts

## Overview

Video production commands generate video scripts, storyboards, and video content for marketing campaigns.

## Main Command: `/design:video`

**Description:** Generate video content from design descriptions

**Usage:**
```bash
/design:video <description>
```

**Examples:**
```bash
/design:video "product demo animation showing setup process"
/design:video "customer testimonial video script"
/design:video "explainer video for feature overview"
```

## Video Types Supported

### Product Demo Videos
- Feature walkthroughs
- Setup guides
- Use case demonstrations
- Before/after comparisons

### Testimonial Videos
- Customer success stories
- Case study narratives
- Expert interviews
- User feedback compilations

### Educational Videos
- Tutorials and how-tos
- Explainer animations
- Process breakdowns
- Training content

### Social Media Videos
- TikTok/Instagram Reels (15-60 seconds)
- YouTube Shorts (15-60 seconds)
- LinkedIn videos (30-120 seconds)
- Twitter/X videos (up to 10 minutes)

### Campaign Videos
- Product launch announcements
- Promotional content
- Event recaps
- Brand story videos

## Video Production Workflow

### Phase 1: Concept & Script

1. **Define video objective**
   - What action should viewer take?
   - Key message?
   - Target audience?

2. **Create script outline**
   - Hook (first 3 seconds)
   - Problem statement
   - Solution presentation
   - Call-to-action
   - Duration target

3. **Generate script using agents**
   - Use `copywriter` agent for compelling narrative
   - Use `content-creator` for structure
   - Get `content-reviewer` approval

### Phase 2: Storyboard

1. **Visual planning**
   - Describe each scene/shot
   - Specify visuals, text overlays
   - Note transitions and timing

2. **Generate storyboard images**
   - Use `/design:generate` for scene illustrations
   - Create mood boards
   - Establish visual consistency

### Phase 3: Production

1. **Gather assets**
   - B-roll footage
   - Product screenshots
   - Brand graphics
   - Music/sound effects

2. **Generate video**
   - Use ai-multimodal skill for video generation
   - Apply brand colors and fonts
   - Add captions and overlays

3. **Post-production**
   - Edit timing and pacing
   - Color grading for brand consistency
   - Audio balancing
   - Subtitle generation

### Phase 4: Optimization

1. **Platform-specific versions**
   - 16:9 (YouTube, LinkedIn)
   - 9:16 (TikTok, Instagram Reels, Stories)
   - 1:1 (Instagram Feed, LinkedIn)
   - 4:5 (Pinterest)

2. **File optimization**
   - Compress for web
   - Generate thumbnails
   - Create preview frames

3. **Distribution**
   - Upload to platforms
   - Add captions/descriptions
   - Schedule posting

## Related Commands

### `/slides:create`
Create presentation decks that can become video storyboards

**Usage:**
```bash
/slides:create "product demo presentation"
/slides:create "customer success story slides"
```

**Output:** HTML/PDF presentations that can be used as storyboards

### `/design:generate`
Generate individual frames/scenes for videos

**Usage:**
```bash
/design:generate "scene 1: user opening app dashboard"
/design:generate "scene 2: customer using feature X"
```

### `/social [platform] reel`
Create social platform-specific video scripts

**Usage:**
```bash
/social tiktok reel
/social instagram reel
/social youtube "shorts"
```

## Video Script Template

When creating video scripts, follow this structure:

```markdown
# [Video Title]

## Metadata
- Duration: [seconds]
- Platform: [YouTube/TikTok/LinkedIn]
- Aspect Ratio: [16:9/9:16/1:1]
- Target Audience: [description]

## Hook (0-3 seconds)
[Compelling opening that grabs attention]

## Problem (3-10 seconds)
[Identify the pain point or opportunity]

## Solution (10-25 seconds)
[Present your solution/product]

## Benefits (25-35 seconds)
[Show value and results]

## Social Proof (35-40 seconds)
[Testimonial or credibility indicator]

## CTA (40-45 seconds)
[Clear call-to-action]

---

## Scene Breakdown

### Scene 1: [Name]
- **Visuals:** [What's on screen]
- **Audio:** [Voiceover/music/SFX]
- **Duration:** [seconds]
- **Text Overlays:** [Any on-screen text]
- **Transitions:** [How to enter/exit scene]

### Scene 2: [Name]
[Same structure]

...

## Production Notes
- [Any special effects needed]
- [Brand elements to include]
- [Accessibility considerations]
```

## Storyboard Template

Visual planning document:

```markdown
# [Video Title] - Storyboard

## Scene 1: Hook
[Description of visual]
Duration: [X seconds]

## Scene 2: [Name]
[Description of visual]
Duration: [X seconds]

...

## Production Assets Needed
- [ ] Asset 1
- [ ] Asset 2
- [ ] Audio files
- [ ] Brand graphics
```

## Skills Used for Video Production

### ai-multimodal
- Text-to-video generation
- Video frame extraction
- Video analysis and description
- Subtitle generation
- Audio processing

### media-processing
- Video editing (trim, crop)
- Format conversion (MP4, WebM, etc.)
- Resolution/bitrate optimization
- Thumbnail generation
- Audio mixing

### content-marketing
- Video strategy and positioning
- Platform-specific optimization
- Audience targeting
- Distribution planning

### copywriting
- Script writing and dialogue
- Voiceover narration
- Text overlay copy
- CTA optimization

## Video Output Locations

```
assets/
├── videos/
│   ├── product-demos/
│   │   └── {feature}_20251209.mp4
│   ├── testimonials/
│   │   └── {customer}_20251209.mp4
│   ├── tutorials/
│   │   └── {topic}_20251209.mp4
│   ├── social/
│   │   ├── tiktok/
│   │   ├── instagram/
│   │   ├── youtube/
│   │   └── linkedin/
│   ├── scripts/
│   │   └── {name}_20251209.md
│   └── storyboards/
│       └── {name}_20251209.md

docs/
├── video-guidelines.md       # Video production standards
└── content-calendar.md       # Scheduled video releases
```

## Video Asset Naming

```
video_{type}_{campaign}_{description}_{timestamp}_{platform}.{ext}

Examples:
- video_demo_product-launch_intro_20251209_youtube.mp4
- video_tutorial_feature-x_setup_20251209_vertical.mp4
- video_testimonial_customer-win_success_20251209_social.mp4
- video_social_black-friday_promo_20251209_tiktok.mp4
```

## Platform-Specific Video Formats

| Platform | Aspect Ratio | Duration | Specs |
|----------|--------------|----------|-------|
| **YouTube** | 16:9 | 30s-10min | MP4, H.264, max 256GB |
| **YouTube Shorts** | 9:16 | 15-60s | MP4, vertical |
| **TikTok** | 9:16 | 15-600s | MP4/MOV, min 540p |
| **Instagram Reels** | 9:16 | 15-90s | MP4/MOV, min 600p |
| **Instagram Feed** | 1:1 or 4:5 | 3s-60min | MP4, min 600p |
| **LinkedIn** | 16:9 | 3s-10min | MP4, H.264 |
| **Pinterest** | Various | 15-60s | MP4/MOV |
| **Twitter/X** | 16:9 or 1:1 | up to 10min | MP4, max 15min |

## Video Production Checklist

Before uploading video:

- [ ] Brand colors and fonts correct
- [ ] Audio clear and properly mixed
- [ ] Subtitles/captions accurate
- [ ] Platform-specific aspect ratio correct
- [ ] File size optimized
- [ ] Thumbnail appealing and on-brand
- [ ] Metadata (title, description, tags) complete
- [ ] CTA clearly visible
- [ ] Accessibility features included (captions for deaf users)

## Video Performance Metrics

Track these metrics post-launch:

- Views
- Engagement rate (likes, comments)
- Click-through rate (CTR)
- Conversion rate
- Watch time average
- Drop-off points
- Share count

## Best Practices

1. **Hook First** - Grab attention in first 3 seconds
2. **Keep It Short** - Longer videos need more engagement
3. **Mobile First** - Design for vertical viewing
4. **Add Subtitles** - 85% watch without sound
5. **Brand Consistency** - Match design guidelines
6. **Clear CTA** - Tell viewers what to do next
7. **Test Platform Formats** - Each platform has ideal specs
8. **Monitor Performance** - Adjust based on metrics

## Common Video Creation Scenarios

### Scenario: Product Launch Video
```bash
# 1. Create script
/content:good "write 60-second product launch video script"

# 2. Generate script document
/design:video "product launch announcement video"

# 3. Create storyboard images
/design:good "create 6 storyboard scenes for launch video"

# 4. Generate video
# (Handled by video production agent)

# 5. Optimize for platforms
# (Multiple aspect ratios created automatically)
```

### Scenario: Social Media Video Series
```bash
# 1. Plan series
/brainstorm "4-part video tutorial series ideas"

# 2. Create scripts for each episode
/content:good "write TikTok script for episode 1"

# 3. Generate videos
/design:video "create vertical video for episode 1"

# 4. Distribute across platforms
/social tiktok reel
/social instagram reel
```

## Troubleshooting

**Video quality is poor?**
- Check resolution requirements for platform
- Ensure high-quality source materials
- Verify video codec (H.264 recommended)

**Audio is muffled or low quality?**
- Use professional voiceover services if needed
- Ensure audio levels normalized
- Remove background noise

**Video won't upload to platform?**
- Check file size limits
- Verify format compatibility
- Ensure required metadata complete

**Subtitles are inaccurate?**
- Review subtitle generation settings
- Manually correct major errors
- Use professional subtitle services for important videos

## Next Steps

1. Plan your first video (script, storyboard)
2. Use `/design:video` to generate initial concept
3. Create storyboard with `/design:generate`
4. Review with content team
5. Produce and optimize video
6. Publish to platforms
7. Monitor performance metrics
