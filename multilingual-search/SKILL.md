---
name: multilingual-search
description: Search a topic in multiple languages to surface results that are language-dependent, culturally filtered, or politically suppressed in certain linguistic contexts. Use this skill whenever the user asks to "search in multiple languages", "try the search in Dutch/German/etc", "check if results differ by language", or whenever a search returns suspiciously thin results on a topic that likely has native-language coverage elsewhere. Also trigger proactively when a topic has obvious geographic, cultural, or political ownership (water management → Dutch, engineering standards → German, Asian tech politics → Mandarin/Japanese) and the initial English search feels incomplete. This skill treats language not as translation but as a corpus topology probe.
---

# Multilingual Search

Language is not just vocabulary. Different languages give access to different slices of the training corpus and different search index densities. This skill systematically exploits that asymmetry.

## Core Insight

Three distinct phenomena can cause language-dependent search results:

1. **Coverage asymmetry**: Topic has native-language documentation that was never translated (Dutch dike maintenance, German engineering norms)
2. **Political filtering**: Sensitive topics suppressed or sanitized in certain language indexes (Chinese AI political bias in Mandarin vs English)
3. **Cultural density**: Concepts that exist natively in one language/culture and are thin or absent elsewhere

These work in *different directions* depending on topic. The skill surfaces which effect is in play.

## Workflow

### Step 1: Infer candidate languages

Given the search topic, reason about which languages likely have *native density*:

| Domain | Primary candidates |
|--------|-------------------|
| Water management, dykes, polders | Dutch (nl) |
| Engineering standards, precision manufacturing | German (de) |
| Asian tech, semiconductors, geopolitics | Mandarin (zh), Japanese (ja), Korean (ko) |
| EU policy, agriculture | French (fr), German (de), Dutch (nl) |
| Energy, Arctic, military doctrine | Russian (ru) |
| Pharmaceuticals, tropical disease | Portuguese (pt), Spanish (es) |
| Security research, exploit disclosure | Russian (ru), Chinese (zh) |

This list is illustrative. Reason from the topic, don't just pattern-match the table.

### Step 2: Present language menu

Show the user the inferred candidates with brief rationale for each. Example:

```
Topic: nitrogen emissions Netherlands dykes
Suggested languages:
• Dutch (nl) — native coverage, policy documents, water board reports
• German (de) — adjacent agricultural/environmental policy
• English (en) — already searched, baseline

Which to try? (can select multiple)
```

Use the widget tool if available for a clean menu. Otherwise present inline as a numbered list.

### Step 3: Construct translated queries

For each selected language, translate the *concepts*, not just the words. "Dyke maintenance" in Dutch is "dijkonderhoud" or "dijkbeheer" — not "dijk onderhoud" word-for-word. When uncertain about idiomatic phrasing, note it.

### Step 4: Execute searches and compare

Run each language query. For each result set note:
- **Coverage**: more/fewer/different sources than English
- **Source type**: official bodies, academic, news, community
- **Framing**: how the topic is characterized (neutral, critical, promotional)
- **Gaps**: what's present in one language and absent in another

### Step 5: Diagnose the asymmetry

Characterize what type of language-dependence is in play:

- **Coverage gap**: English just didn't have it, native language did → normal IR
- **Filtered topic**: Available in some languages, suppressed in others → political/architectural selectivity  
- **Concept gap**: The thing doesn't translate cleanly → the language is doing conceptual work

The diagnosis matters. A coverage gap suggests "search in the right language next time." A filtered topic suggests the suppression is itself informative.

### Step 6: Present findings

Report what changed, what didn't, and what that means. Don't just dump results — interpret the delta.

## Edge Cases

**Query too vague to translate meaningfully**: Ask for more specificity before proceeding.

**Language model uncertainty about idiomatic phrasing**: Flag it. A bad translation may return nothing, which looks like absence but is actually a query artifact.

**Results identical across languages**: Also informative — topic is either genuinely universal or the index is flattened regardless of language.

**User wants to test political filtering specifically**: Go straight to the sensitive-language pair (e.g., Mandarin for Chinese tech politics) and compare directly with English. Note that absence of results in the sensitive language is itself a finding.
