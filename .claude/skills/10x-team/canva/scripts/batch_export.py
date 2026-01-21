#!/usr/bin/env python3
"""
Batch Export Script
Export multiple Canva designs at once
"""

import argparse
import json
import sys
import time
from pathlib import Path
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Export multiple Canva designs')
    parser.add_argument('--designs', '-d', nargs='+', required=True, help='Design IDs to export')
    parser.add_argument('--format', '-f', required=True,
                        choices=['pdf', 'png', 'jpg', 'pptx', 'mp4', 'gif'],
                        help='Export format')
    parser.add_argument('--output', '-o', default='output/exports', help='Output directory')
    parser.add_argument('--quality', '-q', choices=['standard', 'print'], help='PDF quality')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between exports in seconds')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout per export in seconds')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []
    errors = []

    try:
        client = get_client()

        for i, design_id in enumerate(args.designs, 1):
            print(f"[{i}/{len(args.designs)}] Exporting {design_id}...")

            try:
                # Get design info for filename
                design_info = client.get_design(design_id)
                design = design_info.get('design', {})
                title = design.get('title', design_id)

                # Clean filename
                safe_title = "".join(c if c.isalnum() or c in ' -_' else '_' for c in title)[:50]

                # Export and download
                files = client.export_and_download(
                    design_id=design_id,
                    format_type=args.format,
                    output_dir=str(output_dir),
                    filename=safe_title,
                    quality=args.quality,
                    timeout=args.timeout
                )

                results.append({
                    'design_id': design_id,
                    'title': title,
                    'files': files,
                    'status': 'success'
                })

                print(f"  Success: {', '.join(files)}")

            except Exception as e:
                error_msg = str(e)
                errors.append({
                    'design_id': design_id,
                    'error': error_msg
                })
                print(f"  Error: {error_msg}")

            # Delay between exports to avoid rate limits
            if i < len(args.designs):
                time.sleep(args.delay)

        if args.json:
            print(json.dumps({
                'successful': results,
                'errors': errors,
                'summary': {
                    'total': len(args.designs),
                    'success': len(results),
                    'failed': len(errors)
                }
            }, indent=2))
        else:
            print(f"\n{'=' * 50}")
            print(f"Batch Export Complete")
            print(f"  Total: {len(args.designs)}")
            print(f"  Success: {len(results)}")
            print(f"  Failed: {len(errors)}")
            print(f"  Output: {output_dir}")

            if errors:
                print(f"\nFailed exports:")
                for err in errors:
                    print(f"  - {err['design_id']}: {err['error']}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
