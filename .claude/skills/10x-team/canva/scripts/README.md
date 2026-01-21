# Scripts

Python scripts for Canva API operations. These scripts are called by the Claude Code skills to interact with the Canva Connect API.

## Why Scripts Are at Root Level

These scripts are kept at root level (not inside `.claude/`) because:
1. They are executable Python files, not Claude Code configuration
2. They need to be run via `python scripts/script_name.py`
3. They share a common `canva_client.py` module

## Available Scripts

### Core
| Script | Description |
|--------|-------------|
| `canva_client.py` | Core API client class - used by all other scripts |

### Discovery (Read-Only)
| Script | Description |
|--------|-------------|
| `auth_check.py` | Verify API credentials and show account info |
| `list_designs.py` | List all designs with filtering options |
| `list_folders.py` | Display folder structure as tree |

### Actions
| Script | Description |
|--------|-------------|
| `export_design.py` | Export design to PDF/PNG/PPTX/MP4/GIF |

## Usage

All scripts require the `.env` file to be configured with Canva API credentials.

```bash
# Verify setup
python scripts/auth_check.py

# List your designs
python scripts/list_designs.py --limit 20

# Export a design
python scripts/export_design.py --id "DESIGN_ID" --format pdf
```

## Adding New Scripts

When adding new scripts:
1. Import `canva_client` for API access
2. Use argparse for command-line arguments
3. Save outputs to `../output/` folder
4. Follow the existing naming convention

## Dependencies

Install required packages:
```bash
pip install -r ../requirements.txt
```
