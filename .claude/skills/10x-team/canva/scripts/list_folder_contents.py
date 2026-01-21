#!/usr/bin/env python3
"""
List Folder Contents Script
List items in a specific Canva folder
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='List contents of a Canva folder')
    parser.add_argument('folder_id', help='Folder ID (use "root" for Projects root, "uploads" for Uploads)')
    parser.add_argument('--types', '-t', nargs='+', choices=['design', 'folder', 'image'],
                        help='Filter by item types')
    parser.add_argument('--sort', '-s',
                        choices=['modified_descending', 'modified_ascending', 'name_descending', 'name_ascending'],
                        default='modified_descending', help='Sort order')
    parser.add_argument('--limit', '-l', type=int, default=50, help='Maximum items to return')
    parser.add_argument('--all', '-a', action='store_true', help='Fetch all items (pagination)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        all_items = []
        continuation = None

        while True:
            result = client.list_folder_items(
                folder_id=args.folder_id,
                limit=min(args.limit, 100),
                continuation=continuation,
                item_types=args.types,
                sort_by=args.sort
            )

            items = result.get('items', [])
            all_items.extend(items)

            if not args.all or not result.get('continuation'):
                break

            continuation = result.get('continuation')

            if len(all_items) >= args.limit and not args.all:
                break

        if args.json:
            print(json.dumps({'items': all_items, 'total': len(all_items)}, indent=2))
        else:
            print(f"Folder Contents: {args.folder_id}")
            print(f"=" * 50)
            print(f"Total items: {len(all_items)}\n")

            # Group by type
            designs = [i for i in all_items if i.get('type') == 'design']
            folders = [i for i in all_items if i.get('type') == 'folder']
            images = [i for i in all_items if i.get('type') == 'image']

            if folders:
                print(f"Folders ({len(folders)}):")
                for item in folders:
                    print(f"  [F] {item.get('name', 'Unnamed')} ({item.get('id')})")

            if designs:
                print(f"\nDesigns ({len(designs)}):")
                for item in designs:
                    name = item.get('name') or item.get('title') or 'Untitled'
                    print(f"  [D] {name} ({item.get('id')})")

            if images:
                print(f"\nImages ({len(images)}):")
                for item in images:
                    print(f"  [I] {item.get('name', 'Unnamed')} ({item.get('id')})")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
