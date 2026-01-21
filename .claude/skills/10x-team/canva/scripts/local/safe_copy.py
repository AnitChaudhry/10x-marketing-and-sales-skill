#!/usr/bin/env python3
"""
Safe Copy Utility
ALWAYS use this to create working copies before any file modification.
NEVER modify original files directly.
"""

import os
import sys
import shutil
import json
from pathlib import Path
from datetime import datetime
import argparse


def get_output_dir(file_type: str) -> Path:
    """Get appropriate output directory based on file type"""
    base = Path(__file__).parent.parent.parent / 'output'

    type_dirs = {
        'pdf': base / 'pdf',
        'pptx': base / 'pptx',
        'ppt': base / 'pptx',
        'docx': base / 'docx',
        'doc': base / 'docx',
        'xlsx': base / 'xlsx',
        'xls': base / 'xlsx',
        'csv': base / 'csv',
    }

    return type_dirs.get(file_type.lower(), base / 'other')


def safe_copy(source_path: str, preserve_name: bool = True) -> dict:
    """
    Create a safe working copy of a file.

    CRITICAL: This function should be called before ANY file modification.

    Args:
        source_path: Path to the original file
        preserve_name: If True, keeps original filename; if False, adds timestamp

    Returns:
        dict with paths and status
    """
    source = Path(source_path)

    if not source.exists():
        return {
            'success': False,
            'error': f"Source file not found: {source_path}",
            'original': str(source),
            'copy': None
        }

    # Determine file type
    file_type = source.suffix.lower().lstrip('.')

    # Create working directory
    base_dir = Path(__file__).parent.parent.parent
    working_dir = base_dir / 'output' / 'working'
    working_dir.mkdir(parents=True, exist_ok=True)

    # Create output directory for final files
    output_dir = get_output_dir(file_type)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate copy filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    if preserve_name:
        copy_name = f"{source.stem}_copy{source.suffix}"
    else:
        copy_name = f"{source.stem}_{timestamp}_copy{source.suffix}"

    copy_path = working_dir / copy_name

    # Copy the file
    try:
        shutil.copy2(source, copy_path)
    except Exception as e:
        return {
            'success': False,
            'error': f"Failed to copy: {str(e)}",
            'original': str(source),
            'copy': None
        }

    # Log the operation
    log_operation(
        original=str(source),
        copy=str(copy_path),
        file_type=file_type,
        timestamp=timestamp
    )

    return {
        'success': True,
        'original': str(source),
        'copy': str(copy_path),
        'output_dir': str(output_dir),
        'file_type': file_type,
        'timestamp': timestamp,
        'message': f"Safe copy created. Original file is protected."
    }


def log_operation(original: str, copy: str, file_type: str, timestamp: str):
    """Log file operation for audit trail"""
    base_dir = Path(__file__).parent.parent.parent
    log_dir = base_dir / 'output' / 'logs'
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / 'file_operations.json'

    # Load existing logs
    logs = []
    if log_file.exists():
        try:
            with open(log_file, 'r') as f:
                logs = json.load(f)
        except:
            logs = []

    # Add new log entry
    logs.append({
        'timestamp': timestamp,
        'operation': 'safe_copy',
        'original': original,
        'copy': copy,
        'file_type': file_type,
        'original_modified': False
    })

    # Save logs
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)


def verify_original_unchanged(original_path: str, expected_hash: str = None) -> bool:
    """Verify original file was not modified"""
    import hashlib

    source = Path(original_path)
    if not source.exists():
        return False

    # Calculate current hash
    with open(source, 'rb') as f:
        current_hash = hashlib.md5(f.read()).hexdigest()

    if expected_hash:
        return current_hash == expected_hash

    return True  # If no expected hash, just check existence


def get_file_hash(file_path: str) -> str:
    """Get MD5 hash of file for verification"""
    import hashlib

    with open(file_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def main():
    parser = argparse.ArgumentParser(
        description='Create safe working copy of a file (NEVER modifies original)'
    )
    parser.add_argument('--source', '-s', required=True,
                        help='Path to source file')
    parser.add_argument('--type', '-t',
                        help='File type (auto-detected if not provided)')
    parser.add_argument('--preserve-name', action='store_true', default=True,
                        help='Preserve original filename')

    args = parser.parse_args()

    result = safe_copy(args.source, args.preserve_name)

    if result['success']:
        print("=" * 60)
        print("SAFE COPY CREATED")
        print("=" * 60)
        print(f"\n[OK] Original file is PROTECTED and will NOT be modified:")
        print(f"     {result['original']}")
        print(f"\n[*] Working copy created at:")
        print(f"    {result['copy']}")
        print(f"\n[*] Final output will go to:")
        print(f"    {result['output_dir']}")
        print("\n" + "=" * 60)
    else:
        print(f"\n[X] Error: {result['error']}")
        sys.exit(1)

    # Output JSON for script consumption
    print("\n--- JSON Output ---")
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
