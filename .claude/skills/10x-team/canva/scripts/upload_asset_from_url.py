#!/usr/bin/env python3
"""
Upload Asset from URL Script
Upload an asset from URL to Canva (Preview API)
"""

import argparse
import json
import sys
import time
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Upload asset from URL (max 100MB for videos)')
    parser.add_argument('url', help='Source URL of the asset')
    parser.add_argument('--name', '-n', required=True, help='Asset name')
    parser.add_argument('--wait', action='store_true', default=True, help='Wait for upload to complete')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        print(f"Starting upload from URL...")
        result = client.create_url_asset_upload(
            name=args.name,
            url=args.url
        )

        job_id = result.get('job', {}).get('id')
        if not job_id:
            raise Exception(f"Failed to start upload job: {result}")

        print(f"Upload job started: {job_id}")

        if args.wait:
            print("Waiting for upload to complete...")
            start_time = time.time()

            while time.time() - start_time < args.timeout:
                status_result = client.get_url_asset_upload_status(job_id)
                status = status_result.get('job', {}).get('status')

                if status == 'success':
                    result = status_result
                    break
                elif status == 'failed':
                    error = status_result.get('job', {}).get('error', {})
                    raise Exception(f"Upload failed: {error.get('message', 'Unknown error')}")

                time.sleep(2)
            else:
                raise TimeoutError(f"Upload timed out after {args.timeout} seconds")

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            job = result.get('job', {})
            status = job.get('status', 'unknown')

            print(f"\nUpload Job Status: {status.upper()}")
            print("=" * 50)

            if status == 'success':
                asset_result = job.get('result', {})
                asset = asset_result.get('asset', {})
                print(f"  Asset ID: {asset.get('id', 'N/A')}")
                print(f"  Name: {asset.get('name', 'N/A')}")
                print(f"  Type: {asset.get('type', 'N/A')}")

                thumbnail = asset.get('thumbnail', {})
                if thumbnail.get('url'):
                    print(f"  Thumbnail: {thumbnail.get('url')}")
            else:
                print(f"  Job ID: {job_id}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
