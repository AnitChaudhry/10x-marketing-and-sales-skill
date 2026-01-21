#!/usr/bin/env python3
"""
Import Design Script
Import a PPTX, PDF, AI, or PSD file into Canva as a new design
"""

import argparse
import json
import sys
from pathlib import Path
from canva_client import get_client


SUPPORTED_FORMATS = ['.pptx', '.ppt', '.pdf', '.ai', '.psd']


def main():
    parser = argparse.ArgumentParser(
        description='Import a file into Canva as a design',
        epilog=f'Supported formats: {", ".join(SUPPORTED_FORMATS)}'
    )
    parser.add_argument('file', help='Path to file to import')
    parser.add_argument('--title', '-t', help='Title for imported design (default: filename)')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds (default: 300)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--no-wait', action='store_true', help='Start import and return immediately (no waiting)')

    args = parser.parse_args()

    file_path = Path(args.file)

    if not file_path.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    if file_path.suffix.lower() not in SUPPORTED_FORMATS:
        print(f"Error: Unsupported format: {file_path.suffix}", file=sys.stderr)
        print(f"Supported formats: {', '.join(SUPPORTED_FORMATS)}", file=sys.stderr)
        sys.exit(1)

    title = args.title or file_path.stem

    try:
        client = get_client()

        if args.no_wait:
            # Start import job only
            result = client.create_design_import(str(file_path), title)

            if args.json:
                print(json.dumps(result, indent=2))
            else:
                job = result.get('job', {})
                print(f"Import job started!")
                print(f"  Job ID: {job.get('id')}")
                print(f"  Status: {job.get('status')}")
                print(f"\nUse 'python get_import_status.py {job.get('id')}' to check status")
        else:
            # Import and wait for completion
            print(f"Importing {file_path.name}...")
            result = client.import_and_wait(str(file_path), title, args.timeout)

            if args.json:
                print(json.dumps(result, indent=2))
            else:
                job = result.get('job', {})
                designs = job.get('result', {}).get('designs', [])

                print(f"\nImport completed successfully!")
                print(f"  Status: {job.get('status')}")
                print(f"  Designs created: {len(designs)}")

                for i, design in enumerate(designs, 1):
                    print(f"\n  Design {i}:")
                    print(f"    ID: {design.get('id')}")
                    print(f"    Title: {design.get('title', 'Untitled')}")
                    print(f"    Pages: {design.get('page_count', 'N/A')}")
                    urls = design.get('urls', {})
                    if urls.get('edit_url'):
                        print(f"    Edit URL: {urls.get('edit_url')}")
                    if urls.get('view_url'):
                        print(f"    View URL: {urls.get('view_url')}")

    except TimeoutError as e:
        print(f"Timeout: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
