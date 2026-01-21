#!/usr/bin/env python3
"""
List folder structure in Canva account
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from canva_client import get_client


def get_folder_tree(client, folder_id: str, depth: int, max_depth: int) -> dict:
    """Recursively build folder tree"""

    if depth > max_depth:
        return None

    try:
        folder = client.get_folder(folder_id)
        items = client.list_folder_items(folder_id, limit=100)

        folder_data = {
            'id': folder_id,
            'name': folder.get('folder', {}).get('name', 'Unknown'),
            'items': [],
            'subfolders': []
        }

        for item in items.get('items', []):
            item_type = item.get('type')

            if item_type == 'folder':
                subfolder = get_folder_tree(
                    client,
                    item.get('folder', {}).get('id'),
                    depth + 1,
                    max_depth
                )
                if subfolder:
                    folder_data['subfolders'].append(subfolder)
            else:
                folder_data['items'].append({
                    'type': item_type,
                    'id': item.get(item_type, {}).get('id'),
                    'name': item.get(item_type, {}).get('name', 'Untitled')
                })

        return folder_data

    except Exception as e:
        return {'id': folder_id, 'error': str(e)}


def print_tree(folder: dict, prefix: str = '', is_last: bool = True):
    """Print folder tree in ASCII format"""

    connector = '└── ' if is_last else '├── '
    name = folder.get('name', 'Unknown')
    items_count = len(folder.get('items', []))

    print(f"{prefix}{connector}[D] {name} ({items_count} items)")

    new_prefix = prefix + ('    ' if is_last else '│   ')

    subfolders = folder.get('subfolders', [])
    for i, subfolder in enumerate(subfolders):
        is_last_subfolder = (i == len(subfolders) - 1)
        print_tree(subfolder, new_prefix, is_last_subfolder)


def list_folders(args):
    """List folder structure"""

    client = get_client()

    print("=" * 60)
    print("CANVA FOLDER STRUCTURE")
    print("=" * 60)

    # Build folder tree
    print("\n[*] Scanning folder structure...")

    # Start from root (Projects folder)
    tree = get_folder_tree(client, 'root', 0, args.depth)

    # Print tree
    print("\n[D] Projects")
    for i, subfolder in enumerate(tree.get('subfolders', [])):
        is_last = (i == len(tree.get('subfolders', [])) - 1)
        print_tree(subfolder, '', is_last)

    # Show root items
    if tree.get('items'):
        print(f"\n   [F] {len(tree['items'])} items at root level")

    # Also show uploads folder
    if args.include_uploads:
        print("\n[D] Uploads")
        uploads = get_folder_tree(client, 'uploads', 0, 1)
        print(f"   [F] {len(uploads.get('items', []))} uploaded assets")

    # Save to output
    output_dir = Path(__file__).parent.parent / 'output' / 'explorations'
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = output_dir / f'folders_{timestamp}.json'

    with open(output_path, 'w') as f:
        json.dump(tree, f, indent=2)

    print(f"\n[*] Data saved to: {output_path}")

    return tree


def main():
    parser = argparse.ArgumentParser(description='List Canva folder structure')
    parser.add_argument('--depth', type=int, default=3,
                        help='Maximum depth to traverse (default: 3)')
    parser.add_argument('--include-uploads', action='store_true',
                        help='Also show Uploads folder')
    parser.add_argument('--output', '-o', type=str,
                        help='Output file path')

    args = parser.parse_args()
    list_folders(args)


if __name__ == '__main__':
    main()
