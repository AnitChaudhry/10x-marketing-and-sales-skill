---
name: canva-video
description: |
  Create and edit video designs in Canva. Use this skill when user wants to work with
  videos, animations, or motion graphics. Handles video creation, editing, timeline
  management, and export. Follows 3-mode workflow for safe operations.
  For static images use canva-image-editor. For presentations use canva-presentation.
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# Canva Video Skill

Create and edit video designs, animations, and motion graphics in Canva.

---

## ⚠️ CRITICAL DESIGN PRESERVATION RULES (MANDATORY)

**These rules are NON-NEGOTIABLE. Violating them will break the video design.**

### 🚫 NEVER DO THESE THINGS:

1. **NEVER add new elements to existing videos** - Only modify EXISTING elements
2. **NEVER change existing element timings** - Unless user EXPLICITLY requests it
3. **NEVER change font sizes/styles** - Unless user EXPLICITLY requests it
4. **NEVER change element positions** - Unless user EXPLICITLY requests it
5. **NEVER change animations** - Unless user EXPLICITLY requests it
6. **NEVER change backgrounds** - Unless user EXPLICITLY requests it
7. **NEVER modify audio levels** - Unless user EXPLICITLY requests it
8. **NEVER change video duration** - Unless user EXPLICITLY requests it
9. **NEVER remove existing elements** - Unless user EXPLICITLY requests it
10. **NEVER modify the template structure** - Unless user EXPLICITLY requests it

### ✅ ALWAYS DO THESE THINGS:

1. **ALWAYS replace text within existing elements** only
2. **ALWAYS replace video clips in existing placeholders** only
3. **ALWAYS preserve all timing and animations** when replacing content
4. **ALWAYS analyze video structure first** before any modification
5. **ALWAYS identify content elements vs template elements** before editing
6. **ALWAYS duplicate the design first** before making changes

### Updating Content - THE CORRECT WAY:

```python
# WRONG - Adds new text element
add_text.py --design "ID" --text "New text"

# CORRECT - Updates existing text element
update_text.py --design "ID" --element "EXISTING_ELEMENT_ID" --text "New text"
```

---

## Scope of This Skill

**This skill handles:**
- Video Posts (Instagram, TikTok, YouTube)
- Video Stories
- Video Ads
- Animated Presentations
- Motion Graphics
- Video Intros/Outros
- Animated Logos
- GIF Creation

**Operations supported:**
- Edit video elements (REPLACE existing, not ADD new)
- ~~Create new video designs~~ → Duplicate existing designs instead
- ~~Add/remove video clips~~ → Replace clips in existing placeholders
- ~~Add text animations~~ → Update text in existing animated elements
- Manage audio tracks (with explicit permission)
- Export to MP4 or GIF

## Video Design Types

| Type | Dimensions | Duration |
|------|------------|----------|
| Instagram Reel | 1080x1920 | Up to 90s |
| TikTok Video | 1080x1920 | Up to 3min |
| YouTube Short | 1080x1920 | Up to 60s |
| YouTube Video | 1920x1080 | Variable |
| Facebook Video | 1280x720 | Variable |
| Video Ad | Various | 15-30s |
| Animated Post | 1080x1080 | 5-15s |
| Animated Story | 1080x1920 | 5-15s |

## 3-Mode Workflow

### MODE 1: PLAN

1. **Analyze Video Structure**
   ```python
   python skills/canva-video/scripts/analyze_video.py \
     --id "DESIGN_ID"
   ```

2. **Document Video Elements**
   ```
   ## Video Analysis: "[Name]"

   ### Overview
   - Dimensions: 1080x1920
   - Duration: 15 seconds
   - Frame Rate: 30fps

   ### Timeline
   | Time | Element | Type | Duration |
   |------|---------|------|----------|
   | 0-3s | Intro | Animation | 3s |
   | 3-10s | Main Content | Video Clip | 7s |
   | 10-13s | Text Overlay | Animated Text | 3s |
   | 13-15s | CTA | Animation | 2s |

   ### Audio
   - Background Music: "Upbeat Track" (15s)
   - Voiceover: None

   ### Proposed Changes
   1. Extend duration to 20 seconds
   2. Add new text at 15-18s
   3. Replace background music
   ```

### MODE 2: CLARIFY

Video-specific questions:

1. **Timing**
   - "At what timestamp should this appear?"
   - "How long should it stay on screen?"

2. **Animation**
   - "What animation style? (fade, slide, bounce)"
   - "Should text animate in word-by-word or all at once?"

3. **Audio**
   - "Keep current background music?"
   - "Should audio fade out at the end?"

4. **Export**
   - "What quality/resolution for export?"
   - "Include audio in export?"

### MODE 3: IMPLEMENT

```python
# Add text element with animation
python skills/canva-video/scripts/add_text.py \
  --design "DESIGN_ID" \
  --text "Your Message Here" \
  --start 5.0 \
  --duration 3.0 \
  --animation "fade-in"

# Add video clip
python skills/canva-video/scripts/add_clip.py \
  --design "DESIGN_ID" \
  --clip "path/to/video.mp4" \
  --start 0.0 \
  --trim-start 2.0 \
  --trim-end 10.0

# Update timing
python skills/canva-video/scripts/update_timing.py \
  --design "DESIGN_ID" \
  --element "ELEMENT_ID" \
  --start 3.0 \
  --duration 5.0

# Change video duration
python skills/canva-video/scripts/set_duration.py \
  --design "DESIGN_ID" \
  --duration 20.0

# Add background music
python skills/canva-video/scripts/add_audio.py \
  --design "DESIGN_ID" \
  --audio "path/to/music.mp3" \
  --volume 0.5 \
  --loop true
```

## Available Scripts

### Analysis Scripts
- `analyze_video.py` - Full video breakdown
- `get_timeline.py` - Timeline elements and timing
- `extract_frames.py` - Get keyframes as images
- `get_audio_info.py` - Audio track details

### Edit Scripts
- `add_text.py` - Add animated text
- `add_clip.py` - Insert video clip
- `add_image.py` - Add static or animated image
- `add_audio.py` - Add music/voiceover
- `update_timing.py` - Change element timing
- `update_animation.py` - Change animation style
- `set_duration.py` - Change total duration
- `remove_element.py` - Delete element from timeline

### Creation Scripts
- `create_video.py` - New blank video
- `create_from_template.py` - From Canva template

## Animation Types

Text animations:
- `fade-in` / `fade-out`
- `slide-up` / `slide-down` / `slide-left` / `slide-right`
- `zoom-in` / `zoom-out`
- `bounce`
- `typewriter`
- `wipe`
- `pop`

Element animations:
- `pan` - Move across screen
- `ken-burns` - Slow zoom on images
- `rotate`
- `scale`
- `baseline` - None (static)

## Audio Handling

```python
# Add background music
python skills/canva-video/scripts/add_audio.py \
  --design "DESIGN_ID" \
  --audio "music.mp3" \
  --type "background" \
  --volume 0.3

# Add voiceover
python skills/canva-video/scripts/add_audio.py \
  --design "DESIGN_ID" \
  --audio "voiceover.mp3" \
  --type "voiceover" \
  --start 2.0

# Adjust audio timing
python skills/canva-video/scripts/update_audio.py \
  --design "DESIGN_ID" \
  --audio-id "AUDIO_ID" \
  --fade-in 1.0 \
  --fade-out 2.0
```

## Video Export

Use `canva-export` skill with these options:
- **MP4** - Standard video format
- **GIF** - Animated GIF (no audio)
- **WebM** - Web-optimized video

Quality options:
- `720p` - 1280x720, smaller file
- `1080p` - 1920x1080, standard
- `4K` - 3840x2160, highest quality

## Timeline Best Practices

1. **Leave breathing room** - Don't cram too many elements
2. **Text timing** - 2-3 seconds minimum for readability
3. **Transitions** - Use sparingly, keep consistent
4. **Audio levels** - Music lower than voiceover
5. **CTA timing** - Save call-to-action for end

## Safety Guidelines

1. **Preview before export** - Check timing looks right
2. **Backup audio** - Keep original audio files
3. **Version control** - Duplicate before major changes
4. **File sizes** - Be aware of upload limits

## Example Interactions

### "Add text that says 'Shop Now' at the end"
```
[PLAN]
- Video is 15 seconds
- Add "Shop Now" at 12-15s
- Recommend animation style

[CLARIFY]
- "Add at 12s, display for 3s until end?"
- "Animation style: 'pop' or 'slide-up'?"
- "Font and color preferences?"

[IMPLEMENT]
- Add text element
- Apply animation
- Verify timing
```

### "Replace the background music"
```
[PLAN]
- Current music: "Upbeat.mp3" (15s)
- Need new music file

[CLARIFY]
- "What music file should I use?"
- "Same volume level?"
- "Fade in/out at ends?"

[IMPLEMENT]
- Remove current audio
- Add new audio track
- Apply fades if requested
```

## Output Files

- `output/videos/` - Exported videos
- `output/frames/` - Extracted keyframes
- `output/audio/` - Extracted audio
- `output/logs/video_edits.json` - Edit history
