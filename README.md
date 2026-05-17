# skill-commons

> A curated commons of LLM-agnostic skills. Plain text. No vendor lock-in.

## What this is

A curated collection of skills — structured markdown instructions that extend LLM behavior in well-defined, auditable ways.

Skills are plain text. They work on Claude, on local models, on whatever can read a markdown file and act on it. There is no SDK, no API dependency, no platform requirement. A skill is a document.

## What a skill is

A skill is a markdown file with a YAML block:

```yaml
---
name: skill-name
description: "When to use this skill and what it does."
---
```

The body contains instructions. The LLM reads it and follows them. That's the entire mechanism.

The `description` field is the trigger — it tells the model when to consult the skill. Make it specific and honest.

The format used is compatible with Claude's native skill system and should be portable to any LLM that accepts markdown in context.

## Threat model

Skills are instructions. A malicious skill is a prompt injection vector. This commons is curated by a single maintainer for that reason. There is no open contribution pipeline. Submissions are reviewed through wetware, not tooling, because natural language intent cannot be statically analyzed.

If you want to submit a skill: open an issue. It will be read. It may be declined. No explanation owed.

Do not install skills from untrusted sources. The format is portable precisely because it has no sandbox.

## Current skills

| Skill | What it does |
|---|---|
| [enshittification-detector](skills/enshittification-detector/SKILL.md) | Filters technology claims, vendor narratives, and consensus recommendations for hidden dependencies, mismatched threat models, and commercial interests dressed as best practice |
| [false-binary](skills/false-binary/SKILL.md) | Detects false either/or framings and proposes the both/sequence/transcendence exit |

## How to use

Copy the relevant `SKILL.md` to wherever your LLM runtime expects skills. Include it in context. The model will use it when the description matches.

On Claude.ai: Settings → Skills → install the `.skill` file.

On local models: include the file content in your system prompt or context window.

## Governance

Single maintainer. Submissions via issue. No roadmap, no committee, no versioning ceremony.

The enshittification-detector applies to this repo as much as anywhere else. If it ever requires a platform account to use, captures a community to extract from, or introduces a dependency it claimed to eliminate — file an issue and quote that back at me.

## Contact

Via GitHub, at least for now. I will respond to interesting offers but do not care to be a spam magnet.

