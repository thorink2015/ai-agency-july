# Component Library — States, Tokens & A11y Contract

**Purpose:** Define the *contract* (anatomy, states, tokens, accessibility, minimal markup) for every core UI component so any developer or future Claude session builds them consistently, on-token, and WCAG 2.2 AA-conformant — without inventing values or re-deriving behaviour. This is a spec, not a framework: it describes what each component MUST do, not one implementation.
**Status:** v1 foundation — adjustable.

---

> **How to read this doc.** Each component lists: **Purpose** → **Anatomy** → **States** → **Tokens used** (by name — see [`design-tokens.md`](./design-tokens.md)) → **A11y** (role/keyboard/ARIA) → **Minimal HTML**. Reference tokens by name (`--cta-bg`, `--space-4`), never raw hex. All colour pairings are pre-validated in [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — do not create new ones.
>
> **Global rules (apply to every component below):**
> - **Focus:** never `outline: none` without a replacement. Base treatment is `outline: 2px solid var(--focus-ring); outline-offset: 2px` (already set on interactive elements in `tokens.css`). Satisfies WCAG 2.4.7 (AA). Aim for the AAA 2.4.13 target: a ≥2px-thick indicator at ≥3:1 contrast vs the unfocused state.
> - **Target size:** interactive controls MUST be ≥24×24 CSS px (WCAG 2.5.8 AA) **or** meet the 24px-spacing exception. We standardize on **44×44** (`--target-min`) with **8px** min spacing (`--target-spacing`) to also satisfy mobile HIG and AAA 2.5.5.
> - **Colour is never the only signal** (WCAG 1.4.1): pair every colour cue with text and/or an icon.
> - **Motion:** any non-essential transition/animation is gated behind `@media (prefers-reduced-motion: no-preference)`; provide an opacity/instant fallback. `tokens.css` already neutralizes durations under `prefers-reduced-motion: reduce`.
> - **Labels are programmatic:** placeholder text is NEVER the accessible name (fails 1.3.1 / 3.3.2 / 4.1.2). Every control has a real `<label>` or `aria-label`.
> - **Focus not obscured (2.4.11 AA):** sticky headers/footers, cookie banners, and the chat widget must not fully cover a focused element. Use `scroll-margin-top`/`scroll-padding-top` equal to the sticky header height.

---

## 0. Component index

| Component | Native element (prefer) | Primary a11y pattern |
|---|---|---|
| [Button](#1-button) | `<button>` / `<a>` | Native button/link |
| [Link](#2-link) | `<a href>` | Native link |
| [Input / Textarea / Select](#3-input--textarea--select) | `<input>` `<textarea>` `<select>` | Labelled field + `aria-describedby` |
| [Checkbox / Radio / Toggle](#4-checkbox--radio--toggle) | `<input type>` / `role=switch` | Native + grouping |
| [Card](#5-card) | `<article>` / `<div>` | Content container; one link per card |
| [Badge / Pill](#6-badge--pill) | `<span>` | Decorative / status text |
| [Alert / Toast](#7-alert--toast) | `<div role=alert/status>` | Live region |
| [Accordion (FAQ)](#8-accordion-faq) | `<button>` + region | Disclosure |
| [Tabs](#9-tabs) | `role=tablist` | APG Tabs pattern |
| [Navbar + mobile menu](#10-navbar--mobile-menu) | `<nav>` + disclosure | Landmark + menu button |
| [Footer](#11-footer) | `<footer>` | `contentinfo` landmark |
| [Breadcrumb](#12-breadcrumb) | `<nav aria-label>` | Ordered list |
| [Modal / Dialog](#13-modal--dialog) | `<dialog>` / `role=dialog` | Focus trap + `aria-modal` |
| [Tooltip](#14-tooltip) | `[aria-describedby]` | Supplemental, non-essential |

**Native-first rule:** reach for the semantic HTML element before any ARIA. ARIA is a fallback for what HTML can't express, not an upgrade. "No ARIA is better than bad ARIA."

---

## 1. Button

**Purpose.** Trigger an action or submit a form. The single most important interactive element on a conversion site — every CTA is a button (or a link styled as one; see semantics below).

**Variants & when to use:**

| Variant | Use for | Fill | Text token | Notes |
|---|---|---|---|---|
| **Primary** | The one main action per view (e.g. "Book a call") | `--cta-bg` → hover `--cta-bg-hover` | `--cta-text` (white, 6.29:1 AA) | Max **one** per viewport section. |
| **Secondary** | Alternate/lower-priority action | transparent, `1.5px` border `--color-brand-600` | `--color-brand-700` | Outlined. |
| **Ghost** | Tertiary / in dense UI, toolbars | transparent, no border | `--color-brand-700` | Hover bg `--color-brand-50`. |
| **Danger** | Destructive confirm (rare on marketing site) | `--color-danger` (white 4.83:1 AA) | white | Only inside confirm dialogs. |

**Sizes** (height driven by padding + `min-height`, all meet 44px target):

| Size | Font | Padding (Y × X) | Min height |
|---|---|---|---|
| `sm` | `--text-sm` | `--space-2` × `--space-4` | `--target-min` (44px) |
| `md` (default) | `--text-base` | `--space-3` × `--space-6` | `--target-min` (44px) |
| `lg` | `--text-lg` | `--space-4` × `--space-8` | 52px |

> Even `sm` must keep a 44px hit target. If visual height is smaller, expand the tappable area with padding or a `::before` overlay — do not ship a 32px CTA.

**Anatomy.** `[optional leading icon] · label · [optional trailing icon]`. Icon-only buttons MUST have `aria-label`.

**States:**

| State | Visual | Token / rule |
|---|---|---|
| Default | Filled brand | `--cta-bg`, `--radius-md`, `--shadow-xs` |
| Hover | Darken | `--cta-bg-hover`; `transition: var(--duration-fast) var(--ease-standard)` |
| Active/pressed | Slightly darker + no lift | `--color-brand-800`; remove shadow |
| Focus-visible | Ring | `outline: 2px solid var(--focus-ring); outline-offset: 2px` (or `--shadow-focus`) |
| Disabled | Muted, no pointer | `opacity: var(--opacity-disabled)`; `cursor: not-allowed`; `aria-disabled` or `disabled` |
| Loading | Spinner + label, width locked | `aria-busy="true"`; keep accessible name; disable re-submit |

**Tokens used:** `--cta-bg`, `--cta-bg-hover`, `--cta-text`, `--color-brand-50/700/800`, `--color-danger`, `--radius-md`, `--shadow-xs`, `--focus-ring`, `--target-min`, `--space-*`, `--text-sm/base/lg`, `--fw-semibold`, `--duration-fast`, `--ease-standard`, `--opacity-disabled`.

**A11y:**
- Use `<button type="button|submit">` for actions; use `<a href>` only for navigation (see §2 semantics). Never `<div onclick>`.
- **Keyboard:** `Enter` and `Space` activate a `<button>` natively; a link-styled-as-button (`<a>`) only activates on `Enter` unless you add `Space` handling — prefer a real `<button>`.
- **Name:** visible label = accessible name. Icon-only → `aria-label`. Don't hide the label from AT.
- **Loading:** set `aria-busy="true"`; keep the button in the tab order but block duplicate submits; do NOT swap the label to an empty spinner (announces as unnamed).
- **Disabled:** a truly `disabled` button is removed from tab order and gives no focus feedback — for form CTAs prefer keeping it enabled and validating on submit (better for screen-reader users), or use `aria-disabled="true"` + intercept the click.
- **Contrast exemption:** disabled controls are exempt from 1.4.3 contrast — but never make an *enabled* control look disabled.

```html
<!-- Primary, default -->
<button type="submit" class="btn btn--primary btn--md">Book a call</button>

<!-- Loading -->
<button type="submit" class="btn btn--primary" aria-busy="true" disabled>
  <span class="btn__spinner" aria-hidden="true"></span>
  Booking…
</button>

<!-- Icon-only -->
<button type="button" class="btn btn--ghost" aria-label="Open chat">
  <svg aria-hidden="true" focusable="false" width="20" height="20"><!-- icon --></svg>
</button>
```

---

## 2. Link

**Purpose.** Navigate to another URL, section, or resource. Distinct from a button, which *does* something on the current page.

**Button vs link — the one rule that matters:**

| If it… | Use | Because |
|---|---|---|
| Changes the URL / navigates | `<a href>` | Right-click, open-in-new-tab, crawlable, back button |
| Triggers an action, opens a modal, submits, toggles UI | `<button>` | Correct role & keyboard semantics |

> A "Book a call" that navigates to `/book` is an `<a>` styled as a button. A "Book a call" that opens a modal in place is a `<button>`. Style can match; **semantics must be correct**.

**Anatomy.** Text (+ optional icon). External links: append a visually-hidden "(opens in new tab)" and a visible icon when `target="_blank"`.

**States:**

| State | Token / rule |
|---|---|
| Default | `--link`, underline (or clear affordance) |
| Hover | `--link-hover`, underline |
| Focus-visible | outline `--focus-ring`, offset |
| Visited | Optional; keep AA contrast |

**Tokens used:** `--link`, `--link-hover`, `--focus-ring`, on dark: `--link` remaps to `--color-brand-300` via `.surface-dark`.

**A11y:**
- Links need an accessible name from text; icon-only links need `aria-label`. No empty/`#` links.
- **Underline or non-colour affordance** in body copy so links aren't distinguished by colour alone (1.4.1). Nav/footer links may drop underline if grouped in an obvious nav context.
- `target="_blank"` → add `rel="noopener"` and announce the new tab.
- Skip link: first focusable element is a "Skip to main content" link that becomes visible on focus (targets `#main`).

```html
<a href="/book" class="btn btn--primary">Book a call</a>
<p>Read our <a href="/case-studies" class="link">case studies</a> for proof.</p>
<a href="https://example.com" class="link" target="_blank" rel="noopener">
  Docs <svg aria-hidden="true">…</svg><span class="sr-only"> (opens in new tab)</span>
</a>
```

---

## 3. Input / Textarea / Select

**Purpose.** Collect typed or chosen data — the backbone of the lead form, the highest-value surface on the site.

**Anatomy.** `label (required marker) → control → help text → error text`. Every part is programmatically linked.

```
┌ Label * ─────────────────┐
│ [ control            ]   │  ← border --border-interactive
└──────────────────────────┘
  Help text (--text-muted)
  ⚠ Error text (--color-danger)   ← only when invalid
```

**States:**

| State | Border | Other | Token |
|---|---|---|---|
| Default | `--border-interactive` (3:1) | — | never `--border` (fails 3:1 on controls) |
| Hover | `--color-neutral-600` | — | |
| Focus | `--focus-ring` + ring | `outline`/`box-shadow` | `--shadow-focus` |
| Filled | as default | — | |
| Error | `--color-danger` | icon + message, `aria-invalid` | `--color-danger` |
| Disabled | `--border` | `opacity --opacity-disabled` | `disabled` |
| Read-only | subtle | `readonly` | `--bg-subtle` |

**Tokens used:** `--border-interactive`, `--focus-ring`, `--shadow-focus`, `--color-danger`, `--color-neutral-600`, `--text-base` (min 16px on mobile to prevent iOS zoom), `--text-muted`, `--radius-md`, `--space-3/4`, `--target-min` (min-height 44px).

**A11y:**
- **Real `<label for>`** linked to the control's `id`. Placeholder is not a label. Keep labels visible (floating labels OK if they don't disappear on input).
- **Help + error linked via `aria-describedby`** (space-separated ids). When invalid: `aria-invalid="true"` and the error text carries the error id.
- **Required:** mark with a visible `*` AND text; use `required` (and `aria-required` only if not native). Prefer marking the *optional* fields if most are required — but always be explicit, not colour-only.
- **Input types & autofill (huge for conversion & 3.3.7 Redundant Entry):** use correct `type` (`email`, `tel`, `url`) + `inputmode` + `autocomplete` (`name`, `email`, `tel`, `organization`) so autofill works and users don't re-type.
- **Errors:** shown inline next to the field, in text (not colour alone), with an icon; on submit, move focus to the first invalid field (or a summary that links to it).
- **Select:** prefer native `<select>` for reliability; a custom listbox must implement the APG combobox/listbox keyboard model.
- **Never block paste** (relevant to any auth/OTP field — 3.3.8 AA).

```html
<div class="field">
  <label for="email" class="field__label">Work email <span aria-hidden="true">*</span></label>
  <input
    id="email" name="email" type="email" inputmode="email"
    autocomplete="email" required
    class="field__control"
    aria-describedby="email-help email-error"
    aria-invalid="true" />
  <p id="email-help" class="field__help">We only use this to send your booking link.</p>
  <p id="email-error" class="field__error">
    <svg aria-hidden="true">⚠</svg> Enter a valid email like name@example.com.
  </p>
</div>
```

---

## 4. Checkbox / Radio / Toggle

**Purpose.** Boolean opt-ins (checkbox), single-choice from a set (radio), and immediate on/off state changes (toggle/switch).

**Anatomy.** Control + adjacent label (whole label is clickable). Groups get a `<fieldset>` + `<legend>`.

**States:** default / hover / focus-visible (ring) / checked / disabled / error (group-level). Checked fill uses `--color-brand-600`; the check/dot is white (validated) or a validated icon.

**Tokens used:** `--color-brand-600` (checked), `--border-interactive` (unchecked border, 3:1 per 1.4.11), `--focus-ring`, `--radius-sm` (checkbox) / `--radius-full` (radio & toggle knob), `--target-min`, `--target-spacing` (≥8px between adjacent controls).

**A11y:**
- **Checkbox/Radio:** use native `<input type="checkbox|radio">` — free keyboard + state. Wrap related radios in `<fieldset><legend>`. `Space` toggles; `↑/↓/←/→` moves within a radio group (roving native behaviour).
- **Toggle/Switch:** use `<button role="switch" aria-checked>` (or a checkbox styled as a switch). `Space`/`Enter` toggles. The label must state what it controls; state is conveyed by `aria-checked`, not colour alone.
- **Target:** the control OR its label must give a ≥24px (we use 44px) target; label click must toggle.
- **Non-text contrast:** the unchecked border and the checked indicator must each hit 3:1 against their background (1.4.11).

```html
<fieldset class="group">
  <legend>How can we reach you?</legend>
  <label class="choice"><input type="radio" name="contact" value="sms" /> Text/SMS</label>
  <label class="choice"><input type="radio" name="contact" value="call" /> Phone call</label>
</fieldset>

<label class="choice"><input type="checkbox" name="consent" required /> I agree to be contacted.</label>

<button type="button" role="switch" aria-checked="false" class="switch">
  <span class="switch__track"><span class="switch__knob"></span></span>
  Enable SMS notifications
</button>
```

---

## 5. Card

**Purpose.** Group related content (feature, case study, pricing tier, testimonial) into a scannable, elevated container.

**Anatomy.** Optional media → optional eyebrow/badge → heading → body → optional footer/CTA. Padding `--space-6`.

**States:** static by default. Interactive card (whole card links somewhere) gets hover elevation and a focus ring **on the link**, not the div.

**Tokens used:** `--bg`, `--border` (decorative hairline), `--radius-lg`, `--shadow-md` (rest) → `--shadow-lg` (hover, motion-gated), `--space-6`, heading `--font-display`.

**A11y:**
- A card is a container, not a control. If the whole card is clickable, use **one** real `<a>` and make it cover the card via a stretched pseudo-element (`::after { position:absolute; inset:0 }`) so the accessible name comes from the heading link — avoids nested/duplicate links.
- Don't put multiple competing links inside a "whole-card" clickable card (ambiguous focus/name). If you need multiple actions, don't stretch the link.
- Use `<article>` for self-contained content; heading level fits the page outline.

```html
<article class="card">
  <span class="badge">Med spa</span>
  <h3 class="card__title"><a href="/case/med-spa" class="card__link">Booked 38% more consults</a></h3>
  <p class="card__body">AI answered every after-hours lead in under 30 seconds…</p>
</article>
```

---

## 6. Badge / Pill

**Purpose.** Compact status, category, or metadata label (e.g. "New", "24/7", "HIPAA-aware", "Med spa").

**Anatomy.** Small text, optional dot/icon, `--radius-full` (pill) or `--radius-sm` (tag).

**Variants (all validated):** neutral (`--bg-subtle` + `--text-secondary`), brand (`--color-brand-50` + `--color-brand-700`), success/warning/danger/info using semantic colours with **ink or white per the contrast rules** (warning & accent = INK text only).

**Tokens used:** `--radius-full`, `--text-xs`/`--text-sm`, `--fw-medium`, `--space-1/2/3`, semantic colours + validated text pairings.

**A11y:**
- Badges are usually **decorative/supplemental**. If a badge conveys *essential* status (e.g. "Sold out"), the meaning must also be in the surrounding text — never colour or a lone dot alone (1.4.1).
- A status dot needs a text equivalent or `aria-label` on the status container.
- Don't use a badge as the only accessible name of a control.

```html
<span class="badge badge--brand">24/7 coverage</span>
<span class="badge badge--success"><span class="dot" aria-hidden="true"></span> Live</span>
```

---

## 7. Alert / Toast

**Purpose.** Communicate a contextual message. **Alert** = inline, persistent (form-level error, info banner). **Toast** = transient, floating confirmation (e.g. "Message sent").

**Anatomy.** Icon + message (+ optional action/dismiss). Semantic colour on a tinted background, never colour alone.

**Semantic mapping (text/icon carry meaning, not just colour):**

| Type | Bg tint | Border/icon | Text | Live region |
|---|---|---|---|---|
| Info | `--color-brand-50` | `--color-info` | `--text` | `role="status"` |
| Success | success tint | `--color-success-strong` | `--text` | `role="status"` (polite) |
| Warning | warning tint | `--color-warning` (INK text) | `--text` | `role="status"` |
| Danger | danger tint | `--color-danger` | `--text` | `role="alert"` (assertive) |

**Tokens used:** semantic colours + validated tints, `--radius-md`/`--radius-lg`, `--shadow-lg` (toast), `--space-4`, `--z-toast` (1400), `--duration-slow` enter/exit (motion-gated).

**A11y:**
- **Live regions:** errors/critical → `role="alert"` (assertive, interrupts). Confirmations/info → `role="status"` (polite). The region must exist in the DOM *before* content is injected so AT announces the change.
- **Toast auto-dismiss:** if it auto-hides, respect WCAG 2.2.2 — either persist >5s isn't required for a *status*, but never auto-dismiss a message the user must act on; provide a dismiss button and don't rely on time-out alone. Pause-on-hover/focus for anything auto-advancing.
- **Dismiss** is a real `<button aria-label="Dismiss">`; toasts must be reachable/dismissible by keyboard and must not steal focus.
- **Focus not obscured (2.4.11):** a bottom toast must not cover a focused field/footer control.

```html
<div class="alert alert--danger" role="alert">
  <svg aria-hidden="true">⚠</svg>
  <p>We couldn't send your message. Check the highlighted fields and try again.</p>
</div>

<div class="toast toast--success" role="status">
  <p>Thanks — we'll text you within a minute.</p>
  <button type="button" class="toast__close" aria-label="Dismiss">×</button>
</div>
```

---

## 8. Accordion (FAQ)

**Purpose.** Progressive disclosure of Q&A — the FAQ section (also feeds FAQ structured data for SEO/GEO).

**Anatomy.** For each item: a heading containing a **button** (the trigger) + a collapsible **region** (the answer). Chevron indicates state.

**States:** collapsed / expanded / focus-visible / hover. Chevron rotates (motion-gated).

**Tokens used:** `--border` (dividers), `--radius-lg`, `--space-4/6`, `--font-display` (question), `--duration-base`/`--ease-standard` (height/opacity, motion-gated), `--focus-ring`.

**A11y (APG Disclosure/Accordion):**
- Each trigger is a `<button>` inside a heading (`<h3>`) of the correct level. Not a `<div>`.
- Trigger: `aria-expanded="true|false"` and `aria-controls="<panel-id>"`. Panel: `id`, and `role="region"` with `aria-labelledby="<trigger-id>"` (region role optional if many items — omit to avoid landmark noise).
- **Keyboard:** `Enter`/`Space` toggles. Optional `↑/↓` to move between headers, `Home/End` to first/last. Content inside the panel is in normal tab order.
- Multiple panels MAY be open at once (recommended for FAQ so users can compare) — don't force single-open.
- Chevron is `aria-hidden`; state comes from `aria-expanded`, not the icon.
- **SEO tie-in:** answer text must be real, crawlable DOM (not injected on click) and mirrored in FAQ JSON-LD.

```html
<h3>
  <button class="accordion__trigger" aria-expanded="false" aria-controls="faq-1-panel" id="faq-1">
    How fast does the AI respond to a new lead?
    <svg class="accordion__chevron" aria-hidden="true">▾</svg>
  </button>
</h3>
<div id="faq-1-panel" role="region" aria-labelledby="faq-1" hidden>
  <p>Typically under 30 seconds, 24/7 — including nights and weekends.</p>
</div>
```

---

## 9. Tabs

**Purpose.** Switch between related panels in the same context (e.g. "By industry", "By channel", pricing monthly/annual).

**Anatomy.** `tablist` → `tab`s → matching `tabpanel`s. Active tab has an indicator (underline/fill) with a **non-colour** cue too.

**States:** selected / unselected / hover / focus-visible / disabled.

**Tokens used:** `--color-brand-600` (active indicator), `--text-secondary` (inactive) → `--text` (active), `--border` (track), `--focus-ring`, `--radius-md`, `--duration-fast` (indicator, motion-gated).

**A11y (APG Tabs):**
- `role="tablist"` on the container; each tab is `role="tab"` with `aria-selected` and `aria-controls`; each panel is `role="tabpanel"` with `aria-labelledby` and `tabindex="0"` if it has no focusable child.
- **Keyboard:** `←/→` (or `↑/↓` if vertical) move between tabs; `Home/End` jump to first/last. Use **roving tabindex** (only the selected tab is `tabindex="0"`, others `-1`). Choose automatic (select on focus) or manual (`Enter`/`Space` to select) activation — manual is safer when panels are heavy.
- Selected state must not rely on colour alone (add weight/underline/indicator).
- Prefer native `<button>`s for tabs.

```html
<div class="tabs">
  <div role="tablist" aria-label="Pricing period">
    <button role="tab" id="tab-monthly" aria-selected="true"  aria-controls="panel-monthly" tabindex="0">Monthly</button>
    <button role="tab" id="tab-annual"  aria-selected="false" aria-controls="panel-annual"  tabindex="-1">Annual</button>
  </div>
  <div role="tabpanel" id="panel-monthly" aria-labelledby="tab-monthly" tabindex="0">…</div>
  <div role="tabpanel" id="panel-annual"  aria-labelledby="tab-annual"  tabindex="0" hidden>…</div>
</div>
```

---

## 10. Navbar + mobile menu

**Purpose.** Primary site navigation + persistent access to the primary CTA on every page.

**Anatomy.** Logo (home link) → nav links → primary CTA. On small screens: logo + a menu **button** that discloses the nav panel.

**States:** default / scrolled (condensed, subtle shadow) / mobile open/closed. Current page link gets `aria-current="page"` + a non-colour indicator.

**Tokens used:** `--bg` (+ blur/`--shadow-sm` when scrolled), `--z-sticky` (1100), `--gutter`, `--container-content`, `--space-*`, CTA tokens, `--focus-ring`, `--duration-base` (menu, motion-gated).

**A11y:**
- Wrap in `<nav aria-label="Primary">` (a landmark). Provide a **skip link** before it.
- **Mobile menu = disclosure:** the toggle is a `<button aria-expanded aria-controls>` with an accessible name ("Menu"/"Close"), not a bare icon. On open, move focus into the panel; on close, return focus to the toggle. `Esc` closes.
- If the mobile panel is a full-screen overlay, trap focus within it and mark background inert (`inert`/`aria-hidden`).
- **Sticky header + 2.4.11:** ensure focused in-page targets aren't hidden under the sticky bar — set `scroll-margin-top` = header height on focusable anchors.
- **44px targets** for the toggle and every link; ≥8px spacing.
- `aria-current="page"` on the active link (plus visual + non-colour indicator).

```html
<a class="skip-link" href="#main">Skip to main content</a>
<header class="navbar">
  <nav aria-label="Primary" class="navbar__inner">
    <a href="/" class="navbar__logo" aria-label="{{BRAND_NAME}} home">…</a>
    <button class="navbar__toggle" aria-expanded="false" aria-controls="site-menu">
      <span class="sr-only">Menu</span><svg aria-hidden="true">☰</svg>
    </button>
    <ul id="site-menu" class="navbar__menu">
      <li><a href="/how-it-works" aria-current="page">How it works</a></li>
      <li><a href="/pricing">Pricing</a></li>
      <li><a href="/book" class="btn btn--primary">Book a call</a></li>
    </ul>
  </nav>
</header>
```

---

## 11. Footer

**Purpose.** Secondary navigation, trust signals, NAP (Name/Address/Phone), legal links, and a final CTA.

**Anatomy.** Column groups (product, company, legal, contact) → NAP block → social → copyright. Often on a `.surface-dark` background.

**Tokens used:** `.surface-dark` (remaps `--text`, `--link` → `--color-brand-300`, `--bg` → `--color-ink`), `--space-*`, `--container-content`, `--gutter`, `--border` (0.12 white hairline on dark).

**A11y:**
- `<footer>` = `contentinfo` landmark (one per page, top-level). Group link columns under headings (`<h2>`/`<h3>` visually small but present) for screen-reader navigation.
- **NAP consistency (SEO/GEO + trust):** address in `<address>`, phone as a `tel:` link, email as `mailto:`. Must match the Organization JSON-LD and every other listing exactly.
- On dark background, links use the remapped `--link` (brand-300, validated 9.45:1 on ink); keep underline/affordance.
- Consistent-help (3.2.6 A): if contact/help appears in the footer across pages, keep it in the same relative location.

```html
<footer class="footer surface-dark">
  <div class="footer__inner">
    <address class="footer__nap">
      {{LEGAL_ENTITY}}<br />{{ADDRESS}}, {{CITY}}, {{REGION}} {{POSTAL}}<br />
      <a href="tel:{{PHONE}}">{{PHONE}}</a> · <a href="mailto:{{EMAIL}}">{{EMAIL}}</a>
    </address>
    <nav aria-label="Footer"> … </nav>
    <p class="footer__legal">© <span id="yr"></span> {{LEGAL_ENTITY}}. All rights reserved.</p>
  </div>
</footer>
```

---

## 12. Breadcrumb

**Purpose.** Show the user's location in the site hierarchy on deep pages (blog posts, case studies) and feed BreadcrumbList structured data.

**Anatomy.** Ordered list of links; last item = current page (not a link). Separators are decorative.

**Tokens used:** `--text-muted` (separators/inactive), `--link`, `--text` (current), `--text-sm`, `--space-2`.

**A11y:**
- Wrap in `<nav aria-label="Breadcrumb">` around an `<ol>`. Each crumb is an `<li>`; links are `<a>`.
- Current page: `<a aria-current="page">` or plain text, styled distinctly (not colour alone).
- Separators (`/`, `›`) are CSS `::before` content or `aria-hidden` — never read out.

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li><a href="/">Home</a></li>
    <li><a href="/case-studies">Case studies</a></li>
    <li><a aria-current="page">Med spa</a></li>
  </ol>
</nav>
```

---

## 13. Modal / Dialog

**Purpose.** Focus the user on a single task without leaving the page — book-a-call scheduler, demo request, video, confirm. Use sparingly; never trap users.

**Anatomy.** Backdrop (scrim) → dialog surface (title, body, actions, close button).

**States:** closed / opening / open / closing. Scrim `--opacity-backdrop`; surface `--shadow-xl`.

**Tokens used:** `--z-overlay` (1200, scrim) / `--z-modal` (1300, surface), `--opacity-backdrop`, `--bg`, `--radius-xl`/`--radius-2xl`, `--shadow-xl`, `--space-6/8`, `--duration-slow` + `--ease-decelerate` (motion-gated), `--focus-ring`.

**A11y (APG Dialog — the highest-risk component to get wrong):**
- Prefer the native `<dialog>` element with `showModal()` (gives free focus trap, backdrop, `Esc`). Otherwise `role="dialog"` + `aria-modal="true"`.
- **Name it:** `aria-labelledby` → the title id (or `aria-label`). `aria-describedby` for body if helpful.
- **Focus management:** on open, move focus into the dialog (first field or the dialog container); **trap focus** (Tab cycles within); on close, **return focus to the trigger**.
- **`Esc` closes.** A visible, keyboard-reachable close `<button aria-label="Close">`.
- Background content is `inert`/`aria-hidden` while open; prevent body scroll.
- **2.4.11:** the dialog and its focused controls must not be obscured; don't let the chat widget/sticky bar overlap it.

```html
<dialog id="book" class="modal" aria-labelledby="book-title">
  <div class="modal__surface">
    <button class="modal__close" aria-label="Close" data-close>×</button>
    <h2 id="book-title" class="modal__title">Book a call</h2>
    <div class="modal__body"><!-- scheduler / form --></div>
  </div>
</dialog>
<!-- open with dialog.showModal(); close returns focus to the trigger -->
```

---

## 14. Tooltip

**Purpose.** Supplemental, non-essential hint on hover/focus (e.g. explain "speed-to-lead"). **Never** put essential info or interactive controls in a tooltip.

**Anatomy.** Trigger (has an accessible name already) + floating bubble referenced by `aria-describedby`.

**Tokens used:** `--color-ink` (bg) + `--text-on-dark`, `--radius-md`, `--shadow-lg`, `--text-sm`, `--z-tooltip` (1500), `--duration-fast` (motion-gated).

**A11y (APG Tooltip):**
- Trigger must be focusable natively (a `<button>`/link/field). Tooltip is `role="tooltip"` with an `id`; trigger points via `aria-describedby`.
- **Show on both hover AND keyboard focus**; **dismissable** with `Esc` and it must not disappear when the pointer moves over it (WCAG 1.4.13 Content on Hover — hoverable, dismissable, persistent).
- Tooltips can't contain interactive content or the only copy of essential info — that content must live elsewhere too.
- Don't use `title` attribute as your tooltip (no keyboard/touch support, inconsistent).

```html
<button type="button" class="info" aria-describedby="tt-speed">
  What is speed-to-lead? <svg aria-hidden="true">ⓘ</svg>
</button>
<span role="tooltip" id="tt-speed" class="tooltip">
  How fast you respond after a lead comes in. Under 5 minutes ≈ higher conversion.
</span>
```

---

## 15. Cross-component checklist (ship gate)

- [ ] Every interactive control is a **native element** (button/link/input) or a documented APG pattern — no `<div onclick>`.
- [ ] Every control has a **visible label / accessible name**; icon-only controls have `aria-label`.
- [ ] **Focus-visible** is present and ≥3:1 on every focusable element; never `outline:none` without a replacement.
- [ ] **Target size ≥44px** (min 24px + spacing) with ≥8px between adjacent controls.
- [ ] **Colour is never the only cue** — status/errors/links/active-states also use text/icon/underline/weight.
- [ ] **Contrast**: text ≥4.5:1 (3:1 large); UI borders/indicators ≥3:1 (uses `--border-interactive`, not `--border`).
- [ ] **Keyboard**: full operability, logical order, no traps; `Esc` closes overlays; roving tabindex where specified.
- [ ] **Errors** are inline, in text, linked via `aria-describedby`, with `aria-invalid`; focus moves to first error.
- [ ] **Live regions** (`role=alert`/`status`) exist before content injection.
- [ ] **Reduced motion** honoured; **sticky/overlay/chat** never obscure the focused element (2.4.11).
- [ ] States implemented for **default / hover / active / focus-visible / disabled / loading/error** where applicable.
- [ ] Tokens referenced **by name**; no hardcoded hex/px/ms.

---

## Related

- [`interactive-elements.md`](./interactive-elements.md) — CTA hierarchy, forms & validation UX, conversion elements, sticky mobile CTA, interaction feedback.
- [`design-tokens.md`](./design-tokens.md) — token names, roles, and how to consume them in components.
- [`../brand/color-system.md`](../brand/color-system.md) — canonical colour & contrast rules (raw hex allowed there).
- [`../brand/iconography.md`](../brand/iconography.md) — icon sizing, `aria-hidden`, and accessible-name rules for icon-in-control.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — validated colour pairings and ratios used by every component state.
- [`../00-foundations/principles.md`](../00-foundations/principles.md) — the design principles these components encode.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — **source of truth** for all values.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — generated CSS custom properties consumed here.
