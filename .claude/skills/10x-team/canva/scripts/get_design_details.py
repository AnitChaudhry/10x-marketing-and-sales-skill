#!/usr/bin/env python3
"""
Get Design Details Script
Get detailed information about a specific Canva design
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Get details of a Canva design')
    parser.add_argument('design_id', help='Design ID')
    parser.add_argument('--pages', '-p', action='store_true', help='Include page details')
    parser.add_argument('--formats', '-f', action='store_true', help='Include available export formats')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        # Get basic design info
        result = client.get_design(args.design_id)
        design = result.get('design', {})

        # Optionally get pages
        pages_data = None
        if args.pages:
            pages_result = client.get_design_pages(args.design_id)
            pages_data = pages_result.get('pages', [])

        # Optionally get export formats
        formats_data = None
        if args.formats:
            formats_result = client.get_export_formats(args.design_id)
            formats_data = formats_result.get('formats', [])

        if args.json:
            output = {'design': design}
            if pages_data is not None:
                output['pages'] = pages_data
            if formats_data is not None:
                output['export_formats'] = formats_data
            print(json.dumps(output, indent=2))
        else:
            print(f"Design Details")
            print(f"=" * 50)
            print(f"ID: {design.get('id')}")
            print(f"Title: {design.get('title', 'Untitled')}")
            print(f"Owner: {design.get('owner', {}).get('display_name', 'Unknown')}")
            print(f"Created: {design.get('created_at', 'N/A')}")
            print(f"Modified: {design.get('updated_at', 'N/A')}")
            print(f"Page Count: {design.get('page_count', 'N/A')}")

            urls = design.get('urls', {})
            if urls.get('edit_url'):
                print(f"Edit URL: {urls.get('edit_url')}")
            if urls.get('view_url'):
                print(f"View URL: {urls.get('view_url')}")

            if pages_data:
                print(f"\nPages ({len(pages_data)}):")
                for i, page in enumerate(pages_data, 1):
                    print(f"  {i}. {page.get('id', 'N/A')}")
                    if page.get('thumbnail'):
                        print(f"     Thumbnail: {page.get('thumbnail', {}).get('url', 'N/A')[:50]}...")

            if formats_data:
                print(f"\nAvailable Export Formats:")
                for fmt in formats_data:
                    print(f"  - {fmt.get('type', 'unknown')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
