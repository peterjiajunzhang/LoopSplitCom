# Domain and hosting

The production website uses `https://loopsplit.app/`. Cloudflare manages the domain and DNS; the existing GitHub Pages `main`/root deployment continues to serve the static site. The tracked `CNAME` file keeps the custom-domain binding with the source.

| Name | DNS record | Target | Mode |
|---|---|---|---|
| `loopsplit.app` | Apex CNAME, flattened by Cloudflare | `peterjiajunzhang.github.io` | DNS only, Auto TTL |
| `www.loopsplit.app` | CNAME | `peterjiajunzhang.github.io` | DNS only, Auto TTL |

GitHub Pages manages the site's TLS certificate and HTTPS enforcement. `loopsplit.app` is the canonical hostname; GitHub redirects the `www` variant to it. The original `https://peterjiajunzhang.github.io/LoopSplitCom/` URLs remain important for already-released app and store links and must continue to redirect, including support/privacy paths. Keep the DNS target free of the repository path.

Canonical links, social URLs, SoftwareApplication metadata, `robots.txt` and `sitemap.xml` use the new root domain. Existing Firebase-hosted invitation and app-association endpoints remain on their current host; this website deployment does not replace them.

## Planned Web App and MCP deployment

| Address | Suggested hosting | Status |
|---|---|---|
| `loopsplit.app` | Existing GitHub Pages marketing website | Current production target |
| `app.loopsplit.app` | Firebase Hosting for the React/Vite SPA | Planned; no DNS target created |
| `mcp.loopsplit.app` | Cloud Run for the Node/Express MCP service | Planned; no DNS target created |

The current `LoopSplit/web` and `LoopSplit/server` projects already use Firebase Auth, Firestore and a trusted Node/Express API. Firebase Hosting can forward `/api/**` to Cloud Run, preserving the SPA's relative API routes. That is the recommended next deployment path for the existing implementation. Moving the marketing website or rewriting the backend for another runtime is not required to launch the Web App.

The Web App, OAuth bridge and MCP service have their own production readiness work; configuring this website domain does not publish them. Add their DNS records only when their actual deployment targets are known.

References: [GitHub Pages domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Cloudflare CNAME flattening](https://developers.cloudflare.com/dns/cname-flattening/), [Firebase Hosting with Cloud Run](https://firebase.google.com/docs/hosting/cloud-run).
