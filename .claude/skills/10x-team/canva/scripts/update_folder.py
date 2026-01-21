#!/usr/bin/env python3
"""
Update Folder Script
Rename a Canva folder
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Rename a Canva folder')
    parser.add_argument('folder_id', help='Folder ID')
    parser.add_argument('name', help='New folder name')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()
        result = client.update_folder(args.folder_id, args.name)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            folder = result.get('folder', {})
            print(f"\nFolder Renamed Successfully!")
            print("=" * 50)
            print(f"  ID:   {folder.get('id', args.folder_id)}")
            print(f"  Name: {folder.get('name', args.name)}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
