#!/usr/bin/env python3
"""
Integration Helper
Provides utilities for integrating Canva designs with other skills/workflows

This module is designed to work with:
- 10x-Outreach-Skill: Attach designs to emails
- Automation workflows: Batch design creation
- Other skills: Asset sharing
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Any
from canva_client import get_client
from design_types import get_design_type, DESIGN_TYPES


class DesignAsset:
    """Represents an exported design asset ready for integration"""

    def __init__(
        self,
        design_id: str,
        title: str,
        file_path: str,
        format: str,
        dimensions: Dict[str, int],
        platform: str,
        design_type: str,
        created_at: str = None
    ):
        self.design_id = design_id
        self.title = title
        self.file_path = file_path
        self.format = format
        self.dimensions = dimensions
        self.platform = platform
        self.design_type = design_type
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "design_id": self.design_id,
            "title": self.title,
            "file_path": self.file_path,
            "file_path_absolute": str(Path(self.file_path).absolute()),
            "format": self.format,
            "dimensions": self.dimensions,
            "platform": self.platform,
            "design_type": self.design_type,
            "created_at": self.created_at,
            "file_exists": Path(self.file_path).exists()
        }

    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


class IntegrationHelper:
    """Helper class for cross-skill integration"""

    def __init__(self, output_dir: str = "output/integration"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.manifest_file = self.output_dir / "assets_manifest.json"
        self.client = get_client()

    def create_and_export_design(
        self,
        design_type: str,
        title: str,
        export_format: str = "png",
        filename: Optional[str] = None
    ) -> DesignAsset:
        """
        Create a design and export it in one step.
        Returns a DesignAsset ready for integration.

        Args:
            design_type: Type name from design_types.py (e.g., 'instagram_post')
            title: Design title
            export_format: Export format (png, jpg, pdf, etc.)
            filename: Optional filename (without extension)

        Returns:
            DesignAsset object with file path and metadata
        """
        config = get_design_type(design_type)
        if not config:
            raise ValueError(f"Unknown design type: {design_type}")

        # Create design
        if config.get('canva_preset'):
            result = self.client.create_design(
                design_type=config['canva_preset'],
                title=title
            )
        else:
            result = self.client.create_design(
                width=config['width'],
                height=config['height'],
                title=title
            )

        design = result.get('design', {})
        design_id = design.get('id')

        if not design_id:
            raise Exception(f"Failed to create design: {result}")

        # Export design
        safe_filename = filename or self._safe_filename(title)
        files = self.client.export_and_download(
            design_id=design_id,
            format_type=export_format,
            output_dir=str(self.output_dir / "designs"),
            filename=safe_filename
        )

        if not files:
            raise Exception("Export completed but no files downloaded")

        # Create asset object
        asset = DesignAsset(
            design_id=design_id,
            title=title,
            file_path=files[0],
            format=export_format,
            dimensions={"width": config['width'], "height": config['height']},
            platform=config['platform'],
            design_type=design_type
        )

        # Update manifest
        self._add_to_manifest(asset)

        return asset

    def export_existing_design(
        self,
        design_id: str,
        design_type: str,
        export_format: str = "png",
        filename: Optional[str] = None
    ) -> DesignAsset:
        """
        Export an existing Canva design for integration.

        Args:
            design_id: Canva design ID
            design_type: Type name for metadata
            export_format: Export format
            filename: Optional filename

        Returns:
            DesignAsset object
        """
        # Get design info
        design_info = self.client.get_design(design_id)
        design = design_info.get('design', {})
        title = design.get('title', 'Untitled')

        # Get dimensions from design type or use default
        config = get_design_type(design_type)
        if config:
            dimensions = {"width": config['width'], "height": config['height']}
            platform = config['platform']
        else:
            dimensions = {"width": 1080, "height": 1080}
            platform = "unknown"

        # Export
        safe_filename = filename or self._safe_filename(title)
        files = self.client.export_and_download(
            design_id=design_id,
            format_type=export_format,
            output_dir=str(self.output_dir / "designs"),
            filename=safe_filename
        )

        if not files:
            raise Exception("Export completed but no files downloaded")

        asset = DesignAsset(
            design_id=design_id,
            title=title,
            file_path=files[0],
            format=export_format,
            dimensions=dimensions,
            platform=platform,
            design_type=design_type
        )

        self._add_to_manifest(asset)
        return asset

    def get_latest_asset(self, platform: Optional[str] = None) -> Optional[DesignAsset]:
        """Get the most recently created asset, optionally filtered by platform"""
        manifest = self._load_manifest()
        assets = manifest.get('assets', [])

        if platform:
            assets = [a for a in assets if a.get('platform') == platform]

        if not assets:
            return None

        latest = max(assets, key=lambda x: x.get('created_at', ''))
        return self._asset_from_dict(latest)

    def get_assets_for_integration(
        self,
        platform: Optional[str] = None,
        design_type: Optional[str] = None,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Get assets ready for integration with other skills.

        Returns list of asset dictionaries with file paths.
        """
        manifest = self._load_manifest()
        assets = manifest.get('assets', [])

        # Filter
        if platform:
            assets = [a for a in assets if a.get('platform') == platform]
        if design_type:
            assets = [a for a in assets if a.get('design_type') == design_type]

        # Sort by creation time (newest first)
        assets.sort(key=lambda x: x.get('created_at', ''), reverse=True)

        # Limit
        assets = assets[:limit]

        # Verify files exist
        for asset in assets:
            asset['file_exists'] = Path(asset.get('file_path', '')).exists()

        return assets

    def prepare_for_outreach(
        self,
        design_id: str,
        design_type: str = "email_header"
    ) -> Dict[str, Any]:
        """
        Prepare a design for the outreach skill.

        Returns a dictionary with all info needed for email attachment.
        """
        asset = self.export_existing_design(
            design_id=design_id,
            design_type=design_type,
            export_format="png"
        )

        return {
            "attachment_path": str(Path(asset.file_path).absolute()),
            "attachment_name": Path(asset.file_path).name,
            "mime_type": "image/png",
            "design_info": {
                "id": asset.design_id,
                "title": asset.title,
                "dimensions": asset.dimensions
            }
        }

    def _safe_filename(self, title: str) -> str:
        """Create safe filename from title"""
        safe = "".join(c if c.isalnum() or c in ' -_' else '_' for c in title)
        safe = safe.strip()[:50]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{safe}_{timestamp}"

    def _load_manifest(self) -> dict:
        """Load assets manifest"""
        if self.manifest_file.exists():
            with open(self.manifest_file) as f:
                return json.load(f)
        return {"assets": []}

    def _save_manifest(self, manifest: dict):
        """Save assets manifest"""
        with open(self.manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)

    def _add_to_manifest(self, asset: DesignAsset):
        """Add asset to manifest"""
        manifest = self._load_manifest()
        manifest['assets'].append(asset.to_dict())
        manifest['last_updated'] = datetime.now().isoformat()
        self._save_manifest(manifest)

    def _asset_from_dict(self, data: dict) -> DesignAsset:
        """Create DesignAsset from dictionary"""
        return DesignAsset(
            design_id=data.get('design_id'),
            title=data.get('title'),
            file_path=data.get('file_path'),
            format=data.get('format'),
            dimensions=data.get('dimensions'),
            platform=data.get('platform'),
            design_type=data.get('design_type'),
            created_at=data.get('created_at')
        )


def main():
    """CLI interface for integration helper"""
    import argparse

    parser = argparse.ArgumentParser(description='Integration Helper for Canva Skills')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create and export a design')
    create_parser.add_argument('design_type', help='Design type (e.g., instagram_post)')
    create_parser.add_argument('--title', '-t', required=True, help='Design title')
    create_parser.add_argument('--format', '-f', default='png', help='Export format')
    create_parser.add_argument('--filename', help='Output filename')

    # Export command
    export_parser = subparsers.add_parser('export', help='Export existing design')
    export_parser.add_argument('design_id', help='Canva design ID')
    export_parser.add_argument('--type', '-t', default='custom', help='Design type for metadata')
    export_parser.add_argument('--format', '-f', default='png', help='Export format')

    # List command
    list_parser = subparsers.add_parser('list', help='List available assets')
    list_parser.add_argument('--platform', '-p', help='Filter by platform')
    list_parser.add_argument('--limit', '-l', type=int, default=10, help='Max results')

    # Outreach command
    outreach_parser = subparsers.add_parser('outreach', help='Prepare design for outreach')
    outreach_parser.add_argument('design_id', help='Canva design ID')

    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    helper = IntegrationHelper()

    if args.command == 'create':
        asset = helper.create_and_export_design(
            design_type=args.design_type,
            title=args.title,
            export_format=args.format,
            filename=args.filename
        )
        if args.json:
            print(asset.to_json())
        else:
            print(f"\nDesign Created and Exported!")
            print(f"  Design ID: {asset.design_id}")
            print(f"  File: {asset.file_path}")
            print(f"  Format: {asset.format}")

    elif args.command == 'export':
        asset = helper.export_existing_design(
            design_id=args.design_id,
            design_type=args.type,
            export_format=args.format
        )
        if args.json:
            print(asset.to_json())
        else:
            print(f"\nDesign Exported!")
            print(f"  File: {asset.file_path}")

    elif args.command == 'list':
        assets = helper.get_assets_for_integration(
            platform=args.platform,
            limit=args.limit
        )
        if args.json:
            print(json.dumps(assets, indent=2))
        else:
            print(f"\nAvailable Assets ({len(assets)}):")
            for a in assets:
                exists = "OK" if a.get('file_exists') else "MISSING"
                print(f"  [{exists}] {a.get('title')} ({a.get('design_type')})")
                print(f"         File: {a.get('file_path')}")

    elif args.command == 'outreach':
        result = helper.prepare_for_outreach(args.design_id)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\nReady for Outreach!")
            print(f"  Attachment: {result['attachment_path']}")
            print(f"  MIME Type: {result['mime_type']}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
