# Website media provenance

`../../content/media.json` controls the seven homepage languages. `manifest.json` records the delivered files, original ASC IDs, public CDN sources and SHA-256 checksums. These are LoopSplit’s own product assets.

- Screenshots: 21 full 1284×2778 PNGs from the released iOS 1.2.1 localizations, three per language (balances, Loops and receipt scanning).
- Video: the existing approved R7 typography-r2 campaign, Header and Search for all seven languages. The two English MP4s and posters are retained. The 12 non-English videos use Apple’s processed H.264 SDR rendition, re-encoded using libx264 CRF21, yuv420p, faststart and no audio for web delivery. Every derivative decodes to 900 frames at 30fps / 30 seconds. This is a delivery transformation; it does not recreate the UI or alter the approved story. Derivatives do not have the original frozen export’s byte hash.
- Posters: one per composition and language, retaining the corresponding video aspect ratio.

The original heavy exports were no longer present locally. Official App Asset Library reads recovered the approved video assets; original file size and canvas each identified a unique matching frozen campaign asset. No store assets or listing metadata were changed.

Keep media attribution and this technical provenance in repository documentation. Customer-facing captions describe the product in the selected language.
