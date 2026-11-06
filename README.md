# LoopSplit website

Static site for LoopSplit: home page, support and privacy policy. No build step or dependencies. Download entry points use the verified App Store ID `6817176363` and Google Play package `com.loop.loopsplit`. Main navigation leads to the homepage’s two-store download section rather than assuming an Apple device.

Preview locally from this folder:

```sh
python3 -m http.server 4173
```

Then open `http://localhost:4173/`.

The site deploys from the `main` branch with GitHub Pages to https://peterjiajunzhang.github.io/LoopSplitCom/.

These URLs are used by the app (`AppInfo`) and App Store Connect, so keep the paths stable:

- Support: `/support/`
- Privacy Policy: `/privacy/`
- Cross-platform Terms of Use (English / 简体中文): `/terms/`
- Android Terms of Use (existing link retained): `/terms/android/`

Invite links (`/j/<code>`) and `apple-app-site-association` are served by Firebase Hosting from the LoopSplit app repo, not from here.

## Brand copy and sharing card

The homepage headline is **Scan receipts. Split costs.**, matching the released App Store English subtitle. Keep the page title, social title, image alt text and sharing card aligned with this wording. Website copy covers both released stores; it does not change their listings.

The editable sharing card is `assets/social-card.svg`; the website serves its 1200×630 PNG export for social platform compatibility. After editing the SVG, run `swift scripts/render-social-card.swift` on macOS and inspect the resulting PNG. This optional asset export uses system AppKit and adds no website build dependencies. Change the social image URL cache key when replacing the card.

## User help center

`support/` covers the released 1.2 series on iPhone, iPad and Android. Nine static guides cover getting started, expenses, Loops, balances, receipts and estimates, Pro, account/sync issues, search/calculations, and privacy/diagnostics. The hub filters guide topics locally with `assets/help.js`; every guide remains accessible without JavaScript. Each article includes a table of contents, steps, expected outcomes and related guides. Update button labels and behavior against the released app when changing these pages, and include new article URLs in `sitemap.xml`.

## Policy publication

Privacy and Terms retain their October 30, 2026 effective dates. The November 5 Android launch refresh updates only the factual availability statements for the already-released privacy controls on both platforms. Preserve the existing data, regional defaults, deletion and access-cutover disclosures when revising these pages.

## Android launch update

The November 5 homepage, support navigation and getting-started guide link to both stores. Android Pro help links to Google Play subscription management; diagnostic guidance uses each platform’s actual English control labels. Requirements are iOS/iPadOS 17+ and Android 9+ (Android minSdk 28). No new analytics, automatic store redirects, app builds or Firebase Hosting changes are introduced. See [release alignment and verification](WEBSITE_RELEASE_ALIGNMENT.md) for scope and evidence.

## Store badges

The final download section uses one pair of official English download badges, App Store first. The hero’s Download LoopSplit button and the main navigation both lead to this section. Original SVG artwork is stored locally in `assets/store-badges/`; [asset sources and usage notes](assets/store-badges/README.md) record its provenance. Both badges display at 48px high with 12px clear space and preserve their intrinsic proportions. The App Store badge appears once in the page layout. Keep the footer trademark credits and the real app listing links when changing these entry points.

## Product overview video

The homepage reuses approved ASC typography-r2 English media. Desktop uses the wide Header composition; at 640px and below it uses the Search composition, without cropping either video. Playback is visitor-controlled, with native controls, inline playback, posters and `preload="none"`. Both files have no audio. The video summary and text feature sections keep the overview accessible without playback. See `WEBSITE_RELEASE_ALIGNMENT.md` for provenance and release boundaries.
