#!/usr/bin/env python3
"""
Search Designs Script
Search and filter Canva designs with various criteria
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Search Canva designs')
    parser.add_argument('query', nargs='?', help='Search query (max 255 chars)')
    parser.add_argument('--limit', '-l', type=int, default=50, help='Max results (max: 100)')
    parser.add_argument('--ownership', '-o', choices=['owned', 'shared'], help='Filter by ownership')
    parser.add_argument('--sort', '-s',
                       choices=['relevance', 'modified_descending', 'modified_ascending',
                               'title_descending', 'title_ascending'],
                       default='modified_descending',
                       help='Sort order')
    parser.add_argument('--all', '-a', action='store_true', help='Get all results (pagination)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        all_designs = []
        continuation = None

        while True:
            result = client.list_designs(
                limit=min(args.limit, 100),
                continuation=continuation,
                ownership=args.ownership,
                sort_by=args.sort,
                query=args.query
            )

            designs = result.get('designs', [])
            all_designs.extend(designs)

            if not args.all or not result.get('continuation'):
                break

            continuation = result.get('continuation')

            if len(all_designs) >= args.limit:
                all_designs = all_designs[:args.limit]
                break

        if args.json:
            print(json.dumps({'designs': all_designs, 'total': len(all_designs)}, indent=2))
        else:
            print(f"\nSearch Results: {len(all_designs)} design(s)")
            print("=" * 70)

            for design in all_designs:
                design_id = design.get('id', 'N/A')
                title = design.get('title', 'Untitled')
                created = design.get('created_at', 'N/A')[:10] if design.get('created_at') else 'N/A'
                modified = design.get('updated_at', 'N/A')[:10] if design.get('updated_at') else 'N/A'

                print(f"\n  {title}")
                print(f"    ID: {design_id}")
                print(f"    Created: {created} | Modified: {modified}")

                urls = design.get('urls', {})
                if urls.get('edit_url'):
                    print(f"    Edit: {urls.get('edit_url')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
