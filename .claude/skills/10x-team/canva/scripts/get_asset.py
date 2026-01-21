#!/usr/bin/env python3
"""
Get Asset Script
Get details about a Canva asset
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Get Canva asset details')
    parser.add_argument('asset_id', help='Asset ID')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()
        result = client.get_asset(args.asset_id)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            asset = result.get('asset', {})
            print(f"\nAsset Details")
            print("=" * 50)
            print(f"  ID:     {asset.get('id', 'N/A')}")
            print(f"  Name:   {asset.get('name', 'N/A')}")
            print(f"  Type:   {asset.get('type', 'N/A')}")
            print(f"  Created: {asset.get('created_at', 'N/A')}")
            print(f"  Updated: {asset.get('updated_at', 'N/A')}")

            tags = asset.get('tags', [])
            if tags:
                print(f"  Tags:   {', '.join(tags)}")

            thumbnail = asset.get('thumbnail', {})
            if thumbnail.get('url'):
                print(f"\n  Thumbnail: {thumbnail.get('url')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
