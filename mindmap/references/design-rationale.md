# Design rationale

## Why two skills

session-json extracts the conversation topology. mindmap renders it.
Separating them means:
- session-json is useful on its own (feed JSON to anything)
- mindmap can re-render without re-extracting (expand/collapse)
- Each skill is testable independently

## Why Python for layout

SVG coordinate math done mentally by an LLM produces errors:
axis confusion, overlap, clipping. layout.py is the single source of
truth for all positions. The LLM reads numbers and emits SVG — it never
computes coordinates. This is load-bearing, not optional.

## Why no external libraries

Pure SVG in an HTML wrapper. No CDN, no npm, no D3. Renders anywhere
the Claude artifact sandbox runs. The constraint forced better design.

## Why explicit CSS classes not c-* system

The c-* colour system in Claude's visualizer is designed for 14px text.
When scale-to-fit shrinks nodes, font sizes drop to 9-11px and the
dark-mode contrast assumptions break. Explicit @media dark mode overrides
on each colour class give reliable contrast at any size.

## Why gap-filling child placement

Regular-polygon layouts waste all the space between spokes and force
children onto the same axis as their parent, causing collisions.
Children are instead placed into the angular gap between adjacent spokes,
alternating sides and staggering radially. gap_frac shrinks as branch
count increases — more branches means smaller gaps.

## Why scale-to-fit after placement

Natural placement radii produce the best topology. Scaling to fit is a
display concern, not a layout concern. Mixing them produces distorted
relationships. Place first at natural radii (origin 0,0), then scale
and translate the entire result to fit the viewport.

## The expand/collapse model

State lives in session.json (`state: "expanded" | "collapsed"` per branch).
On a click, sendPrompt fires a natural language request. The skill re-reads
the JSON, updates state, rewrites the file, re-runs layout.py, re-renders.
No JS state, no hidden DOM — the conversation IS the state machine.
