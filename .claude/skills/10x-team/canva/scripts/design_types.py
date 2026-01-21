#!/usr/bin/env python3
"""
Design Types Configuration
Complete reference for all supported design types and dimensions
"""

# All dimensions in pixels

DESIGN_TYPES = {
    # ==========================================
    # INSTAGRAM
    # ==========================================
    "instagram_post": {
        "width": 1080,
        "height": 1080,
        "aspect_ratio": "1:1",
        "description": "Standard square Instagram feed post",
        "platform": "instagram",
        "use_case": "General feed content"
    },
    "instagram_post_portrait": {
        "width": 1080,
        "height": 1350,
        "aspect_ratio": "4:5",
        "description": "Portrait Instagram post (best engagement)",
        "platform": "instagram",
        "use_case": "Maximum screen real estate on mobile"
    },
    "instagram_post_landscape": {
        "width": 1080,
        "height": 566,
        "aspect_ratio": "1.91:1",
        "description": "Landscape Instagram post",
        "platform": "instagram",
        "use_case": "Wide visuals, panoramas"
    },
    "instagram_story": {
        "width": 1080,
        "height": 1920,
        "aspect_ratio": "9:16",
        "description": "Instagram Story or Reel",
        "platform": "instagram",
        "use_case": "Full-screen vertical content"
    },
    "instagram_reel": {
        "width": 1080,
        "height": 1920,
        "aspect_ratio": "9:16",
        "description": "Instagram Reel",
        "platform": "instagram",
        "use_case": "Short-form video content"
    },
    "instagram_reel_cover": {
        "width": 1080,
        "height": 1440,
        "aspect_ratio": "3:4",
        "description": "Instagram Reel cover/thumbnail",
        "platform": "instagram",
        "use_case": "Profile grid thumbnail"
    },

    # ==========================================
    # FACEBOOK
    # ==========================================
    "facebook_post": {
        "width": 1080,
        "height": 1080,
        "aspect_ratio": "1:1",
        "description": "Facebook feed post (square)",
        "platform": "facebook",
        "use_case": "General feed content"
    },
    "facebook_post_landscape": {
        "width": 1200,
        "height": 630,
        "aspect_ratio": "1.91:1",
        "description": "Facebook landscape post / link preview",
        "platform": "facebook",
        "use_case": "Link previews, shared articles"
    },
    "facebook_cover": {
        "width": 820,
        "height": 312,
        "aspect_ratio": "2.63:1",
        "description": "Facebook page cover photo",
        "platform": "facebook",
        "use_case": "Page header banner"
    },
    "facebook_cover_photo": {
        "width": 851,
        "height": 315,
        "aspect_ratio": "2.7:1",
        "description": "Facebook profile cover photo",
        "platform": "facebook",
        "use_case": "Personal profile header"
    },
    "facebook_story": {
        "width": 1080,
        "height": 1920,
        "aspect_ratio": "9:16",
        "description": "Facebook Story",
        "platform": "facebook",
        "use_case": "Full-screen ephemeral content"
    },
    "facebook_event_cover": {
        "width": 1920,
        "height": 1005,
        "aspect_ratio": "1.91:1",
        "description": "Facebook event cover",
        "platform": "facebook",
        "use_case": "Event promotion"
    },
    "facebook_group_cover": {
        "width": 1640,
        "height": 856,
        "aspect_ratio": "1.91:1",
        "description": "Facebook group cover",
        "platform": "facebook",
        "use_case": "Group header banner"
    },

    # ==========================================
    # LINKEDIN
    # ==========================================
    "linkedin_post": {
        "width": 1200,
        "height": 628,
        "aspect_ratio": "1.91:1",
        "description": "LinkedIn feed post (landscape)",
        "platform": "linkedin",
        "use_case": "Standard feed content"
    },
    "linkedin_post_square": {
        "width": 1200,
        "height": 1200,
        "aspect_ratio": "1:1",
        "description": "LinkedIn square post",
        "platform": "linkedin",
        "use_case": "Feed content, infographics"
    },
    "linkedin_post_portrait": {
        "width": 720,
        "height": 900,
        "aspect_ratio": "4:5",
        "description": "LinkedIn portrait post (mobile optimized)",
        "platform": "linkedin",
        "use_case": "Mobile-first content"
    },
    "linkedin_banner": {
        "width": 1584,
        "height": 396,
        "aspect_ratio": "4:1",
        "description": "LinkedIn personal profile banner",
        "platform": "linkedin",
        "use_case": "Personal branding"
    },
    "linkedin_company_banner": {
        "width": 1128,
        "height": 191,
        "aspect_ratio": "5.9:1",
        "description": "LinkedIn company page banner",
        "platform": "linkedin",
        "use_case": "Company branding"
    },
    "linkedin_article_cover": {
        "width": 1920,
        "height": 1080,
        "aspect_ratio": "16:9",
        "description": "LinkedIn article cover image",
        "platform": "linkedin",
        "use_case": "Article header"
    },

    # ==========================================
    # TWITTER/X
    # ==========================================
    "twitter_post": {
        "width": 1200,
        "height": 675,
        "aspect_ratio": "16:9",
        "description": "Twitter/X post image",
        "platform": "twitter",
        "use_case": "Tweet image"
    },
    "twitter_header": {
        "width": 1500,
        "height": 500,
        "aspect_ratio": "3:1",
        "description": "Twitter/X profile header",
        "platform": "twitter",
        "use_case": "Profile banner"
    },
    "twitter_card": {
        "width": 1200,
        "height": 628,
        "aspect_ratio": "1.91:1",
        "description": "Twitter card / link preview",
        "platform": "twitter",
        "use_case": "Shared link preview"
    },

    # ==========================================
    # YOUTUBE
    # ==========================================
    "youtube_thumbnail": {
        "width": 1280,
        "height": 720,
        "aspect_ratio": "16:9",
        "description": "YouTube video thumbnail",
        "platform": "youtube",
        "use_case": "Video thumbnail for clicks"
    },
    "youtube_banner": {
        "width": 2560,
        "height": 1440,
        "aspect_ratio": "16:9",
        "description": "YouTube channel banner",
        "platform": "youtube",
        "use_case": "Channel art"
    },
    "youtube_end_screen": {
        "width": 1920,
        "height": 1080,
        "aspect_ratio": "16:9",
        "description": "YouTube end screen",
        "platform": "youtube",
        "use_case": "End screen elements"
    },

    # ==========================================
    # PINTEREST
    # ==========================================
    "pinterest_pin": {
        "width": 1000,
        "height": 1500,
        "aspect_ratio": "2:3",
        "description": "Standard Pinterest pin",
        "platform": "pinterest",
        "use_case": "Standard pin format"
    },
    "pinterest_pin_long": {
        "width": 1000,
        "height": 2100,
        "aspect_ratio": "1:2.1",
        "description": "Long Pinterest pin",
        "platform": "pinterest",
        "use_case": "Infographics, step-by-step"
    },
    "pinterest_square": {
        "width": 1000,
        "height": 1000,
        "aspect_ratio": "1:1",
        "description": "Square Pinterest pin",
        "platform": "pinterest",
        "use_case": "Product showcases"
    },

    # ==========================================
    # TIKTOK
    # ==========================================
    "tiktok_video": {
        "width": 1080,
        "height": 1920,
        "aspect_ratio": "9:16",
        "description": "TikTok video",
        "platform": "tiktok",
        "use_case": "Full-screen vertical video"
    },

    # ==========================================
    # EMAIL
    # ==========================================
    "email_header": {
        "width": 600,
        "height": 200,
        "aspect_ratio": "3:1",
        "description": "Email header/banner",
        "platform": "email",
        "use_case": "Email marketing header"
    },
    "email_banner": {
        "width": 600,
        "height": 300,
        "aspect_ratio": "2:1",
        "description": "Email promotional banner",
        "platform": "email",
        "use_case": "Email body banner"
    },

    # ==========================================
    # PRESENTATIONS
    # ==========================================
    "presentation_16_9": {
        "width": 1920,
        "height": 1080,
        "aspect_ratio": "16:9",
        "description": "Widescreen presentation",
        "platform": "presentation",
        "use_case": "Modern presentations",
        "canva_preset": "presentation"
    },
    "presentation_4_3": {
        "width": 1024,
        "height": 768,
        "aspect_ratio": "4:3",
        "description": "Standard presentation",
        "platform": "presentation",
        "use_case": "Traditional presentations"
    },

    # ==========================================
    # DOCUMENTS
    # ==========================================
    "document_a4": {
        "width": 595,
        "height": 842,
        "aspect_ratio": "1:1.41",
        "description": "A4 document",
        "platform": "print",
        "use_case": "Standard print document"
    },
    "document_letter": {
        "width": 612,
        "height": 792,
        "aspect_ratio": "1:1.29",
        "description": "US Letter document",
        "platform": "print",
        "use_case": "US standard print"
    },

    # ==========================================
    # MARKETING MATERIALS
    # ==========================================
    "poster_a3": {
        "width": 1191,
        "height": 1684,
        "aspect_ratio": "1:1.41",
        "description": "A3 poster",
        "platform": "print",
        "use_case": "Large print posters"
    },
    "poster_a2": {
        "width": 1684,
        "height": 2384,
        "aspect_ratio": "1:1.41",
        "description": "A2 poster",
        "platform": "print",
        "use_case": "Extra large posters"
    },
    "flyer_a5": {
        "width": 420,
        "height": 595,
        "aspect_ratio": "1:1.41",
        "description": "A5 flyer",
        "platform": "print",
        "use_case": "Handouts, flyers"
    },
    "business_card": {
        "width": 1050,
        "height": 600,
        "aspect_ratio": "1.75:1",
        "description": "Business card (3.5x2 inch)",
        "platform": "print",
        "use_case": "Standard business card"
    },

    # ==========================================
    # DIGITAL ADS
    # ==========================================
    "ad_leaderboard": {
        "width": 728,
        "height": 90,
        "aspect_ratio": "8:1",
        "description": "Leaderboard ad",
        "platform": "ads",
        "use_case": "Website header banner"
    },
    "ad_medium_rectangle": {
        "width": 300,
        "height": 250,
        "aspect_ratio": "6:5",
        "description": "Medium rectangle ad",
        "platform": "ads",
        "use_case": "Sidebar ad"
    },
    "ad_skyscraper": {
        "width": 160,
        "height": 600,
        "aspect_ratio": "1:3.75",
        "description": "Skyscraper ad",
        "platform": "ads",
        "use_case": "Tall sidebar ad"
    },
    "ad_large_rectangle": {
        "width": 336,
        "height": 280,
        "aspect_ratio": "6:5",
        "description": "Large rectangle ad",
        "platform": "ads",
        "use_case": "In-content ad"
    },
    "ad_square": {
        "width": 250,
        "height": 250,
        "aspect_ratio": "1:1",
        "description": "Square ad",
        "platform": "ads",
        "use_case": "Sidebar square"
    },

    # ==========================================
    # BRANDING
    # ==========================================
    "logo_square": {
        "width": 500,
        "height": 500,
        "aspect_ratio": "1:1",
        "description": "Square logo",
        "platform": "branding",
        "use_case": "Brand logo"
    },
    "logo_horizontal": {
        "width": 800,
        "height": 200,
        "aspect_ratio": "4:1",
        "description": "Horizontal logo",
        "platform": "branding",
        "use_case": "Header logo"
    },
    "favicon": {
        "width": 512,
        "height": 512,
        "aspect_ratio": "1:1",
        "description": "Website favicon",
        "platform": "web",
        "use_case": "Browser tab icon"
    },
}

# Platform groupings for easy lookup
PLATFORMS = {
    "instagram": [
        "instagram_post",
        "instagram_post_portrait",
        "instagram_post_landscape",
        "instagram_story",
        "instagram_reel",
        "instagram_reel_cover"
    ],
    "facebook": [
        "facebook_post",
        "facebook_post_landscape",
        "facebook_cover",
        "facebook_cover_photo",
        "facebook_story",
        "facebook_event_cover",
        "facebook_group_cover"
    ],
    "linkedin": [
        "linkedin_post",
        "linkedin_post_square",
        "linkedin_post_portrait",
        "linkedin_banner",
        "linkedin_company_banner",
        "linkedin_article_cover"
    ],
    "twitter": [
        "twitter_post",
        "twitter_header",
        "twitter_card"
    ],
    "youtube": [
        "youtube_thumbnail",
        "youtube_banner",
        "youtube_end_screen"
    ],
    "pinterest": [
        "pinterest_pin",
        "pinterest_pin_long",
        "pinterest_square"
    ],
    "tiktok": [
        "tiktok_video"
    ],
    "email": [
        "email_header",
        "email_banner"
    ],
    "presentation": [
        "presentation_16_9",
        "presentation_4_3"
    ],
    "print": [
        "document_a4",
        "document_letter",
        "poster_a3",
        "poster_a2",
        "flyer_a5",
        "business_card"
    ],
    "ads": [
        "ad_leaderboard",
        "ad_medium_rectangle",
        "ad_skyscraper",
        "ad_large_rectangle",
        "ad_square"
    ],
    "branding": [
        "logo_square",
        "logo_horizontal",
        "favicon"
    ]
}


def get_design_type(name: str) -> dict:
    """Get design type configuration by name"""
    return DESIGN_TYPES.get(name)


def get_platform_types(platform: str) -> list:
    """Get all design types for a platform"""
    return PLATFORMS.get(platform, [])


def list_all_types() -> list:
    """List all design type names"""
    return list(DESIGN_TYPES.keys())


def list_platforms() -> list:
    """List all platforms"""
    return list(PLATFORMS.keys())


def search_types(query: str) -> list:
    """Search design types by keyword"""
    query = query.lower()
    results = []
    for name, config in DESIGN_TYPES.items():
        if (query in name.lower() or
            query in config.get("description", "").lower() or
            query in config.get("platform", "").lower() or
            query in config.get("use_case", "").lower()):
            results.append(name)
    return results


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Design Types Reference")
    parser.add_argument("--list", "-l", action="store_true", help="List all design types")
    parser.add_argument("--platforms", "-p", action="store_true", help="List all platforms")
    parser.add_argument("--get", "-g", help="Get specific design type info")
    parser.add_argument("--platform", help="List types for a specific platform")
    parser.add_argument("--search", "-s", help="Search design types")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.list:
        types = list_all_types()
        if args.json:
            print(json.dumps(types, indent=2))
        else:
            print("Available Design Types:")
            print("=" * 50)
            for t in types:
                config = DESIGN_TYPES[t]
                print(f"  {t}: {config['width']}x{config['height']} - {config['description']}")

    elif args.platforms:
        platforms = list_platforms()
        if args.json:
            print(json.dumps(PLATFORMS, indent=2))
        else:
            print("Available Platforms:")
            print("=" * 50)
            for p in platforms:
                print(f"\n{p.upper()}:")
                for t in PLATFORMS[p]:
                    config = DESIGN_TYPES[t]
                    print(f"  - {t}: {config['width']}x{config['height']}")

    elif args.get:
        config = get_design_type(args.get)
        if config:
            if args.json:
                print(json.dumps(config, indent=2))
            else:
                print(f"\n{args.get.upper()}")
                print("=" * 50)
                for key, value in config.items():
                    print(f"  {key}: {value}")
        else:
            print(f"Design type '{args.get}' not found")

    elif args.platform:
        types = get_platform_types(args.platform)
        if types:
            if args.json:
                result = {t: DESIGN_TYPES[t] for t in types}
                print(json.dumps(result, indent=2))
            else:
                print(f"\n{args.platform.upper()} Design Types:")
                print("=" * 50)
                for t in types:
                    config = DESIGN_TYPES[t]
                    print(f"  {t}: {config['width']}x{config['height']} - {config['description']}")
        else:
            print(f"Platform '{args.platform}' not found")

    elif args.search:
        results = search_types(args.search)
        if results:
            if args.json:
                result = {t: DESIGN_TYPES[t] for t in results}
                print(json.dumps(result, indent=2))
            else:
                print(f"\nSearch results for '{args.search}':")
                print("=" * 50)
                for t in results:
                    config = DESIGN_TYPES[t]
                    print(f"  {t}: {config['width']}x{config['height']} - {config['description']}")
        else:
            print(f"No design types found for '{args.search}'")

    else:
        parser.print_help()
