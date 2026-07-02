# Deploy — instant33.com (Cloudflare Pages)

**Purpose:** How the live site is deployed and the one setting that had to be right.
**Status:** live-prep, 2026-07-02.

---

## What serves the site

- **Host:** Cloudflare Pages, project `ai-agency-july`, connected to this GitHub repo.
- **Production branch:** `main` (auto-deploys on every merge).
- **Served directory:** `designs/01-dispatch/` — declared in [`wrangler.toml`](wrangler.toml) via `pages_build_output_dir`.
- **Domain:** `instant33.com` (apex) + `www.instant33.com` (redirects to apex via `_redirects`).
- **No build step** — static files served as-is.

## The gotcha that caused the first 404

Cloudflare Pages was serving the **repo root** (which has no `index.html`) instead of `designs/01-dispatch/`, so `instant33.com` returned a 404. For a no-build project, the **Build output directory** — not the Root directory — decides what is served.

**Fix (in this repo):** `wrangler.toml` at the repo root sets `pages_build_output_dir = "designs/01-dispatch"`.

**Fix (in the Cloudflare dashboard, needed once so Cloudflare reads the wrangler.toml):**
1. Project → **Settings → Builds & deployments → Build configuration → Edit**.
2. Set **Root directory** to empty (`/`). *(With the root directory set to a subfolder, Cloudflare looks for `wrangler.toml` there and won't find the repo-root one.)*
3. Leave **Build command** empty and **Framework preset** = None. Save.
4. **Deployments → Retry deployment** (or merge any commit to `main`).

*(Equivalent alternative if you'd rather not use wrangler.toml: leave Root directory empty and set **Build output directory** = `designs/01-dispatch` directly in that same dialog.)*

## Verify after redeploy

- `https://instant33.com/` loads the page (not a 404).
- `https://www.instant33.com/` redirects to the apex.
- `https://instant33.com/robots.txt`, `/sitemap.xml`, `/llms.txt` load.
- A random path (e.g. `/nope`) shows the styled 404.
- Run https://pagespeed.web.dev/analysis?url=https://instant33.com and https://search.google.com/test/rich-results?url=https://instant33.com


## Rebrand (2026-07-02)

The site brand is **Instant33** (matches the domain). Name + logo (lightning bolt) applied across all pages, meta, OG image, icons, manifest, JSON-LD, llms.txt, and legal pages. Contact email set to hello@instant33.com; legal entity shown as "Instant33"; effective date July 2, 2026. Still to fill: [STATE OF INCORPORATION], [BUSINESS ADDRESS]. Internal folder stays `designs/01-dispatch/` so the Pages deploy path is unaffected.

## Analytics & security (added 2026-07-02, post-launch)

- **Google Analytics 4** (`G-95TQKGDL1Y`) installed on all pages via gtag.js (async).
- **Content-Security-Policy** added in `_headers` (allows Google Fonts + GA, blocks framing/object/base-uri). Tested: no CSP violations, GA + fonts + funnel + pricing toggle all work.
- **`/.well-known/security.txt`** (RFC 9116) added — update the contact address when email is live.
- **Moved `COPY-NOTES.md` out of the deploy root** → `designs/COPY-NOTES.md`, so internal notes are no longer served publicly.

### GDPR/consent note
GA4 sets cookies. The site is US-focused (per the Privacy Policy), so this is common practice, but for EU/UK visitors a consent banner + Google Consent Mode is the compliant setup. Say the word and I'll add a lightweight, no-dependency consent banner wired to Consent Mode v2.

## Still owner-only (dashboard / DNS — cannot be automated from the coding env)

- Google Search Console verification + sitemap submission (the get-ranked step).
- Email Routing + SPF/DMARC records.
- Bot Fight Mode, TLS min 1.2, SSL Full (strict) — reported done.
