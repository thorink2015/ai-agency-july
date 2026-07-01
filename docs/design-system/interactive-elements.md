# Interactive Elements & Conversion Patterns

**Purpose:** Prescribe how CTAs, forms/validation, and the core conversion elements (book-a-call, demo, chat widget, sticky mobile CTA) behave — the interaction rules that turn a lead into a booked call — so every page converts, stays WCAG 2.2 AA, and honours reduced motion. This governs *behaviour and hierarchy*; component states live in [`components.md`](./components.md).
**Status:** v1 foundation — adjustable.

---

> **Scope.** This doc answers: *Which* CTA is primary and where does it go? *How* do forms validate accessibly? *What* are the exact conversion surfaces and their feedback (loading/success/error)? Reference tokens by name (`--cta-bg`, `--space-4`); see [`design-tokens.md`](./design-tokens.md). Every pattern here assumes the global a11y rules in [`components.md`](./components.md) (native elements, visible focus, 44px targets, colour-never-alone, reduced-motion gating).
>
> **North-star behaviour:** the core promise is *speed-to-lead*. The site must make "start a conversation / book a call" the path of least resistance on every screen, at every scroll depth, on every device.

---

## 0. TL;DR — the rules you'll break by accident

- [ ] **One primary CTA per view.** Everything else is secondary/ghost or a link. Competing primaries kill conversion and confuse AT users.
- [ ] **CTA verb = the action.** "Book a call" navigates → `<a href>`. "Start chat" opens the widget → `<button>`. Semantics must match behaviour.
- [ ] **Never rely on placeholder as label.** Every field has a real `<label>`.
- [ ] **Errors are text + icon, inline, and linked** via `aria-describedby` + `aria-invalid`; focus moves to the first error.
- [ ] **Correct `type`/`inputmode`/`autocomplete`** on every field — right keyboard, autofill, no re-typing (3.3.7).
- [ ] **Sticky mobile CTA** must not obscure focused content or the last field (2.4.11); leave scroll padding.
- [ ] **Loading/success/error feedback** is announced to screen readers via live regions, not just visual.
- [ ] **All non-essential motion** is gated behind `prefers-reduced-motion: no-preference`.
- [ ] **Honeypot + timing** for spam — never a CAPTCHA that blocks paste or fails 3.3.8.

---

## 1. CTA hierarchy & placement

### 1.1 One primary per view

A "view" is what's on screen at a given scroll position on a given breakpoint. At most **one** primary (filled) CTA competes for attention there. This is both a conversion rule (Hick's law — fewer choices, faster action) and an a11y clarity rule.

| Tier | Style (see `components.md` §1) | Job | Example |
|---|---|---|---|
| **Primary** | Filled `--cta-bg` | The one action we want | "Book a call" |
| **Secondary** | Outlined brand | Viable alternative | "See how it works" |
| **Tertiary / ghost** | Text/ghost | Low-stakes escape hatch | "Read case studies" |
| **Inline link** | Underlined `--link` | In-copy navigation | "…our [pricing]" |

> If two actions feel equally important, they aren't. Pick the one tied to revenue (book/chat) as primary; demote the other to secondary.

### 1.2 Placement map (marketing site)

| Location | Primary CTA | Notes |
|---|---|---|
| Navbar (all pages) | "Book a call" | Persistent; the always-available conversion path. |
| Hero | "Book a call" (+ secondary "See how it works") | Above the fold; primary is the LCP-adjacent focal element. |
| After each proof section | Repeat primary | Re-offer the CTA at natural decision points (after value/proof). |
| Pricing | "Book a call" per tier | One primary per card; consistent verb. |
| Final CTA band | Primary, large | Full-width closer before footer. |
| Footer | "Book a call" | Consistent-help location (3.2.6) — same relative place site-wide. |
| Mobile sticky bar | Primary (see §4) | Appears after hero scrolls out. |

**Rhythm rule:** a user should never have to scroll more than ~1.5 viewports without a primary CTA in reach. Keep the *same verb* everywhere ("Book a call") so it reads as one consistent action, not many.

### 1.3 Button vs link semantics (conversion-critical)

| CTA behaviour | Element | Why it matters |
|---|---|---|
| Navigates to `/book` or a scheduler page | `<a href="/book">` | Crawlable, right-click/new-tab, back button, prefetchable |
| Opens a modal/scheduler in place | `<button>` | Correct role, `Space`+`Enter` activation |
| Opens the chat widget | `<button>` | It's an action, not navigation |
| Submits the lead form | `<button type="submit">` | Native form submission + validation |

Style the `<a>` and `<button>` identically; **do not** swap the element to get a look. A `<div>`/`<span>` CTA is a defect (no keyboard, no role, no name).

### 1.4 CTA copy

- Lead with the benefit/verb, second person, no hype: **"Book a call"**, **"Get your setup"**, **"See it answer a lead"**. Avoid "Submit", "Click here", "Learn more" as the *primary*.
- The visible label IS the accessible name — keep it descriptive enough to stand alone out of context (screen-reader users may hear it in a links list).

---

## 2. Forms & validation UX

The lead form is the highest-value surface. Optimize for completion and accessibility together.

### 2.1 Field design principles

- [ ] **Ask for the minimum.** Every field costs conversions. For a lead form: name, email OR phone, and one context field is often enough. Defer the rest to the call.
- [ ] **One column, labels above** fields (fastest to complete, best for zoom/reflow at 320px).
- [ ] **Labels are visible and persistent** (`<label for>`); placeholders are *examples/format hints*, not labels.
- [ ] **Group related choices** in `<fieldset><legend>`.
- [ ] **Logical tab order** matches visual order (2.4.3).

### 2.2 Required vs optional

- Mark state **explicitly and redundantly** (never colour alone): visible `*` **and** the word, or label most-required forms by marking the *optional* ones "(optional)".
- Use the native `required` attribute (gives free constraint + AT announcement). Add `aria-required="true"` only if you can't use native.
- Don't disable the submit button waiting for validity — a `disabled` submit gives keyboard/AT users no feedback about *why*. Keep it enabled and validate on submit (and optionally on blur).

### 2.3 Input types, inputmode & autocomplete (autofill + 3.3.7)

Correct attributes = right mobile keyboard, working browser autofill, and no re-entry of known data.

| Field | `type` | `inputmode` | `autocomplete` |
|---|---|---|---|
| Full name | `text` | — | `name` |
| Email | `email` | `email` | `email` |
| Phone | `tel` | `tel` | `tel` |
| Business name | `text` | — | `organization` |
| Website | `url` | `url` | `url` |
| Message | (textarea) | `text` | `off` |

- **Autofill:** always set `autocomplete` — it's the biggest completion-rate lever and directly supports 3.3.7 Redundant Entry (don't make users re-type what the browser/they already have). If you collect data across steps, auto-populate or let users *select* prior values rather than retype (exception: security fields).
- **Never block paste** on any field (email, phone, and especially any OTP/verification) — blocking paste fails 3.3.8 Accessible Authentication (AA).

### 2.4 Validation timing & inline errors

**Timing:** validate on **submit** for the whole form; additionally validate a field **on blur** *after first interaction* (don't yell while the user is still typing). Re-validate on input once a field is already errored so the error clears as they fix it.

**Accessible inline errors (the pattern):**

1. Set `aria-invalid="true"` on the field.
2. Put the message in an element with an `id`; reference it from the field's `aria-describedby` (space-separated with any help id).
3. Error text is **specific and actionable**, includes an **icon**, uses `--color-danger` **plus** text (not colour alone): *"Enter a valid email like name@example.com"* — not "Invalid".
4. On submit with errors: render an **error summary** at the top (`role="alert"`, focusable) linking to each bad field, **and** move focus to the summary (or directly to the first invalid field).
5. On success of a previously-errored field, remove `aria-invalid`, clear the message, and (optionally) confirm via a polite live region.

```html
<form novalidate>
  <!-- Error summary appears only after a failed submit; receives focus -->
  <div id="form-errors" class="alert alert--danger" role="alert" tabindex="-1" hidden>
    <p>Fix these to continue:</p>
    <ul><li><a href="#email">Enter a valid email</a></li></ul>
  </div>

  <div class="field">
    <label for="email">Work email <span aria-hidden="true">*</span></label>
    <input id="email" name="email" type="email" inputmode="email"
           autocomplete="email" required
           aria-describedby="email-help email-error" aria-invalid="true" />
    <p id="email-help" class="field__help">We'll send your booking link here.</p>
    <p id="email-error" class="field__error"><svg aria-hidden="true">⚠</svg> Enter a valid email like name@example.com.</p>
  </div>

  <button type="submit" class="btn btn--primary">Book a call</button>
</form>
```

### 2.5 Spam prevention (accessible)

| Technique | How | A11y note |
|---|---|---|
| **Honeypot** | Hidden field real users never fill; reject if filled | Hide with CSS **and** `aria-hidden="true"` + `tabindex="-1"` + `autocomplete="off"`; label it plausibly (e.g. "company website"). Don't use `display:none` on a required field. |
| **Time-trap** | Reject submits faster than ~2–3s | Invisible to users; no interaction cost. |
| **Server checks / rate limiting** | Validate & throttle server-side | Zero user friction. |
| **CAPTCHA — last resort** | Only if abuse is real | If used, it MUST have an accessible alternative and NEVER block paste/password-manager (3.3.8). Prefer invisible/risk-based over image puzzles. |

> Default to honeypot + timing + server-side. A puzzle CAPTCHA is a cognitive-function test — a WCAG 3.3.8 risk and a conversion tax. Avoid unless data forces it.

---

## 3. Primary conversion elements

### 3.1 Book-a-call (the main conversion)

**Behaviour:** primary CTA everywhere. Two acceptable implementations:

1. **Navigate** to `/book` (embedded scheduler page) — `<a href="/book">`. Best for SEO/prefetch/shareability.
2. **Open a modal** scheduler in place — `<button>` that opens the dialog (see `components.md` §13: focus trap, `Esc`, return focus).

**Rules:**
- Keep the scheduler above the fold on `/book`; pre-fill known fields (name/email) via `autocomplete`/query params (3.3.7).
- If it embeds a third-party scheduler in an `<iframe>`, give the iframe a `title`, ensure keyboard access reaches it, and don't let it be obscured by sticky UI (2.4.11).
- Provide a **fallback**: a `tel:`/`mailto:` and the lead form for users who can't/won't use the scheduler.

### 3.2 Demo / "see it work"

**Behaviour:** secondary CTA ("See it answer a lead"). Options: a short muted autoplay clip, an interactive sample chat, or a form to request a live demo.

**Rules:**
- **Autoplay video:** muted, `playsinline`; if it moves/animates >5s it MUST be pausable/stoppable (WCAG 2.2.2) — provide a visible pause control. Respect `prefers-reduced-motion` (don't autoplay; show a poster + play button).
- Captions/transcript for any spoken content.
- An interactive demo is a real, keyboard-operable widget — not a decorative animation.

### 3.3 Chat widget (speed-to-lead in action)

The chat widget is both product demo and conversion surface. It's also the most common a11y offender (obscuring focus, no keyboard support).

**Rules:**
- **Launcher is a real `<button>`** with an accessible name ("Open chat"), 44px target, in the tab order, with visible focus.
- **Focus management:** opening moves focus into the panel; closing returns focus to the launcher; `Esc` closes.
- **2.4.11 Focus Not Obscured:** the widget must NOT cover a focused field, the sticky CTA, or footer links. Offset it, or collapse it when a form field is focused. Test keyboard-only.
- **Live messages** use a polite live region (`aria-live="polite"`) so incoming AI replies are announced; don't spam assertive.
- **Reduced motion:** disable bounce/pulse launcher animations under `prefers-reduced-motion`.
- **Consistent placement** across pages (3.2.6 Consistent Help) — same corner, same relative position.
- Don't auto-open aggressively on load; if it auto-opens, it must be easily dismissable and must not trap or steal focus.

```html
<button id="chat-launch" class="chat-launcher" aria-expanded="false" aria-controls="chat-panel">
  <span class="sr-only">Open chat</span><svg aria-hidden="true">💬</svg>
</button>
<section id="chat-panel" class="chat-panel" role="dialog" aria-label="Chat with us" hidden>
  <div class="chat-log" aria-live="polite" aria-atomic="false"><!-- messages --></div>
  <!-- input + send button; never block paste -->
</section>
```

---

## 4. Sticky mobile CTA

**Purpose.** Keep the primary action reachable on small screens where the navbar CTA has scrolled away.

**Behaviour & rules:**
- Appears **after the hero scrolls out of view**; contains the single primary CTA ("Book a call") — optionally a secondary "Chat" icon.
- Fixed to the bottom, `--z-sticky` (1100), full-width or edge-padded, `--shadow-lg` upward, safe-area inset padding (`env(safe-area-inset-bottom)`).
- **Must not obscure content or focus (2.4.11):** add bottom `scroll-padding`/`padding` to the page equal to the bar's height so the last form field and footer links aren't hidden under it, and a focused field never sits behind it.
- **44px target**, ≥8px from screen edges; the CTA is a real `<a>`/`<button>` with visible focus.
- **Hide it when the on-page form/scheduler is in view** (it's redundant and risks covering the submit button).
- **Reduced motion:** slide-in is gated; provide an instant/opacity fallback.
- Don't stack multiple sticky layers (cookie banner + chat + CTA) that together bury the viewport — coordinate their z-index and never let them cover a focused element.

```html
<div class="sticky-cta" role="region" aria-label="Quick actions">
  <a href="/book" class="btn btn--primary btn--md">Book a call</a>
  <button type="button" class="btn btn--ghost" aria-label="Open chat"><svg aria-hidden="true">💬</svg></button>
</div>
```

---

## 5. Interaction feedback (loading / success / error)

Every user action gets **immediate, perceivable, and announced** feedback — visual for sighted users, live-region for AT. Silence reads as "it's broken" and triggers rage-clicks/duplicate submits.

### 5.1 Loading / pending

| Signal | Rule |
|---|---|
| **Button** | On submit: `aria-busy="true"`, keep the accessible name, show an inline spinner, **lock width** (no layout shift/CLS), and **block duplicate submits**. Don't replace the label with a bare spinner. |
| **Announce** | For longer waits, a polite live region: "Booking your call…". |
| **Skeletons** | Use for content loads; mark the region `aria-busy="true"` until ready. Skeleton shimmer is motion — gate behind reduced-motion (fall back to a static placeholder). |
| **Timing** | Give feedback within ~100ms of the click. If work exceeds ~1s, show progress; beyond ~10s, allow cancel. |

### 5.2 Success

- **Announce** via `role="status"` (polite): *"Thanks — we'll text you within a minute."* Region must exist in the DOM before you inject the message.
- Confirm with text + icon (not colour/checkmark alone). Prefer an inline confirmation or a dedicated thank-you state over a toast that may auto-dismiss before it's read.
- **Preserve context:** don't wipe the form to a blank screen with no explanation; state what happens next (the speed-to-lead promise — "you'll hear from us in seconds").

### 5.3 Error (submission/network)

- **Announce** via `role="alert"` (assertive) — it interrupts, appropriate for a failure the user must act on.
- **Never lose their input.** Repopulate the form; keep entered data (3.3.7).
- Message is specific + recoverable: what failed, what to do ("Couldn't send — check your connection and try again"), with a retry affordance. Provide a fallback path (`tel:`/`mailto:`) if the form keeps failing.
- Colour + icon + text; move focus to the alert or first offending field.

### 5.4 Reduced-motion & non-text feedback matrix

| Feedback | Full motion | `prefers-reduced-motion: reduce` |
|---|---|---|
| Button loading | Spinning icon | Static "Booking…" text + `aria-busy` |
| Success toast | Slide+fade in | Instant appear (opacity only), still announced |
| Skeleton | Shimmer sweep | Static grey placeholder |
| Sticky CTA reveal | Slide up | Instant show |
| Field error | (no motion needed) | (same) — text/icon always present |

**Tokens for feedback:** `--color-danger` (error), `--color-success-strong` (success text on white), `--color-warning` (INK text), `--duration-fast/base/slow` + `--ease-standard` (all motion-gated), `--z-toast` (1400), `--shadow-lg` (toast/sticky). Reference by name; validated pairings in [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md).

---

## 6. Ship gate — interactive & conversion

- [ ] Exactly **one primary CTA per view**; consistent verb site-wide; correct button-vs-link semantics.
- [ ] Primary CTA in navbar, hero, after each proof section, pricing, final band, footer, and mobile sticky bar.
- [ ] Every field: real `<label>`, correct `type`/`inputmode`/`autocomplete`, required/optional stated non-colour-only.
- [ ] Validation: on submit (+ on-blur after first interaction); `aria-invalid` + `aria-describedby`; error summary focused; input preserved.
- [ ] **Paste never blocked**; autofill works; known data not re-requested (3.3.7).
- [ ] Spam handled via honeypot + timing + server-side; no paste-blocking / cognitive-test CAPTCHA (3.3.8).
- [ ] Book-a-call, demo, and chat widget: keyboard-operable, focus-managed, `Esc`-closable, not obscuring focus (2.4.11), consistent placement (3.2.6).
- [ ] Autoplay/animated media pausable if >5s (2.2.2) and disabled/poster under reduced motion.
- [ ] Sticky mobile CTA doesn't cover focused content/last field; scroll-padding added; 44px target; motion-gated.
- [ ] Loading/success/error each **announced** via `role=status`/`alert` and shown with text+icon (not colour alone); no CLS on state swap; duplicate submits blocked.
- [ ] All non-essential motion gated behind `prefers-reduced-motion: no-preference`.

---

## Related

- [`components.md`](./components.md) — component-level anatomy, states, tokens, and a11y (Button, Input, Modal, Toast, etc.) that these patterns compose.
- [`design-tokens.md`](./design-tokens.md) — token names for CTA colours, motion, spacing, z-index used here.
- [`../brand/color-system.md`](../brand/color-system.md) — canonical colour & contrast rules for CTA and semantic states.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — validated pairings for CTA, error, success, warning states.
- [`../00-foundations/brand-strategy.md`](../00-foundations/brand-strategy.md) — voice/positioning behind CTA copy (speed-to-lead, human+AI, no hype).
- [`../00-foundations/principles.md`](../00-foundations/principles.md) — the design principles these interactions encode.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — generated CSS custom properties consumed by these patterns.
