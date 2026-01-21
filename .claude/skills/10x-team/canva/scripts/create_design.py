#!/usr/bin/env python3
"""
Create Design Script
Create a new blank design in Canva
"""

import argparse
import json
import sys
from canva_client import get_client


# Common design presets
DESIGN_PRESETS = {
    'instagram_post': {'type': 'instagram_post'},
    'instagram_story': {'type': 'instagram_story'},
    'facebook_post': {'type': 'facebook_post'},
    'presentation': {'type': 'presentation'},
    'doc': {'type': 'doc'},
    'whiteboard': {'type': 'whiteboard'},
    'poster': {'type': 'poster'},
    'flyer': {'type': 'flyer'},
    'a4': {'type': 'a4_document'},
    'letter': {'type': 'us_letter_document'},
}


def main():
    parser = argparse.ArgumentParser(description='Create a new design in Canva')
    parser.add_argument('--type', '-t', help=f'Design type: {", ".join(DESIGN_PRESETS.keys())} or custom')
    parser.add_argument('--width', '-W', type=int, help='Custom width in pixels')
    parser.add_argument('--height', '-H', type=int, help='Custom height in pixels')
    parser.add_argument('--title', help='Design title')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--list-types', action='store_true', help='List available design types')

    args = parser.parse_args()

    if args.list_types:
        print("Available design types:")
        for name in DESIGN_PRESETS:
            print(f"  {name}")
        print("\n  Or use --width and --height for custom dimensions")
        return

    if not args.type and not (args.width and args.height):
        parser.error("Either --type or both --width and --height are required")

    try:
        client = get_client()

        design_type = None
        width = None
        height = None

        if args.type:
            if args.type in DESIGN_PRESETS:
                design_type = args.type
            else:
                design_type = args.type  # Try as-is
        else:
            width = args.width
            height = args.height

        result = client.create_design(
            design_type=design_type,
            width=width,
            height=height,
            title=args.title
        )

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            design = result.get('design', {})
            print(f"Design created successfully!")
            print(f"  ID: {design.get('id')}")
            print(f"  Title: {design.get('title', 'Untitled')}")
            print(f"  URL: {design.get('urls', {}).get('edit_url', 'N/A')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
