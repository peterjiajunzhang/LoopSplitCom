# LoopSplit website

Static site for LoopSplit: home page, support and privacy policy. No build step or dependencies. Download entry points use the verified App Store ID `6817176363` and Google Play package `com.loop.loopsplit`. The homepage’s official store badges link directly to each store in one click.

Preview locally from this folder:

```sh
python3 -m http.server 4173
```

Then open `http://localhost:4173/`.

The site deploys from the `main` branch with GitHub Pages at https://loopsplit.app/. Cloudflare manages domain registration and DNS. The former `https://peterjiajunzhang.github.io/LoopSplitCom/` address is retained as a redirect for existing app and store links. See [domain configuration and the planned Web App/MCP hosting](HOSTING.md).

The [shared expense guides](https://loopsplit.app/guides/) cover rent and utilities, couples and recurring bills. Their static HTML, article/breadcrumb metadata, canonical links and sitemap are maintained alongside the Help Center. `llms.txt` is a convenience index of official facts and documentation, not a guarantee of AI citations. Search Console, Bing and IndexNow results are recorded separately from indexing and acquisition outcomes.

See the app repository's [November 5 search launch receipt](https://github.com/peterjiajunzhang/LoopSplit/blob/main/docs/monetization/search-launch-2026-11-05.md) for backend verification, published content checks and acquisition follow-up.

These URLs are used by the app (`AppInfo`) and App Store Connect, so keep the paths stable:

- Support: `/support/`
- Privacy Policy: `/privacy/`
- Cross-platform Terms of Use (English / 简体中文): `/terms/`
- Android Terms of Use (existing link retained): `/terms/android/`

Invite links (`/j/<code>`) and `apple-app-site-association` are served by Firebase Hosting from the LoopSplit app repo, not from here.

## Brand copy and sharing card

The homepage headline is **Less money talk. More good times.**, taken from the approved product video. Chinese uses **好好相处，账算清楚。** The original shared-expense / recurring-bill / repayment introduction is retained, with free expense tracking, no daily limits, no ads and on-device scanning as supporting labels. The hero pairs this copy with real released-product artwork; it does not change store listings.

The editable sharing card is `assets/social-card.svg`; the website serves its 1200×630 PNG export for social platform compatibility. After editing the SVG, run `swift scripts/render-social-card.swift` on macOS and inspect the resulting PNG. This optional asset export uses system AppKit and adds no website build dependencies. Change the social image URL cache key when replacing the card.

## User help center

`support/` covers the released 1.2 series on iPhone, iPad and Android. Nine static guides cover getting started, expenses, Loops, balances, receipts and estimates, Pro, account/sync issues, search/calculations, and privacy/diagnostics. The hub filters guide topics locally with `assets/help.js`; every guide remains accessible without JavaScript. Each article includes a table of contents, steps, expected outcomes and related guides. Update button labels and behavior against the released app when changing these pages, and include new article URLs in `sitemap.xml`.

## Policy publication

Privacy and Terms retain their October 30, 2026 effective dates. The November 5 Android launch refresh updates only the factual availability statements for the already-released privacy controls on both platforms. Preserve the existing data, regional defaults, deletion and access-cutover disclosures when revising these pages.

## Android launch update

The November 5 homepage, support navigation and getting-started guide link to both stores. Android Pro help links to Google Play subscription management; diagnostic guidance uses each platform’s actual English control labels. Requirements are iOS/iPadOS 17+ and Android 9+ (Android minSdk 28). No new analytics, automatic store redirects, app builds or Firebase Hosting changes are introduced. See [release alignment and verification](WEBSITE_RELEASE_ALIGNMENT.md) for scope and evidence.

## Store badges

Each homepage has one pair of official localized badges in its hero, App Store first, linking directly to the corresponding store. The final section uses direct text links. Original SVG artwork and provenance are in [assets/store-badges/](assets/store-badges/README.md). Desktop badges display at 48px with 12px clear space; phone badges at 40px with 10px clear space. Colors and proportions remain unchanged.

Apple campaign links use the provider token actually generated in App Store Connect, with separate `website_home_20261105` and `website_guides_20261105` campaigns. Google Play uses matching UTM campaign names and encoded referrer parameters, with language and placement in `utm_content`. These are store attribution links, not a website click collector or proof of installation.

## Seven website languages

English is `/`; Simplified Chinese, Traditional Chinese, French, Spanish, Italian and Japanese use `/zh-hans/`, `/zh-hant/`, `/fr/`, `/es/`, `/it/` and `/ja/`. Each includes a homepage, guide index, three practical guides and a help hub. Detailed help articles remain English; localized hubs label those links accordingly. Privacy and Terms remain English / Simplified Chinese with their existing terms and effective dates.

Edit `content/landing.json` and `content/guides.json`, then run `python3 scripts/build-landing.py`. Generated HTML is committed and served without a runtime build. The renderer maintains canonical URLs, reciprocal language alternates, language switching and the 54-page sitemap. Keep existing support and policy paths stable.

### Localized screenshots and video

`content/media.json` maps every homepage language to three released 1.2.1 screenshots and both approved video compositions with their posters. Screenshots retain their full original aspect ratio; feature cards expand to fit, and use a vertical layout on phones and narrow windows. Update this mapping when replacing media. The renderer checks dimensions, file existence and distinct language paths rather than silently falling back to English. Source IDs, hashes and video delivery transformations are recorded in [assets/media/](assets/media/README.md).

## Product overview video

All seven homepage languages reuse the approved ASC typography-r2 campaign in their own language. Desktop uses the wide Header composition; at 640px and below it uses the Search composition, without cropping either video. Non-English videos are web delivery encodes of Apple's processed approved assets; the existing English files are unchanged. Muted playback starts when the player enters view, pauses outside view or when the tab is hidden, and respects reduced motion, data-saving preferences and manual pauses. Browser/device policy can still require pressing Play. Native controls, inline playback, posters and `preload="none"` remain available. All files have no audio. The video summary and text feature sections keep the overview accessible without playback. See `WEBSITE_RELEASE_ALIGNMENT.md` for provenance and release boundaries.
