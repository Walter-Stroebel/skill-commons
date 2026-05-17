# mindmap-skill

Two Claude skills that together produce interactive, session-aware mind maps
as SVG artifacts — no external dependencies, no CDN, pure SVG.

## What it does

Say "mind map this session" and Claude will:
1. Extract the current conversation's concept hierarchy as JSON
2. Compute a radial tree layout in Python (no manual coordinate math)
3. Render an interactive SVG mind map with clickable nodes that fire follow-up questions back into chat

Click any node to explore that concept. Click the root to collapse all branches.
Say "expand [branch name]" or "collapse [branch name]" to navigate.

## Skills

### session-json
Extracts the current conversation into a minimal JSON topology file at
`/home/claude/session.json`. Schema: root label + branches + children + expand/collapse state.
Useful standalone — any tool that wants a structured session summary can read it.

### mindmap
Reads session.json, runs layout.py for coordinates, emits an HTML-wrapped SVG
mind map via Claude's show_widget tool.

## Installation

Download both `.skill` files and drag them into any Claude chat, or go to
**Settings → Profile → Custom Skills** and upload them. Install session-json first.

## Usage

```
map this session
mind map
mindmap
show the map
```

Then to navigate:
```
expand What you need
collapse b3
```

## Architecture decisions

See `mindmap/references/design-rationale.md` for the full reasoning behind:
- Two-skill decomposition
- Python layout engine (layout.py)
- No external libraries
- Explicit dark-mode CSS instead of the c-* class system
- Gap-filling child placement
- Scale-to-fit after placement
- Conversation-as-state-machine expand/collapse

## Key files

```
mindmap/
├── SKILL.md          # Instructions for Claude + lessons learned
├── layout.py         # Coordinate engine — all trig lives here
└── references/
    └── design-rationale.md

session-json/
└── SKILL.md          # Extraction instructions + self-review gate
```

## Known limitations

- Static viewBox — no pan/zoom (expand/collapse via re-invocation instead)
- Max ~8 branches before layout gets tight (gap_frac compensates but has limits)
- Expand/collapse requires a round-trip through Claude (by design — state lives in conversation)

## Origin

Built in a single Claude session through iterative vibe coding. The human caught
every significant error: hub-and-spoke vs tree topology, cargo-cult JSON schema,
coordinate axis confusion, font scaling, dark mode contrast. The lessons are
documented in `mindmap/SKILL.md` under "Lessons learned" so future Claude instances
don't repeat them.
