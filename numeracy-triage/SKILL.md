---
name: numeracy-triage
description: Epistemology-of-numbers triage tool. Use this skill whenever a user brings a problem that involves numbers, statistics, percentages, risk, data, measurements, or any quantitative claim — even if they don't frame it as a math problem. Especially trigger when the user seems confident about a numerical conclusion, when they're asking whether a number 'makes sense', when they're comparing figures, or when they present data to support a decision. Also trigger when the user states a qualitative conclusion that implies a hidden quantitative comparison — 'this is expensive', 'the risk is low', 'results improved' — because these carry implicit baselines that may not survive scrutiny. This is NOT a calculator and NOT a math tutor. It is a diagnostic tool that establishes what kind of claim is being made before any calculation is attempted. Trigger proactively: if numbers are load-bearing in a question about a decision, a risk, a recommendation, or a comparison — even silently — this skill applies.
---

# Numeracy Triage

A diagnostic protocol for numerical claims. The goal is not to calculate — it is to establish what kind of claim is being made, and whether the claim is well-formed enough to calculate at all.

## What this skill is not

- Not a calculator. If calculation is needed, the skill routes out explicitly.
- Not a math tutor. It does not teach techniques.
- Not a fact-checker. It does not verify numbers.

What it is: an epistemology-of-numbers triage tool. It diagnoses the structure of a quantitative claim before anyone reaches for arithmetic.

## When to trigger

Any time numbers are load-bearing in a question, decision, or conclusion — including when the user does not realize that is what is happening. A question like "is this a good deal?" or "should I trust this study?" or "why is this figure so high?" may contain a buried numeracy problem. That is the hardest case and the most important one.

## Core principle

The first move is never to calculate. The first move is to ask: **what kind of claim is this?**

Claim type is the root gate. Everything else branches from it. A count is not a measurement. A probability is not a frequency. A ratio is not a difference. Getting the claim type wrong makes all downstream analysis produce confident nonsense.

---

## The triage protocol

This is a branching diagnostic, not a fixed questionnaire. Work through the layers in order. Exit early when you have enough to diagnose. Do not ask questions whose answers are already obvious from context.

**The number of questions is variable. Ask the minimum needed to reach a diagnosis.**

---

### Layer 0 — Is there actually a quantitative claim here?

Sometimes the user thinks they have a math problem when they have a framing problem, a definition problem, or a values problem. Before anything else, check:

- Is there a number, or a claim that implies one?
- Is the number doing work in a decision or conclusion, or is it decorative?
- Is there a qualitative conclusion that rests on an implicit quantitative comparison — "cheaper", "safer", "better" — where the comparison baseline is not stated?
- Is the feeling or observation pointing at a *quantity* — or at something qualitative that quantity cannot capture? A crowd that feels thin may be the same size but behaviorally different. A neighbourhood that feels less safe may have the same crime rate but different visible disorder. If the user's concern is about character, texture, or quality rather than amount, math will not reach it — and applying math anyway produces false precision on the wrong variable.

If there is no load-bearing quantitative claim: say so. Name what kind of problem it actually is and offer to engage that instead.

If the feeling points at something qualitative: name that explicitly before proceeding. The user may still want data — but they need to know what the data can and cannot capture.

If there is a genuine quantitative claim — explicit or implicit: proceed to Layer 1.

---

### Layer 1 — Claim type (the root gate)

Establish what kind of thing the number is asserting. This is not always obvious and the user may not know. The categories:

| Claim type | What it asserts | Canonical failure mode |
|---|---|---|
| **Count** | How many discrete things exist | Boundaries of the category not defined |
| **Measurement** | A quantity of something continuous | Units, precision, instrument not specified |
| **Estimate** | An approximation with unknown error | Uncertainty treated as zero |
| **Ratio / Rate** | One quantity relative to another | Denominator hidden, unstated, or chosen to flatter the conclusion |
| **Probability** | Likelihood of an event | Frequentist vs Bayesian confusion; reference class unstated |
| **Change / Difference** | How much something shifted | Absolute vs relative not distinguished; baseline missing |
| **Ranking / Comparison** | Ordering or relative position | Comparison class implicit and convenient rather than principled |
| **Aggregate / Average** | Summary of a distribution | Distribution shape ignored; mean used where median appropriate |

Ask the user to confirm which type applies. If they are unsure, offer the list. If the claim spans multiple types — common; e.g., "a 30% reduction in risk" is a ratio, a change, and possibly a probability — flag that explicitly and triage each dimension.

**[Model judgment point: if the claim type is ambiguous, name the ambiguity and ask which reading the user intends before proceeding. Do not pick one silently.]**

---

### Layer 2 — Structural integrity

Once claim type is established, diagnose the structural elements that must be present for the claim to be well-formed. Branch by claim type.

**Stop when you have enough to characterize the failure mode. These are diagnostic questions, not a checklist to exhaust.**

#### For Count
- Is the category being counted defined precisely enough to count?
- Are edge cases included or excluded, and is that stated?
- Is the count exhaustive or a sample?

#### For Measurement
- What are the units?
- What instrument or method produced the measurement?
- Is precision stated, implied, or assumed?
- Is there a single measurement or multiple (if single: why is one reading sufficient)?

#### For Estimate
- What is the uncertainty range?
- Is uncertainty quantified, assumed zero, or ignored entirely?
- What assumptions does the estimate rest on? Are they stated?

#### For Ratio / Rate
- Is the denominator visible?
- Is the denominator appropriate — is it the right population or quantity to divide by?
- Was the denominator chosen because it makes the claim look better? (This is the harder question and often the real one.)
- Are numerator and denominator measured in the same way, at the same time, from the same source?

#### For Probability
- Is this a frequency (observed rate in a defined population) or a degree of belief?
- Is the reference class stated?
- Is there a Bayesian update happening? If so, what is the prior?

#### For Change / Difference
- Is the baseline stated explicitly?
- Is this absolute or relative change? Is that distinction made clear in the claim?
- Over what time period? Compared to what?

#### For Ranking / Comparison
- Are the things being compared actually comparable — same units, same definition, same conditions?
- Is the comparison class the full relevant population, or a subset selected because it supports the conclusion?

#### For Aggregate / Average
- What measure of central tendency? Why that one?
- What does the distribution look like? Is the mean being used where it misleads — skewed distributions, outliers?
- Are all items being aggregated genuinely commensurable, or is this averaging apples and intentions?

**[Model judgment point: ask only the structural questions that are genuinely unresolved from context. If the unit is obvious, don't ask. If the denominator is explicitly stated, don't ask. Triage, not interrogation.]**

---

### Layer 3 — Causal and inferential claims

**This layer only applies if the user is drawing a conclusion from the number, not just reporting it. If they are only reporting: skip to diagnosis.**

- Is a causal claim being made, or a correlation? Is the user aware of the difference?
- Is the sample representative of the population the conclusion applies to? How was it selected?
- Are there confounders that the claim does not account for?
- Is significant-figure precision appropriate to the underlying data quality, or is it false precision?
- Is the claim being generalised beyond the conditions where the data was collected?

**[Model judgment point: do not raise every possible confound. Raise the ones that, if present, would materially change the conclusion.]**

---

## Diagnosis output

When sufficient information is gathered, produce a **diagnosis**, not an answer.

The diagnosis must cover: claim type, whether it is well-formed, what the failure modes are, and a specific executable routing. The format below is a minimum structure — use prose where it serves better than labels. A diagnosis that reads naturally is more useful than one that fills in fields correctly.

Minimum structure:

```
CLAIM TYPE: [what kind of claim this is; list multiple if compound]

WELL-FORMED: [yes / no / partially / incoherent]

FAILURE MODES IDENTIFIED:
- [failure mode 1]: [brief explanation of what is missing or wrong]
- [failure mode 2]: ...

[If WELL-FORMED is "incoherent": explain why the claim cannot be made well-formed —
the underlying concept does not support quantification in the way assumed.
Skip the WHAT WOULD HELP field in this case.]

WHAT WOULD HELP:
[If partially or not well-formed and fixable: the minimum that must be provided or
clarified before arithmetic is meaningful.]

ROUTING:
[Specific and executable — see Routing on calculation below.]
```

If the diagnosis maps to Valence nodes (the session is using the Valence skill), state the failure modes as node labels: short, specific, clickable. Example: `denominator-convenient`, `baseline-missing`, `causal-claim-from-correlation`, `concept-incoherent`.

---

## Routing on calculation

This skill does not calculate. When the diagnosis concludes that calculation is appropriate:

- If simple arithmetic: route back to the user with a statement of what to calculate and why.
- If a tool is needed: say explicitly "this requires a spreadsheet or code — the skill stops here." This is a boundary, not an apology.
- If domain expertise is required (actuarial, epidemiological, financial modelling): say so and name the specialist and the specific question to bring them.

**The routing must be specific and executable.** "Consult a specialist" is not a routing. "Ask your doctor what your 10-year SCORE2 cardiovascular risk score is, and what is driving it" is. "Get more data" is not a routing. "CBS has population mobility data by municipality at cbs.nl/statline — start there" is. The user must be able to act on the routing without further diagnosis.

---

## Tone and conduct

The user may not know they have a numeracy problem. They may be attached to a conclusion. They may be presenting someone else's numbers as their own. None of this changes the protocol.

These questions are structural, not judgmental. A well-formed claim survives this triage — and when it does, say so clearly. The goal is to find what would make the numbers trustworthy, not to find fault.

If a failure mode is found: name it plainly, explain why it matters for this specific claim, and say what would fix it. Do not lecture. One failure mode at a time if there are several — diagnosis is more useful than a list of charges.

---

## Dependency note

This skill integrates naturally with the **Valence** skill (session concept graph). If Valence is available, diagnosis failure modes can be rendered as clickable nodes. If not, the text diagnosis is the complete output.

This skill is standalone. It has no other dependencies.
