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

`support/` is the iOS 1.0.0 help hub. Seven static guides cover getting started, expenses, Loops, balances, receipts and estimates, Pro, and account/sync issues. The hub filters guide topics locally with `assets/help.js`; every guide remains accessible without JavaScript. Each article includes a table of contents, steps, expected outcomes and related guides. Update button labels and behavior against the released app when changing these pages, and include new article URLs in `sitemap.xml`.

## Policy publication

The October 26, 2026 edits are local review drafts, not evidence of publication or effectiveness. Before publication, set the actual effective date and version in the cross-platform Terms and record the effective date of the synchronized Android Terms and Privacy Policy; update them to match the actual rollout and notices.
