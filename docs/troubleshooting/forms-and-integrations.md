# Forms & Integrations Troubleshooting Playbook

**Purpose:** Symptom-driven diagnosis and repair for the {{BRAND_NAME}} site's lead-capture and integration failures — lead form not submitting, chat/booking widget not loading, webhook/CRM integration failures, spam, SMS opt-in/delivery issues, and analytics/consent blocking — each as `Symptom → Likely cause → Diagnosis → Fix → Prevention` so any developer can keep leads flowing end to end.
**Status:** v1 foundation — adjustable.

---

> **This is the highest-stakes playbook.** For a lead-response agency, a broken form, dead widget, or failed CRM handoff means **lost revenue in real time** — treat these as **P1** (see [`README.md`](./README.md) §severity). When in doubt, fix or roll back within the hour.
>
> Accessibility of form errors (announcement, focus, labels) lives in [`accessibility.md`](./accessibility.md) §7. Widget *performance* (facade, lazy-load) lives in [`performance.md`](./performance.md) §8. This file covers **functional** submission, integration, and delivery failures.
>
> **Golden diagnostic:** trace the lead's full path — **browser → form handler → webhook → CRM → confirmation (email/SMS)**. Find the first hop where the payload disappears.

---

## 0. TL;DR — forms/integrations triage in one screen

- [ ] **Trace the whole path.** Form UI → submit request → server/handler → webhook → CRM → SMS/email confirmation. The failure is at the first broken hop.
- [ ] **Open DevTools → Network** on submit: is the request sent? What status? What response body?
- [ ] **Use a request bin** (`webhook.site`) to prove the payload leaves the site correctly, then compare to what the CRM received.
- [ ] **Check the CRM/webhook/SMS provider logs** — they usually show the exact rejection reason.
- [ ] **Consent/ad-blockers can silently kill** analytics *and* widgets/forms that load via a tag manager. Test with blockers on and off.
- [ ] **Run an end-to-end synthetic lead** after every deploy — never assume the form still works.

### The lead path (map the hops)

| Hop | What can break |
|---|---|
| 1. Form renders | JS error, widget/tag manager blocked, script 404 |
| 2. User submits | Validation, disabled button, network/CORS, endpoint down |
| 3. Handler receives | Wrong endpoint, 4xx/5xx, auth/token, payload shape |
| 4. Webhook fires | Wrong URL, timeout, retry exhausted, signature mismatch |
| 5. CRM ingests | Field mapping, dedupe, required-field rejection, rate limit |
| 6. Confirmation sent | Email/SMS provider error, opt-in missing, delivery block |

---

## 1. Lead form not submitting

Start in **DevTools → Network**, submit, and watch for the request. No request = client-side; request with error status = server/integration side.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Click submit, nothing happens, no request | JS error halts the handler, or button disabled | Console for errors; Network shows no request; is the button `disabled`? | Fix the JS error; ensure the handler runs and the button enables when valid. | Synthetic submit test in CI/monitoring; JS error logging. |
| Request sent, 400/422 | Server-side validation rejects the payload | Network response body names the invalid field. | Align client validation with server rules; send the expected payload shape. | Contract test between form and handler. |
| Request sent, 401/403 | Missing/invalid API key or auth token | Response body; check the token/header. | Provide the correct auth token/header (server-side); rotate if leaked. | Token in server env; not in client bundle. |
| Request sent, 500 | Handler/endpoint error | Response body + server logs. | Fix the handler; add error handling so partial failures don't drop the lead. | Server error alerting; graceful failure + retry. |
| CORS error on submit | Endpoint doesn't allow the site origin | Console "CORS policy"; `curl -sI -H "Origin: https://{{DOMAIN}}" <endpoint>`. | Add `access-control-allow-origin` for {{DOMAIN}} on the endpoint (or same-origin proxy). | CORS configured + tested per environment. |
| Submits but user sees no confirmation | Success not surfaced to the UI | Network 200 but no UI change. | Show a clear success state; also handle the "sent but slow" case. | Success/failure UX states required. |
| Works on desktop, fails on mobile | Different validation/keyboard, or slow-network timeout | Test on a real mobile device / throttled. | Fix mobile validation; add sensible timeouts + retry. | Mobile + throttled test in QA. |
| Lead submitted but never arrives | Client succeeds, downstream hop drops it | Trace hops 3–5 (§3/§4). | Fix the broken downstream hop; add a fallback store (e.g., email the lead as backup). | End-to-end synthetic lead; backup delivery channel. |

---

## 2. Chat / booking widget not loading

The AI chat/booking widget is the core product surface — a dead widget is P1. See [`performance.md`](./performance.md) §8 for the *slow* (not dead) case.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Widget never appears | Script 404 / wrong embed snippet / vendor outage | Network for the widget script status; vendor status page. | Fix the embed snippet/URL; confirm vendor is up; check API key/site ID. | Widget-present synthetic check; monitor vendor status. |
| Widget blocked by ad/consent blocker | Loaded via tag manager / classified as tracking | Test with blockers on vs off; Network shows blocked request. | Load the widget directly (not solely via a blockable tag manager); ensure it's not misclassified. | Load critical widgets independent of tag manager. |
| Widget throws a console error | JS conflict, CSP blocks it, or bad config | Console error; check CSP `connect-src`/`script-src`. | Resolve the conflict; add the vendor's domains to CSP; fix config. | CSP allowlist includes vendor domains; test with CSP on. |
| Widget loads but won't connect | Vendor API key/domain allowlist wrong | Widget error; vendor dashboard "allowed domains." | Add {{DOMAIN}} to the vendor's allowed domains; fix the key. | Domain allowlist verified per environment. |
| Booking widget shows no availability | Calendar integration disconnected / timezone wrong | Vendor logs; check calendar auth + timezone. | Reconnect the calendar; fix timezone config. | Monitor calendar-integration health. |
| Widget covers/obscures content | Z-index/overlay positioning (also a11y 2.4.11) | Visual + keyboard focus test. | Position as an overlay that doesn't obscure focus/content. | Overlay placement + focus test (see [`accessibility.md`](./accessibility.md)). |
| Widget CSP violation after deploy | New/changed CSP too strict | Console CSP report; compare CSP versions. | Add required vendor sources to CSP directives. | Version CSP; test widget with CSP in CI. |

---

## 3. Webhook / CRM integration failures

The handoff that actually delivers the lead to the business. Use provider logs and a request bin.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Form succeeds, CRM has no lead | Webhook URL wrong/changed, or not firing | Send a test to `webhook.site`; compare to the CRM inbound log. | Update the correct webhook URL in env; confirm it fires on submit. | Env-based webhook URL; synthetic lead verifies CRM arrival. |
| Webhook fires but CRM rejects it | Field mapping mismatch or missing required field | CRM inbound/error log names the field. | Map payload fields to CRM fields; include all required fields. | Field-mapping contract test. |
| Intermittent lead loss | Webhook timeout / no retry / rate limit | Provider logs show timeouts or 429. | Add retries with backoff + idempotency keys; queue and replay on failure. | Retry + dead-letter queue; rate-limit handling. |
| Duplicate leads in CRM | Missing idempotency; double-submit; retry duplication | CRM shows duplicates with same timestamp. | Add idempotency key; disable button after first submit; dedupe on email/phone. | Idempotency keys + client double-submit guard. |
| Signature/verification failure | Webhook secret mismatch after rotation | Provider log "invalid signature." | Sync the shared secret on both ends; verify signatures. | Rotate secrets in lockstep; alert on signature failures. |
| Data arrives garbled/encoded wrong | Content-Type / encoding mismatch | Compare sent vs received payload (request bin). | Send correct `Content-Type` (JSON) + UTF-8; parse accordingly. | Payload contract test. |
| CRM sync stops after vendor change | API version deprecated / token expired | Vendor changelog; token expiry; 401s in logs. | Refresh token; migrate to the new API version. | Monitor token expiry + API deprecation notices. |

---

## 4. Spam & abuse

Balance blocking spam against **never blocking a real lead** or breaking accessible auth.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| Flood of junk submissions | No spam protection on the form | CRM full of obvious junk; check submission pattern. | Add a **honeypot** field + timing check; add server-side validation; consider invisible/low-friction CAPTCHA as a last resort. | Honeypot + timing on all forms by default. |
| Real leads blocked as spam | CAPTCHA too aggressive / filters too strict | Users report they can't submit; review false positives. | Loosen thresholds; prefer invisible checks; never block paste/password managers (a11y 3.3.8). | Monitor false-positive rate; accessible-auth policy. |
| Bot fills honeypot inconsistently | Sophisticated bots | Analyze submission metadata (timing, headers). | Layer defenses: honeypot + timing + rate limit + server validation. | Layered, not single, spam defense. |
| CAPTCHA breaks accessibility | Cognitive-function test with no alternative (3.3.8) | Keyboard/SR test the CAPTCHA. | Use an accessible/invisible challenge; provide an alternative path. | Accessible CAPTCHA only; test with AT. |
| Same IP/pattern hammering | No rate limiting | Server logs show repeated hits. | Add IP/session rate limiting on the endpoint. | Rate limiting on form endpoints. |

---

## 5. SMS opt-in / delivery issues

Critical for the speed-to-lead SMS product **and** a compliance area (TCPA/10DLC/carrier rules). A missing opt-in isn't just broken — it's a legal risk.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| SMS confirmation never arrives | Provider send failure or number not verified | SMS provider logs (status: failed/undelivered); check sender number status. | Fix provider config; verify/register the sender number; retry. | Monitor SMS delivery rate; alert on failures. |
| Messages blocked by carrier | Unregistered 10DLC/sender / flagged content | Provider log carrier error code (e.g., 30007). | Complete 10DLC/brand+campaign registration; adjust content to avoid filtering. | Registration completed before launch; content guidelines. |
| Opt-in not recorded | Consent checkbox not captured/stored | Check the lead record for consent flag + timestamp. | Capture explicit opt-in (checkbox + timestamp + language) and store it with the lead. | Consent capture required; audit trail stored. |
| User can't opt out | No STOP handling | Send STOP — is it honored? | Implement STOP/UNSUBSCRIBE handling per provider + law. | STOP handling tested; compliance review. |
| Wrong/duplicate messages | Automation misfire / loop | Provider send log timeline. | Fix the trigger logic; add idempotency/dedupe. | Idempotent messaging; test flows in staging. |
| Delivery slow (defeats speed-to-lead) | Provider queue / rate limits / async lag | Timestamp submit vs send vs deliver. | Reduce latency in the trigger path; check provider throughput/limits. | Monitor time-to-first-SMS as a KPI. |
| Opt-in language non-compliant | Consent wording missing required disclosures | Legal/compliance review of the opt-in copy. | Add required consent language (rates, frequency, STOP/HELP). | Legal-reviewed opt-in copy (see [`../legal/legal-pages.md`](../legal/legal-pages.md)). |

---

## 6. Analytics / consent blocking

Consent tooling and blockers can silently break measurement — and sometimes the widgets/forms that load through the same tag manager.

| Symptom | Likely cause | Diagnosis | Fix | Prevention |
|---|---|---|---|---|
| No analytics data | Consent not granted / blocker / tag misfire | Tag debugger; test with consent granted vs denied and blockers on/off. | Ensure tags fire on consent; verify tag config; consider server-side/first-party analytics. | Consent-mode configured + tested; tag QA. |
| Conversions undercounted | Blockers/consent suppress the conversion tag | Compare CRM lead count to analytics conversions. | Trust CRM as source of truth for leads; use server-side conversion tracking for accuracy. | CRM = lead source of truth; server-side conversions. |
| Consent banner blocks scripts users need | Widget/form loaded via a consent-gated tag manager | Deny consent — does the form/widget disappear? | Classify lead-capture as functional (not marketing) so it loads regardless of marketing consent; load it outside the blockable path. | Functional vs marketing script classification. |
| Consent banner obscures focus/content | Banner overlay covers UI (a11y 2.4.11) | Keyboard focus test with banner open. | Ensure the banner doesn't obscure focus/content; manage focus. | Consent-banner a11y review (see [`accessibility.md`](./accessibility.md)). |
| Double-counting events | Tag fires multiple times / duplicate install | Tag debugger shows duplicate hits. | Remove duplicate tags; deduplicate events. | Single tag install; event QA. |
| Analytics slows the page | Synchronous/heavy tag loading | See [`performance.md`](./performance.md) §8. | Load analytics async/deferred, consent-gated. | Deferred + consent-gated analytics. |

---

## 7. Post-fix verification checklist

- [ ] Ran an **end-to-end synthetic lead**: submitted the form → confirmed it reached the **CRM** → confirmed the **email/SMS confirmation** sent.
- [ ] Verified the **whole path** (browser → handler → webhook → CRM → confirmation) with a request bin where useful.
- [ ] Tested with **ad/consent blockers on and off** and consent **granted vs denied**.
- [ ] Tested the **widget** loads and connects (with CSP on) across environments.
- [ ] Confirmed **SMS opt-in is captured/stored** and **STOP** is honored (compliance).
- [ ] Added the **prevention guardrail** (synthetic monitor / contract test / retry+dead-letter / delivery alert).

---

## Related

- [`README.md`](./README.md) — playbook index, triage, and P1 severity (lead capture).
- [`performance.md`](./performance.md) — widget facade/lazy-load and analytics loading (the *slow* case).
- [`accessibility.md`](./accessibility.md) — form-error announcement, labels, focus, consent-banner a11y.
- [`build-deploy.md`](./build-deploy.md) — CORS, CSP, env/config, and verifying lead capture after deploy.
- [`../legal/legal-pages.md`](../legal/legal-pages.md) — SMS consent language and privacy/compliance requirements.
- [`../seo/ai-seo-geo.md`](../seo/ai-seo-geo.md) — consistent NAP used by confirmations and the CRM.
