# LoopSplit website

Static site for LoopSplit: home page, support and privacy policy. No build step or dependencies.

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

## User help center

`support/` is the iOS 1.2.0 help hub. Nine static guides cover getting started, expenses, Loops, balances, receipts and estimates, Pro, account/sync issues, search/calculations, and privacy/diagnostics. The hub filters guide topics locally with `assets/help.js`; every guide remains accessible without JavaScript. Each article includes a table of contents, steps, expected outcomes and related guides. Update button labels and behavior against the released app when changing these pages, and include new article URLs in `sitemap.xml`.

## Policy publication

Privacy and Terms retain their October 30, 2026 effective dates. The November 4 website refresh updates the availability statements for the now-public iOS 1.2.0 privacy controls; it does not imply that Android has been publicly released. Preserve the existing data, regional defaults, deletion and access-cutover disclosures when revising these pages.

## Product overview video

The homepage reuses approved ASC typography-r2 English media. Desktop uses the wide Header composition; at 640px and below it uses the Search composition, without cropping either video. Playback is visitor-controlled, with native controls, inline playback, posters and `preload="none"`. Both files have no audio. The video summary and text feature sections keep the overview accessible without playback. See `WEBSITE_RELEASE_ALIGNMENT.md` for provenance and release boundaries.
