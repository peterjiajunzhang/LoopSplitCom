# Website alignment with released iOS 1.2.0

## November 4, 2026 release alignment

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
