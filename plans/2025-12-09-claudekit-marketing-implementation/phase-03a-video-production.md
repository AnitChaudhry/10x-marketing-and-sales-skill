# Phase 3a: Video Production Skill

## Context Links

- [Plan Overview](./plan.md)
- [Phase 3: Marketing Skills](./phase-03-marketing-skills.md)
- [Research: Video Integration](../reports/RESEARCH-SUMMARY-VIDEO-INTEGRATION.md)
- [Source: ClaudeKit Marketing Overview](../../docs/overall/ClaudeKit-Marketing-Claude-Code-for-Sales-and-Marketing.md#L84-110)

---

## Overview

| Field | Value |
|-------|-------|
| **Timeline** | Dec 21-24, 2025 (parallel with Phase 3) |
| **Priority** | High |
| **Implementation Status** | DONE |
| **Review Status** | APPROVED |
| **Completion Timestamp** | 2025-12-10 15:14:28 UTC |
| **Description** | Implement video production skill with Veo 3.1 + Gemini integration |
| **Estimated Hours** | 32-40 hours |

---

## Technology Stack

## Important
Use the existing `/skill:create <prompt>` slash command to create new skills.

### Core APIs

| API | Purpose | Model | Cost |
|-----|---------|-------|------|
| Veo 3.1 | Video generation | Gemini API | $0.15-0.40/sec |
| Gemini 2.5 Pro | Video understanding | gemini-2.5-pro | Per-token |
| Imagen 4 | Storyboard generation | imagen-4.0-generate-001 | $0.02-0.08/image |

### MCP Integrations (Phase 5)

| MCP Server | URL | Capabilities |
|------------|-----|--------------|
| YouTube | github.com/ZubeidHendricks/youtube-mcp-server | Upload, analytics, metadata |
| TikTok | github.com/Seym0n/tiktok-mcp | Upload, virality analysis |
| VidCap | github.com/mrgoonie/vidcap-mcp-server | Captions, summaries |

---

## Architecture

### Skill Directory Structure

```
.claude/skills/video-production/
├── SKILL.md                           # Main skill definition
├── references/
│   ├── video-script-templates.md      # Script structures per format
│   ├── storyboard-format.md           # Storyboard creation guide
│   ├── veo-prompt-guide.md            # Veo 3.1 prompt engineering
│   ├── platform-video-specs.md        # Platform requirements
│   ├── audio-directive-guide.md       # Native audio prompting
│   ├── thumbnail-design-guide.md      # Thumbnail best practices
│   └── video-seo-optimization.md      # Video SEO strategies
├── scripts/
│   ├── generate-video.cjs             # Veo 3.1 wrapper
│   ├── create-storyboard.cjs          # Imagen 4 storyboard generator
│   ├── analyze-video.cjs              # Gemini video understanding
│   ├── optimize-for-platform.cjs      # Aspect ratio converter
│   └── extract-captions.cjs           # Caption extraction
└── templates/
    ├── product-demo.json              # Product demo structure
    ├── explainer.json                 # Explainer video structure
    ├── testimonial.json               # Testimonial structure
    └── short-form.json                # Shorts/Reels/TikTok structure
```

---

## Key Capabilities

### 1. Video Script Generation (Gemini 2.5)

**Inputs:**
- Topic/product description
- Target audience
- Platform (YouTube, TikTok, Reels)
- Duration target
- Brand guidelines context

**Outputs:**
- Scene-by-scene script
- Dialogue with speaker labels
- Visual descriptions
- Audio/music cues
- Timing markers

**Script Template Structure:**
```markdown
## Scene {N}: {Title}
- **Duration:** {X} seconds
- **Visual:** {Description of visual elements}
- **Audio:** {Dialogue in quotes, SFX, ambience}
- **Camera:** {Movement/angle}
- **Transition:** {Cut type to next scene}
```

### 2. Storyboard Creation (Imagen 4)

**Process:**
1. Extract key frames from script
2. Generate reference images for each scene
3. Include composition guides
4. Add timing annotations
5. Export as visual reference document

**Imagen 4 Storyboard Prompts:**
```
Professional storyboard frame for marketing video:
Scene: {scene_description}
Style: Clean illustration, simplified backgrounds
Perspective: {camera_angle}
Include composition guides (rule of thirds)
Brand colors: {primary_color}, {secondary_color}
```

### 3. Video Generation (Veo 3.1)

**Key Specifications:**
- Output: 8-second clips at 1080p
- Native audio: Dialogue, SFX, ambience, music
- Aspect ratios: 9:16 (vertical), 16:9 (horizontal)
- Generation time: 3-5 minutes per clip

**Prompt Engineering Best Practices:**

```
STRUCTURE:
[SUBJECT] + [ACTION] + [SETTING] + [STYLE] + [CAMERA] + [LIGHTING] + [MOTION] + [AUDIO] + [CONSTRAINTS]

AUDIO DIRECTIVES:
- Dialogue: "Speaker name says: 'Quote here'"
- SFX: "SFX: [description] tied to [action]"
- Ambience: "Ambient: [2-3 elements max]"
- Music: "Music: [genre/mood, subtle]"

QUALITY PHRASES:
- "crystal clear dialogue"
- "professional audio mixing"
- "balanced audio levels"
- "synchronized dialogue and action"
```

**Veo 3.1 Prompt Template:**
```
Marketing video clip for {brand}: {scene_description}

Visual: {detailed_visual}
Setting: {environment}
Style: Professional, polished, {style_adjectives}
Camera: {movement}, {angle}
Lighting: {lighting_setup}

Audio:
- "{speaker_name}" says: "{dialogue}"
- SFX: {sound_effect} as {action_trigger}
- Ambient: {ambient_sounds}
- Music: Subtle {genre} background

Technical: 8 seconds, {aspect_ratio}, high quality, professional grade
```

### 4. Video Understanding (Gemini 2.5 Pro)

**Capabilities:**
- 1M token context window
- Processes up to 6 hours video
- Scene detection
- Quality assessment
- Content analysis
- Transcript extraction

**Use Cases:**
- Quality review of generated videos
- Feedback for iteration
- Competitor video analysis
- Content summarization

### 5. Platform Optimization

**Platform Specifications:**

| Platform | Aspect | Resolution | Max Duration | Frame Rate |
|----------|--------|-----------|--------------|------------|
| YouTube Shorts | 9:16 | 1080×1920 | 3 min | 24-60 fps |
| TikTok | 9:16 | 1080×1920 | 60 min | 24-60 fps |
| Instagram Reels | 9:16 | 1080×1920 | 3 min | 30 fps |
| YouTube Long | 16:9 | 1920×1080 | ∞ | 24-60 fps |

**Key Insight:** All short-form platforms unified on 9:16 - generate once, distribute everywhere.

---

## Video Pipeline Workflow

```
SCRIPT GENERATION (Gemini 2.5)
↓ 2-3 minutes
STORYBOARD CREATION (Imagen 4)
↓ 1-2 minutes
PROMPT ENGINEERING (Gemini 2.5)
↓ 1 minute
VIDEO GENERATION (Veo 3.1 async)
↓ 3-5 minutes
SCENE ASSEMBLY (FFmpeg)
↓ 1-2 minutes
QUALITY REVIEW (Gemini video understanding)
↓ 1-2 minutes
PLATFORM OPTIMIZATION (aspect ratio conversion)
↓ 1-2 minutes
TRANSCRIPTION + CAPTIONS
↓ 2-3 minutes
MULTI-PLATFORM PUBLISHING (YouTube + TikTok MCPs)
↓ 1-2 minutes
COMPLETE

Total: 15-25 minutes
Cost: $3-25 per campaign (depending on variants)
```

---

## Reference Files Specifications

### video-script-templates.md

**Content:**
- Product demo script structure (30/60/90 sec)
- Explainer video framework (hook → problem → solution → CTA)
- Testimonial video format
- Short-form content patterns (TikTok trends, Shorts hooks)
- B-roll integration points
- Music cue timing

### storyboard-format.md

**Content:**
- Frame composition guidelines
- Shot types (wide, medium, close-up, detail)
- Transition notation
- Timing markers
- Audio sync points
- Thumbnail selection criteria

### veo-prompt-guide.md

**Content:**
- Prompt structure template
- Audio directive syntax
- Quality phrases reference
- Common mistakes to avoid
- Platform-specific adjustments
- Example prompts by video type

### platform-video-specs.md

**Content:**
- Complete spec table (all platforms)
- Optimal posting times
- Hashtag strategies
- Thumbnail requirements
- Caption formatting
- Music/audio guidelines

### audio-directive-guide.md

**Content:**
- Dialogue formatting rules
- SFX integration patterns
- Ambience layering
- Music ducking guidelines
- Lip-sync expectations
- Audio quality phrases

---

## Scripts Specifications

### generate-video.cjs

**Purpose:** Veo 3.1 API wrapper with retry logic

**Features:**
- Prompt construction from template
- Authentication handling
- Async job polling
- Error recovery
- Cost tracking
- Result caching

**Interface:**
```javascript
generateVideo({
  prompt: string,
  aspectRatio: '9:16' | '16:9',
  duration: number,  // up to 8 seconds
  audioConfig: AudioConfig,
  brandContext: BrandContext
}): Promise<VideoResult>
```

### create-storyboard.cjs

**Purpose:** Generate visual storyboard from script

**Features:**
- Script parsing
- Scene extraction
- Imagen 4 API calls
- Image assembly
- Annotation overlay
- PDF/PNG export

### analyze-video.cjs

**Purpose:** Gemini video understanding wrapper

**Features:**
- Video upload to File API
- Content analysis
- Quality scoring
- Scene detection
- Transcript extraction
- Improvement suggestions

### optimize-for-platform.cjs

**Purpose:** Format videos for target platforms

**Features:**
- Aspect ratio conversion
- Resolution scaling
- Frame rate adjustment
- Audio normalization
- Metadata embedding
- Thumbnail extraction

---

## Implementation Steps

### Day 1: Core Infrastructure

1. Create skill directory structure
2. Write SKILL.md main definition
3. Implement Veo 3.1 client wrapper
4. Set up authentication flow
5. Create basic test harness

### Day 2: Script & Storyboard

6. Write video-script-templates.md
7. Write storyboard-format.md
8. Implement script generation with Gemini
9. Implement storyboard creation with Imagen 4
10. Test script → storyboard flow

### Day 3: Video Generation

11. Write veo-prompt-guide.md
12. Write audio-directive-guide.md
13. Implement video generation script
14. Implement quality review with Gemini
15. Test full generation pipeline

### Day 4: Platform & Polish

16. Write platform-video-specs.md
17. Implement platform optimizer
18. Implement caption extraction
19. Create video templates (product-demo, explainer, etc.)
20. Integration testing
21. Documentation updates

---

## Cost Estimation

### Per Video Campaign

| Component | Cost Range |
|-----------|------------|
| Veo 3.1 generation (2-4 scenes) | $2.40-4.80 |
| Imagen 4 storyboard (4 images) | $0.04-0.20 |
| Gemini API calls | $0.50-1.00 |
| **Total single video** | **$3-6** |

### Multi-Platform Full Campaign

| Component | Cost Range |
|-----------|------------|
| Veo generation (12-16 clips) | $12-20 |
| Imagen + Gemini processing | $2-3 |
| Platform API calls | ~$0-1 |
| **Total campaign** | **$14-25** |

### Comparison

- Professional video production: $500-5,000
- Stock video services: $50-200/clip
- AI video startups: $100-1,000/campaign
- **ClaudeKit approach: $3-25** ✓

---

## Agent Integration

### Primary: content-creator agent

- Invokes video-production skill
- Manages script generation
- Coordinates storyboard creation
- Triggers video generation

### Secondary: campaign-manager agent

- Multi-video campaign orchestration
- Platform distribution coordination
- Analytics integration
- Performance tracking

---

## Related Commands (Phase 4)

```
/content/video [type] [topic]
  - type: youtube | tiktok | reel | explainer | demo | testimonial
  - Activates video-production skill
  - Runs full pipeline
  - Outputs to assets/videos/

/content/video/script [type]
  - Generate script only

/content/video/storyboard [script-path]
  - Generate storyboard from script

/content/video/generate [storyboard-path]
  - Generate video from storyboard
```

---

## Todo List

- [x] Create video-production skill directory
- [x] Write SKILL.md main definition
- [x] Create video-script-templates.md reference
- [x] Create storyboard-format.md reference
- [x] Create veo-prompt-guide.md reference
- [x] Create platform-video-specs.md reference
- [x] Create audio-directive-guide.md reference
- [x] Implement generate-video.cjs script
- [x] Implement create-storyboard.cjs script
- [x] Implement analyze-video.cjs script
- [x] Implement optimize-for-platform.cjs script
- [x] Create video templates (JSON)
- [x] Integration testing
- [x] Update skill-catalog.md

---

## Success Criteria

1. video-production skill loads correctly
2. Script generation produces structured output
3. Storyboard images align with script scenes
4. Veo 3.1 generates usable video clips
5. Platform optimization produces correct formats
6. Quality review provides actionable feedback
7. Full pipeline completes in <30 minutes
8. Cost per video under $10

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Veo 3.1 quality inconsistent | Medium | High | Retry with simplified prompts |
| Audio sync issues | Medium | Medium | Fallback to music-only track |
| API rate limits | Low | Medium | Queue system, exponential backoff |
| Platform API changes | Low | High | Abstract API layers, version pinning |
| SynthID watermark issues | Low | Medium | Monitor platform acceptance |

---

## Security Considerations

- Store API keys in environment variables
- Never commit credentials
- Use minimal permission scopes
- Audit MCP server code before use
- Log all API operations
- PII redaction in transcripts

---

## Dependencies

```
@google-cloud/vertexai@1.5.0
google-ai-generativelanguage@1.0.0
fluent-ffmpeg@2.1.2
ffmpeg-static@5.1.0
axios@1.6.0
```

---

## Next Steps

After Phase 3a completion:
1. Test end-to-end video generation
2. Proceed to Phase 5 for MCP integrations (YouTube, TikTok)
3. Create /content/video commands in Phase 4
4. Integrate with campaign workflows

---

## Unresolved Questions

1. SynthID watermark policy on YouTube/TikTok monetization?
2. Maximum scene extensions before quality degrades?
3. Lip-sync precision guarantees?
4. Batch processing limits at scale?
5. Alternative image gen for storyboards (Midjourney, DALL-E)?
