#!/usr/bin/env python3
"""
Get Brand Template Script
Get brand template details and dataset (Enterprise feature)
"""

import argparse
import json
import sys
from canva_client import get_client


def main():
    parser = argparse.ArgumentParser(description='Get Canva brand template details (Enterprise)')
    parser.add_argument('template_id', help='Brand template ID')
    parser.add_argument('--dataset', '-d', action='store_true', help='Include dataset definition for autofill')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        client = get_client()

        # Get template info
        result = client.get_brand_template(args.template_id)
        template = result.get('brand_template', {})

        # Get dataset if requested
        dataset = None
        if args.dataset:
            dataset_result = client.get_brand_template_dataset(args.template_id)
            dataset = dataset_result.get('dataset', {})
            result['dataset'] = dataset

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\nBrand Template Details")
            print("=" * 50)
            print(f"  ID:      {template.get('id', 'N/A')}")
            print(f"  Title:   {template.get('title', 'N/A')}")
            print(f"  Created: {template.get('created_at', 'N/A')}")
            print(f"  Updated: {template.get('updated_at', 'N/A')}")

            if dataset:
                fields = dataset.get('fields', [])
                print(f"\nDataset Fields ({len(fields)}):")
                for field in fields:
                    field_name = field.get('name', 'unknown')
                    field_type = field.get('type', 'unknown')
                    required = field.get('required', False)
                    req_str = " (required)" if required else ""
                    print(f"  - {field_name}: {field_type}{req_str}")

                print(f"\nTo create autofill:")
                print(f"  .venv\\Scripts\\python.exe scripts/create_autofill.py \"{args.template_id}\" --data '{{...}}'")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if "403" in str(e) or "forbidden" in str(e).lower():
            print("Note: Brand templates require Canva Enterprise plan.", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
