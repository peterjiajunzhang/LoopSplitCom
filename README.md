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

Invite links (`/j/<code>`) and `apple-app-site-association` are served by Firebase Hosting from the LoopSplit app repo, not from here.
