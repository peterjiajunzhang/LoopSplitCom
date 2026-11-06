# Website maintenance rules

## Store downloads — owner requirement

- Both the homepage hero **and** final download section must show the official App Store and Google Play download badges, in all seven languages. Never fix one placement by removing the badges from the other.
- Use the shared `store_badges` renderer for prominent download calls to action, including guide pages. Plain navigation links may remain text.
- Use the existing original localized SVG files in `assets/store-badges/`, App Store first. Keep their colors, text, proportions and required clear space. Do not replace them with custom buttons, standalone store icons, generated logos or text pills for visual consistency.
- Each badge links directly to the corresponding LoopSplit store listing in one click. Preserve attribution parameters and the page language.
- Edit the renderer rather than only generated HTML. Run `python3 scripts/build-landing.py` and `python3 scripts/check_store_badges.py`. The build must reject a homepage missing either official badge at either placement.
- Before publishing a download-layout change, inspect **both ends** of the page at desktop and phone widths. Preserve the language-specific screenshots, videos and complete image aspect ratios.

Publish authorized changes through the existing GitHub Pages deployment. Keep unrelated working files intact.
