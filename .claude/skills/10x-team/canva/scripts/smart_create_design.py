#!/usr/bin/env python3
"""
Smart Create Design Script
Create designs by platform/type name instead of specifying dimensions manually
"""

import argparse
import json
import sys
from design_types import DESIGN_TYPES, get_design_type, list_all_types, list_platforms, get_platform_types, search_types
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(
        description='Create Canva designs by platform/type name',
        epilog='Example: smart_create_design.py instagram_post --title "My Post"'
    )
    parser.add_argument('design_type', nargs='?', help='Design type name (e.g., instagram_post, linkedin_banner)')
    parser.add_argument('--title', '-t', help='Design title')
    parser.add_argument('--list', '-l', action='store_true', help='List all available design types')
    parser.add_argument('--platforms', '-p', action='store_true', help='List all platforms')
    parser.add_argument('--platform', help='List types for a specific platform')
    parser.add_argument('--search', '-s', help='Search for design types')
    parser.add_argument('--info', '-i', help='Show info about a design type without creating')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    # Handle list/search operations
    if args.list:
        types = list_all_types()
        if args.json:
            print(json.dumps({t: DESIGN_TYPES[t] for t in types}, indent=2))
        else:
            print("\nAvailable Design Types:")
            print("=" * 70)
            current_platform = None
            for t in sorted(types):
                config = DESIGN_TYPES[t]
                if config['platform'] != current_platform:
                    current_platform = config['platform']
                    print(f"\n{current_platform.upper()}:")
                print(f"  {t:<30} {config['width']:>4}x{config['height']:<4} - {config['description']}")
        return

    if args.platforms:
        platforms = list_platforms()
        if args.json:
            print(json.dumps(platforms, indent=2))
        else:
            print("\nAvailable Platforms:")
            for p in platforms:
                types = get_platform_types(p)
                print(f"  {p}: {len(types)} design type(s)")
        return

    if args.platform:
        types = get_platform_types(args.platform)
        if not types:
            print(f"Platform '{args.platform}' not found", file=sys.stderr)
            print(f"Available platforms: {', '.join(list_platforms())}", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps({t: DESIGN_TYPES[t] for t in types}, indent=2))
        else:
            print(f"\n{args.platform.upper()} Design Types:")
            print("=" * 70)
            for t in types:
                config = DESIGN_TYPES[t]
                print(f"  {t:<30} {config['width']:>4}x{config['height']:<4} - {config['description']}")
        return

    if args.search:
        results = search_types(args.search)
        if not results:
            print(f"No design types found for '{args.search}'", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps({t: DESIGN_TYPES[t] for t in results}, indent=2))
        else:
            print(f"\nSearch Results for '{args.search}':")
            print("=" * 70)
            for t in results:
                config = DESIGN_TYPES[t]
                print(f"  {t:<30} {config['width']:>4}x{config['height']:<4} - {config['description']}")
        return

    if args.info:
        config = get_design_type(args.info)
        if not config:
            print(f"Design type '{args.info}' not found", file=sys.stderr)
            similar = search_types(args.info)
            if similar:
                print(f"Did you mean: {', '.join(similar[:5])}", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps(config, indent=2))
        else:
            print(f"\n{args.info.upper()}")
            print("=" * 50)
            print(f"  Dimensions:    {config['width']} x {config['height']} px")
            print(f"  Aspect Ratio:  {config['aspect_ratio']}")
            print(f"  Platform:      {config['platform']}")
            print(f"  Description:   {config['description']}")
            print(f"  Use Case:      {config['use_case']}")
            if config.get('canva_preset'):
                print(f"  Canva Preset:  {config['canva_preset']}")
            print(f"\nTo create this design:")
            print(f"  .venv\\Scripts\\python.exe scripts/smart_create_design.py {args.info} --title \"My Design\"")
        return

    # Create design
    if not args.design_type:
        parser.print_help()
        print("\nExamples:")
        print("  smart_create_design.py instagram_post --title \"My Post\"")
        print("  smart_create_design.py linkedin_banner --title \"Profile Banner\"")
        print("  smart_create_design.py --list  # See all options")
        return

    config = get_design_type(args.design_type)
    if not config:
        print(f"Error: Design type '{args.design_type}' not found", file=sys.stderr)
        similar = search_types(args.design_type)
        if similar:
            print(f"Did you mean: {', '.join(similar[:5])}", file=sys.stderr)
        print(f"\nUse --list to see all available types", file=sys.stderr)
        sys.exit(1)

    try:
        client = get_client()

        # Check if this type has a Canva preset
        if config.get('canva_preset'):
            # Use preset
            result = client.create_design(
                design_type=config['canva_preset'],
                title=args.title
            )
        else:
            # Use custom dimensions
            result = client.create_design(
                width=config['width'],
                height=config['height'],
                title=args.title
            )

        if args.json:
            output = {
                'design_type': args.design_type,
                'config': config,
                'result': result
            }
            print(json.dumps(output, indent=2))
        else:
            design = result.get('design', {})
            print(f"\nDesign Created Successfully!")
            print("=" * 50)
            print(f"  Type:        {args.design_type}")
            print(f"  Dimensions:  {config['width']} x {config['height']} px")
            print(f"  Platform:    {config['platform']}")
            print(f"  ID:          {design.get('id')}")
            print(f"  Title:       {design.get('title', 'Untitled')}")

            urls = design.get('urls', {})
            if urls.get('edit_url'):
                print(f"\n  Edit URL: {urls.get('edit_url')}")
            if urls.get('view_url'):
                print(f"  View URL: {urls.get('view_url')}")

            print(f"\nNext steps:")
            print(f"  1. Open the edit URL to add content in Canva")
            print(f"  2. Export when done:")
            print(f"     .venv\\Scripts\\python.exe scripts/export_design.py \"{design.get('id')}\" --format png")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
