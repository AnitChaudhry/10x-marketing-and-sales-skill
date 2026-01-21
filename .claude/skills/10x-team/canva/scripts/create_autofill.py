#!/usr/bin/env python3
"""
Create Autofill Script
Create a design by autofilling a brand template (Enterprise feature)
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Create design from brand template autofill (Enterprise)')
    parser.add_argument('template_id', help='Brand template ID')
    parser.add_argument('--data', '-d', required=True, help='Autofill data as JSON string')
    parser.add_argument('--data-file', '-f', help='Autofill data from JSON file (overrides --data)')
    parser.add_argument('--title', '-t', help='Title for generated design')
    parser.add_argument('--wait', action='store_true', default=True, help='Wait for autofill to complete')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        # Parse data
        if args.data_file:
            with open(args.data_file) as f:
                data = json.load(f)
        else:
            data = json.loads(args.data)

        client = get_client()

        print(f"Starting autofill job...")
        result = client.create_autofill(
            brand_template_id=args.template_id,
            data=data,
            title=args.title
        )

        job_id = result.get('job', {}).get('id')
        if not job_id:
            raise Exception(f"Failed to start autofill job: {result}")

        print(f"Autofill job started: {job_id}")

        if args.wait:
            print("Waiting for autofill to complete...")
            result = client.wait_for_autofill(job_id, timeout=args.timeout)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            job = result.get('job', {})
            status = job.get('status', 'unknown')

            print(f"\nAutofill Job Status: {status.upper()}")
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
                error = job.get('error', {})
                if error:
                    print(f"  Error: {error.get('message', 'Unknown error')}")

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if "403" in str(e) or "forbidden" in str(e).lower():
            print("Note: Autofill requires Canva Enterprise plan.", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
