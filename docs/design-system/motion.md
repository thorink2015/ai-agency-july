# Motion System

**Purpose:** The site's animation and transition system — why motion exists (feedback, continuity, hierarchy — never decoration-first), the duration and easing tokens and when to use each, copy-paste patterns for hover / press / enter-exit / reveal-on-scroll / page transitions / skeleton loading, GPU-friendly performance rules, and the MANDATORY `prefers-reduced-motion` handling with concrete fallbacks — so any developer or future Claude session adds motion that feels responsive, on-brand, and accessible.
**Status:** v1 foundation — adjustable.

---

> **All values here reference [design tokens](./design-tokens.md) by name** (`--duration-fast`, `--ease-standard`). Do not hardcode ms/curves in components. Raw numbers appear only to explain the _reasoning_ behind a token.
>
> Brand direction: **motion that feels responsive, not decorative** — calm confidence, fast, competent. Snappy on interaction; restrained on ambient. When in doubt, use less, and use it faster.

---

## 0. TL;DR — the motion rules

- [ ] **Motion earns its place.** Every animation must do one of: give **feedback**, preserve **continuity**, or signal **hierarchy**. If it does none, delete it.
- [ ] **Only animate `transform` and `opacity`.** These are GPU-composited and never trigger layout/paint. Everything else is a performance and CLS risk.
- [ ] **Use the tokens.** Durations come from `--duration-instant → --duration-slower`; curves from `--ease-standard / -decelerate / -accelerate / -spring`. Never invent a `450ms cubic-bezier(...)`.
- [ ] **Fast on interaction, slower on transition.** Hover/press = `--duration-fast` (150ms). Enter/exit = `--duration-slow` (300ms). Large page-level moves = `--duration-slower` (500ms) max.
- [ ] **`prefers-reduced-motion` is not optional.** Gate all non-essential motion behind `@media (prefers-reduced-motion: no-preference)`, or neutralize it under `reduce`. Fallback = instant or opacity-only. This is shipped globally in `tokens.css`.
- [ ] **Never animate more than ~150KB of layout.** No animating `width`, `height`, `top`, `left`, `margin`, or `box-shadow` on scroll/hover-heavy elements. Animate a `transform` proxy instead.
- [ ] **`will-change` is a scalpel, not a blanket.** Add it right before an animation, remove it after. Never leave it in a static stylesheet on many elements.
- [ ] **Respect the flash/auto-move SCs.** No auto-moving content that can't be paused after 5s (WCAG 2.2.2); nothing flashes more than 3×/second (2.3.1).
- [ ] **Focus must stay visible through motion.** Animation must never hide or obscure the focused element (2.4.7 / 2.4.11).

---

## 1. Why motion — the three jobs

Motion on this site exists to serve the user, not to entertain. Before adding any animation, name which job it does. If you can't, it's decoration — cut it.

| Job | What it does | Examples on this site | Anti-pattern to avoid |
|---|---|---|---|
| **Feedback** | Confirms the system received input and is responding. Reinforces "fast, competent." | Button press-down, input focus ring grow, toggle slide, "message sent" checkmark, chat "typing…" dots | A CTA that reacts 400ms after click — feels broken, not premium |
| **Continuity** | Connects two states so the eye doesn't lose context. Preserves spatial logic. | Accordion expand, drawer slide-in, modal scale-up from trigger, tab underline sliding, card → detail transition | Cross-fading unrelated content (looks like a glitch, breaks continuity) |
| **Hierarchy** | Directs attention in a deliberate order; establishes what's primary. | Staggered reveal of feature cards, hero headline settling before subcopy, sequential onboarding steps | Everything animating at once (no hierarchy) or endless looping ambient motion (steals attention) |

**The decoration-first test:** _"If this animation were instant, would the user lose information or context?"_ If **no**, it's decoration — either remove it or make it so subtle/fast it's felt, not seen. We are a trust-and-speed brand; twitchy, showy motion reads as hype and undermines the promise.

---

## 2. Duration tokens — and when to use each

Durations are perceptual, not linear. Small UI needs to feel **instant**; large surfaces need enough time to be **traceable** without feeling slow. Anything over 500ms on the web reads as sluggish.

| Token | Value | Use for | Do NOT use for |
|---|---|---|---|
| `--duration-instant` | `100ms` | Micro-feedback: press-down, checkbox tick, tooltip show, color-only hover shifts | Anything that moves a large distance (looks jerky) |
| `--duration-fast` | `150ms` | **Default for interaction:** hover states, focus ring, small icon spins, toggle | Full-panel enter/exit (too abrupt) |
| `--duration-base` | `200ms` | Slightly larger state changes: dropdown open, tab-switch content, chip select | Page-level or hero transitions |
| `--duration-slow` | `300ms` | **Default for enter/exit:** modal, drawer, accordion, toast, reveal-on-scroll | Micro-feedback (feels laggy on a button) |
| `--duration-slower` | `500ms` | Large / full-viewport transitions: route change, hero orchestration, section wipe | Anything a user triggers repeatedly (feels heavy) |

**Rule of thumb:** the farther an element travels and the larger it is, the longer (within reason) it may take. A 4px press → `instant`. A full-height drawer → `slow`. Never exceed `--duration-slower` for interactive UI.

---

## 3. Easing tokens — and when to use each

Easing communicates physics and intent. The wrong curve makes motion feel cheap. Match the curve to whether the element is **arriving**, **leaving**, or **moving between two on-screen states**.

| Token | Curve | Feels like | Use for |
|---|---|---|---|
| `--ease-standard` | `cubic-bezier(0.4, 0, 0.2, 1)` | Balanced ease-in-out | **Default.** Any move that starts and ends on screen: hover, toggle, tab underline, accordion, color/opacity changes |
| `--ease-decelerate` | `cubic-bezier(0, 0, 0.2, 1)` | Fast start, gentle stop | **Entering** the screen: modal/drawer/toast appearing, reveal-on-scroll, content mounting. Draws the eye to where it lands |
| `--ease-accelerate` | `cubic-bezier(0.4, 0, 1, 1)` | Gentle start, fast exit | **Leaving** the screen: dismiss, close, unmount. Gets out of the way quickly |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Slight overshoot / bounce | **Sparingly** — a single confirming beat: success checkmark, "booked!" state, an occasional playful hover. Never on text or large panels |

**Guidance:** enters decelerate (they slow into place), exits accelerate (they speed away), everything in-between is standard. Reserve `--ease-spring` for one delightful moment per view — overuse it and the calm-confidence brand turns cartoonish. Never use `linear` except for continuous, non-decorative motion like a determinate progress bar or a spinner.

---

## 4. Standard patterns (copy-paste)

Every snippet uses tokens, animates only `transform`/`opacity`, and is written so the reduced-motion layer in §6 neutralizes it automatically. Composable transition shorthand:

```css
/* Reusable transition helpers — declare the property explicitly.
   NEVER `transition: all` (it animates unknown/expensive properties). */
.u-transition       { transition: transform var(--duration-fast) var(--ease-standard),
                                   opacity   var(--duration-fast) var(--ease-standard); }
.u-transition-enter { transition: transform var(--duration-slow) var(--ease-decelerate),
                                   opacity   var(--duration-slow) var(--ease-decelerate); }
.u-transition-exit  { transition: transform var(--duration-base) var(--ease-accelerate),
                                   opacity   var(--duration-base) var(--ease-accelerate); }
```

### 4.1 Hover (feedback + affordance)

Small, fast, `transform`-based lift. Pair with a color change (also cheap). Never animate `box-shadow` geometry directly on hover-heavy grids — swap a pre-rendered shadow via opacity or keep it on a `::after` layer.

```css
.card {
  transition: transform var(--duration-fast) var(--ease-standard),
              box-shadow var(--duration-fast) var(--ease-standard);
}
@media (hover: hover) {              /* don't apply hover motion on touch */
  .card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
}

.btn {
  transition: background-color var(--duration-fast) var(--ease-standard),
              transform        var(--duration-instant) var(--ease-standard);
}
@media (hover: hover) {
  .btn:hover { background-color: var(--cta-bg-hover); }
}
```

### 4.2 Press (feedback)

The most important micro-interaction on a conversion site — it makes CTAs feel instant and physical. Keep it tiny (~1–2% scale) and `instant`.

```css
.btn:active { transform: scale(0.98); transition-duration: var(--duration-instant); }
```

### 4.3 Enter / exit (continuity)

Enter with `--ease-decelerate`, exit with `--ease-accelerate`. Combine a small translate with opacity — never slide from far off-screen (reads as decorative and can cause horizontal overflow).

```css
/* Modal / drawer / toast — driven by a state class or [data-state] */
.panel {
  opacity: 0;
  transform: translateY(8px) scale(0.98);
  transition: opacity   var(--duration-slow) var(--ease-decelerate),
              transform var(--duration-slow) var(--ease-decelerate);
}
.panel[data-state="open"] { opacity: 1; transform: none; }
.panel[data-state="closing"] {                  /* exit */
  opacity: 0; transform: translateY(8px) scale(0.98);
  transition-duration: var(--duration-base);
  transition-timing-function: var(--ease-accelerate);
}
```

### 4.4 Reveal-on-scroll (hierarchy)

Content fades/rises **once** as it enters the viewport, in a deliberate order. Use `IntersectionObserver` to add a class — do **not** drive per-frame scroll animation on the main thread (janky and reduced-motion-hostile). Content must be **visible by default** if JS never runs (progressive enhancement).

```css
/* Default = visible. JS adds .reveal to opt an element into the hidden→shown motion. */
.reveal            { opacity: 0; transform: translateY(16px); }
.reveal.is-visible { opacity: 1; transform: none;
                     transition: opacity   var(--duration-slow) var(--ease-decelerate),
                                 transform var(--duration-slow) var(--ease-decelerate); }
.reveal:nth-child(2) { transition-delay: 60ms; }   /* stagger for hierarchy */
.reveal:nth-child(3) { transition-delay: 120ms; }  /* keep total stagger < 300ms */
```

```js
// Progressive enhancement: only hide+animate when motion is welcome.
if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
  const io = new IntersectionObserver((entries, obs) => {
    for (const e of entries) {
      if (e.isIntersecting) { e.target.classList.add('is-visible'); obs.unobserve(e.target); }
    }
  }, { threshold: 0.15, rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
}
// If reduced motion is set, elements simply stay visible (default state) — no .reveal needed.
```

### 4.5 Page transitions (continuity)

Prefer the native **View Transitions API** where supported; it's GPU-driven and degrades gracefully. Keep route changes short — a crossfade or a small slide, `--duration-slow` to `--duration-slower` max. Never block content paint on a transition.

```css
@view-transition { navigation: auto; }            /* opt in (progressive) */

@media (prefers-reduced-motion: no-preference) {
  ::view-transition-old(root) { animation: fade var(--duration-slow) var(--ease-accelerate) both; }
  ::view-transition-new(root) { animation: fade var(--duration-slow) var(--ease-decelerate) both reverse; }
}
@keyframes fade { from { opacity: 0; } to { opacity: 1; } }
```

Browsers without View Transitions get an instant navigation — acceptable and fast. Do **not** hand-roll full-page overlay animations that delay the LCP.

### 4.6 Skeleton loading (feedback + continuity)

Skeletons reduce perceived wait and prevent layout shift (reserve final dimensions → protects **CLS < 0.1**). Use a slow, low-contrast shimmer via `transform` on a gradient — not an infinite opacity flash. Under reduced motion, show a **static** placeholder (no shimmer).

```css
.skeleton {
  background: var(--color-neutral-100);
  border-radius: var(--radius-md);
  position: relative; overflow: hidden;
}
@media (prefers-reduced-motion: no-preference) {
  .skeleton::after {
    content: ""; position: absolute; inset: 0;
    background: linear-gradient(90deg, transparent, rgb(255 255 255 / 0.6), transparent);
    transform: translateX(-100%);
    animation: skeleton-shimmer 1.4s var(--ease-standard) infinite;
  }
}
@keyframes skeleton-shimmer { to { transform: translateX(100%); } }
```

> **AI-specific:** the chat/SMS assistant's "typing…" indicator is feedback, not decoration — keep it (dots pulsing via opacity/transform, ≤ 3 changes/sec). Under reduced motion, show static "…" or "Assistant is typing".

---

## 5. Performance rules

Motion that stutters destroys the "fast, competent" brand faster than no motion at all. Every animation must hold **60fps** and protect the Core Web Vitals budgets (**INP ≤ 200ms**, **CLS < 0.1**, **LCP ≤ 2.5s**).

### 5.1 Animate only `transform` and `opacity`

These run on the compositor thread — no layout, no paint, no main-thread cost. Everything else is expensive.

| ✅ Cheap (composite only) | ❌ Expensive (layout / paint) | Do this instead |
|---|---|---|
| `transform: translate / scale / rotate` | `top`, `left`, `right`, `bottom`, `margin` | `transform: translate()` |
| `opacity` | `width`, `height` | `transform: scale()` (+ set final box size) |
| `filter` (sparingly, GPU) | `box-shadow` geometry (on many/large elements) | swap opacity of a pre-rendered shadow layer |
| — | `color` / `background` on huge surfaces per-frame | fine for discrete state changes, not per-frame |

### 5.2 Avoid layout thrash

- **Never** animate a property that changes layout (`width`, `height`, `top/left`, `margin`, `padding`, `font-size`) on scroll or hover-heavy elements. Use a `transform` proxy and set final dimensions statically.
- **Batch DOM reads/writes.** Don't read `offsetHeight` then write a style in the same loop — it forces synchronous reflow. Read all, then write all (or use `requestAnimationFrame`).
- **Don't drive animation from the `scroll` event.** Use `IntersectionObserver` (visibility) or CSS scroll-driven animations. Per-frame scroll handlers block INP.
- **Reserve space for async content** (images, embeds, skeletons) with explicit `width`/`height` or `aspect-ratio` → no CLS when it loads.

### 5.3 `will-change` sparingly

`will-change` promotes an element to its own compositor layer. Useful **immediately before** a known animation; harmful when left on many elements (memory blow-up, can worsen performance).

```css
/* ✅ Scoped: promote only while the interaction is imminent, then release. */
@media (hover: hover) { .card:hover { will-change: transform; } }
/* On animation end / interaction end, remove it (in JS: el.style.willChange = 'auto'). */
```

- [ ] Never put `will-change` in a base rule that matches dozens of elements.
- [ ] Prefer letting the browser auto-promote via an active `transform`/`opacity` transition; add `will-change` only if you measure jank.
- [ ] Remove `will-change` after the animation completes.

### 5.4 Budget & scope

- Keep JS driving motion out of the critical path — animation libraries count against the **< 150KB initial JS** budget. Prefer CSS; reach for a library only for orchestration you can't express in CSS.
- Limit concurrent animations. A staggered reveal of 30 cards at once thrashes; virtualize or cap the animated set to what's in view.
- Test on a mid-tier phone with CPU throttling, not just a desktop.

---

## 6. `prefers-reduced-motion` — MANDATORY

Some users experience nausea, dizziness, or migraines from motion (vestibular disorders). Honoring `prefers-reduced-motion` is a **hard requirement**, not a nicety, and supports WCAG 2.2 (2.3.3 Animation from Interactions, AAA; and the intent of 2.2.2 / 2.3.1 at AA).

### 6.1 The global safety net (already shipped in `tokens.css`)

A global `reduce` rule neutralizes animation/transition durations and disables smooth scroll, so **nothing you build can ship uncontrolled motion by accident**:

```css
/* Present in tokens/tokens.css — do not remove. */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

This is a **backstop**, not a substitute for intent. It kills _duration_, but the element still jumps to its final state. That's correct for most transitions, but for anything that only makes sense _with_ motion (reveal-on-scroll, shimmer, parallax), you must also author the reduced-motion end state explicitly (below).

### 6.2 The authoring pattern — gate motion, keep the outcome

Wrap **non-essential** motion in `@media (prefers-reduced-motion: no-preference)` so the default (no-motion) state is fully usable, then add motion only when welcome:

```css
/* ✅ Default: final, visible, no motion. Motion is additive. */
.reveal { opacity: 1; transform: none; }              /* usable with zero motion */

@media (prefers-reduced-motion: no-preference) {
  .reveal            { opacity: 0; transform: translateY(16px); }
  .reveal.is-visible { opacity: 1; transform: none;
                       transition: opacity var(--duration-slow) var(--ease-decelerate),
                                   transform var(--duration-slow) var(--ease-decelerate); }
}
```

Mirror the check in JS (see §4.4) so observers/timeline animations don't run at all under `reduce`.

### 6.3 Concrete fallbacks by pattern

| Pattern | Full-motion behavior | Reduced-motion fallback (mandatory) |
|---|---|---|
| **Hover lift** | `translateY(-4px)` + shadow | Color/shadow change only, no translate (or nothing) |
| **Press** | `scale(0.98)` | Instant background/opacity change — feedback preserved |
| **Enter/exit (modal, drawer, toast)** | Slide + fade over 300ms | **Instant opacity** fade (or immediate show/hide). Never slide |
| **Reveal-on-scroll** | Fade + rise, staggered | **Show immediately, fully visible** — no transform, no observer |
| **Page transition** | View-transition crossfade | Instant navigation (skip the animation) |
| **Skeleton shimmer** | Moving gradient | **Static** placeholder block, no shimmer |
| **"Typing…" indicator** | Pulsing dots | Static "…" or text "Assistant is typing" |
| **Parallax / ambient background** | Depth movement on scroll | **Disable entirely** — static background |
| **Auto-advancing carousel** | Auto-play with motion | **Pause by default**; require explicit user control (also satisfies 2.2.2) |

### 6.4 Reduced-motion rules

- [ ] **Essential motion is exempt but rare.** Only motion conveying information that has no static equivalent may stay (e.g., a determinate progress bar). A decorative hero animation is never essential.
- [ ] **`opacity`-only is the safe fallback.** Fades don't cause vestibular issues; large translate/scale/rotate/parallax do. When in doubt, cross-fade or show instantly.
- [ ] **No parallax, no auto-play, no scroll-jacking** under `reduce`. Disable them, don't just shorten them.
- [ ] **Test both modes.** DevTools → Rendering → "Emulate CSS prefers-reduced-motion: reduce". OS: macOS Reduce Motion / Windows "Show animations".
- [ ] **Never gate _content_ behind motion.** If reveal-on-scroll fails or is disabled, the content must already be visible and readable.

---

## 7. Accessibility & safety guardrails

Beyond `prefers-reduced-motion`, motion must not violate WCAG 2.2 timing/flash/focus criteria.

| Rule | Requirement | SC |
|---|---|---|
| **No unstoppable auto-motion** | Anything that auto-moves/auto-updates for **> 5s** (carousel, marquee, ticker) needs a visible pause/stop/hide control | 2.2.2 Pause, Stop, Hide (A) |
| **No dangerous flashing** | Nothing flashes more than **3 times per second** | 2.3.1 Three Flashes (A) |
| **Motion doesn't hide focus** | An animating sticky header / drawer / chat widget must never fully cover the keyboard-focused element | 2.4.11 Focus Not Obscured (AA) |
| **Focus stays visible during transitions** | The focus indicator must remain visible while panels animate in/out | 2.4.7 Focus Visible (AA) |
| **No motion-only meaning** | Never rely on animation alone to convey state; pair with text/icon/color | 1.4.1 Use of Color (A) intent |
| **Interaction motion is dismissible** | Motion triggered by interaction (parallax, hover-reveal) should be reducible; honoring `prefers-reduced-motion` satisfies this | 2.3.3 Animation from Interactions (AAA) |

- [ ] Carousels **do not auto-advance** by default; if they do, expose pause and respect `reduce`.
- [ ] Scroll-triggered reveals use `IntersectionObserver`, run once, and never re-trigger loops.
- [ ] Modal/drawer open moves focus in; the animation never delays focus reaching the panel.

---

## 8. Do / Don't

| ✅ Do | ❌ Don't |
|---|---|
| Animate `transform` + `opacity` only | Animate `width`, `height`, `top`, `left`, `margin` |
| Declare each transition property explicitly | Use `transition: all` |
| Use `--duration-fast` for interaction, `--duration-slow` for enter/exit | Exceed `--duration-slower` (500ms) on interactive UI |
| Enter with `--ease-decelerate`, exit with `--ease-accelerate` | Use `--ease-spring` on text or large panels |
| Gate ambient/reveal motion behind `no-preference` | Ship reveal-on-scroll that hides content when JS/motion is off |
| Reserve space for async content (CLS) | Let animated content push layout on load |
| Add `will-change` right before an animation, remove after | Leave `will-change` in base styles on many elements |
| Drive scroll reveals with `IntersectionObserver` | Animate from the `scroll` event per frame |
| Give feedback within ~100ms of interaction | Delay a CTA reaction (feels broken) |
| Pause auto-motion after 5s; cap flashes at 3/sec | Auto-play carousels/marquees with no control |

---

## 9. Motion review checklist (per component)

- [ ] Every animation does a **job** (feedback / continuity / hierarchy) — no decoration-first motion.
- [ ] Uses **duration + easing tokens** only; no hardcoded ms/curves.
- [ ] Interaction motion is `--duration-fast`/`instant`; enter/exit is `--duration-slow`; nothing over `--duration-slower`.
- [ ] Animates **only `transform`/`opacity`** (plus discrete color/shadow state); no layout properties.
- [ ] No `transition: all`; each property named.
- [ ] **Reduced-motion fallback authored** (§6.3) and verified in emulation — content stays usable, no parallax/shimmer/slide.
- [ ] Non-essential motion gated behind `@media (prefers-reduced-motion: no-preference)` (CSS **and** JS).
- [ ] `will-change` scoped and released; not in shared base rules.
- [ ] No auto-motion > 5s without pause; no flash > 3/sec; focus never obscured or hidden by animation.
- [ ] Async/animated content reserves space → **CLS < 0.1**; feedback within ~100ms → protects **INP**.
- [ ] Tested at 60fps on a throttled mid-tier device.

---

## Related

- [`design-tokens.md`](./design-tokens.md) — the source of `--duration-*`, `--ease-*`, and motion-related tokens used throughout this doc.
- [`layout-and-grid.md`](./layout-and-grid.md) — sticky-header condense behaviour and scroll-margin, which interact with page transitions and focus.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — focus-ring and state-colour contrast that motion must preserve.
- [`../00-foundations/principles.md`](../00-foundations/principles.md) — the whitespace, hierarchy, and restraint principles behind "motion that feels responsive, not decorative".
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — `--duration-*`, `--ease-*` custom properties and the global `prefers-reduced-motion` safety net.
- [`../../tokens/tailwind.tokens.js`](../../tokens/tailwind.tokens.js) — `transitionDuration` / `transitionTimingFunction` scales for utility-based motion.
