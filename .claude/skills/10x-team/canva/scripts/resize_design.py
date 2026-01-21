#!/usr/bin/env python3
"""
Resize Design Script
Create a resized copy of a Canva design (Premium feature)
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Resize a Canva design (Premium feature)')
    parser.add_argument('design_id', help='Design ID to resize')
    parser.add_argument('--width', '-w', type=int, required=True, help='New width in pixels')
    parser.add_argument('--height', '-H', type=int, required=True, help='New height in pixels')
    parser.add_argument('--title', '-t', help='Title for the resized design')
    parser.add_argument('--wait', action='store_true', default=True, help='Wait for resize to complete')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    # Validate dimensions (max 25M total pixels)
    total_pixels = args.width * args.height
    if total_pixels > 25000000:
        print(f"Error: Total pixels ({total_pixels:,}) exceeds maximum (25,000,000)", file=sys.stderr)
        sys.exit(1)

    try:
        client = get_client()

        print(f"Starting resize job...")
        result = client.create_resize(
            design_id=args.design_id,
            width=args.width,
            height=args.height,
            title=args.title
        )

        job_id = result.get('job', {}).get('id')
        if not job_id:
            raise Exception(f"Failed to start resize job: {result}")

        print(f"Resize job started: {job_id}")

        if args.wait:
            print("Waiting for resize to complete...")
            result = client.wait_for_resize(job_id, timeout=args.timeout)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            job = result.get('job', {})
            status = job.get('status', 'unknown')

            print(f"\nResize Job Status: {status.upper()}")
            print("=" * 50)

            if status == 'success':
                design_result = job.get('result', {})
                design = design_result.get('design', {})
                print(f"  New Design ID: {design.get('id', 'N/A')}")
                print(f"  Title: {design.get('title', 'N/A')}")
                print(f"  Dimensions: {args.width} x {args.height}")

                urls = design.get('urls', {})
                if urls.get('edit_url'):
                    print(f"\n  Edit URL: {urls.get('edit_url')}")
            else:
                print(f"  Job ID: {job_id}")
                error = job.get('error', {})
                if error:
                    print(f"  Error: {error.get('message', 'Unknown error')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
