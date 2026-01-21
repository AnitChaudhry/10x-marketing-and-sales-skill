# Social Media Content Strategy & Commands

## Overview

Social media commands generate platform-specific content optimized for each channel's unique audience, format, and algorithm.

## Main Command: `/social`

**Description:** Social media content generation for various platforms

**Usage:**
```bash
/social <platform> <type>
```

## Supported Platforms

| Platform | Max Length | Best For | Frequency |
|----------|-----------|----------|-----------|
| **Twitter/X** | 280 chars | News, thoughts, engagement | Daily+ |
| **LinkedIn** | 3,000 chars | Professional insights, B2B | 2-3x week |
| **Instagram** | Caption unlimited | Visual storytelling, B2C | Daily |
| **TikTok** | Unlimited | Entertainment, trends, viral | 1-3x day |
| **YouTube** | Unlimited | Long-form, tutorials | 1-2x week |

## Content Types by Platform

### Twitter/X
- **post** - Single tweet (280 characters)
- **thread** - Multi-tweet thread (5-20 tweets)
- **reply** - Response to existing tweet
- **retweet** - Share with comment

**Examples:**
```bash
/social twitter post "product launch announcement"
/social twitter thread "10 tips for SaaS marketing"
/social x thread "behind-the-scenes company culture"
```

**Best Practices:**
- Lead with value or curiosity
- Use hashtags sparingly (2-3)
- Engage with community, don't just broadcast
- Post multiple times daily for visibility
- Threads should have strong opening tweet

### LinkedIn
- **post** - Single post with image/link
- **article** - Long-form article (LinkedIn native)
- **carousel** - Multi-image carousel post

**Examples:**
```bash
/social linkedin post "industry insights"
/social linkedin article "thought leadership piece"
/social linkedin carousel "5-part professional development guide"
```

**Best Practices:**
- Professional but personal tone
- Share business insights and lessons learned
- Use images (posts with images get 2x engagement)
- Engage with others' content first
- Post 1-3 times per week for B2B

### Instagram
- **post** - Feed post with image/carousel
- **reel** - Short-form video (15-90 sec)
- **story** - 24-hour story (1-10 images/videos)
- **carousel** - Multi-image swipeable post

**Examples:**
```bash
/social instagram post "product launch announcement"
/social instagram reel "5-minute tutorial"
/social instagram story "behind-the-scenes"
/social instagram carousel "10 tips carousel"
```

**Best Practices:**
- High-quality visuals essential
- Captions tell the story, not just image
- Use calls-to-action (link in bio)
- Hashtags: 20-30 per post
- Reels get 30% more impressions than feed posts
- Post 1x daily for consistent growth

### TikTok
- **reel** - Short-form video (15-600 sec)
- **series** - Multi-part video series
- **trend** - Trending sound/format use

**Examples:**
```bash
/social tiktok reel "behind-the-scenes product creation"
/social tiktok trend "trending audio with product twist"
/social tiktok series "7-part marketing tips series"
```

**Best Practices:**
- First 3 seconds hook viewers (50% stop-through)
- Vertical video (9:16 aspect ratio)
- Trending sounds get 50% more views
- Authenticity > perfection (TikTok algorithm favors genuine)
- Caption important moments
- Post 3-5x per day for algorithm boost
- Go viral quickly or disappear (1-24 hour relevance window)

### YouTube
- **shorts** - YouTube Shorts (15-60 sec)
- **community** - Community tab post
- **premiere** - Scheduled video premiere
- **transcript** - Video transcript/caption

**Examples:**
```bash
/social youtube "shorts tutorial segment"
/social youtube community "poll or announcement"
```

**Best Practices:**
- Strong thumbnail (3:2 aspect ratio)
- Compelling title (60 characters max)
- Description with links and timestamps
- Chapters/timestamps improve SEO
- Tags but don't keyword stuff
- Consistency more important than frequency

## Social Media Strategy Framework

### Content Pillars (4-6 Main Topics)

Define 4-6 pillar topics your brand will consistently create about:

Example for SaaS:
1. **Product Updates** - Feature releases, roadmap
2. **Thought Leadership** - Industry insights, advice
3. **Behind-the-Scenes** - Company culture, team
4. **Customer Stories** - Testimonials, case studies
5. **Education** - How-tos, tips, learning
6. **Community** - Engagement, questions, conversations

### Content Mix by Platform

**Twitter:** 50% replies/engagement, 25% thoughts, 15% promotes, 10% polls
**LinkedIn:** 40% insights, 30% promotes, 20% engagement, 10% stories
**Instagram:** 40% product/service, 30% lifestyle/behind-scenes, 20% educational, 10% promotional
**TikTok:** 60% entertainment/trend-following, 25% educational, 15% promotional
**YouTube:** 70% primary content, 20% shorts, 10% community posts

## Social Media Content Calendar

### Template

```markdown
# Social Media Calendar - [Month] [Year]

## Overview
- Content pillars: [Pillar 1], [Pillar 2], etc.
- Posting frequency: [X posts per day/week]
- Team: [Team members]

## Weekly Schedule

### Week 1: [Dates]

#### Monday
- **Platform:** Twitter
- **Content:** [Description]
- **Time:** 9 AM
- **Link:** [Link]

#### Tuesday
- **Platform:** LinkedIn
- **Content:** [Description]
- **Time:** 8 AM
- **Link:** [Link]

...

## Performance Metrics
| Date | Platform | Content | Impressions | Engagement |
|------|----------|---------|------------|-----------|
| | | | | |
```

## Content Generation Workflow

### Single Post
```bash
/social [platform] [type]
# Prompts for content idea if not provided
# Generates platform-optimized copy
# Saves to assets/social/{platform}/
```

### Content Series
```bash
# 1. Plan series
/plan "create 7-day content series"

# 2. Generate each piece
/social [platform] [type] "topic: [specific topic]"

# 3. Coordinate timing
# (Schedule across platforms in calendar)
```

### Campaign Launch
```bash
# 1. Create copy
/content:good "social media campaign for product launch"

# 2. Generate platform-specific versions
/social twitter thread "product launch"
/social linkedin post "product launch B2B angle"
/social instagram carousel "product launch visual story"
/social tiktok reel "product launch entertainment style"

# 3. Design visuals
/design:generate "[platform]-specific graphics"

# 4. Schedule posts
# (Coordinate timing across platforms)
```

## Output Locations

```
assets/
├── social/
│   ├── twitter/
│   │   ├── posts/
│   │   ├── threads/
│   │   └── replies/
│   ├── linkedin/
│   │   ├── posts/
│   │   ├── articles/
│   │   └── carousels/
│   ├── instagram/
│   │   ├── posts/
│   │   ├── reels/
│   │   ├── stories/
│   │   └── captions/
│   ├── tiktok/
│   │   ├── reels/
│   │   ├── trends/
│   │   └── scripts/
│   └── youtube/
│       ├── shorts/
│       ├── scripts/
│       └── metadata/

docs/
├── social-media-calendar.md     # Content calendar
├── social-media-strategy.md     # Overall strategy
└── social-media-performance.md  # Analytics tracking
```

## Social Media File Naming

```
social_{platform}_{type}_{campaign}_{description}_{timestamp}.{ext}

Examples:
- social_twitter_thread_launch_10tips_20251209.txt
- social_instagram_carousel_features_5steps_20251209.md
- social_tiktok_reel_tutorial_setup_20251209.txt
- social_linkedin_article_insights_20251209.md
```

## Platform-Specific Templates

### Twitter Thread Template
```markdown
# Twitter Thread: [Title]

## Tweet 1 (Hook)
[Compelling opening tweet that makes people want to read more]

## Tweet 2
[First point with explanation]

## Tweet 3
[Supporting evidence or example]

## Tweet 4
[Second main point]

## Tweet 5
[Practical takeaway]

## Tweet 6 (CTA)
[Call-to-action - link, follow, etc.]

---

## Notes
- Best time to post: [day/time]
- Hashtags: #tag1 #tag2
- Related: [Link to related thread]
```

### LinkedIn Post Template
```markdown
# LinkedIn Post: [Title]

## Hook (First Line)
[Stop-the-scroll hook that makes people continue reading]

## Story/Context
[2-3 sentence explanation or story]

## Main Message
[Key insight or lesson learned]

## Supporting Points
- Point 1: [Explanation]
- Point 2: [Explanation]
- Point 3: [Explanation]

## Takeaway
[What should readers do with this?]

## Call-to-Action
[Specific action: Comment your thoughts, connect, visit link, etc.]

---

## Image: [Description]
Hashtags: #hashtag1 #hashtag2 #hashtag3
```

### Instagram Caption Template
```markdown
# Instagram Post: [Title]

## Hook (First Line)
[Emoji] [Stop-the-scroll line]

## Story
[Main message or story - 2-3 paragraphs]

## Call-to-Action
[What you want followers to do]

## Hashtags
#hashtag1 #hashtag2 [30-40 hashtags total]

---

## Image/Video Description
## Type: [post/reel/carousel/story]
## Aspect Ratio: [1:1/4:5/9:16]
## Visuals: [Description]
```

### TikTok Script Template
```markdown
# TikTok: [Title]

## Hook (0-3 seconds)
[Visuals: Description]
[Audio: Suggested sound/voiceover]
[Text: On-screen text]

## Body (3-45 seconds)
[Scene breakdown by 5-10 second increments]

## Ending/CTA (45-60 seconds)
[Final action or hashtag]

---

## Production Notes
- Target audience: [Age/interest]
- Trending sound: [Yes/No - which?]
- Special effects: [None/Effects to use]
- Voiceover: [Yes/No]
- Music: [Suggested track]
```

## Social Media Performance Metrics

### Key Metrics by Platform

**Twitter:**
- Impressions
- Engagement rate (likes, replies, retweets)
- Click-through rate
- Followers gained

**LinkedIn:**
- Impressions
- Engagement rate
- Click-through rate
- Profile views
- Followers gained

**Instagram:**
- Reach
- Engagement rate (likes, comments)
- Saves
- Shares
- Follower growth
- Website clicks

**TikTok:**
- Views
- Watch time average
- Engagement rate (likes, comments, shares)
- Follower growth
- Click-through rate

**YouTube:**
- Views
- Watch time
- Click-through rate (CTR)
- Average view duration
- Engagement rate
- Subscriber growth

### Tracking Template

```markdown
# Social Media Performance - [Month] [Year]

## Twitter
- Posts: [count]
- Total Impressions: [number]
- Engagement Rate: [%]
- Followers: [number] (+[count] this month)

## LinkedIn
- Posts: [count]
- Total Impressions: [number]
- Engagement Rate: [%]
- Followers: [number] (+[count])

## Instagram
- Posts: [count]
- Total Reach: [number]
- Engagement Rate: [%]
- Followers: [number] (+[count])

## TikTok
- Videos: [count]
- Total Views: [number]
- Engagement Rate: [%]
- Followers: [number] (+[count])

## Overall
- Total followers: [number]
- Best performing content: [type/topic]
- Engagement rate average: [%]
```

## Best Practices

1. **Platform First** - Optimize for each platform's unique format/algorithm
2. **Audience First** - Know who you're talking to on each platform
3. **Consistency Matters** - Regular posting > sporadic posting
4. **Engagement Drives Algorithm** - Reply to comments and DMs
5. **Authenticity Wins** - Especially on TikTok and Instagram
6. **Timing Matters** - Post when your audience is active
7. **Repurpose Content** - One blog becomes 10+ social posts
8. **Tell Stories** - Connect emotionally, not just promote
9. **Use Trends** - Participate in trending topics/sounds
10. **Test and Adjust** - Track metrics and optimize

## Common Platform Strategies

### Twitter: Community Building
- Share hot takes and opinions
- Engage with followers' content daily
- Thread format for depth
- Participate in trending conversations

### LinkedIn: Thought Leadership
- Share professional insights and lessons
- Tell career/business stories
- Ask engaging questions
- Mix promotional with educational

### Instagram: Visual Storytelling
- High-quality, consistent visuals
- Behind-the-scenes content builds connection
- Reels for algorithm boost
- Strong community engagement

### TikTok: Entertainment & Trends
- Authenticity beats polish
- Jump on trending sounds/challenges
- Don't overthink it - raw content performs
- Consistent posting essential

### YouTube: Authority Building
- Consistent upload schedule
- Longer, valuable content builds audience
- Series format keeps viewers coming back
- Transcripts help SEO

## Repurposing Content Across Platforms

One blog post → Multiple social assets:

```
Blog Post "5 Marketing Tips"
├── Twitter: 5-tweet thread (one tip per tweet)
├── LinkedIn: 1 professional insight post
├── Instagram: 5-image carousel
├── TikTok: 5 short clips (one tip each)
├── Email: Newsletter featuring post
└── YouTube: 5-minute video version
```

## Scheduling Posts: `/social:schedule`

### Overview

The `/social:schedule` command creates optimized posting schedules for your social media content. This command plans when and where to post your content across platforms based on audience analytics and platform best practices.

**Important:** This is schedule PLANNING only. The command generates a calendar and timing recommendations. Actual API-based posting is not yet implemented.

### Command Syntax

```bash
/social:schedule <period>
/social:schedule <period> [--campaign "Campaign Name"]
```

### Schedule Types

#### 1. Day Schedule (`day`)

Plans optimal posting times for a single day across all platforms.

```bash
/social:schedule day
```

**Output:** Single-day posting plan with hourly recommendations
- Considers timezone and audience peak hours
- Recommends specific post times
- Balances content type across platforms
- Filename: `schedule-day.md`

**Use case:** Daily content planning, quick scheduling for tomorrow

#### 2. Week Schedule (`week`)

Plans a full week of content distribution across platforms.

```bash
/social:schedule week
```

**Output:** 7-day content calendar with optimal posting times
- Distributes content evenly across days
- Avoids posting conflicts
- Balances platform coverage (Twitter, LinkedIn, Instagram, TikTok, YouTube)
- Considers content type frequency per platform
- Filename: `schedule-week.md`

**Use case:** Weekly content planning, consistent posting strategy

#### 3. Month/Campaign Schedule (`month` or `campaign`)

Plans content distribution for a full month or specific campaign.

```bash
/social:schedule month
/social:schedule campaign "Product Launch"
/social:schedule campaign "Black Friday Sale"
```

**Output:** Full month (or campaign-specific) content calendar
- Distributes 20-30 posts across platforms
- Aligns with campaign milestones if specified
- Ensures consistent posting frequency
- Includes backup posting times
- Filename: `schedule-month.md` or `schedule-campaign-{name}.md`

**Use case:** Monthly content planning, campaign launch coordination

### Command Workflow

```
1. GATHER CONTENT
   ↓
2. TIMING ANALYSIS
   ↓
3. CREATE SCHEDULE
   ↓
4. GENERATE OUTPUT
```

#### Step 1: Gather Content

The command scans `content/social/` directory for pending posts:
- Collects all content waiting to be scheduled
- If directory is empty, prompts for content topics
- Organizes by content type (post, thread, reel, article, etc.)

#### Step 2: Timing Analysis

Uses platform data and audience insights to determine optimal times:
- **Platform peak hours:** When each platform's audience is most active
- **Timezone:** Considers user's audience timezone
- **Content type:** Different content types perform better at different times
  - Educational content: Morning (8-10 AM)
  - Entertainment: Evening (5-9 PM)
  - News/updates: Mid-morning (11 AM-12 PM)
  - Stories: Throughout day
- **Platform algorithms:** Posting frequency that maximizes visibility
- **Engagement patterns:** Historical data on audience activity

#### Step 3: Create Schedule

Distributes content across the period while:
- Balancing platforms (no more than 2 posts per platform per day)
- Avoiding posting conflicts (no same-platform posts within 2 hours)
- Maintaining content variety (mix of content types)
- Respecting platform frequency guidelines:
  - Twitter: 1-3 posts per day
  - LinkedIn: 2-3 posts per week
  - Instagram: 1 post per day
  - TikTok: 1-3 posts per day
  - YouTube: 1 post per week

#### Step 4: Generate Output

Creates schedule documents and organizes them:

```
assets/posts/
├── schedule-day.md
├── schedule-week.md
├── schedule-month.md
└── schedule-campaign-product-launch.md

docs/
├── social-media-calendar.md (main reference)
└── posting-times.md (timezone-specific times)
```

### Output Format

#### Schedule Document Structure

```markdown
# Social Media Schedule - [Period]

## Overview
- Period: [Dates]
- Total Posts: [Number]
- Platforms: [Twitter, LinkedIn, Instagram, TikTok, YouTube]
- Average Posts/Day: [Number]
- Timezone: [User's Timezone]

## Daily Breakdown

### Day 1: Monday [Date]

#### 9:00 AM - Twitter
- Content Type: Thread
- Topic: [Topic]
- Description: [Brief description]
- Engagement Goal: [e.g., 100+ retweets]

#### 12:00 PM - LinkedIn
- Content Type: Post
- Topic: [Topic]
- Description: [Brief description]
- Target Audience: [e.g., B2B professionals]

#### 5:00 PM - Instagram
- Content Type: Reel
- Topic: [Topic]
- Description: [Brief description]
- Duration: [15-60 seconds]

### Day 2: Tuesday [Date]
...

## Platform Summary

### Twitter
- Posts: [Count]
- Types: [thread, post, reply, retweet]
- Best Times: [9 AM, 12 PM, 6 PM]
- Frequency: [3x per week average]

### LinkedIn
- Posts: [Count]
- Types: [article, post, carousel]
- Best Times: [8 AM, 12 PM]
- Frequency: [2-3x per week]

### Instagram
- Posts: [Count]
- Types: [post, reel, story, carousel]
- Best Times: [9 AM, 1 PM, 5 PM]
- Frequency: [Daily]

### TikTok
- Posts: [Count]
- Types: [reel, trend, series]
- Best Times: [12 PM, 6 PM, 9 PM]
- Frequency: [1-3x per day]

### YouTube
- Posts: [Count]
- Types: [shorts, premiere, community]
- Best Times: [3 PM, 6 PM]
- Frequency: [1x per week]

## Optimization Notes
- Peak engagement expected: [Time range]
- Low-activity times to avoid: [Times]
- Holiday adjustments: [If applicable]
- Campaign priorities: [If applicable]

## Next Steps
1. Review schedule for content availability
2. Adjust times based on team capacity
3. Prepare content assets by [date]
4. Activate schedule on [date]
```

### Example Usage

#### Daily Schedule

```bash
/social:schedule day

# Output: assets/posts/schedule-day.md
# Shows optimal posting times for today/tomorrow
```

**Example Output:**
```markdown
# Social Media Schedule - Today (Dec 24, 2025)

## Overview
- Timezone: America/Los_Angeles
- Total Posts: 4
- Platforms: Twitter, LinkedIn, Instagram, TikTok

## Daily Schedule

### 9:00 AM - Twitter Thread
Topic: "5 Tips for Holiday Marketing"
→ Link to content file

### 12:00 PM - LinkedIn Post
Topic: "Year-End Reflections on Marketing"
→ Link to content file

### 5:00 PM - Instagram Reel
Topic: "Product Showcase"
→ Link to content file

### 8:00 PM - TikTok Video
Topic: "Behind-the-scenes year review"
→ Link to content file
```

#### Weekly Schedule

```bash
/social:schedule week

# Output: assets/posts/schedule-week.md
# Shows 7-day distribution across platforms
```

**Example Output:**
```markdown
# Social Media Schedule - Week of Dec 23-29, 2025

## Overview
- Total Posts: 18
- Daily Average: 2.6 posts
- Platforms: All 5 major platforms

## Weekly Breakdown

### Monday (Dec 23)
- 9:00 AM: Twitter thread (5 tips)
- 12:00 PM: LinkedIn article (year review)
- 5:00 PM: Instagram post (team photo)

### Tuesday (Dec 24)
- 10:00 AM: TikTok reel (holiday greeting)
- 2:00 PM: Twitter post (holiday wishes)
- 6:00 PM: Instagram story (behind-scenes)

### Wednesday (Dec 25)
- No scheduled posts (Holiday)

### Thursday (Dec 26)
- 9:00 AM: LinkedIn post (comeback momentum)
- 1:00 PM: YouTube shorts (quick tips)
- 5:00 PM: Instagram carousel (5-step process)

### Friday (Dec 27)
- 10:00 AM: Twitter thread (week recap)
- 3:00 PM: TikTok reel (trending format)
- 7:00 PM: Instagram reel (trending sound)

### Saturday (Dec 28)
- 12:00 PM: LinkedIn post (weekend reading)
- 5:00 PM: Twitter poll (engagement)

### Sunday (Dec 29)
- 6:00 PM: Instagram story (week preview)
- 8:00 PM: TikTok reel (entertainment)

## Platform Summary
Twitter: 4 posts (threads + replies)
LinkedIn: 3 posts (articles + posts)
Instagram: 5 posts (reels + carousels)
TikTok: 3 posts (reels)
YouTube: 1 shorts

## Performance Targets
- Twitter engagement: 300+ likes, 50+ retweets
- LinkedIn reach: 5,000+ impressions
- Instagram reach: 10,000+ impressions
- TikTok views: 50,000+
- YouTube views: 5,000+
```

#### Campaign Schedule

```bash
/social:schedule campaign "Product Launch"

# Output: assets/posts/schedule-campaign-product-launch.md
# Shows campaign-specific posting timeline
```

**Example Output:**
```markdown
# Social Media Schedule - Product Launch Campaign

## Campaign Overview
- Launch Date: January 15, 2026
- Duration: 4 weeks (Dec 15 - Jan 15)
- Total Posts: 60
- Budget Focus: Heavy front-loading (week 1)
- Platforms: All 5 major platforms

## Campaign Phases

### Phase 1: Teaser (Week 1, Dec 15-21)
- Build anticipation
- Posts: 15 total
- Twitter: Daily tweets + 2 threads
- LinkedIn: 3 thought leadership posts
- Instagram: 3 teaser posts + stories
- TikTok: 3 behind-scenes clips
- YouTube: 1 sneak peek shorts

### Phase 2: Launch Week (Week 2, Dec 22-28)
- Maximum visibility and engagement
- Posts: 25 total
- Heavy increase in all platforms
- Live Q&As and real-time engagement
- Influencer coordination

### Phase 3: Momentum (Week 3-4, Dec 29-Jan 15)
- Customer stories and testimonials
- Posts: 20 total
- Reduced frequency but higher quality
- Focus on engagement and conversion

## Daily Posting Schedule

### Day 1: Monday, Dec 15
- 8:00 AM: Twitter post (Teaser)
- 12:00 PM: LinkedIn post (Industry context)
- 5:00 PM: Instagram post + story

... (continues for full campaign duration)

## Success Metrics
- Twitter: 10,000+ impressions, 500+ engagement
- LinkedIn: 50,000+ impressions, 1,000+ clicks
- Instagram: 100,000+ impressions, 5,000+ engagement
- TikTok: 500,000+ total views
- YouTube: 50,000+ total views
```

### Schedule Planning Considerations

#### Timezone Management

The command automatically:
- Detects user's timezone from profile
- Converts recommendations to local time
- Allows scheduling for different audience timezones

```bash
/social:schedule week --timezone "America/New_York"
```

#### Platform-Specific Best Times

| Platform | Best Times | Frequency | Strategy |
|----------|-----------|-----------|----------|
| **Twitter** | 9-10 AM, 12-1 PM, 5-6 PM | 3x/day | Real-time engagement, news |
| **LinkedIn** | 8 AM, 12 PM, 5-6 PM | 2-3x/week | Professional morning, lunch |
| **Instagram** | 9-10 AM, 1-2 PM, 5-6 PM | 1x/day | Peak engagement windows |
| **TikTok** | 6-10 AM, 7-11 PM | 2-3x/day | Morning scroll, night wind-down |
| **YouTube** | 3-4 PM, 6-8 PM | 1x/week | After-school, evening |

#### Content Type Timing

- **Educational:** 8-10 AM (morning learning)
- **Entertainment:** 5-9 PM (evening relaxation)
- **News/Updates:** 11 AM-12 PM (daily briefings)
- **Behind-the-scenes:** 2-4 PM (curiosity peak)
- **Promotional:** Varies by audience behavior
- **Stories/Casual:** Throughout day (evergreen)

### Integration with Content Creation

The schedule works with your content pipeline:

```
1. Create content with `/social [platform] [type]`
   ↓ Saves to content/social/

2. Review and organize content
   ↓ Prepare content assets

3. Run `/social:schedule [period]`
   ↓ Generates optimal posting plan

4. Approve schedule
   ↓ Review in assets/posts/

5. Execute schedule manually
   ↓ Use schedule document as reference
   ↓ Post at recommended times
```

### Tips for Effective Scheduling

1. **Review Before Scheduling** - Ensure all content is ready and approved
2. **Account for Holidays** - Adjust schedule for seasonal events
3. **Build in Flexibility** - Leave 20% of slots for real-time content
4. **Monitor Early Results** - Track performance of first week's posts
5. **Adjust Frequency** - If engagement drops, increase posting frequency
6. **Cross-Platform Coordination** - Ensure consistent messaging across platforms
7. **Team Preparation** - Schedule content creation 2 weeks in advance
8. **Time Buffer** - Post 30 minutes before peak engagement time (not exactly at peak)

### Common Schedule Patterns

#### Startup Growth Schedule
```
Monday-Friday: 3 posts/day (Twitter, LinkedIn, TikTok)
Saturday: 2 posts/day (Instagram, TikTok)
Sunday: 1 post/day (Instagram, YouTube Shorts)
Goal: Maximum visibility, rapid follower growth
```

#### B2B Professional Schedule
```
Monday-Friday: 2 posts/day (LinkedIn, Twitter)
Saturday-Sunday: 1 post/week (LinkedIn article only)
Goal: Thought leadership, professional credibility
```

#### E-Commerce Schedule
```
Monday-Friday: 4 posts/day (all platforms)
Saturday-Sunday: 3 posts/day (Instagram, TikTok focus)
Goal: Sales conversion, product discovery
```

#### Content Creator Schedule
```
Daily: 1-2 posts/day (TikTok, Instagram focus)
Weekly: 1 YouTube video
Twitter: 3-5 posts/day
Goal: Entertainment, community building
```

## YouTube to Social Posts

### `/youtube:social`
Convert YouTube video to multi-platform social posts.

**Usage:**
```bash
/youtube:social "https://youtube.com/watch?v=xxx"
/youtube:social "https://youtu.be/abc" twitter,linkedin
```

**Workflow:**
1. Extract video info via VidCap API (`vidcap.py summary`, `vidcap.py comments`)
2. Generate platform-specific content using hook writing rules
3. Apply brand voice consistency
4. Output per platform to `assets/posts/{platform}/`

**Hook Writing Rules (references/hook-writing.md):**
- AVOID: Punching keywords, clickbait, excessive emojis
- USE: Curiosity gaps, contrarian takes, story openers, specific numbers

## Implementation Status

### Working ✅
- `/social` - Content generation for all platforms
- `/youtube:social` - YouTube to social posts
- `/social:schedule` - Schedule planning (generates calendar docs)

### Not Implemented ❌ (from task.md)
- **X (Twitter) API** - Actual posting
- **Facebook Page API** - Actual posting
- **Threads API** - Actual posting
- **Instagram API** - Actual posting
- **YouTube API** - Actual posting
- **TikTok API** - Actual posting

**Note:** `/social:schedule` creates schedule documents only. API-based auto-posting requires external integrations.

## Next Steps

1. Define content pillars in `docs/social-media-strategy.md`
2. Create content calendar in `docs/social-media-calendar.md`
3. Generate first week of content:
   - `/social twitter post "topic"`
   - `/social linkedin post "topic"`
   - `/social instagram post "topic"`
   - `/social tiktok reel "topic"`
4. Create schedule with `/social:schedule week`
5. Review and approve schedule
6. Execute schedule following recommendations (manual posting)
7. Monitor performance in `docs/social-media-performance.md`
8. Optimize based on metrics
