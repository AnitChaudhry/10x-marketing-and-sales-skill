#!/usr/bin/env python3
"""
Template Loader for 100X Outreach System

Loads, parses, and renders Jinja2 templates with YAML frontmatter
for all platforms (LinkedIn, Twitter, Instagram, Email).
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from jinja2 import Environment, BaseLoader, TemplateNotFound

try:
    from rich.console import Console
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


@dataclass
class Template:
    """A loaded template with metadata"""
    name: str
    path: str
    platform: str
    category: str
    type: str
    description: str
    max_length: int
    subject: Optional[str]  # For emails
    tags: List[str]
    content: str
    metadata: Dict[str, Any]


class TemplateLoader:
    """
    Loads and renders templates from the templates directory.

    Supports:
    - LinkedIn: connection-requests, messages, inmails, comments
    - Twitter: dms, tweets, replies
    - Instagram: dms, comments, stories
    - Email: outreach, follow-up, promotional, newsletters
    """

    PLATFORM_CATEGORIES = {
        'linkedin': ['connection-requests', 'messages', 'inmails', 'comments'],
        'twitter': ['dms', 'tweets', 'replies'],
        'instagram': ['dms', 'comments', 'stories'],
        'email': ['outreach', 'follow-up', 'promotional', 'newsletters']
    }

    def __init__(self, templates_dir: str = "templates"):
        self.templates_dir = Path(templates_dir)
        self._templates: Dict[str, Template] = {}  # path -> Template
        self._jinja_env = Environment(loader=BaseLoader())
        self._load_all_templates()

    def _load_all_templates(self):
        """Load all templates from all platforms"""
        for platform, categories in self.PLATFORM_CATEGORIES.items():
            platform_dir = self.templates_dir / platform
            if not platform_dir.exists():
                continue

            for category in categories:
                category_dir = platform_dir / category
                if not category_dir.exists():
                    continue

                for template_file in category_dir.glob("*.md"):
                    template = self._load_template(template_file, platform, category)
                    if template:
                        key = f"{platform}/{category}/{template_file.stem}"
                        self._templates[key] = template

    def _load_template(self, path: Path, platform: str, category: str) -> Optional[Template]:
        """Load a single template file"""
        try:
            content = path.read_text(encoding='utf-8')

            # Parse YAML frontmatter
            frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)

            if frontmatter_match:
                frontmatter = yaml.safe_load(frontmatter_match.group(1))
                body = frontmatter_match.group(2).strip()
            else:
                frontmatter = {}
                body = content.strip()

            return Template(
                name=frontmatter.get('name', path.stem),
                path=str(path),
                platform=platform,
                category=category,
                type=frontmatter.get('type', category),
                description=frontmatter.get('description', ''),
                max_length=frontmatter.get('max_length', 10000),
                subject=frontmatter.get('subject'),
                tags=frontmatter.get('tags', []),
                content=body,
                metadata=frontmatter
            )
        except Exception as e:
            print(f"Warning: Could not load template {path}: {e}")
            return None

    def get_template(self, platform: str, category: str, name: str) -> Optional[Template]:
        """Get a specific template by platform/category/name"""
        key = f"{platform}/{category}/{name}"
        return self._templates.get(key)

    def list_templates(self, platform: str = None, category: str = None,
                       tags: List[str] = None) -> List[Template]:
        """List templates with optional filters"""
        templates = list(self._templates.values())

        if platform:
            templates = [t for t in templates if t.platform == platform]

        if category:
            templates = [t for t in templates if t.category == category]

        if tags:
            templates = [t for t in templates if any(tag in t.tags for tag in tags)]

        return sorted(templates, key=lambda t: (t.platform, t.category, t.name))

    def render(self, template: Template, variables: Dict[str, Any]) -> Dict[str, str]:
        """
        Render a template with variables.

        Returns dict with:
        - content: Rendered message content
        - subject: Rendered subject (for emails)
        - truncated: Whether content was truncated
        """
        try:
            # Render content
            jinja_template = self._jinja_env.from_string(template.content)
            rendered_content = jinja_template.render(**variables)

            # Render subject if present
            rendered_subject = None
            if template.subject:
                subject_template = self._jinja_env.from_string(template.subject)
                rendered_subject = subject_template.render(**variables)

            # Check length and truncate if needed
            truncated = False
            if len(rendered_content) > template.max_length:
                rendered_content = rendered_content[:template.max_length - 3] + "..."
                truncated = True

            return {
                'content': rendered_content.strip(),
                'subject': rendered_subject,
                'truncated': truncated,
                'length': len(rendered_content),
                'max_length': template.max_length
            }
        except Exception as e:
            return {
                'content': f"Error rendering template: {e}",
                'subject': None,
                'truncated': False,
                'error': str(e)
            }

    def render_by_path(self, path: str, variables: Dict[str, Any]) -> Dict[str, str]:
        """Render a template by its path (platform/category/name)"""
        template = self._templates.get(path)
        if not template:
            return {'content': f"Template not found: {path}", 'error': 'not_found'}
        return self.render(template, variables)

    def get_variables(self, template: Template) -> List[str]:
        """Extract variable names from a template"""
        # Find all {{ variable }} patterns
        pattern = r'\{\{\s*(\w+)(?:\s*\|[^}]*)?\s*\}\}'
        variables = re.findall(pattern, template.content)

        if template.subject:
            variables.extend(re.findall(pattern, template.subject))

        return list(set(variables))

    def preview(self, template: Template, variables: Dict[str, Any] = None) -> str:
        """Generate a preview of the template"""
        if variables is None:
            # Use placeholder values
            var_names = self.get_variables(template)
            variables = {var: f"[{var}]" for var in var_names}

        result = self.render(template, variables)
        return result['content']

    def get_platforms(self) -> List[str]:
        """Get list of available platforms"""
        return list(self.PLATFORM_CATEGORIES.keys())

    def get_categories(self, platform: str) -> List[str]:
        """Get categories for a platform"""
        return self.PLATFORM_CATEGORIES.get(platform, [])

    def search(self, query: str) -> List[Template]:
        """Search templates by name, description, or tags"""
        query_lower = query.lower()
        results = []

        for template in self._templates.values():
            if (query_lower in template.name.lower() or
                query_lower in template.description.lower() or
                any(query_lower in tag.lower() for tag in template.tags)):
                results.append(template)

        return results

    def export_template_list(self, output_path: str = None) -> str:
        """Export list of all templates to markdown"""
        lines = ["# Available Templates\n"]

        for platform in self.get_platforms():
            lines.append(f"\n## {platform.title()}\n")
            templates = self.list_templates(platform=platform)

            current_category = None
            for t in templates:
                if t.category != current_category:
                    current_category = t.category
                    lines.append(f"\n### {current_category.replace('-', ' ').title()}\n")

                lines.append(f"- **{t.name}** (`{t.platform}/{t.category}/{Path(t.path).stem}`)")
                if t.description:
                    lines.append(f"  - {t.description}")
                if t.tags:
                    lines.append(f"  - Tags: {', '.join(t.tags)}")

        content = "\n".join(lines)

        if output_path:
            Path(output_path).write_text(content, encoding='utf-8')

        return content


def print_rich_output(loader: TemplateLoader, output_type: str, data=None):
    """Print formatted output"""
    if not RICH_AVAILABLE:
        if output_type == 'list' and data:
            for t in data:
                print(f"{t.platform}/{t.category}/{Path(t.path).stem}: {t.name}")
        return

    console = Console()

    if output_type == 'list' and data:
        table = Table(title="Templates")
        table.add_column("Path", style="cyan")
        table.add_column("Name", style="green")
        table.add_column("Type")
        table.add_column("Tags")
        table.add_column("Max Length")

        for t in data:
            table.add_row(
                f"{t.platform}/{t.category}/{Path(t.path).stem}",
                t.name,
                t.type,
                ", ".join(t.tags[:3]),
                str(t.max_length)
            )

        console.print(table)


def main():
    """CLI interface for template loader"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Template Loader CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # List templates
    list_parser = subparsers.add_parser('list', help='List templates')
    list_parser.add_argument('--platform', choices=['linkedin', 'twitter', 'instagram', 'email'])
    list_parser.add_argument('--category', help='Category filter')
    list_parser.add_argument('--tags', nargs='+', help='Tag filter')

    # Get template
    get_parser = subparsers.add_parser('get', help='Get template details')
    get_parser.add_argument('path', help='Template path (platform/category/name)')

    # Render template
    render_parser = subparsers.add_parser('render', help='Render template')
    render_parser.add_argument('path', help='Template path')
    render_parser.add_argument('--vars', help='JSON string of variables')
    render_parser.add_argument('--var', action='append', nargs=2, metavar=('KEY', 'VALUE'),
                               help='Variable key-value pair')

    # Search templates
    search_parser = subparsers.add_parser('search', help='Search templates')
    search_parser.add_argument('query', help='Search query')

    # Export list
    export_parser = subparsers.add_parser('export', help='Export template list')
    export_parser.add_argument('--output', help='Output file path')

    # Variables
    vars_parser = subparsers.add_parser('variables', help='Show template variables')
    vars_parser.add_argument('path', help='Template path')

    args = parser.parse_args()

    loader = TemplateLoader()

    if args.command == 'list':
        templates = loader.list_templates(
            platform=args.platform,
            category=args.category,
            tags=args.tags
        )
        print_rich_output(loader, 'list', templates)

    elif args.command == 'get':
        parts = args.path.split('/')
        if len(parts) == 3:
            template = loader.get_template(parts[0], parts[1], parts[2])
            if template:
                print(f"Name: {template.name}")
                print(f"Platform: {template.platform}")
                print(f"Category: {template.category}")
                print(f"Type: {template.type}")
                print(f"Description: {template.description}")
                print(f"Max Length: {template.max_length}")
                print(f"Tags: {', '.join(template.tags)}")
                if template.subject:
                    print(f"Subject: {template.subject}")
                print(f"\nContent:\n{template.content}")
            else:
                print(f"Template not found: {args.path}")
        else:
            print("Path must be: platform/category/name")

    elif args.command == 'render':
        variables = {}
        if args.vars:
            variables = json.loads(args.vars)
        if args.var:
            for key, value in args.var:
                variables[key] = value

        result = loader.render_by_path(args.path, variables)
        if result.get('subject'):
            print(f"Subject: {result['subject']}\n")
        print(result['content'])
        if result.get('truncated'):
            print(f"\n[Truncated to {result['max_length']} characters]")

    elif args.command == 'search':
        results = loader.search(args.query)
        print_rich_output(loader, 'list', results)

    elif args.command == 'export':
        content = loader.export_template_list(args.output)
        if not args.output:
            print(content)
        else:
            print(f"Exported to {args.output}")

    elif args.command == 'variables':
        parts = args.path.split('/')
        if len(parts) == 3:
            template = loader.get_template(parts[0], parts[1], parts[2])
            if template:
                variables = loader.get_variables(template)
                print("Variables in this template:")
                for var in sorted(variables):
                    print(f"  - {var}")
            else:
                print(f"Template not found: {args.path}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
