# Website launch audit — October 22, 2026

Production: https://peterjiajunzhang.github.io/LoopSplitCom/

## Release source

Apple's public lookup endpoint (`https://itunes.apple.com/lookup?id=6817176363&country=us`) confirmed version 1.0.0, release date October 22, 2026 and minimum OS 26.2. Live store copy and screenshots take precedence over the older iOS checkout and historical release notes.

## Completed

- Replaced prelaunch messaging with working App Store links and device requirements.
- Replaced the old home-screen preview with three official 1.0.0 App Store screenshots: scanning, Loops and balances. Example data is labelled. Updated site and touch icons from the live store artwork.
- Added a receipt → recurring cost → repayment explanation and a final download section.
- Matched scanning limits (3 total per free account across devices), Pro scanning/cropping, 3 active free Loops per Book and Book-level Pro sharing to the released listing.
- Updated FAQ for receipt recognition, review before saving, downloading, restoring/cancelling purchases, invite acceptance and leaving Books. Corrected the suggestion that repayments always use the minimum possible transfer count.
- Removed the homepage's blanket no-analytics claim to remain consistent with existing Android SDK disclosures. Existing privacy policy, Android terms and ownership verification remain available.
- Added sharing artwork, Open Graph metadata, Smart App Banner, application structured data and sitemap.
- Updated the Firebase invite landing page in the iOS repository with the real download button, including Chinese text. Retained invite-code parsing and universal-link association.

## Validation

- Checked all local HTML link and asset paths, fragment targets, unique IDs and image alt attributes across home, support, privacy and Android terms.
- Checked changed files for whitespace errors and remaining prelaunch messaging.
- Browser reviewed the narrow-screen homepage in system dark mode and exercised the support navigation and receipt-scanning FAQ disclosure. Other device sizes and light mode have responsive CSS but were not individually browser-tested in this run.
- Live store imagery and icon are downloaded copies served locally, with no dependency on Apple image URLs at page-load time.

## Maintenance

No custom domain was configured; the existing GitHub Pages URL remains the official address referenced by the released app. GitHub Pages project-level robots.txt cannot control the origin's root robots.txt; the sitemap can be submitted directly in Search Console. Search appearance and social preview caches may update later. Update this site when shipping new app functionality or changing Pro entitlements.
