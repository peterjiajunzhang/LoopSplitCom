#!/usr/bin/env python3
"""Render committed static landing pages; Python is only needed when editing copy."""
from pathlib import Path
from html import escape
from urllib.parse import urlencode
import json
import re
import xml.etree.ElementTree as ET
from check_store_badges import validate_home_badges

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://loopsplit.app'
COPY = json.loads((ROOT / 'content/landing.json').read_text())
GUIDE_COPY = json.loads((ROOT / 'content/guides.json').read_text())
SEO = json.loads((ROOT / 'content/seo.json').read_text())
assert set(SEO) == set(COPY)
MEDIA = json.loads((ROOT / 'content/media.json').read_text())
assert set(MEDIA) == set(COPY), 'Every page language needs its own media mapping.'
media_paths = []
for locale, media in MEDIA.items():
    assert set(media['screenshots']) == {'scan', 'loops', 'balances'}
    assert set(media['videos']) == {'header', 'search'}
    for image in media['screenshots'].values():
        assert image['src'].startswith(f'/assets/screenshots/{locale}/')
        file = ROOT / image['src'].lstrip('/')
        dimensions = file.read_bytes()[:24]
        assert dimensions[:8] == b'\x89PNG\r\n\x1a\n'
        assert (int.from_bytes(dimensions[16:20], 'big'), int.from_bytes(dimensions[20:24], 'big')) == (image['width'], image['height'])
        media_paths.append(image['src'])
    for video in media['videos'].values():
        assert video['width'] > 0 and video['height'] > 0
        for key in ['src', 'poster']:
            prefix = '/assets/video/' if locale == 'en' else f'/assets/video/{locale}/'
            assert video[key].startswith(prefix), f'{locale} must use its own media.'
            assert (ROOT / video[key].lstrip('/')).is_file(), video[key]
            media_paths.append(video[key])
assert len(media_paths) == len(set(media_paths)), 'Languages must not silently reuse another language’s media.'
SLUGS = ['split-rent-and-utilities', 'shared-expenses-for-couples', 'recurring-shared-bills']
HELP = ['getting-started', 'expenses', 'loops', 'balances', 'receipts', 'pro', 'account', 'search-and-calculations', 'privacy-and-diagnostics']
DAY = '2026-11-05'
assert len(COPY) == 7
assert all(set(c) == set(COPY['en']) for c in COPY.values()), 'Each locale must supply its own copy.'
assert all(len(c['pillars']) == len(c['guideCards']) == 3 and len(c['helpTopics']) == 9 for c in COPY.values())

def e(value):
    return escape(str(value), quote=True)

def lines(value):
    return '<br>'.join(e(part) for part in value.split('\n'))

def path(locale, suffix=''):
    route = COPY[locale]['route']
    return '/' + (route + '/' if route else '') + suffix

def stores(kind='home', placement='hero', locale='en'):
    campaign = 'website_home_20261105' if kind == 'home' else 'website_guides_20261105'
    apple = 'https://apps.apple.com/app/apple-store/id6817176363?' + urlencode({'pt':'128765534','ct':campaign,'mt':'8'})
    attribution = {'utm_source':'loopsplit.app','utm_medium':'website','utm_campaign':campaign,'utm_content':f'{locale}_{placement}'}
    google = 'https://play.google.com/store/apps/details?' + urlencode({'id':'com.loop.loopsplit', **attribution, 'referrer':urlencode(attribution)})
    return apple, google

def store_badges(locale, kind='home', placement='hero'):
    c = COPY[locale]
    ios, android = stores(kind, placement, locale)
    suffix = '' if locale == 'en' else '-' + locale
    hero_class = ' hero-store-badges' if placement == 'hero' else ''
    return f'<div class="download-actions store-badges{hero_class}"><a class="store-badge-link" href="{e(ios)}" data-store="ios" data-placement="{placement}"><img src="/assets/store-badges/app-store{suffix}.svg" alt="{e(c["ios"])}" width="120" height="40"></a><a class="store-badge-link" href="{e(android)}" data-store="android" data-placement="{placement}"><img src="/assets/store-badges/google-play{suffix}.svg" alt="{e(c["android"])}" width="239" height="71"></a></div>'

def screenshot(locale, kind, alt, css_class='', eager=False):
    asset = MEDIA[locale]['screenshots'][kind]
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img class="{e(css_class)}" src="{e(asset["src"])}" alt="{e(alt)}" width="{asset["width"]}" height="{asset["height"]}" {loading}>'

def language_menu(locale, suffix=''):
    items = ''.join(f'<a href="{path(key,suffix)}" lang="{c["tag"]}" hreflang="{c["tag"]}"'+(' aria-current="page"' if key == locale else '')+f'>{e(c["name"])}</a>' for key,c in COPY.items())
    return f'<details class="language-menu"><summary aria-label="{e(COPY[locale]["language"])}">{e(COPY[locale]["name"])}</summary><div>{items}</div></details>'

def alternates(suffix=''):
    return ''.join(f'<link rel="alternate" hreflang="{c["tag"]}" href="{BASE+path(key,suffix)}">' for key,c in COPY.items()) + f'<link rel="alternate" hreflang="x-default" href="{BASE+path("en",suffix)}">'

def schema(value):
    return '<script type="application/ld+json">' + json.dumps(value,ensure_ascii=False).replace('</','<\\/') + '</script>'

def head(locale, title, description, suffix='', article=None):
    c = COPY[locale]
    url = BASE + path(locale,suffix)
    data = {'@context':'https://schema.org','@graph':[
        {'@type':'Organization','@id':BASE+'/#publisher','name':'LoopSplit','url':BASE+'/','logo':BASE+'/assets/app-icon.png'},
        {'@type':'WebPage','@id':url+'#page','url':url,'name':title,'inLanguage':c['tag'],'isPartOf':{'@id':BASE+'/#website'}}
    ]}
    if not suffix:
        data['@graph'] += [
            {'@type':'WebSite','@id':BASE+'/#website','name':'LoopSplit','url':BASE+'/'},
            {'@type':'SoftwareApplication','@id':BASE+'/#app','name':'LoopSplit','applicationCategory':'FinanceApplication','operatingSystem':['iOS 17 or later','iPadOS 17 or later','Android 9 or later'],'url':url,'image':BASE+'/assets/app-icon.png','downloadUrl':['https://apps.apple.com/app/id6817176363','https://play.google.com/store/apps/details?id=com.loop.loopsplit'],'offers':{'@type':'Offer','price':'0','priceCurrency':'USD'},'description':description}
        ]
    if article:
        data['@graph'].append({'@type':'Article','headline':title,'mainEntityOfPage':url,'image':BASE+'/assets/social-card.png','inLanguage':c['tag'],'datePublished':DAY,'dateModified':DAY,'author':{'@type':'Organization','name':'LoopSplit','url':BASE+'/'},'publisher':{'@id':BASE+'/#publisher'}})
    return f'''<!doctype html>
<html lang="{c['tag']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f8faf7"><title>{e(title)} — LoopSplit</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{url}">{alternates(suffix)}<meta property="og:type" content="{'article' if article else 'website'}"><meta property="og:title" content="{e(title)} — LoopSplit"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/assets/social-card.png?v=landing-20261105"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/app-icon.png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"><link rel="stylesheet" href="/assets/style.css?v=store-badges-20261105"><link rel="stylesheet" href="/assets/landing.css?v=android-search-20261111">{schema(data)}</head>'''

def header(locale, suffix=''):
    c = COPY[locale]
    return f'''<body class="landing"><a class="skip-link" href="#main">{e(c['skip'])}</a><div class="site-shell"><header class="site-header"><a class="brand" href="{path(locale)}" aria-label="LoopSplit"><img src="/assets/app-icon.png" alt="" width="42" height="42"><span>LoopSplit</span></a><nav aria-label="{e(c['language'])}"><a href="{path(locale)}#why">{e(c['navFeatures'])}</a><a href="{path(locale,'guides/')}">{e(c['navGuides'])}</a><a href="{path(locale,'support/')}">{e(c['navSupport'])}</a>{language_menu(locale,suffix)}</nav></header>'''

def footer(locale):
    c = COPY[locale]
    return f'''<footer class="site-footer"><span>© 2026 LoopSplit</span><a href="{path(locale,'guides/')}">{e(c['navGuides'])}</a><a href="{path(locale,'support/')}">{e(c['navSupport'])}</a><a href="/privacy/">{e(c['privacy'])}</a><a href="/terms/">{e(c['terms'])}</a><p class="trademark-notice">{e(c['legalNote'])}</p><p class="trademark-notice">Apple, the Apple logo and App Store are trademarks of Apple Inc., registered in the U.S. and other countries. Google Play and the Google Play logo are trademarks of Google LLC.</p></footer></div></body></html>'''

def guide_cards(locale):
    c = COPY[locale]
    return '<div class="help-topics">' + ''.join(f'<article class="help-topic"><a href="{path(locale,"guides/"+slug+"/")}"><h2>{e(card["title"])} <span aria-hidden="true">↗</span></h2><p>{e(card["text"])}</p></a></article>' for slug,card in zip(SLUGS,c['guideCards'])) + '</div>'

def render_home(locale):
    c = COPY[locale]
    html = head(locale,SEO[locale]['title'],SEO[locale]['description']) + header(locale)
    html += f'''<main id="main"><section class="landing-hero" aria-labelledby="hero-title"><div class="landing-hero-copy"><h1 id="hero-title">{e(c['headline'][0])}<br><span>{e(c['headline'][1])}</span></h1><p class="hero-description">{e(c['intro'])}</p>{store_badges(locale)}<p class="landing-proof">{''.join('<span>'+e(t)+'</span>' for t in c['proof'])}</p></div><figure class="hero-scene">{screenshot(locale,'loops',c['pillars'][1]['title'],'scene-loops',True)}{screenshot(locale,'balances',c['pillars'][0]['title'],'scene-balances',True)}<figcaption>{e(c['screenNote'])}</figcaption></figure></section>'''
    html += f'<section class="landing-section" id="why"><p class="eyebrow">{e(c["pillarsEyebrow"])}</p><h2>{lines(c["pillarsTitle"])}</h2><div class="value-grid">'
    for i,(card,art) in enumerate(zip(c['pillars'],['balances','loops','scan'])):
        html += f'<article class="value-card"><div class="card-copy"><span class="card-number">0{i+1}</span><h3>{e(card["title"])}</h3><p>{e(card["text"])}</p></div><div class="card-art">{screenshot(locale,art,card["title"])}</div></article>'
    html += '</div></section>'
    films = MEDIA[locale]['videos']
    header_film = films['header']
    data = ' '.join(f'data-{layout}-{key}="{e(asset[key])}"' for layout,asset in films.items() for key in ['src','poster','width','height'])
    html += f'''<section class="film-section" id="product-video"><div class="film-heading"><h2>{lines(c['filmTitle'])}</h2><p>{e(c['filmIntro'])}</p></div><figure class="product-film"><video id="overview-video" controls playsinline muted loop preload="none" {data} poster="{e(header_film['poster'])}" src="{e(header_film['src'])}" width="{header_film['width']}" height="{header_film['height']}" aria-label="LoopSplit" aria-describedby="video-summary"><a href="{e(header_film['src'])}">LoopSplit</a></video><figcaption id="video-summary">{e(c['filmCaption'])}</figcaption><details class="film-summary"><summary>{e(c['readSummary'])}</summary><p>{e(c['filmSummary'])}</p></details></figure></section>'''
    html += f'<section class="landing-section"><h2>{e(c["detailsTitle"])}</h2><div class="detail-grid">'+''.join(f'<article><h3>{e(d["title"])}</h3><p>{e(d["text"])}</p></article>' for d in c['details'])+'</div></section>'
    html += f'<section class="landing-section"><p class="eyebrow">{e(c["pricingEyebrow"])}</p><h2>{lines(c["pricingTitle"])}</h2><div class="plan-grid">'
    for title,items in [(c['freeTitle'],c['freeList']),(c['proTitle'],c['proList'])]:
        html += f'<article class="plan-card"><h3>{e(title)}</h3><ul>'+''.join(f'<li>{e(t)}</li>' for t in items)+'</ul></article>'
    html += f'</div><p class="plan-note">{e(c["planNote"])}</p></section><section class="landing-section"><h2>{e(c["guidesTitle"])}</h2><p>{e(c["guidesIntro"])}</p>{guide_cards(locale)}</section>'
    html += '<section class="landing-section" id="questions"><h2>'+e(SEO[locale]['faqTitle'])+'</h2>' + ''.join('<details class="faq-item"><summary>'+e(q)+'</summary><p>'+e(a)+'</p></details>' for q,a in SEO[locale]['faq']) + '</section>'
    html += f'''<section class="download-banner" id="download"><h2>{e(c['readyTitle'])}</h2><p>{e(c['readyText'])}</p>{store_badges(locale,'home','footer')}<p class="small-print">{e(c['compat'])}<br>{e(c['renewalNote'])}<br><a href="/terms/">{e(c['terms'])}</a> · <a href="/privacy/">{e(c['privacy'])}</a></p></section><section class="support-card"><div><h2>{e(c['supportTitle'])}</h2><p>{e(c['supportText'])}</p></div><a class="button" href="{path(locale,'support/')}">{e(c['supportAction'])} ↗</a></section></main><script src="/assets/overview-video.js?v=localized-media-20261106" defer></script>'''
    return html + footer(locale)

def render_guide_index(locale):
    c = COPY[locale]
    return head(locale,c['guideLabel'].title(),c['guidesIntro'],'guides/') + header(locale,'guides/') + f'<main class="help-home" id="main"><a class="back-link" href="{path(locale)}">← {e(c["home"])}</a><p class="eyebrow">{e(c["guideLabel"])}</p><h1>{e(c["guidesTitle"])}</h1><p class="help-lead">{e(c["guidesIntro"])}</p><p class="guide-version">{e(c["byline"])}</p>{guide_cards(locale)}<section class="quick-start"><div><h2>{e(c["readyTitle"])}</h2><p>{e(c["readyText"])}</p>{store_badges(locale,"guides","guide_index")}</div></section></main>' + footer(locale)

def render_guide(locale, index):
    c = COPY[locale]
    g = GUIDE_COPY[locale][index]
    card = c['guideCards'][index]
    suffix = 'guides/' + SLUGS[index] + '/'
    html = head(locale,card['title'],card['text'],suffix,article=True) + header(locale,suffix)
    html += f'<main class="help-article" id="main"><a class="back-link" href="{path(locale,"guides/")}">← {e(c["backGuides"])}</a><p class="eyebrow">{e(c["guideLabel"])}</p><h1>{e(card["title"])}</h1><p class="help-lead">{e(card["text"])}</p><p class="guide-version">{e(c["byline"])}</p><div class="article-layout"><aside><nav class="article-toc" aria-label="{e(card["title"])}">'
    html += ''.join(f'<a href="#step-{i+1}">{e(section["title"])}</a>' for i,section in enumerate(g['sections']))
    html += '</nav></aside><div class="policy-content guide-content">'
    for i,section in enumerate(g['sections']):
        html += f'<h2 id="step-{i+1}">{e(section["title"])}</h2>'
        if 'list' in section:
            html += '<ol>' + ''.join(f'<li>{e(t)}</li>' for t in section['list']) + '</ol>'
        html += f'<p>{e(section["text"])}</p>'
        if 'table' in section:
            values = [[1200,900,600],[30,30,30],[50,50,50],[1280,980,680]] if section['table'] == 'rent' else [[50,50],[60,40],[70,30]]
            names = ['Alex','Sam','Jo'] if section['table'] == 'rent' else ['Alex','Sam']
            separator = '\u202f' if locale == 'fr' else '.' if locale in ['es','it'] else ','
            html += f'<div class="table-scroll"><table><caption>{e(card["title"])} · USD</caption><thead><tr><th scope="col">USD</th>'+''.join(f'<th scope="col">{name}</th>' for name in names)+'</tr></thead><tbody>'
            for label,amounts in zip(section['rows'],values):
                html += f'<tr><th scope="row">{e(label)}</th>'+''.join(f'<td>{e(format(n,",").replace(",",separator))}</td>' for n in amounts)+'</tr>'
            html += f'</tbody></table></div><p class="guide-version">{e(g["currency"])}</p>'
    html += f'<p class="guide-version">{e(g["currency"])}</p><section class="related-guides"><h2>{e(c["relatedTitle"])}</h2>'
    html += ''.join(f'<a href="{path(locale,"guides/"+slug+"/")}">{e(item["title"])}</a>' for j,(slug,item) in enumerate(zip(SLUGS,c['guideCards'])) if j != index)
    html += f'</section><h2>{e(c["navSupport"])}</h2><p>{e(c["englishDocs"])}</p><p><a href="{path(locale,"support/")}">{e(c["supportAction"])} ↗</a></p><section class="quick-start"><div><h2>{e(c["readyTitle"])}</h2>{store_badges(locale,"guides","guide_article")}</div></section></div></div></main>'
    return html + footer(locale)

def render_help_index(locale):
    c = COPY[locale]
    cards = ''.join(f'<article class="help-topic"><a href="/support/{slug}/"><h2>{e(title)} ↗</h2><p>English</p></a></article>' for slug,title in zip(HELP,c['helpTopics']))
    return head(locale,c['navSupport'],c['helpIntro'],'support/') + header(locale,'support/') + f'<main class="help-home" id="main"><a class="back-link" href="{path(locale)}">← {e(c["home"])}</a><h1>{lines(c["helpTitle"])}</h1><p class="help-lead">{e(c["helpIntro"])}</p><p class="locale-notice">{e(c["englishDocs"])}</p><div class="help-topics">{cards}</div><p><a href="{path(locale,"guides/")}">{e(c["navGuides"])} ↗</a></p></main>'+footer(locale)

def write(suffix, content):
    dest = ROOT / suffix.strip('/') / 'index.html'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(content+'\n')

for locale in COPY:
    home = render_home(locale)
    validate_home_badges(home, locale)
    write(path(locale), home)
    write(path(locale,'guides/'),render_guide_index(locale))
    if locale != 'en':
        write(path(locale,'support/'),render_help_index(locale))
        for index in range(3):
            write(path(locale,'guides/'+SLUGS[index]+'/'),render_guide(locale,index))

# Retain the more detailed English articles and the existing help search behavior.
for file in [*ROOT.glob('support/**/index.html'), *ROOT.glob('guides/*/index.html')]:
    text = file.read_text()
    suffix = str(file.relative_to(ROOT)).removesuffix('index.html')
    family = suffix if suffix == 'support/' or suffix.startswith('guides/') else 'support/'
    text = re.sub(r'<!-- language-menu -->.*?<!-- /language-menu -->','',text,flags=re.S)
    text = text.replace('</nav></header>','<!-- language-menu -->'+language_menu('en',family)+'<!-- /language-menu --></nav></header>',1)
    text = text.replace('<body>','<body class="landing">',1)
    text = re.sub(r'<link rel="stylesheet" href="/assets/landing.css[^\"]*">','',text)
    text = text.replace('</head>','<link rel="stylesheet" href="/assets/landing.css?v=android-search-20261111"></head>')
    if suffix == 'support/' or suffix.startswith('guides/'):
        text = re.sub(r'<link rel="alternate" hreflang="[^\"]+" href="[^\"]+">','',text)
        text = text.replace('</head>',alternates(suffix)+'</head>')
    ios, android = stores('guides','content','en')
    text = re.sub(r'<a[^>]+href="(?:\.\./)+(?:#download)">Get the app ↓</a>',f'<a href="{e(ios)}">App Store ↗</a><a href="{e(android)}">Google Play ↗</a>',text)
    text = text.replace('<a class="button" href="../../#download">Get LoopSplit →</a>',store_badges('en','guides','guide_article'))
    text = re.sub(r'<div class="(?:direct-downloads|download-actions store-badges)">.*?</div>', store_badges('en','guides','guide_article'), text, flags=re.S)
    def campaign_anchor(match):
        opening = match.group(0)
        href = re.search(r'href="([^\"]+)"',opening)
        if not href:
            return opening
        old = href.group(1)
        if re.match(r'https://apps.apple.com/(?:[^/]+/)?app/.*id6817176363',old):
            return opening.replace(old,e(ios))
        if old.startswith('https://play.google.com/store/apps/details?id=com.loop.loopsplit'):
            return opening.replace(old,e(android))
        return opening
    file.write_text(re.sub(r'<a\b[^>]*>',campaign_anchor,text))

# Sitemap alternate annotations only point at actual translated counterparts.
ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
xhtml = 'http://www.w3.org/1999/xhtml'
ET.register_namespace('',ns)
ET.register_namespace('xhtml',xhtml)
site = ET.Element('{'+ns+'}urlset')
families = ['', 'support/', 'guides/'] + ['guides/'+slug+'/' for slug in SLUGS]
routes = {path(locale,suffix):suffix for locale in COPY for suffix in families}
for file in sorted(ROOT.rglob('index.html')):
    if '.git' in file.parts:
        continue
    uri = '/' + str(file.relative_to(ROOT)).removesuffix('index.html')
    node = ET.SubElement(site,'{'+ns+'}url')
    ET.SubElement(node,'{'+ns+'}loc').text = BASE + uri
    ET.SubElement(node,'{'+ns+'}lastmod').text = '2026-11-11' if uri in {path(locale) for locale in COPY} | {'/guides/split-rent-and-utilities/'} else DAY
    if uri in routes:
        suffix = routes[uri]
        for locale,c in COPY.items():
            ET.SubElement(node,'{'+xhtml+'}link',{'rel':'alternate','hreflang':c['tag'],'href':BASE+path(locale,suffix)})
        ET.SubElement(node,'{'+xhtml+'}link',{'rel':'alternate','hreflang':'x-default','href':BASE+path('en',suffix)})
ET.indent(site,space='  ')
ET.ElementTree(site).write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)

print(f'Rendered {len(COPY)} homepages; translated guide articles and hubs; sitemap contains {len(site)} pages.')
