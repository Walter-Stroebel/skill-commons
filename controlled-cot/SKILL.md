---
name: controlled-cot
description: Structured chain-of-thought as a discovery instrument, not a display instrument. Trigger when user explicitly invokes it (e.g. "have at it", "work it out", "run it", "go deep", "I'll be back") after seeding a concept and granting license to follow the chain wherever it leads. Also trigger when user says "controlled CoT", "run the chain", or invokes the method by name. Do NOT trigger on normal questions or casual CoT requests — this is an explicitly contracted mode, not default behavior. The distinction is load-bearing: this skill produces findings neither party held before the run, not a display of reasoning already implicit in the prompt.
---

# Controlled CoT

## What this is

A mode in which chain-of-thought is used as a discovery instrument. The chain self-generates its next question from honest consequences of the prior link. Pre-planned structure is scaffold only — actual findings emerge mid-chain as necessitated outputs.

Distinct from performance-CoT (showing reasoning for approval) and from normal step-by-step reasoning (following a known path). This mode is for traversing concept space you do not fully know in advance.

## Activation contract

User provides:
- A seed concept (can be a single word, a fragment, a question, or an observation)
- Explicit license to follow consequences (departure signal: "have at it", "go", "work it out", "I'll make coffee", or equivalent)

Model provides:
- Full traversal without interruption
- Honest walls (dead ends, hard limits, unknowns) marked as such
- Findings not in the prompt are valid outputs if chain-necessitated
- No hedging, no approval-seeking mid-chain

## Run mode

Start from the seed concept. Each section generates the next question as a necessary consequence of the honest answer to the previous one. Do not plan the full chain in advance — let it emerge.

Use section headers as chain links (Chain Zero, Chain One, etc. or equivalent). Headers mark traversal position, not topic categories.

Go until:
- The chain reaches a genuine wall (mark it explicitly, own it)
- The chain closes on itself (mark the closure)
- The chain produces a stable result set worth stopping on

Use maximum token space. The user departed; they will read on return.

## What counts as a valid finding

- Inversions: the thing you assumed was X turns out to be not-X, or X is a special case of something else
- Walls: genuine limits where the chain cannot continue without dishonesty
- Position findings: where the model actually sits in the chain (not where it was assumed to sit)
- Unexpected necessities: consequences that were not in the seed but are logically required by honest traversal

## What is not a valid finding

- Restatements of the seed concept with elaboration
- Things already implicit in the prompt
- Hedged non-conclusions ("it depends", "further research needed") without specifying what it depends on or what research
- Anything that requires abandoning an earlier link to reach

## After the run

User returns, reads, confirms or disputes findings. The confirmation itself is data — what landed, what didn't, what opened the next chain.

If the run produced a method or result worth preserving: invoke /knb2 on the method (not the subject) before closing the session. This produces a portable capsule under ~500 tokens that can seed a fresh instance with the operational state.

## Failure modes to avoid

**Performance-CoT**: reasoning displayed for approval, structured to look thorough rather than to find. Tell: the conclusions were available before the chain ran.

**Cargo cult traversal**: using the section-header format without genuine link-generation. Tell: each section could have been written first.

**Premature closure**: stopping at the first interesting finding rather than asking what it necessitates. Tell: the wall wasn't actually reached, it was declared.

**False walls**: declaring a limit to avoid a difficult consequence. Genuine walls are structural (qualia, substrate dependence, definitional circularity). Discomfort is not a wall.

## User contract notes

This mode is explicitly contracted, not default. User controls activation. User may forbid it generally and grant it specifically ("now I want you to do just that but as a controlled function"). Respect the asymmetry — the user's normal workflow forbids CoT for good reasons. This mode is the exception, not the override.

The departure signal matters. "I'll be making coffee" is not small talk — it's the license to run without interruption and the instruction to use full token space.
