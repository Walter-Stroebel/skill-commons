---
name: session-json
description: >
  Scans the current session and extracts its conceptual structure as a minimal
  JSON layout file, saved to /home/claude/session.json. Drives the mindmap skill.
  Trigger on: "extract session", "session to json", "map to json", "dump session",
  or when the mindmap skill needs structured session data. Also trigger in diagnostic
  mode when the user says "diagnose", "show json", or "analyse session structure".
---

# Session → JSON Skill

Extracts topology only. The session is always available — don't clone it into JSON.
JSON is a layout contract for the renderer, nothing more.

---

## Step 1 — Scan

Read the session. Find:
- One **root** — dominant subject, 2–5 words
- 3–7 **branches** — major concept clusters, each 2–4 words
- 0–4 **children** per branch — sub-concepts worth showing, 2–4 words each

### What earns a node

- Recurred or organised meaning around it
- A decision reached or an artefact produced
- An unresolved tension worth surfacing

### What doesn't earn a node

- Mentioned once in passing
- A joke or aside
- Anything that is just a restatement of its parent

Max depth: root → branch → child. No grandchildren.

---

## Step 2 — Self-review before writing

For each node ask: **does this earn its place, or am I just cloning the session?**
Merge weak nodes into their nearest strong parent. Cut anything that fails the test.

---

## Step 3 — Write JSON

Minimal schema. No extra keys.

```json
{
  "root": "string",
  "branches": [
    {
      "id": "b0",
      "label": "string",
      "state": "expanded",
      "children": [
        { "id": "b0c0", "label": "string" }
      ]
    }
  ]
}
```

ID convention: branches `b0`, `b1` ... — children `b0c0`, `b0c1` ...
`state` on branches only: `"expanded"` or `"collapsed"`. Default: `"expanded"`.

Write to `/home/claude/session.json`. Verify write succeeded.

---

## Step 4 — Report

### Normal mode
One line: branch count, total node count, path written.

### Diagnostic mode
Triggered by: "diagnose", "show json", "analyse".
Print the JSON in a fenced code block, then rate the extraction honestly:
which nodes earn their place, which are noise, what's missing.
