#!/usr/bin/env python3
"""
Get Design Pages Script
Retrieve page thumbnails and information for a Canva design
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Get Canva design pages with thumbnails')
    parser.add_argument('design_id', help='Design ID')
    parser.add_argument('--offset', '-o', type=int, default=1, help='Page offset (1-indexed)')
    parser.add_argument('--limit', '-l', type=int, default=50, help='Max pages (max: 200)')
    parser.add_argument('--all', '-a', action='store_true', help='Get all pages')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        all_pages = []
        offset = args.offset

        while True:
            result = client.get_design_pages(
                design_id=args.design_id,
                offset=offset,
                limit=min(args.limit, 200)
            )

            pages = result.get('pages', [])
            all_pages.extend(pages)

            if not args.all or len(pages) < args.limit:
                break

            offset += len(pages)

        if args.json:
            print(json.dumps({'pages': all_pages, 'total': len(all_pages)}, indent=2))
        else:
            print(f"\nDesign Pages: {len(all_pages)} page(s)")
            print("=" * 70)

            for i, page in enumerate(all_pages, 1):
                page_id = page.get('id', 'N/A')
                width = page.get('width', 'N/A')
                height = page.get('height', 'N/A')

                print(f"\n  Page {i}:")
                print(f"    ID: {page_id}")
                print(f"    Dimensions: {width} x {height}")

                thumbnail = page.get('thumbnail', {})
                if thumbnail.get('url'):
                    print(f"    Thumbnail: {thumbnail.get('url')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
