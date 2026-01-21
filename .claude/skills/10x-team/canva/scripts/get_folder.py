#!/usr/bin/env python3
"""
Get Folder Script
Get details about a Canva folder
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Get Canva folder details')
    parser.add_argument('folder_id', help='Folder ID (use "root" for Projects, "uploads" for Uploads)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()
        result = client.get_folder(args.folder_id)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            folder = result.get('folder', {})
            print(f"\nFolder Details")
            print("=" * 50)
            print(f"  ID:     {folder.get('id', 'N/A')}")
            print(f"  Name:   {folder.get('name', 'N/A')}")
            print(f"  Created: {folder.get('created_at', 'N/A')}")
            print(f"  Updated: {folder.get('updated_at', 'N/A')}")

            if folder.get('parent_folder_id'):
                print(f"  Parent: {folder.get('parent_folder_id')}")

            print(f"\nTo list contents:")
            print(f"  .venv\\Scripts\\python.exe scripts/list_folder_contents.py \"{args.folder_id}\"")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
