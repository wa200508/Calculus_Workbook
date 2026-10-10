#!/usr/bin/env python3
"""Check generated HTML, internal links/assets, and MathJax error output offline."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import os
import sys
import json

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.math_count, self.errors = [], set(), 0, []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in ('script', 'img') and attrs.get('src'):
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') in ('stylesheet', 'modulepreload'):
            self.links.append(attrs['href'])
        if tag == 'mjx-container':
            self.math_count += 1
        if attrs.get('data-mml-node') == 'merror' or tag == 'mjx-merror':
            self.errors.append('MathJax reported an invalid equation')


def check(dist, base='/'):
    pages = {}
    for path in dist.rglob('*.html'):
        page = Page(); page.feed(path.read_text()); pages[path.resolve()] = page
    if not pages:
        raise ValueError('No built HTML pages found')
    errors = []
    for path, page in pages.items():
        errors.extend(f'{path.relative_to(dist.resolve())}: {error}' for error in page.errors)
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = unquote(url.path)
            if target.startswith('/'):
                if not target.startswith(base):
                    errors.append(f'{path.name}: link ignores deployment base: {link}')
                    continue
                destination = dist / target[len(base):]
            else:
                destination = path.parent / target if target else path
            if destination.is_dir():
                destination /= 'index.html'
            if not destination.exists() and not destination.suffix:
                destination = destination.with_suffix('.html')
            destination = destination.resolve()
            if not destination.exists():
                errors.append(f'{path.name}: missing internal target {link}')
            elif url.fragment and destination in pages and unquote(url.fragment) not in pages[destination].ids:
                errors.append(f'{path.name}: missing anchor {link}')
    index = json.loads((ROOT / 'site/generated/problem-index.json').read_text())
    required = ['generated/notation.html', 'generated/tricks.html'] + [item['link'].lstrip('/') + '.html' for item in index]
    for name in required:
        page = pages.get((dist / name).resolve())
        if not page or not page.math_count:
            errors.append(f'{name}: expected rendered math is missing')
    if errors:
        raise ValueError('\n'.join(sorted(set(errors))))
    return len(pages), sum(page.math_count for page in pages.values())


if __name__ == '__main__':
    base = os.environ.get('SITE_BASE', '/')
    try:
        count, equations = check(ROOT / 'site/.vitepress/dist', base)
    except ValueError as error:
        print(error, file=sys.stderr); sys.exit(1)
    print(f'Checked {count} HTML pages, internal links/assets, and {equations} rendered math expressions.')
