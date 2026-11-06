# Domain and hosting

The production website uses `https://loopsplit.app/`. Cloudflare manages the domain and DNS; the existing GitHub Pages `main`/root deployment continues to serve the static site. The tracked `CNAME` file keeps the custom-domain binding with the source.

| Name | DNS record | Target | Mode |
|---|---|---|---|
| `loopsplit.app` | Apex CNAME, flattened by Cloudflare | `peterjiajunzhang.github.io` | DNS only, Auto TTL |
| `www.loopsplit.app` | CNAME | `peterjiajunzhang.github.io` | Proxied, Auto TTL; Cloudflare redirects at the edge |

GitHub Pages manages the apex TLS certificate; HTTPS enforcement is enabled. `loopsplit.app` is the canonical hostname. Cloudflare's active Universal SSL certificate covers `www`; a Single Redirect in `http_request_dynamic_redirect` matches only `www.loopsplit.app` and returns 301 to `concat("https://loopsplit.app", http.request.uri.path)`, preserving the query string. This handles `www` before an origin request, without depending on a GitHub certificate for that hostname. Keep this rule enabled while `www` is proxied.

The original `https://peterjiajunzhang.github.io/LoopSplitCom/` URLs remain important for already-released app and store links and continue to redirect, including support/privacy paths. Keep the DNS target free of the repository path. On November 5, apex HTTPS returned 200 with valid certificate verification; `https://www.loopsplit.app/support/?ref=domain-check` returned 301 to the same apex path and query; the original GitHub privacy URL returned 301 to the HTTPS apex privacy page.

Google Search Console uses a retained apex TXT verification record. Bing Webmaster Tools uses a separate DNS-only verification CNAME. These verification records are not website routing records and should remain in place. Personal-account GitHub Pages domain verification remains optional and requires the owner's GitHub browser login; the repository domain binding and HTTPS are already configured.

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
