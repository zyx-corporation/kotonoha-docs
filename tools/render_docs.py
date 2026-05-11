#!/usr/bin/env python3
"""Minimal Kotonoha docs renderer.

This script converts a small Markdown subset into static HTML and expands a
Kotonoha-specific figure directive:

    :::svg path="../../assets/svg/example.svg" alt="Example" caption="Example figure"
    :::

The renderer is intentionally minimal. It is suitable for explanatory pages
that need SVG figures and shared CSS without requiring a heavy static-site
framework. Complex pages may still be authored directly in HTML.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

SVG_DIRECTIVE_RE = re.compile(
    r'^:::\s*svg\s+path="(?P<path>[^"]+)"\s+alt="(?P<alt>[^"]*)"(?:\s+caption="(?P<caption>[^"]*)")?\s*$'
)


def parse_inline(text: str) -> str:
    """Escape text and apply a minimal inline Markdown subset."""
    escaped = html.escape(text)
    escaped = re.sub(r'`([^`]+)`', r'<code>\1</code>', escaped)
    escaped = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', escaped)
    escaped = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', escaped)
    return escaped


def render_markdown(source: str) -> str:
    lines = source.splitlines()
    output: list[str] = []
    in_list = False
    in_code = False
    code_lines: list[str] = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            output.append('</ul>')
            in_list = False

    for line in lines:
        if line.startswith('```'):
            if in_code:
                output.append('<pre><code>' + html.escape('\n'.join(code_lines)) + '</code></pre>')
                code_lines = []
                in_code = False
            else:
                close_list()
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        svg_match = SVG_DIRECTIVE_RE.match(line)
        if svg_match:
            close_list()
            path = html.escape(svg_match.group('path'), quote=True)
            alt = html.escape(svg_match.group('alt'), quote=True)
            caption = svg_match.group('caption')
            output.append('<figure class="kt-figure">')
            output.append(f'  <img src="{path}" alt="{alt}">')
            if caption:
                output.append(f'  <figcaption>{parse_inline(caption)}</figcaption>')
            output.append('</figure>')
            continue

        stripped = line.strip()
        if not stripped:
            close_list()
            continue

        if stripped.startswith('#'):
            close_list()
            level = len(stripped) - len(stripped.lstrip('#'))
            level = min(max(level, 1), 6)
            text = stripped[level:].strip()
            output.append(f'<h{level}>{parse_inline(text)}</h{level}>')
            continue

        if stripped.startswith('- '):
            if not in_list:
                output.append('<ul>')
                in_list = True
            output.append(f'<li>{parse_inline(stripped[2:].strip())}</li>')
            continue

        close_list()
        output.append(f'<p>{parse_inline(stripped)}</p>')

    close_list()
    if in_code:
        output.append('<pre><code>' + html.escape('\n'.join(code_lines)) + '</code></pre>')
    return '\n'.join(output)


def render_page(source_path: Path, css_href: str, title: str | None = None) -> str:
    source = source_path.read_text(encoding='utf-8')
    body = render_markdown(source)
    page_title = title or source_path.stem.replace('-', ' ').replace('_', ' ').title()
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page_title)}</title>
  <link rel="stylesheet" href="{html.escape(css_href, quote=True)}">
</head>
<body>
<main>
{body}
</main>
</body>
</html>
'''


def main() -> int:
    parser = argparse.ArgumentParser(description='Render Kotonoha Markdown to HTML.')
    parser.add_argument('source', type=Path, help='Markdown source file')
    parser.add_argument('output', type=Path, help='HTML output file')
    parser.add_argument('--css', default='../assets/css/kotonoha-docs.css', help='CSS href written into the HTML')
    parser.add_argument('--title', default=None, help='HTML title')
    args = parser.parse_args()

    html_text = render_page(args.source, args.css, args.title)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html_text, encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
