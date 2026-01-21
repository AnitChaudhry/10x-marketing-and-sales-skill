#!/usr/bin/env python3
"""
Get Export Formats Script
Get available export formats for a Canva design
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Get available export formats for a design')
    parser.add_argument('design_id', help='Design ID')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()
        result = client.get_export_formats(args.design_id)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            formats = result.get('export_formats', [])
            print(f"\nAvailable Export Formats")
            print("=" * 50)

            format_descriptions = {
                'pdf': 'PDF Document (quality: standard/print)',
                'png': 'PNG Image (size: small/medium/large)',
                'jpg': 'JPEG Image (quality: 1-100)',
                'pptx': 'PowerPoint Presentation',
                'mp4': 'MP4 Video',
                'gif': 'Animated GIF'
            }

            for fmt in formats:
                fmt_type = fmt.get('type', 'unknown')
                desc = format_descriptions.get(fmt_type, fmt_type)
                print(f"  - {fmt_type.upper()}: {desc}")

            print(f"\nTo export:")
            print(f"  .venv\\Scripts\\python.exe scripts/export_design.py \"{args.design_id}\" --format <format>")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
