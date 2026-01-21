#!/usr/bin/env python3
"""
Download Export Script
Download a completed export by job ID
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Download an export from Canva')
    parser.add_argument('export_id', help='Export job ID')
    parser.add_argument('--output', '-o', default='output/exports', help='Output directory')
    parser.add_argument('--filename', '-f', help='Base filename (without extension)')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        print(f"Downloading export {args.export_id}...")
        files = client.download_export(
            export_id=args.export_id,
            output_dir=args.output,
            filename=args.filename,
            timeout=args.timeout
        )

        if args.json:
            print(json.dumps({'files': files}, indent=2))
        else:
            print(f"Downloaded {len(files)} file(s):")
            for f in files:
                print(f"  {f}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
