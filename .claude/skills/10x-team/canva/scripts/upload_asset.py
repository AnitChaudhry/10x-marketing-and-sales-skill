#!/usr/bin/env python3
"""
Upload Asset Script
Upload an image or video to Canva asset library
"""

import argparse
import json
import sys
from pathlib import Path
from canva_client import get_client


# Supported file types based on Canva API documentation
SUPPORTED_IMAGES = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.heic', '.heif', '.tiff', '.tif']
SUPPORTED_VIDEOS = ['.mp4', '.mov', '.avi', '.webm', '.mkv', '.m4v', '.mpeg', '.mpg']
ALL_SUPPORTED = SUPPORTED_IMAGES + SUPPORTED_VIDEOS


def main():
    parser = argparse.ArgumentParser(
        description='Upload an asset to Canva',
        epilog=f'Supported images: {", ".join(SUPPORTED_IMAGES)}\nSupported videos: {", ".join(SUPPORTED_VIDEOS)}'
    )
    parser.add_argument('file', help='Path to file to upload')
    parser.add_argument('--name', '-n', help='Asset name (default: filename)')
    parser.add_argument('--timeout', type=int, default=300, help='Timeout in seconds (default: 300)')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--no-wait', action='store_true', help='Start upload and return immediately')

    args = parser.parse_args()

    file_path = Path(args.file)

    if not file_path.exists():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    if file_path.suffix.lower() not in ALL_SUPPORTED:
        print(f"Error: Unsupported format: {file_path.suffix}", file=sys.stderr)
        print(f"Supported formats: {', '.join(ALL_SUPPORTED)}", file=sys.stderr)
        sys.exit(1)

    # Check file size limits
    file_size = file_path.stat().st_size
    is_video = file_path.suffix.lower() in SUPPORTED_VIDEOS
    max_size = 500 * 1024 * 1024 if is_video else 50 * 1024 * 1024  # 500MB videos, 50MB images

    if file_size > max_size:
        limit_str = "500MB" if is_video else "50MB"
        print(f"Error: File too large. Maximum size for {'videos' if is_video else 'images'} is {limit_str}",
              file=sys.stderr)
        sys.exit(1)

    asset_name = args.name or file_path.stem

    try:
        client = get_client()

        if args.no_wait:
            # Start upload only
            result = client.create_asset_upload(asset_name, str(file_path))

            if args.json:
                print(json.dumps(result, indent=2))
            else:
                job = result.get('job', {})
                print(f"Upload job started!")
                print(f"  Job ID: {job.get('id')}")
                print(f"  Status: {job.get('status')}")
        else:
            # Upload and wait
            print(f"Uploading {file_path.name}...")
            result = client.upload_asset_and_wait(str(file_path), asset_name, args.timeout)

            if args.json:
                print(json.dumps(result, indent=2))
            else:
                job = result.get('job', {})
                asset = job.get('result', {}).get('asset', {})

                print(f"\nUpload completed successfully!")
                print(f"  Asset ID: {asset.get('id')}")
                print(f"  Name: {asset.get('name')}")
                print(f"  Type: {asset.get('type')}")
                if asset.get('thumbnail'):
                    print(f"  Thumbnail: {asset.get('thumbnail', {}).get('url', 'N/A')}")

    except TimeoutError as e:
        print(f"Timeout: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
