# Build & Deploy Troubleshooting Playbook

**Purpose:** Symptom-driven diagnosis and repair for the {{BRAND_NAME}} site's build and deployment failures — build errors, broken images/fonts (404/CORS), env/config problems, cache/stale deploys, redirect loops, mixed content, font FOUT/FOIT, and CDN issues — each as `Symptom → Likely cause → Diagnosis → Fix → Prevention` so any developer can get a correct, current site live.
**Status:** v1 foundation — adjustable.

---

> **This is the deploy-layer incident guide.** Performance budgets that gate builds live in [`../performance/performance-budget.md`](../performance/performance-budget.md); asset/caching/compression tactics live in [`../performance/asset-efficiency.md`](../performance/asset-efficiency.md); redirect/canonical-host *rules* live in [`../seo/technical-seo.md`](../seo/technical-seo.md). This file is what you open when the build breaks or the deployed site is wrong/stale.
>
> **For P1 (site down / broken deploy): roll back first, diagnose second.** A working previous deploy beats a perfect root-cause. See §9.
>
> Reference [design tokens](../design-system/design-tokens.md) by name; literal statuses/headers/paths are diagnostics and stay literal.

---

## 0. TL;DR — build/deploy triage in one screen

- [ ] **Read the build log top to bottom** — the *first* error is the real one; later errors are usually cascades.
- [ ] **Reproduce locally with a production build** (`build` script, not `dev`) before blaming the host. Most "works on my machine" issues are dev-vs-prod differences.
- [ ] **Check env vars** — the #1 cause of "works locally, fails/blank in prod."
- [ ] **Stale in prod?** It's almost always **cache** (CDN or browser), not the build.
- [ ] **`curl -sI <url>`** is your fastest probe for status, redirects, cache, CORS, and security headers.
- [ ] **Never mix HTTP into an HTTPS page** — one `http://` asset trips mixed-content blocking.

### Fast probes

| Question | Command |
|---|---|
| Status / redirects | `curl -sIL <url>` |
| All response headers | `curl -sI <url>` |
| Is it gzip/brotli? | `curl -sI -H "Accept-Encoding: br,gzip" <url>` → `content-encoding` |
| CORS allowed? | `curl -sI -H "Origin: https://{{DOMAIN}}" <asset-url>` → `access-control-allow-origin` |
| Cache state (CDN) | `curl -sI <url>` → `cache-control`, `age`, `x-cache`/`cf-cache-status` |

---

## 1. Build failures

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Build fails in CI, passes locally | Node version / dependency mismatch, uncommitted lockfile | Compare CI Node version to local; check lockfile committed; read the first error. | Pin Node in the host config (`.nvmrc`/engines); commit the lockfile; use `ci`/frozen install. | Pin Node version; require lockfile; run the prod build in CI. |
| "Module not found" | Missing dep, case-sensitivity, or wrong import path | Build log names the module/path; check filename case (Linux CI is case-sensitive). | Add the dep; fix import path/case to match the file exactly. | Case-sensitivity lint; CI mirrors prod OS. |
| Type/lint errors block build | Errors only surfaced in prod build | Read the first type/lint error. | Fix the error; don't disable the check to "make it pass." | Type-check + lint in CI before deploy. |
| Out of memory during build | Large build / memory-heavy step | Log shows "JavaScript heap out of memory." | Raise `--max-old-space-size`; split/optimize the build; reduce concurrency. | Monitor build memory; keep bundles/budgets in check. |
| Env-dependent build step fails | Missing build-time env var | Log: undefined config/secret at build. | Provide the required build-time env var in the host (see §3). | Document required env vars; validate at build start. |
| Fails only on the host, not local prod build | Host-specific config (build command, base dir, output dir) | Compare host build settings to the project. | Set correct build command, publish/output directory, and base path. | Version the host config (netlify.toml/vercel.json/etc.). |

---

## 2. Broken images / fonts (404 / CORS)

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Image/font 404 in prod | Wrong path, case mismatch, or asset not copied to output | DevTools Network 404; `curl -sI <asset-url>`. | Fix the path/case; ensure the asset lands in the build output/public dir. | Broken-link/asset check in deploy smoke test. |
| Asset 404 only after deploy | Hashed filename changed; HTML references an old hash | Compare referenced hash to deployed file. | Deploy HTML + hashed assets together atomically; don't purge old assets before HTML updates. | Atomic deploys; keep prior hashed assets during rollout. |
| Font blocked by CORS | Cross-origin font without `Access-Control-Allow-Origin` | Console "CORS policy" error; `curl -sI -H "Origin: https://{{DOMAIN}}" <font-url>`. | Add `access-control-allow-origin` on the font host, or self-host fonts (recommended). | Self-host fonts; set CORS on any cross-origin assets. |
| Font fetched but not applied | `@font-face` src path/format wrong, or FOIT (see §7) | Network shows font loaded; element uses fallback. | Fix `src`/`format('woff2')`; ensure `font-family` name matches. | Font-loading check in QA. |
| Image loads locally, 404 in prod | Referenced from `/src` or a non-public path | Path points outside the served directory. | Move to the public/static dir or import through the bundler. | Import assets through the bundler or place in public. |
| Mixed image sources 404 intermittently | Image CDN transform/URL error | CDN logs; test the raw CDN URL. | Fix the CDN transform params; validate the CDN base URL. | Validate CDN URLs in smoke test. |

---

## 3. Environment / config problems

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Works locally, blank/broken in prod | Env var missing or not exposed to the client build | Console errors for undefined config; check host env settings. | Set the var in the host env; expose client vars with the required prefix (e.g., `NEXT_PUBLIC_`/`VITE_`/`PUBLIC_`). | Validate required env vars at build start (fail fast). |
| Secrets leaked to the client | Server secret used in client bundle | Search the built JS for the secret value. | Remove from client; keep secrets server-side only; rotate the exposed secret. | Never prefix secrets with a public exposure prefix; secret scan in CI. |
| Wrong API/CRM endpoint hit | Env points to staging/wrong URL | Inspect the compiled config/network calls. | Point env to the correct prod endpoint; separate prod vs staging configs. | Per-environment config; review env before prod deploy. |
| Feature flag/config wrong in prod | Config not per-environment | Compare env config across environments. | Set per-environment config values. | Environment matrix documented. |
| `.env` accidentally committed | Secrets in git history | `git log`/secret scan. | Remove, rotate secrets, add to `.gitignore`, purge history if needed. | `.gitignore` env files; secret scanning in CI. |

---

## 4. Cache / stale deploy

"I deployed but still see the old site" is almost always cache. Isolate *which* cache.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Old page after deploy | CDN edge cache still serving old HTML | `curl -sI <url>` → `age`, `x-cache`/`cf-cache-status: HIT`; hard-reload/incognito. | Purge/invalidate the CDN; set HTML to `no-cache`/short TTL so HTML updates immediately. | HTML `no-cache`; auto cache-purge on deploy. |
| Old JS/CSS but new HTML | Browser cached un-hashed asset | Network shows a stale asset from cache. | Use fingerprinted (hashed) filenames for JS/CSS/fonts so URLs change on update. | Content-hash all static assets. |
| Old assets even after purge | Hashed asset served with wrong cache or purge missed HTML | Check `cache-control` on HTML vs assets. | Hashed assets: `Cache-Control: max-age=31536000, immutable`. HTML: `no-cache`. | Split cache policy: immutable hashed assets, no-cache HTML. |
| Some users see old, some new | Partial CDN propagation | Test from multiple regions/PoPs. | Wait for full invalidation; verify purge covered all PoPs. | Verify global purge in deploy smoke test. |
| Service worker serves old site | Stale SW cache (if a PWA) | Application panel → Service Workers/Cache Storage. | Update SW versioning/skipWaiting; provide an update prompt. | SW cache-busting strategy documented. |
| Stale after rollback | Rolled-back version still cached | Check deployed version vs cache age. | Purge cache after every rollback too. | Rollback runbook includes cache purge. |

---

## 5. Redirect loops & wrong redirects

Rules live in [`../seo/technical-seo.md`](../seo/technical-seo.md); this diagnoses breakage.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| "Too many redirects" (ERR_TOO_MANY_REDIRECTS) | Conflicting rules (e.g., `www`↔apex, `http`↔`https`, slash) loop | `curl -sIL <url>` shows a redirect cycle. | Define one canonical host + one trailing-slash style; redirect everything else to it **once**; remove conflicting rules. | Redirect map reviewed; loop test in smoke test. |
| Redirect chain (multiple hops) | A→B→C instead of A→C | `curl -sIL` shows 2+ 3xx hops. | Collapse to a single 301 to the final URL. | No chains > 1 hop; audit redirects. |
| 302 where 301 intended | Temporary redirect used for a permanent move | `curl -sI` shows `302`. | Use `301` for permanent moves. | Redirect-type review. |
| HTTPS redirect loop behind proxy/CDN | CDN terminates TLS; origin also forces HTTPS → loop | Check `x-forwarded-proto` handling. | Force HTTPS at the edge only, or honor `x-forwarded-proto` at origin — not both blindly. | Document TLS termination point. |
| Redirect breaks after deploy | Rule ordering/precedence changed | Review redirect config order. | Order specific rules before catch-alls. | Version and review redirect config. |

---

## 6. Mixed content

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Console "Mixed Content" warning/block | An `http://` asset on an `https://` page | Console lists the exact blocked URL. | Change the asset URL to `https://` (or protocol-relative → absolute https). | Grep for `http://` asset URLs in CI. |
| Padlock missing / "Not secure" | Insecure subresource downgrades security | DevTools Security panel. | Serve all subresources over HTTPS. | Security panel check in QA. |
| Third-party embed forces HTTP | Widget/iframe loads insecure resources | Console mixed-content from the third-party. | Use the vendor's HTTPS embed; replace vendors that don't support HTTPS. | Vet vendors for HTTPS-only embeds. |
| Form posts to HTTP endpoint | `action` uses `http://` | Inspect the form `action`. | Point the action to HTTPS; enforce HTTPS on the endpoint. | HTTPS-only endpoints; CSP `upgrade-insecure-requests`. |

---

## 7. Font FOUT / FOIT

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Invisible text during load (FOIT) | `font-display: block`/default hides text until the webfont loads | Slow-3G reload; text is blank then appears. | Set `font-display: swap` (or `optional`) so fallback shows immediately. | `font-display: swap` required on all `@font-face`. |
| Visible font swap/reflow (FOUT + CLS) | Fallback and webfont metrics differ | Rendering panel: layout shift on font load. | Match fallback metrics with `size-adjust`/`ascent-override`/`descent-override`; preload the critical font. | Font-metric overrides; preload critical font (see [`../performance/asset-efficiency.md`](../performance/asset-efficiency.md)). |
| Font loads late | Not preloaded / discovered late | Network: font requested after CSS. | Preload the one critical font: `<link rel="preload" as="font" type="font/woff2" crossorigin>`. | Preload critical font only (don't over-preload). |
| Font fetched twice | Missing `crossorigin` on the preload | Network shows two font requests. | Add `crossorigin` (fonts load in CORS mode even same-origin). | Preload lint checks `crossorigin` on `as="font"`. |
| Wrong/legacy font format shipped | TTF/OTF/WOFF instead of WOFF2 | Check the `@font-face` `src` formats. | Ship **WOFF2 only** (subset). | WOFF2-only policy. |

---

## 8. CDN issues

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| High TTFB in some regions | Origin fetch on cache miss / no edge cache | `curl -sI` from regions; check `x-cache`/`age`. | Increase cacheable TTLs; ensure static content is edge-cached. | CDN required; monitor cache hit ratio. |
| CDN serves 403/404 for valid assets | Origin path or permissions misconfigured | CDN logs; origin response. | Fix origin path/permissions; re-point the CDN origin. | CDN config in version control. |
| Compression not applied at edge | CDN not compressing/passing through | `curl -sI -H "Accept-Encoding: br,gzip"` → no `content-encoding`. | Enable Brotli (level 11 static) + Gzip fallback at the CDN. | Compression check in smoke test. |
| Wrong/insecure headers | CDN overriding cache/security headers | `curl -sI` for `cache-control`, `strict-transport-security`, `content-security-policy`. | Set correct headers at the CDN layer (HSTS, CSP, cache split). | Header policy documented + verified post-deploy. |
| Stale content at edge | Purge not triggered on deploy | `age` header high after deploy. | Trigger CDN purge/invalidation in the deploy pipeline. | Automated purge-on-deploy. |
| Intermittent 5xx from edge | Origin instability / cold starts / rate limits | CDN + origin logs; correlate timestamps. | Stabilize origin (see [`performance.md`](./performance.md) §TTFB); add edge caching to reduce origin hits. | Uptime monitoring + alerting. |

---

## 9. Rollback runbook (P1)

When the deployed site is broken and leads are at risk, restore service *before* diagnosing.

- [ ] **Roll back** to the last known-good deploy via the host's one-click/previous-deploy feature.
- [ ] **Purge the CDN cache** so users get the rolled-back version immediately.
- [ ] **Verify** the site is functional (load a page, submit the lead form, open the widget).
- [ ] **Confirm lead capture works** end-to-end (see [`forms-and-integrations.md`](./forms-and-integrations.md)).
- [ ] **Then diagnose** the failed deploy in a preview/branch environment, not prod.
- [ ] **Notify** {{EMAIL}} and log the incident (see [`README.md`](./README.md) §6).

---

## 10. Post-fix verification checklist

- [ ] Reproduced the failure with a **production build** (not dev) before fixing.
- [ ] `curl -sIL <url>` confirms correct **status, single redirect, headers** (cache/CORS/security).
- [ ] **CDN purged** and verified from multiple regions; no stale content.
- [ ] **No mixed content** and the padlock is present (Security panel clean).
- [ ] Fonts load with **swap**, no double-fetch, WOFF2 only.
- [ ] Added the **prevention guardrail** (pinned versions / smoke test / secret scan / config in VCS).

---

## Related

- [`README.md`](./README.md) — playbook index, triage, severity, and rollback-first rule.
- [`../performance/asset-efficiency.md`](../performance/asset-efficiency.md) — font loading, caching, and compression standards.
- [`../performance/performance-budget.md`](../performance/performance-budget.md) — budgets that gate the build.
- [`../seo/technical-seo.md`](../seo/technical-seo.md) — canonical host, trailing-slash, and redirect rules.
- [`performance.md`](./performance.md) — TTFB/CDN performance diagnosis.
- [`forms-and-integrations.md`](./forms-and-integrations.md) — verifying lead capture after a deploy/rollback.
