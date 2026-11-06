#!/usr/bin/env python3
"""Guard the owner's requirement: official badges at both homepage download locations."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import json

ROOT = Path(__file__).resolve().parent.parent


class StoreLinks(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.sections = []
        self.links = []
        self.current = None
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section':
            self.sections.append(attrs)
        elif tag == 'a':
            self.current = None
            if 'data-store' in attrs:
                self.current = {'attrs': attrs, 'images': [], 'sections': list(self.sections)}
                self.links.append(self.current)
        elif tag == 'img' and self.current is not None:
            self.current['images'].append(attrs)

    def handle_endtag(self, tag):
        if tag == 'section' and self.sections:
            self.sections.pop()
        elif tag == 'a':
            self.current = None


def validate_home_badges(html, locale):
    links = StoreLinks(html).links
    suffix = '' if locale == 'en' else '-' + locale
    for placement in ['hero', 'footer']:
        pair = [link for link in links if link['attrs'].get('data-placement') == placement]
        if [link['attrs']['data-store'] for link in pair] != ['ios', 'android']:
            raise ValueError(f'{locale}: {placement} needs both official store badges, App Store first.')
        for link, filename in zip(pair, ['app-store', 'google-play']):
            attrs, images = link['attrs'], link['images']
            expected = f'/assets/store-badges/{filename}{suffix}.svg'
            in_location = any(
                'landing-hero' in section.get('class', '').split() if placement == 'hero'
                else section.get('id') == 'download'
                for section in link['sections']
            )
            if not in_location or 'store-badge-link' not in attrs.get('class', '').split():
                raise ValueError(f'{locale}: {placement} must use official badges in its actual page section.')
            if len(images) != 1 or images[0].get('src') != expected or not images[0].get('alt'):
                raise ValueError(f'{locale}: {placement} must display the original localized {filename} SVG.')
            if not (ROOT / expected.lstrip('/')).is_file():
                raise ValueError(f'Missing official badge: {expected}')
            url = urlsplit(attrs.get('href', ''))
            query = parse_qs(url.query)
            valid_store = (
                url.netloc == 'apps.apple.com' and 'id6817176363' in url.path
                if filename == 'app-store' else
                url.netloc == 'play.google.com' and url.path == '/store/apps/details'
                and query.get('id') == ['com.loop.loopsplit']
            )
            if url.scheme != 'https' or not valid_store:
                raise ValueError(f'{locale}: {placement} must link directly to the correct {filename} listing.')


if __name__ == '__main__':
    locales = json.loads((ROOT / 'content/landing.json').read_text())
    for locale, copy in locales.items():
        file = ROOT / copy['route'] / 'index.html'
        validate_home_badges(file.read_text(), locale)
    print(f'Official App Store + Google Play badges verified in both locations for {len(locales)} languages.')
