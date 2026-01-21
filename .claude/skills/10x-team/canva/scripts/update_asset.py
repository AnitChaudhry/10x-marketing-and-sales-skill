#!/usr/bin/env python3
"""
Update Asset Script
Update asset name and/or tags in Canva
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Update Canva asset name and/or tags')
    parser.add_argument('asset_id', help='Asset ID')
    parser.add_argument('--name', '-n', help='New asset name')
    parser.add_argument('--tags', '-t', nargs='+', help='Tags (space-separated)')
    parser.add_argument('--add-tags', nargs='+', help='Tags to add to existing')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    if not args.name and not args.tags and not args.add_tags:
        parser.error("At least one of --name, --tags, or --add-tags is required")

    try:
        client = get_client()

        # If adding tags, get current tags first
        tags = args.tags
        if args.add_tags:
            current = client.get_asset(args.asset_id)
            current_tags = current.get('asset', {}).get('tags', [])
            tags = list(set(current_tags + args.add_tags))

        result = client.update_asset(
            asset_id=args.asset_id,
            name=args.name,
            tags=tags
        )

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            asset = result.get('asset', {})
            print(f"\nAsset Updated Successfully!")
            print("=" * 50)
            print(f"  ID:   {asset.get('id', args.asset_id)}")
            if args.name:
                print(f"  Name: {asset.get('name', args.name)}")
            if tags:
                print(f"  Tags: {', '.join(asset.get('tags', tags))}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
