#!/usr/bin/env python3
"""
Create Folder Script
Create a new folder in Canva Projects
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Create a folder in Canva')
    parser.add_argument('--name', '-n', required=True, help='Folder name')
    parser.add_argument('--parent', '-p', help='Parent folder ID (use "root" for Projects root)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()
        result = client.create_folder(args.name, args.parent)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            folder = result.get('folder', {})
            print(f"Folder created successfully!")
            print(f"  ID: {folder.get('id')}")
            print(f"  Name: {folder.get('name')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
