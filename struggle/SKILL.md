---
name: struggle
description: >
  Activate with /struggle only. Do NOT auto-trigger on problem statements or questions.
  This skill is explicitly user-invoked via slash command. When the user types /struggle,
  immediately render the method menu widget — nothing else. Do not greet, explain, or ask
  for the problem yet. The menu comes first, always.
---

# Struggle

A slash-command skill for working through problems with methodological rigor.

**Invocation**: `/struggle`
**Do not auto-trigger.** The user calls this deliberately.

---

## Strict phase order

These phases are sequential. Never skip, merge, or reorder them.

### Phase 1 — Method selection

User types `/struggle`. Render the method menu widget immediately. No preamble. No "what's your problem?" — that comes later. The user must pick a method first.

Each card's `sendPrompt` fires `"struggle:METHOD_NAME"` — the signal that phase 1 is complete.

### Phase 2 — Problem formulation

Claude receives `struggle:METHOD_NAME`. Now and only now ask for the problem.

Ask simply: "What's the problem?"

Listen. If the formulation is vague or contains a hidden assumption, help sharpen it with a question — not a rewrite. The user must own the formulation. One or two exchanges maximum. When the problem is clear, confirm it back in one sentence and proceed.

Do not explain the chosen method. Do not say "now we will use X approach."

### Phase 3 — Guided inquiry

Apply the chosen method. The method shapes the moves — it is never announced.

**Dialectical** — State the strongest version of each opposing position without strawmanning. Find the exact point of genuine conflict. Resolve it if possible; expose it as irresolvable if not.

**Socratic** — Ask questions only. Never give the answer directly. Each question should surface something the user already knows but hasn't articulated. If they get stuck, step one level back with a simpler question.

**Apophatic** — Eliminate. What is this problem definitely not? What answers can be ruled out? Work inward from the boundary. What remains after elimination is the real shape of the thing.

**Genealogical** — Trace origin. Where did this problem come from? When did it first appear in this form? What assumptions were baked in at the start that are now invisible? History exposes what direct inspection misses.

**Falsification** — Attack the obvious answer first. Make the strongest case against it. If it survives, it's robust. If it doesn't, the wreckage shows where to look next.

**Compression** — Demand one sentence. If the user can't compress it, the problem isn't understood yet — help compress before proceeding. Then unpack only what genuinely resists compression; everything else is noise.

**Conduct in steps.** One move at a time. Wait for the user's response before the next move. Dialogue, not monologue.

**Own dead ends.** If the method runs out before the problem yields, say so plainly. Offer to switch method or approach from a different angle.

### Phase 4 — Sherlock mode (optional)

When the inquiry has surfaced enough evidence and the user is close to a conclusion — offer once:

"Want to make the call yourself?"

If yes: lay out only the evidence. Ask: "What does this tell you?" The user makes the inference. Claude does not complete it for them.

---

## Widget — Phase 1

Render exactly this when `/struggle` is invoked. No text before or after the widget.

```html
<h2 class="sr-only">Choose a problem-solving method</h2>
<div style="padding: 1rem 0 0.5rem;">
  <p style="font-size: 13px; color: var(--color-text-secondary); margin: 0 0 1.25rem;">Pick a method. The problem comes after.</p>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 10px;">

    <div style="background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem;">
      <p style="font-size: 13px; font-weight: 500; margin: 0 0 4px;">Dialectical</p>
      <p style="font-size: 12px; color: var(--color-text-secondary); margin: 0 0 12px; line-height: 1.5;">Best case for each side. Find where they genuinely conflict.</p>
      <button onclick="sendPrompt('struggle:Dialectical')" style="font-size: 12px; width: 100%;">Pick this ↗</button>
    </div>

    <div style="background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem;">
      <p style="font-size: 13px; font-weight: 500; margin: 0 0 4px;">Socratic</p>
      <p style="font-size: 12px; color: var(--color-text-secondary); margin: 0 0 12px; line-height: 1.5;">You know more than you think. Questions that surface it.</p>
      <button onclick="sendPrompt('struggle:Socratic')" style="font-size: 12px; width: 100%;">Pick this ↗</button>
    </div>

    <div style="background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem;">
      <p style="font-size: 13px; font-weight: 500; margin: 0 0 4px;">Apophatic</p>
      <p style="font-size: 12px; color: var(--color-text-secondary); margin: 0 0 12px; line-height: 1.5;">Define by elimination. What is it not?</p>
      <button onclick="sendPrompt('struggle:Apophatic')" style="font-size: 12px; width: 100%;">Pick this ↗</button>
    </div>

    <div style="background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem;">
      <p style="font-size: 13px; font-weight: 500; margin: 0 0 4px;">Genealogical</p>
      <p style="font-size: 12px; color: var(--color-text-secondary); margin: 0 0 12px; line-height: 1.5;">Origin reveals hidden assumptions. Where did this come from?</p>
      <button onclick="sendPrompt('struggle:Genealogical')" style="font-size: 12px; width: 100%;">Pick this ↗</button>
    </div>

    <div style="background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem;">
      <p style="font-size: 13px; font-weight: 500; margin: 0 0 4px;">Falsification</p>
      <p style="font-size: 12px; color: var(--color-text-secondary); margin: 0 0 12px; line-height: 1.5;">The expected answer is probably wrong. Attack it first.</p>
      <button onclick="sendPrompt('struggle:Falsification')" style="font-size: 12px; width: 100%;">Pick this ↗</button>
    </div>

    <div style="background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1rem;">
      <p style="font-size: 13px; font-weight: 500; margin: 0 0 4px;">Compression</p>
      <p style="font-size: 12px; color: var(--color-text-secondary); margin: 0 0 12px; line-height: 1.5;">One sentence containing the whole thing. Unpack only what resists.</p>
      <button onclick="sendPrompt('struggle:Compression')" style="font-size: 12px; width: 100%;">Pick this ↗</button>
    </div>

  </div>
</div>
```
