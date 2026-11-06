# Website release alignment

## November 6, 2026 complete localized media

Fixed the feature-card image sizing: intrinsic HTML height previously remained fixed while CSS reduced image width, stretching screenshots; fixed-height artwork containers then cropped their bottom edges. Images now use automatic height and their native aspect ratio, containers expand around the full image, and narrow layouts stack copy above artwork.

All seven homepages now select their own released 1.2.1 screenshots and approved typography-r2 Header/Search videos and posters. The 21 PNGs are the complete 1284×2778 screenshots read from the released ASC localizations. The 12 non-English videos were recovered from the existing approved App Asset Library assets, matched uniquely to the frozen campaign by original file size and canvas. They use Apple's processed H.264 SDR rendition, encoded for web delivery without changing the 30-second story. They are not byte-identical to the frozen original MP4s. The two existing English MP4s remain unchanged. No ASC metadata or assets were modified. Provenance, source IDs and delivered-file hashes are recorded in [assets/media/manifest.json](assets/media/manifest.json).

`content/media.json` is the single locale-to-media mapping. The renderer checks complete locale coverage, screenshot dimensions, existing files and separate paths for every language. Video selection and posters follow the page language and responsive composition. Captions no longer describe localized media as an English interface. Existing store attribution links, language navigation, policy text and app release state are preserved. The historical entries below retain their original observations.

## November 5, 2026 landing page and seven languages

This update supersedes the earlier hero and download layout below. The owner selected **好好相处，账算清楚。**; English uses **Less money talk. More good times.** from the approved video. The existing shared-expenses, recurring-bills and repayments introduction and the four benefit labels remain, alongside real product artwork. Official store badges move to the hero and link directly to stores; there is no intermediate download click. All seven homepages use original official localized badge artwork; colors and proportions are preserved. Free scanning / Loop quotas and optional Pro remain explicit farther down the page.

English, Simplified Chinese, Traditional Chinese, French, Spanish, Italian and Japanese each have a homepage, guide index, three practical guides and a help hub. The more detailed English help articles are preserved and labeled English from localized hubs. Policies remain English / Simplified Chinese; their terms and effective dates are unchanged. Canonicals, reciprocal `hreflang` and the sitemap now cover 54 actual pages. Website-only copy and layout changes do not change app listings or app releases.

Store links use the real ASC-generated provider token with separate home and guide campaign names. Google Play links include UTM and encoded referrer parameters. Website clicks, store listing visits and actual downloads must remain separate metrics. Muted videos automatically play in view unless reduced-motion, data-saving, manual pause or browser policy prevents it; native controls remain.

Source files are `content/landing.json`, `content/guides.json` and `scripts/build-landing.py`; generated pages are committed for static hosting. Detailed verification and the AI recommendation baseline are recorded in the app repository’s Monetization directory. Historical entries below retain their original observations.

## November 5, 2026 search launch

Published the shared expense guide index and three original worked examples for roommates, couples and recurring bills. All 18 pages have matching canonical/title/description metadata; guides add Article and Breadcrumb data, and existing pages add social/breadcrumb metadata. The visible homepage headline remains aligned with the App Store; its browser title describes shared expenses and recurring bills. Policy heading levels were adjusted without changing visible policy wording or effective dates.

Google domain ownership is verified; the sitemap reads Success with 18 discovered pages. Bing DNS verification is complete and its submitted sitemap initially reads Processing. IndexNow accepted one notification for the 18 URLs with HTTP 202. Valid HTTPS responses for 25 files match source, and 24 crawler User-Agent checks match normal page content. These checks do not establish indexing, AI recommendations or downloads. Details and follow-up are maintained in the [Monetization search launch receipt](https://github.com/peterjiajunzhang/LoopSplit/blob/main/docs/monetization/search-launch-2026-11-05.md).

## November 5, 2026 custom domain

The owner registered `loopsplit.app` with Cloudflare and authorized DNS and hosting configuration. The existing GitHub Pages site is bound to the apex domain; Cloudflare DNS points the apex and `www` at the GitHub Pages user host. Website canonical, sharing, structured-data and sitemap URLs now use `https://loopsplit.app/`. This changes URLs only in the published policy pages, preserving their effective dates and substantive terms. The old GitHub Pages paths remain the compatibility redirects for released apps and store metadata.

[HOSTING.md](HOSTING.md) records DNS targets, deployment ownership and the recommended separate Firebase Hosting / Cloud Run deployment for the future Web App and MCP service. Those future subdomains are not published by this website task.

## November 5, 2026 store-aligned brand copy

The homepage headline, document/social titles and social image alt text now use **Scan receipts. Split costs.**, exactly matching the English subtitle read back from the READY_FOR_DISTRIBUTION App Store App Info record. This replaces the website-only “Shared bills, kept fair” line. Hero supporting copy and search/social descriptions retain the wider shared-expenses, recurring-bills and repayments story across both released platforms. No store metadata is changed.

The old sharing image also contained the retired headline and an Apple-only availability line. It is replaced by a 1200×630 export of the new editable `assets/social-card.svg`, using the existing LoopSplit icon and brand colors, the store-aligned headline, and iPhone/iPad/Android availability. `scripts/render-social-card.swift` exports the vector source through system AppKit. The social image URL has a new cache key.

The PNG export was visually inspected at full resolution. Browser checks at 1280×900 and 390×844 confirm the intended two-line headline, loaded store badges and no horizontal overflow. Metadata consistency, local references and vector/PNG dimensions pass checks.

## November 5, 2026 official store badge update

The final download section now uses the official black English App Store and Google Play download badges. Apple artwork comes directly from Apple Developer; Google artwork is the English digital SVG from the current Partner Marketing Hub badge library. Both files retain their downloaded bytes; source links and hashes are recorded in `assets/store-badges/README.md`.

The App Store badge comes first. Both display at 48px high with 12px clear space on all sides and retain their intrinsic aspect ratios. Each link has an accessible app-specific name. The page contains one pair of artwork badges in the final download section; the hero’s Download LoopSplit button and main navigation both link there. Footer credits identify the relevant Apple and Google trademarks. No store account, app listing, policy terms, tracking behavior or deployment destination is changed.

Public responses checked for this update return the correct LoopSplit listing in both stores: Apple ID 6817176363 and Google Play package com.loop.loopsplit. The Google Play US page returns HTTP 200 with the product title and an InStock software offer; the earlier Android-pending observations below remain historical.

Browser checks of the final download section at the default desktop viewport and 390×844 confirm loaded badge images, 48px image heights, 12px padding, correct listing links and no horizontal overflow. The pair sits on one row on desktop and wraps into two centered rows on the phone. Clicking the hero’s Download LoopSplit button reaches this section. Existing Android launch content is preserved.

## November 5, 2026 Android public-launch alignment

The owner requested updating the official website and adding the Play link after Android launch. An anonymous US Google Play response now contains the public title **LoopSplit: Shared Expenses**, the approved short description and an Install action. The current app release receipt independently records Android 1.2.1 (14) as publicly available. This website update does not infer the availability of every storefront or device from that US response.

The homepage hero and main navigation lead to the download section, which shows equally visible App Store and Google Play badges; there is no automatic platform redirect. Search/social description and SoftwareApplication download/platform data include Android. The page no longer advertises a single version for both platforms. iOS/iPadOS 17+ is retained; Android 9+ is grounded in the released source’s minSdk 28.

Support navigation and the help hub lead to both platforms. Getting-started help covers Android invitations and the explicit web Open LoopSplit fallback. Pro help separates Apple and Google Play purchase/restore/cancellation paths and advises managing the original purchase rather than buying twice. Diagnostic help distinguishes Product Analytics / Crash Reports on Apple from Usage analytics / Crash diagnostics on Android. The policy/terms edits only change the previously planned or Apple-only availability wording to reflect released 1.2-series controls; the October 30 effective dates, legal rights, data categories, regional defaults and retention statements are preserved.

The existing icon, screenshots and two approved ASC overview videos are unchanged. The video caption identifies its iPhone presentation. This update does not change the app, subscriptions, Firebase invite hosting, AASA/assetlinks, access permissions or telemetry behavior.

Local verification: all 352 local HTML/asset/fragment references resolve across 15 HTML files; 14 sitemap locations and JSON-LD parse correctly; both shared JavaScript files pass syntax checks. Real Chrome inspection at 390×844 and 1280×900 found no horizontal overflow. The mobile store buttons are each 320px wide and about 56px high; desktop buttons sit beside each other. The existing player still selects Search on mobile and Header on desktop. Native app deep-link delivery and OEM camera behavior were not retested by this static website task.

Publication is performed through the existing GitHub Pages main/root workflow. The matching deployment commit, build state and complete served-byte readback are recorded in the LoopSplit app repository’s current website publication receipt after deployment. Private browser screenshots remain outside Git.

## Historical November 4 alignment

The following sections retain their original release and account observations. They are not current Android launch status.

### November 4, 2026 release alignment

The public Apple US lookup endpoint (`https://itunes.apple.com/lookup?id=6817176363&country=us`) returns version 1.2.0, released November 3, 2026 at 18:19 UTC, with minimum OS 17.0. Fresh ASC readback confirms 1.2.0 is READY_FOR_DISTRIBUTION; 1.2.1 is PREPARE_FOR_SUBMISSION. Android production access is still pending, so this refresh does not advertise a public Android launch.

The homepage now shows version 1.2.0 and iOS/iPadOS 17 compatibility. Release highlights cover independent Product Analytics and Crash Reports settings, stronger image access checks, and clearer Pro and account flows. Search and calculations remain in the core feature section. The existing approved videos, screenshots and app icon are retained: the new release does not replace their demonstrated core flows or branding.

The help center now contains nine guides. The new Privacy & Diagnostics guide explains where to find both controls, independent choices, device-local persistence, regional defaults, essential services and the limits of deleting previously submitted diagnostics. Its labels match the current app source. Account and Pro guidance includes the new settings and account-linking clarification. All guides now state the 1.2.0 scope. English and Chinese privacy/terms availability statements reflect the public iOS release while retaining their existing October 30 effective dates and substantive disclosures.

Local reference, metadata, heading, sitemap and JavaScript syntax checks pass. Browser inspection for this refresh is unavailable because local browser use is disabled in Work settings; the browser checks recorded below belong to the previous 1.1.0 publication. Verify the deployed files and GitHub Pages build after pushing this update.

## Historical 1.1.0 publication record

The remainder records the previous release audit and media validation. Its version/status observations describe that earlier publication, not the current App Store state.

## Release boundaries

The public Apple US and UK lookup endpoints return version 1.1.0, released October 30, 2026, with minimum OS 26.2. ASC readback confirms 1.1.0 is READY_FOR_DISTRIBUTION; 1.2.0 is PREPARE_FOR_SUBMISSION. The site therefore describes 1.1.0, adds its inline calculator and Book search/filter features, and continues to show iOS/iPadOS 26.2 as the requirement. Future 1.2.0 privacy switches and iOS 17 compatibility are not advertised as available.

Existing receipt recognition, Loops, estimates and shared Pro remain core capabilities, not claims of newly added 1.1 features. The approved overview video does not contain dedicated calculator/search chapters; the new feature section and help article cover those additions separately.

## Approved media reuse

Reused the existing ASC creative campaign's approved `motion-r7-multilingual-r1/typography-r2` English compositions without modifying their content. Only the English pair is used on the English website; no new locale/size production or ASC writes occurred.

| Asset | Source composition | Dimensions | Duration | SHA-256 |
|---|---|---|---|---|
| assets/video/loopsplit-header-en.mp4 | outputs/en-US/header/movie.mp4 | 3840 × 1646 | 30 seconds | 77efe0a42b2beb05b49d2957ed7f34414a31ccb634c6850ed4ff50d90cf2ea60 |
| assets/video/loopsplit-search-en.mp4 | outputs/en-US/search/movie.mp4 | 1920 × 1280 | 30 seconds | 294fa4465d54c4fc2d5ac2e3de82494afdf6d170a8fc09e32de95fa70454a570 |

The campaign manifest records H.264, yuv420p, BT.709, faststart and no audio for both. Copies match source hashes. Decoded frame count/rate validates 30 seconds at 30fps. Poster images use the 3-second frames in their original aspect ratios. Representative frames from five points in each video were visually reviewed. The film uses the approved six-chapter product narrative and does not add source-attribution captions to the customer-facing website.

The desktop homepage uses Header; widths of 640px and below use Search. One player selects one composition rather than downloading or showing both simultaneously. The player has native playback/fullscreen controls, inline playback, posters and preload="none"; visitors start playback themselves. Changing viewport composition pauses/reset playback. A written summary provides the product explanation without playing the video. No new analytics are added to the website.

## Content alignment

- Homepage release badge and SoftwareApplication metadata updated to 1.1.0.
- Added the search/calculation feature section and eighth help article with instructions, expected results and limitations.
- Updated help guide version scope and shared CSS cache keys.
- Removed the broad "No tracking" homepage pill and aligned the privacy summary with released 1.1 usage statistics/crash reports.
- Made free-trial wording conditional on the actual store offer/eligibility, consistent with current terms.
- Matched account-deletion help to the current policy's cleanup/access-revocation timing.
- Preserved the already published privacy and terms files, including the planned status of 1.2 controls and current access-cutover statements.
- Updated sitemap entries for changed content; retained existing official URLs and Firebase invite-link hosting.

## Validation

All 278 local HTML links, assets and fragment references resolve. Support headings, sitemap XML, shared scripts and source hashes pass checks. At 1280 × 900 the player selected Header and decoded to 3840 × 1646; at 390 × 844 it selected Search and decoded to 1920 × 1280. Actual browser playback was confirmed for both, each reporting 30 seconds. Neither checked viewport overflowed horizontally. The new guide opened from the homepage with its expected canonical URL. This website task did not replay the app flows on a physical device.

## Publication follow-up

After pushing the reviewed main commit, check GitHub Pages completion, compare the served homepage/help/scripts against the committed files, and verify both MP4 responses and live playback. Future app releases should update scope and requirements only after checking public distribution; do not infer release status from a local build.
