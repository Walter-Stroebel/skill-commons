---
name: mindmap
description: >
  Reads /home/claude/session.json and renders it as an interactive SVG mind map.
  Trigger on: "mind map", "map this", "mindmap", "show the map", "map the session".
  On expand/collapse requests ("expand Branch A", "collapse b2"), reload the JSON,
  update the relevant branch state, rewrite the file, re-render. If session.json
  does not exist, invoke the session-json skill first.
---

# Mind Map Skill

Reads session.json → runs layout.py → emits SVG in HTML wrapper.
No external dependencies. No manual coordinate math — Python does all of it.

---

## Coordinate system — locked rule

Everything is screen coordinates: y=0 is top, y increases downward.
layout.py handles all trig and outputs screen-space coords directly.
Never flip, never negate, never describe positions in cartesian terms.
"Top" = low y. "Bottom" = high y. Always. Everywhere.

---

## Step 1 — Load and detect intent

Read `/home/claude/session.json`. If missing, stop and invoke session-json skill.

Detect intent:
- **Fresh map** — "mind map", "map this", "show the map"
- **Expand** — "expand [label or id]" → set that branch `state: "expanded"`, rewrite JSON
- **Collapse** — "collapse [label or id]" → set that branch `state: "collapsed"`, rewrite JSON

After any state change, rewrite session.json before running layout.

---

## Step 2 — Run layout.py

```bash
python /home/claude/mindmap-skill/mindmap/layout.py /home/claude/session.json
```

Parse the full output. Use:
- `coords[id].x/y/w/h` — rect placement
- `coords[id].cx/cy` — edge endpoints and text anchoring
- `viewbox_height` — SVG viewBox height
- `font_title` — scaled title font size (use this, not hardcoded 14px)
- `font_sub` — scaled subtitle font size (use this, not hardcoded 11px)
- `warnings` — log them; abort if overlaps are present

**Do not compute positions yourself. Do not hardcode font sizes.
Trust all numbers from layout.py.**

### What layout.py does (do not re-implement)
- Places branches at even angles, -90° offset (first branch points up)
- Places children in angular gaps between spokes, not on the spoke itself
- Two children per branch: one each side into adjacent gaps, staggered radially
- gap_frac scales with branch count — more branches = tighter angular spread
- scale-to-fit: entire layout scaled so it fits W=680 with MARGIN=48
- font_title and font_sub are pre-scaled to match node sizes
- Overlap checker: warnings array is empty if clean, lists pairs if not

---

## Step 3 — Emit SVG

Output this line first as markdown:

> ⏳ Building map — nodes are clickable once rendered. 🗺️

Then `show_widget`. **HTML wrapper mandatory** — raw SVG causes script to render as text.

### Colour system — explicit, no class magic

Do NOT use `c-*` colour classes on nodes. They don't compose reliably with scaled
font sizes and break in dark mode. Instead use the explicit CSS pattern below.

Define these classes in a `<style>` block inside `<defs>`:

```css
.nr { fill: #7F77DD; stroke: #534AB7; }   /* root — purple mid */
.nb { fill: #1D9E75; stroke: #0F6E56; }   /* branch — teal mid */
.na { fill: #BA7517; stroke: #854F0B; }   /* branch — amber (constraint) */
.nd { fill: #E24B4A; stroke: #A32D2D; }   /* branch — red (warning/scary) */
.nc { fill: var(--color-background-secondary); stroke: var(--color-border-secondary); }  /* child — neutral */
@media (prefers-color-scheme: dark) {
  .nr { fill: #3C3489; stroke: #AFA9EC; }
  .nb { fill: #085041; stroke: #5DCAA5; }
  .na { fill: #633806; stroke: #EF9F27; }
  .nd { fill: #791F1F; stroke: #F09595; }
}
.tt { fill: var(--color-text-primary); font-weight: 500; }   /* child title */
.ts { fill: var(--color-text-secondary); }                   /* child subtitle */
.tw  { fill: #ffffff; font-weight: 500; }                    /* coloured node title */
.tw2 { fill: rgba(255,255,255,0.75); }                       /* coloured node subtitle */
```

Coloured nodes (root, branches): white text always — `.tw` title, `.tw2` subtitle.
Child nodes (neutral): CSS-variable text — `.tt` title, `.ts` subtitle.

### Structure

```
<style>
.vn{cursor:pointer;transition:opacity .15s;}
.vn:hover{opacity:.72;}
</style>
<svg width="100%" viewBox="0 0 680 {viewbox_height}" role="img">
<title>Mind map — {root label}</title>
<desc>...</desc>
<defs>
<marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</marker>
<style>
[colour classes as above]
</style>
</defs>
[EDGES before nodes]
[ROOT node]
[BRANCH nodes]
[CHILD nodes]
</svg>
<script>
(function(){
  var g=function(id){return document.getElementById(id);};
  [one addEventListener per node]
})();
</script>
```

### Node templates

Root:
```svg
<g id="n-root" class="vn">
<rect class="nr" x="{x}" y="{y}" width="{w}" height="{h}" rx="8" stroke-width="0.5"/>
<text class="tw"  font-size="{font_title}" x="{cx}" y="{cy-7}" text-anchor="middle" dominant-baseline="central">{label}</text>
<text class="tw2" font-size="{font_sub}"   x="{cx}" y="{cy+8}" text-anchor="middle" dominant-baseline="central">{subtitle}</text>
</g>
```

Branch (pick .nb / .na / .nd by meaning):
```svg
<g id="n-{id}" class="vn">
<rect class="nb" x="{x}" y="{y}" width="{w}" height="{h}" rx="6" stroke-width="0.5"/>
<text class="tw"  font-size="{font_title}" x="{cx}" y="{cy-6}" text-anchor="middle" dominant-baseline="central">{label}</text>
<text class="tw2" font-size="{font_sub}"   x="{cx}" y="{cy+7}" text-anchor="middle" dominant-baseline="central">{subtitle}</text>
</g>
```

Child (neutral, high contrast at any size):
```svg
<g id="n-{id}" class="vn">
<rect class="nc" x="{x}" y="{y}" width="{w}" height="{h}" rx="5" stroke-width="0.5"/>
<text class="tt" font-size="{font_title}" x="{cx}" y="{cy-6}" text-anchor="middle" dominant-baseline="central">{label}</text>
<text class="ts" font-size="{font_sub}"   x="{cx}" y="{cy+7}" text-anchor="middle" dominant-baseline="central">{subtitle}</text>
</g>
```

### Branch colour guide

| Meaning | Class |
|---------|-------|
| Main flow / process | `.nb` (teal) |
| Constraint / caution | `.na` (amber) |
| Warning / scary / stop | `.nd` (red) |
| Root only | `.nr` (purple) |

Use colour to encode meaning, not sequence.

### Hard rules

- HTML wrapper mandatory. Always.
- `sendPrompt` only. Wire via `addEventListener` in one IIFE after SVG.
- Never inline `onclick` on SVG elements.
- Every connector `<line>` needs `fill="none"`.
- Arrow marker in defs, id `ar`.
- `dominant-baseline="central"` on all text.
- `stroke-width="0.5"` on all rects.
- Edges drawn before nodes.
- No comments in output.
- If layout.py warnings include overlaps: stop, do not render.

### Edges

Root → branch: `<line>` from root cx/cy to branch cx/cy.
Branch → child: `<line>` from branch cx/cy to child cx/cy.
All: `stroke="var(--color-border-secondary)"` `stroke-width="0.5"` `marker-end="url(#ar)"` `fill="none"`.

### Click questions

Generate from label + session context at render time. Don't pre-bake.
Plain language. No jargon. Red nodes get reassuring "what do I do if..." questions.

---

## Step 4 — After

One sentence: what the map shows, which node to click first.

---

## Lessons learned (do not repeat these mistakes)

- **Hub-and-spoke is not a mind map.** Children must fan into gaps between spokes.
- **Fixed position tables break.** layout.py computes positions; never hardcode them.
- **Font sizes must scale.** Use font_title/font_sub from layout.py, not hardcoded values.
- **Outer node font_sub goes down 1pt extra** — at small scales subtitles are optimistic; layout.py already applies a -1pt offset via FONT_SUB=11 (not 12).
- **Overlap checker is load-bearing.** Always check warnings before rendering.
- **gap_frac must shrink with more branches** or children collide at the bottom.
- **scale-to-fit after placement**, not before — place at natural radii, then scale.
- **Never use c-* colour classes on nodes.** They break with scaled fonts and dark mode. Use explicit CSS classes with @media dark mode overrides (see colour system above).
- **Child nodes need neutral fills.** Coloured fills lose contrast at small font sizes. `.nc` class + CSS variable text is readable at any size in any mode.
- **White text on coloured nodes.** `.tw` / `.tw2` — always white, regardless of mode.
- **Screen coords only, always.** y=0 top. Never describe "bottom" when you mean high-y.
- **HTML wrapper non-negotiable.** Raw SVG silently breaks script execution.
