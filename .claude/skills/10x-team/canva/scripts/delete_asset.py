#!/usr/bin/env python3
"""
Delete Asset Script
Delete an asset from Canva (moves to trash)
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Delete a Canva asset')
    parser.add_argument('asset_id', help='Asset ID to delete')
    parser.add_argument('--confirm', '-y', action='store_true', help='Skip confirmation')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    if not args.confirm:
        response = input(f"Are you sure you want to delete asset {args.asset_id}? [y/N]: ")
        if response.lower() != 'y':
            print("Cancelled.")
            return

    try:
        client = get_client()
        result = client.delete_asset(args.asset_id)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Asset {args.asset_id} deleted successfully (moved to trash)")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
