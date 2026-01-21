#!/usr/bin/env python3
"""
Move Items Script
Move designs, folders, or assets between folders in Canva
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Move items to a folder in Canva')
    parser.add_argument('--items', '-i', required=True, nargs='+', help='Item IDs to move')
    parser.add_argument('--folder', '-f', required=True, help='Target folder ID (use "root" for Projects root)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()
        result = client.move_items(args.items, args.folder)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Successfully moved {len(args.items)} item(s) to folder {args.folder}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
