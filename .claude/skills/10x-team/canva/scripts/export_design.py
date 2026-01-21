#!/usr/bin/env python3
"""
Export a Canva design to specified format
"""

import sys
import json
import argparse
import requests
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from canva_client import get_client


def export_design(args):
    """Export a design to specified format"""

    client = get_client()

    print("=" * 60)
    print("CANVA DESIGN EXPORT")
    print("=" * 60)

    # Get design info first
    print(f"\n[*] Getting design info...")
    design = client.get_design(args.id)
    design_info = design.get('design', {})
    title = design_info.get('title', 'Untitled')

    print(f"   Design: {title}")
    print(f"   ID: {args.id}")

    # Check available formats
    formats = client.get_export_formats(args.id)
    available = [f.get('type') for f in formats.get('export_formats', [])]

    if args.format not in available:
        print(f"\n[X] Format '{args.format}' not available for this design")
        print(f"   Available formats: {', '.join(available)}")
        return None

    # Parse pages if specified
    pages = None
    if args.pages:
        if args.pages.lower() == 'all':
            pages = None
        else:
            pages = [int(p.strip()) for p in args.pages.split(',')]

    # Create export job
    print(f"\n[*] Starting export ({args.format.upper()})...")
    export_job = client.create_export(
        design_id=args.id,
        format_type=args.format,
        pages=pages,
        quality=args.quality
    )

    job_id = export_job.get('job', {}).get('id')
    print(f"   Job ID: {job_id}")

    # Wait for completion
    print("   Waiting for export to complete...")
    result = client.wait_for_export(job_id, timeout=args.timeout)

    status = result.get('job', {}).get('status')

    if status != 'completed':
        print(f"\n[X] Export failed with status: {status}")
        return None

    # Get download URL
    urls = result.get('job', {}).get('result', {}).get('urls', [])

    if not urls:
        print("\n[X] No download URLs returned")
        return None

    # Download files
    output_dir = Path(args.output) if args.output else (
        Path(__file__).parent.parent / 'output' / 'exports'
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    downloaded_files = []

    for i, url_info in enumerate(urls):
        url = url_info.get('url')

        # Determine filename
        safe_title = "".join(c if c.isalnum() or c in ' -_' else '_' for c in title)

        if len(urls) > 1:
            filename = f"{safe_title}_page{i+1}.{args.format}"
        else:
            filename = f"{safe_title}.{args.format}"

        filepath = output_dir / filename

        print(f"\n[*] Downloading: {filename}")

        response = requests.get(url, timeout=60)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            f.write(response.content)

        downloaded_files.append(str(filepath))
        print(f"   [OK] Saved to: {filepath}")

    # Log export
    log_dir = Path(__file__).parent.parent / 'output' / 'logs'
    log_dir.mkdir(parents=True, exist_ok=True)

    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'design_id': args.id,
        'design_title': title,
        'format': args.format,
        'quality': args.quality,
        'pages': args.pages,
        'files': downloaded_files
    }

    log_file = log_dir / 'export_log.json'

    # Append to existing log
    existing_logs = []
    if log_file.exists():
        with open(log_file, 'r') as f:
            existing_logs = json.load(f)

    existing_logs.append(log_entry)

    with open(log_file, 'w') as f:
        json.dump(existing_logs, f, indent=2)

    print(f"\n[OK] Export complete! {len(downloaded_files)} file(s) downloaded.")

    return downloaded_files


def main():
    parser = argparse.ArgumentParser(description='Export Canva design')
    parser.add_argument('--id', type=str, required=True,
                        help='Design ID to export')
    parser.add_argument('--format', type=str, default='pdf',
                        choices=['pdf', 'png', 'jpg', 'pptx', 'mp4', 'gif'],
                        help='Export format (default: pdf)')
    parser.add_argument('--quality', type=str, default='standard',
                        choices=['standard', 'high'],
                        help='Export quality (default: standard)')
    parser.add_argument('--pages', type=str, default='all',
                        help='Pages to export (e.g., "1,2,3" or "all")')
    parser.add_argument('--output', '-o', type=str,
                        help='Output directory')
    parser.add_argument('--timeout', type=int, default=300,
                        help='Export timeout in seconds (default: 300)')

    args = parser.parse_args()
    export_design(args)


if __name__ == '__main__':
    main()
