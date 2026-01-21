#!/usr/bin/env python3
"""
Import from URL Script
Import a design from a URL (PDF, PPTX, AI, PSD)
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Import design from URL')
    parser.add_argument('url', help='Source URL of the file to import')
    parser.add_argument('--title', '-t', help='Title for imported design')
    parser.add_argument('--wait', action='store_true', default=True, help='Wait for import to complete')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        print(f"Starting import from URL...")
        result = client.create_url_design_import(
            url=args.url,
            title=args.title
        )

        job_id = result.get('job', {}).get('id')
        if not job_id:
            raise Exception(f"Failed to start import job: {result}")

        print(f"Import job started: {job_id}")

        if args.wait:
            print("Waiting for import to complete...")
            # Poll for completion
            import time
            start_time = time.time()

            while time.time() - start_time < args.timeout:
                status_result = client.get_url_design_import_status(job_id)
                status = status_result.get('job', {}).get('status')

                if status == 'success':
                    result = status_result
                    break
                elif status == 'failed':
                    error = status_result.get('job', {}).get('error', {})
                    raise Exception(f"Import failed: {error.get('message', 'Unknown error')}")

                time.sleep(3)
            else:
                raise TimeoutError(f"Import timed out after {args.timeout} seconds")

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            job = result.get('job', {})
            status = job.get('status', 'unknown')

            print(f"\nImport Job Status: {status.upper()}")
            print("=" * 50)

            if status == 'success':
                design_result = job.get('result', {})
                design = design_result.get('design', {})
                print(f"  Design ID: {design.get('id', 'N/A')}")
                print(f"  Title: {design.get('title', 'N/A')}")

                urls = design.get('urls', {})
                if urls.get('edit_url'):
                    print(f"\n  Edit URL: {urls.get('edit_url')}")
            else:
                print(f"  Job ID: {job_id}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
