# Imagery

**Purpose:** Art direction and technical delivery rules for all photography and illustration on {{BRAND_NAME}} — what to shoot/source, how to treat it on-brand (warm-modern, human+AI, authentic, diverse, never cheesy stock), and the exact format/size/alt-text rules every image must pass before it ships.
**Status:** v1 foundation — adjustable.

---

## TL;DR (extractable answer)

{{BRAND_NAME}} imagery shows **real people getting a fast, human response** — not robots, not glowing brains, not generic stock handshakes. Style: warm, modern-tech, generous whitespace, diverse subjects, candid over posed. Technical: **AVIF first, WebP fallback, JPEG last** via `<picture>`; responsive `srcset`+`sizes`; always set `width`/`height`; hero LCP image **< 150KB** and eager + `fetchpriority="high"`; below-fold images `loading="lazy"`. Every image is either **informative** (real alt text) or **decorative** (`alt=""`).

---

## 1. Art direction principles

The brand is *trustworthy, fast, competent, human+AI, premium-but-approachable, calm confidence.* Imagery must feel the same: **it's about the relief of a lead being answered, not about the technology.**

| Principle | What it means in a photo/illustration |
|---|---|
| **Human first, AI implied** | Lead the frame with a real person (owner, staff, or customer). AI shows up as a clean UI, a chat bubble, a booked slot — never as a robot, android, or humanoid assistant. |
| **The moment of relief** | Capture the outcome: a booked appointment, a reply in seconds, a calm owner. Sell the feeling, not the feature. |
| **Warm-modern** | Natural light, real interiors (clinic, salon chair, job site, home office), soft depth of field. Modern but not sterile; premium but not cold. |
| **Diverse & real** | Range of ages, ethnicities, body types, genders, and industries (med spa, dental, home services, real estate, coaching, clinics). Represent the actual SMB audience. |
| **Calm confidence** | Composed subjects, uncluttered frames, generous negative space for text overlay. No frantic, no hype, no "shocked face" thumbnails. |
| **Speed, shown honestly** | Convey speed with fresh composition and motion cues (a message just sent, a notification landing) — not with cheesy speed-lines or lightning bolts. |

---

## 2. Subject matter — shoot / source this

- **Real people in service settings:** an owner at reception, a stylist between clients, a contractor in a van, an agent showing a home, a coach on a call.
- **Genuine conversations:** a person reading a helpful SMS/chat reply, texting back, smiling at a confirmation.
- **Product-in-context:** a phone or laptop showing the {{BRAND_NAME}} assistant answering, qualifying, and booking — screens must be legible and real (see §6).
- **The booking moment:** a calendar slot filling, a "Booked ✓" confirmation, a handshake *that actually earns the frame* (met, in-context, not staged).
- **Human backup:** a friendly support person on a headset — reinforces "humans on call when it matters."
- **Dashboards & data:** clean, on-brand UI showing response time, leads captured, appointments booked (use real-looking but placeholder data; never expose PII).

## 3. Do / Don't

| Do | Don't |
|---|---|
| Real, candid people in real environments | Obvious posed stock ("business team high-five") |
| Diverse, industry-specific casting | All-same-demographic, all-corporate-office casting |
| Clean UI, chat bubbles, calendars to imply AI | Humanoid robots, androids, glowing blue brains, `01010` matrix rain |
| Natural light, warm neutrals, brand accents | Heavy neon cyberpunk, dark "hacker" aesthetics |
| Generous negative space for headlines | Busy frames with no room for text |
| Authentic screen content (see §6) | Fake gibberish UI, Lorem Ipsum on visible screens |
| Subtle brand duotone/overlay (see §4) | Rainbow gradients, clashing filters, heavy vignettes |
| Motion cues that feel responsive | Cheesy speed-lines, lens flares, lightning bolts |
| Faces looking at the outcome/screen | Direct-to-camera "salesy" smize, stocky thumbs-up |

---

## 4. Treatment & colour

Treatments must use the brand palette from [`color-system.md`](./color-system.md). Reference tokens by name, never raw hex, in code.

### 4.1 Overlays (for text legibility on hero/banner images)

Text over an image must still meet WCAG contrast. Do **not** rely on the raw photo.

- **Ink scrim:** overlay `--color-neutral-ink` at 55–70% (left-to-transparent gradient) behind text. Verify the text/scrim pairing hits **4.5:1** (normal) / **3:1** (large ≥24px) per [`color-system.md`](./color-system.md) §4.
- **Bottom-up gradient:** `linear-gradient(to top, rgb(11 17 32 / 0.75), transparent 60%)` for captions on the lower third.
- Never place body text directly on an unscrimmed photo — contrast is unpredictable per pixel.

### 4.2 Duotone (for abstract / section-break imagery)

Use a **brand duotone** to unify sourced imagery and reduce visual noise:

- **Shadows:** `--color-neutral-ink` (#0B1120). **Highlights:** `--color-neutral-50` or a low-saturation `--color-brand-100`.
- **Accent duotone** (sparingly, for tech/dashboard motifs): shadows `--color-brand-900`, highlights `--color-accent-400`. Decorative only — never as a text background without a scrim.
- Keep duotone **subtle**: photos should still read as real. This is a warm-modern brand, not a poster.

### 4.3 Accent & framing

- Rounded corners on all framed images: `--radius-lg` (12px) for cards, `--radius-2xl` (24px) for hero panels — matches the "rounded-but-crisp" direction.
- Subtle depth only: `--shadow-md` / `--shadow-lg`. No hard drop shadows, no skeuomorphic bevels.
- A thin `--color-brand-600` or `--color-accent-400` keyline is allowed as a decorative highlight (≥3:1 not required — it's not conveying meaning).

---

## 5. Illustration guidance

When photography can't tell the story (abstract concepts, empty states, diagrams), use illustration — but keep it on-brand.

- **Style:** flat/semi-flat, geometric, rounded-but-crisp, generous whitespace. Line weight matches the icon system (see [`iconography.md`](./iconography.md)): **1.5–2px** equivalent stroke.
- **Palette:** brand + accent + neutrals from tokens. One accent max per illustration; let neutrals carry the frame.
- **Never:** clip-art robots, 3D chrome renders, gradient-mesh blobs, or "AI brain" clichés.
- **Format:** ship as **optimized SVG** (see [`iconography.md`](./iconography.md) SVGO checklist) when vector; export to AVIF/WebP raster only when the illustration is photographic/complex (>~15KB SVG or heavy gradients).
- **Spot illustrations** pair well with real UI screenshots to explain "how it works" without overloading the page.

---

## 6. Product / UI screenshots

Screens are our strongest proof. Treat them as first-class imagery.

- Show the **real assistant** answering, qualifying, and booking. Legible text, plausible copy in brand voice (short, direct, reassuring).
- Use **placeholder names/data** — never real customer PII, phone numbers, or emails. Use `{{PHONE}}` / `example.com` conventions where a value would show.
- Prefer a **clean device frame or borderless crop** at `--radius-lg`; keep the OS chrome minimal.
- Recommended crops: **16:9** (wide walkthrough), **4:3** or **3:2** (feature detail), **9:16** (mobile chat/SMS).
- If a screenshot is the LCP element, it still obeys the hero budget in §8 (< 150KB). Consider rendering critical UI as **HTML/CSS instead of an image** where feasible — sharper, lighter, and no CLS.

---

## 7. Technical delivery — formats

**Pipeline (2026): AVIF first, WebP second, JPEG fallback.** AVIF is ~50% smaller than JPEG and 20–50% smaller than WebP at matched perceptual quality, and supports HDR/wide-gamut. WebP has ~96–97% support (safe as a sole modern format for most sites); AVIF ~93–95% (always give it a WebP/JPEG fallback). Treat **JPEG XL as progressive enhancement only** (Safari default; Chrome/Firefox behind flags in 2026) — do not make it a primary format.

### 7.1 Encode quality targets

| Format | Quality | Notes |
|---|---|---|
| **AVIF** | `q 60–80` (65–75 typical), CQ ~23–32, effort/speed ~6 | Primary. Lower CQ = higher quality. |
| **WebP** | `q 75–85` (aim 80–85 for photos) | Fallback #1. Curve is inconsistent — err higher. |
| **JPEG** | `q ~80` (mozjpeg) | Universal fallback only. |
| Rough parity | JPEG q60 ≈ WebP q65 ≈ AVIF q50 | For sanity-checking exports. |

Animated content: use **animated WebP**, not animated AVIF (AVIF encodes too slowly to be practical in 2026). For anything beyond a few seconds, prefer a real video (`<video>` with a poster) over an animated image.

### 7.2 The canonical `<picture>` snippet

```html
<picture>
  <source
    type="image/avif"
    srcset="hero-640.avif 640w, hero-1024.avif 1024w, hero-1600.avif 1600w, hero-2560.avif 2560w"
    sizes="(max-width: 768px) 100vw, 1200px" />
  <source
    type="image/webp"
    srcset="hero-640.webp 640w, hero-1024.webp 1024w, hero-1600.webp 1600w, hero-2560.webp 2560w"
    sizes="(max-width: 768px) 100vw, 1200px" />
  <img
    src="hero-1024.jpg"
    srcset="hero-640.jpg 640w, hero-1024.jpg 1024w, hero-1600.jpg 1600w"
    sizes="(max-width: 768px) 100vw, 1200px"
    width="1600" height="900"
    alt="A med spa owner reading a booking confirmation on her phone."
    fetchpriority="high" decoding="async" />
</picture>
```

> `<picture>` is for **format fallback or art-direction crops only.** For a single image at varying sizes, a plain `<img srcset sizes>` is enough — don't reach for `<picture>` unless you need different formats or different crops.

---

## 8. Technical delivery — responsive sizing & budgets

- **Generate 3–5 variants** stepped by file size, not device names. Typical widths: **640 / 768 / 1024 / 1280 / 1600 / 1920 / 2560**. **Cap at ~2560px** — 2× DPR covers virtually all content; do not target 3×.
- Always pair `srcset` (width `w` descriptors) with a **`sizes`** attribute. Without `sizes`, the browser downloads the largest candidate on every device.
- Use `x` descriptors **only** for fixed-size images (density switching), e.g. logos, avatars.
- **All variants of one image must share the same aspect ratio** (or CLS on swap).

### 8.1 Per-role weight budgets (gzipped/binary transfer)

| Role | Max KB | Format | Loading | Notes |
|---|---|---|---|---|
| **Hero / LCP** | **< 150KB** | AVIF | eager + `fetchpriority="high"` | Exactly **one** `fetchpriority="high"` per page. |
| Full-width section | < 120KB | AVIF | lazy below fold | |
| Card / feature | < 80KB | AVIF | lazy | |
| **Thumbnail / avatar** | **< 40KB** | AVIF/WebP | lazy | Small crops; often `x` descriptors. |
| Logo / icon (raster) | < 15KB | SVG preferred | — | Prefer SVG; see [`iconography.md`](./iconography.md). |
| OG / social share | < 300KB (1200×630) | PNG/JPEG | n/a (meta) | Not on critical path. |

**Page-level guardrails** (from project standards): total initial transfer **< 1MB**, LCP **≤ 2.5s**, CLS **≤ 0.1**.

### 8.2 Aspect ratios

| Use | Ratio | Notes |
|---|---|---|
| Hero (desktop) | 16:9 or 3:2 | Reserve space; scrim for text. |
| Hero (mobile art-direction crop) | 4:5 or 1:1 | Use `<picture>` to swap crop. |
| Feature / card | 4:3 or 3:2 | Consistent across a grid. |
| Portrait / testimonial | 1:1 or 4:5 | Faces framed, headroom balanced. |
| Mobile chat/SMS screenshot | 9:16 | Legible UI. |
| OG image | 1200×630 (1.91:1) | Fixed; see [`../seo/`](../seo/). |

---

## 9. Loading & performance rules

- **LCP image:** eager (no `loading="lazy"`), `fetchpriority="high"`, `decoding="async"`. Optionally add a responsive `<link rel="preload" as="image" imagesrcset sizes>` in `<head>`. **Never lazy-load the LCP/above-the-fold image** — it adds ~500ms+ and trips a Lighthouse warning.
- **Below-fold images:** `loading="lazy"` + `decoding="async"` (+ optional `fetchpriority="low"` to free bandwidth for the LCP). Chrome pre-fetches lazy images ~1250–2500px before the viewport, so they're ready on scroll.
- **CLS:** always set `width` + `height` (or CSS `aspect-ratio`). Pair with CSS `img { max-width: 100%; height: auto; }`. **Never** use CSS `width: auto` — it overrides the reserved-space calculation.
- **Caching:** serve fingerprinted image filenames with `Cache-Control: max-age=31536000, immutable`. Don't double-compress already-compressed AVIF/WebP payloads (skip Brotli/Gzip on them).
- **CDN option:** an image CDN that negotiates format on the `Accept` header can replace hand-authored `<picture>` sources — still enforce the same budgets and `sizes`.

---

## 10. Alt text — informative vs decorative

Every `<img>` needs an `alt` attribute. The only question is **whether it carries information.**

| Type | `alt` value | Rule |
|---|---|---|
| **Informative** | Concise, specific description | Describe *what matters here*, not "image of". Convey the meaning the sighted user gets. |
| **Decorative** | `alt=""` (empty, present) | Background textures, duotone dividers, pure-mood shots that repeat nearby text. Empty alt makes screen readers skip it. |
| **Functional** (image is a link/button) | Describe the **destination/action** | e.g. "Book a demo", not "calendar icon". |
| **Text in image** | Include the exact text | Avoid text-in-images; if unavoidable, the alt must contain it verbatim. |
| **Complex** (chart/dashboard) | Short alt + longer description nearby | Summarize the takeaway in `alt`; put detail in adjacent prose or `aria-describedby`. |

**Alt-text do/don't**

- Do keep it **under ~125 characters**; lead with the meaningful subject.
- Do write in brand voice for informative images (clear, human, second person where natural).
- Don't start with "Image of…" / "Picture of…" — screen readers already announce it.
- Don't stuff keywords; alt is for accessibility first, SEO second.
- Don't leave `alt` **missing** — a missing attribute (screen reader may read the filename) is worse than an empty one. Decorative = `alt=""`, never no `alt`.

---

## 11. Pre-ship checklist (every image)

- [ ] Subject is on-brand per §1–§3 (real, warm-modern, no robot/brain clichés).
- [ ] AVIF exported at q60–80; WebP fallback at q75–85; JPEG fallback if needed.
- [ ] 3–5 responsive variants, capped at ~2560px, **same aspect ratio** across all.
- [ ] `srcset` **and** `sizes` both present (or `x` descriptors for fixed-size).
- [ ] `width` + `height` set (no CLS); CSS uses `height: auto`, never `width: auto`.
- [ ] Weight within the §8.1 role budget (hero < 150KB, thumb < 40KB).
- [ ] LCP image: eager + `fetchpriority="high"` (exactly one per page); everything else `loading="lazy"`.
- [ ] Any text-over-image uses a scrim/overlay and passes WCAG contrast (§4.1).
- [ ] `alt` decided: informative (specific) or decorative (`alt=""`), never missing (§10).
- [ ] No real customer PII visible in screenshots; placeholders used.
- [ ] Fingerprinted filename + `Cache-Control: max-age=31536000, immutable`.

---

## Related

- [`brand-guidelines.md`](./brand-guidelines.md) — master brand overview & index.
- [`iconography.md`](./iconography.md) — icon stroke/grid that illustration line weight matches; SVGO checklist.
- [`color-system.md`](./color-system.md) — canonical colour, duotone/scrim contrast rules.
- [`logo-and-usage.md`](./logo-and-usage.md) — logo on photography, OG-image export matrix.
- [`typography.md`](./typography.md) — type for captions/overlays.
- [`../accessibility/contrast-matrix.md`](../accessibility/contrast-matrix.md) — validated text-over-image pairings.
- [`../seo/`](../seo/) — OG/Twitter image wiring and dimensions.
- [`../../tokens/design-tokens.json`](../../tokens/design-tokens.json) — radius, shadow, and colour values referenced here.
- [`../../tokens/tokens.css`](../../tokens/tokens.css) — CSS custom properties consumed by code.
