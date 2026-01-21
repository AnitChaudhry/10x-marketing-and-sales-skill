#!/usr/bin/env python3
"""
Get Import Status Script
Check the status of a design import job
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Check status of a Canva import job')
    parser.add_argument('job_id', help='Import job ID')
    parser.add_argument('--wait', '-w', action='store_true', help='Wait for completion')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds (with --wait)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        if args.wait:
            print(f"Waiting for import job {args.job_id}...")
            result = client.wait_for_import(args.job_id, args.timeout)
        else:
            result = client.get_design_import_status(args.job_id)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            job = result.get('job', {})
            print(f"Import Job Status")
            print(f"=" * 50)
            print(f"Job ID: {job.get('id')}")
            print(f"Status: {job.get('status')}")

            if job.get('status') == 'success':
                designs = job.get('result', {}).get('designs', [])
                print(f"Designs created: {len(designs)}")

                for i, design in enumerate(designs, 1):
                    print(f"\n  Design {i}:")
                    print(f"    ID: {design.get('id')}")
                    print(f"    Title: {design.get('title', 'Untitled')}")
                    urls = design.get('urls', {})
                    if urls.get('edit_url'):
                        print(f"    Edit URL: {urls.get('edit_url')}")

            elif job.get('status') == 'failed':
                error = job.get('error', {})
                print(f"Error: {error.get('message', 'Unknown error')}")
                print(f"Code: {error.get('code', 'N/A')}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
