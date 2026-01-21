#!/usr/bin/env python3
"""
List Brand Templates Script
List brand templates (Enterprise feature)
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='List Canva brand templates (Enterprise)')
    parser.add_argument('--query', '-q', help='Search query')
    parser.add_argument('--limit', '-l', type=int, default=25, help='Max results (max: 100)')
    parser.add_argument('--ownership', '-o', choices=['owned', 'shared'], help='Filter by ownership')
    parser.add_argument('--sort', '-s',
                       choices=['relevance', 'modified_descending', 'modified_ascending',
                               'title_descending', 'title_ascending'],
                       help='Sort order')
    parser.add_argument('--all', '-a', action='store_true', help='Get all results')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        all_templates = []
        continuation = None

        while True:
            result = client.list_brand_templates(
                limit=min(args.limit, 100),
                continuation=continuation,
                query=args.query,
                ownership=args.ownership,
                sort_by=args.sort
            )

            templates = result.get('brand_templates', [])
            all_templates.extend(templates)

            if not args.all or not result.get('continuation'):
                break

            continuation = result.get('continuation')

        if args.json:
            print(json.dumps({'brand_templates': all_templates, 'total': len(all_templates)}, indent=2))
        else:
            print(f"\nBrand Templates: {len(all_templates)}")
            print("=" * 70)

            if not all_templates:
                print("\n  No brand templates found.")
                print("  Note: Brand templates require Canva Enterprise plan.")
            else:
                for template in all_templates:
                    template_id = template.get('id', 'N/A')
                    title = template.get('title', 'Untitled')
                    created = template.get('created_at', 'N/A')[:10] if template.get('created_at') else 'N/A'

                    print(f"\n  {title}")
                    print(f"    ID: {template_id}")
                    print(f"    Created: {created}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if "403" in str(e) or "forbidden" in str(e).lower():
            print("Note: Brand templates require Canva Enterprise plan.", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
