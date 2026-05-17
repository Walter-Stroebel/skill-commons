# skill-commons

> A curated commons of LLM-agnostic skills. No vendor lock-in. No SDK. No platform requirement.

## What this is

A skill is a structured markdown document that extends LLM behavior in a well-defined, auditable way. You give it to an LLM — in a system prompt, in context, or via a platform's native skill system — and the model reads it and follows it.

That's the entire mechanism. No code execution. No API calls. No dependencies. A skill is a document that teaches an LLM a capability it can then apply to your session.

Skills in this repo are:
- **LLM-agnostic** — written for any model that can read markdown and act on instructions
- **Portable** — copy a `SKILL.md` into any context window and it works
- **Auditable** — you can read exactly what the skill instructs the model to do
- **Composable** — skills can depend on other skills, explicitly documented

## Structure

Each skill lives in its own directory:

```
skill-name/
├── SKILL.md          # The skill itself — instructions + trigger description
└── references/       # Optional: supporting files, rationale, examples
    └── design-rationale.md
```

Some skills include supporting code (like `layout.py` in the mindmap skill) that the LLM is instructed to run during execution. These are bundled with the skill.

## Claude-specific installation

For Claude.ai, skills are packaged as `.skill` files — these are standard zip archives with a `.skill` extension containing the skill directory. Install them via **Settings → Profile → Custom Skills**, or drag into any Claude chat.

Pre-built `.skill` files for all skills in this repo are available in [Releases](../../releases). Download and install. The source in this repo is what's inside them.

To build `.skill` files yourself from source:

```bash
bash package.sh        # Linux/Mac
package.bat            # Windows
```

Output goes to `skills/` (gitignored — these are build artifacts, not source).

## Current skills

| Skill | What it does |
|---|---|
| [mindmap](mindmap/SKILL.md) | Extracts the current session as a radial SVG mind map with clickable nodes that fire follow-up questions back into chat. Requires session-json. |
| [session-json](session-json/SKILL.md) | Extracts the current session's concept hierarchy as a minimal JSON topology file. Drives the mindmap skill. Useful standalone. |
| [enshittification-detector](enshittification-detector/SKILL.md) | Filters technology claims, vendor narratives, and consensus recommendations for hidden dependencies, mismatched threat models, and commercial interests dressed as best practice. |
| [false-binary](false-binary/SKILL.md) | Detects false either/or framings and surfaces the third option — both, sequence, or transcendence. |

## Skill dependencies

```
mindmap → requires → session-json
```

Install session-json before mindmap. Everything else is standalone.

## On local models

Include the `SKILL.md` content in your system prompt or context window. The model will apply the skill when the trigger description matches the user's request. No packaging needed.

## Threat model

Skills are instructions. A malicious skill is a prompt injection vector at scale — any LLM pipeline that reads arbitrary text is potentially vulnerable to a well-constructed skill embedded in that text. This is not theoretical.

This commons is curated by a single maintainer for that reason. There is no open contribution pipeline. Submissions are reviewed through wetware, not tooling, because natural language intent cannot be statically analyzed.

**Do not install skills from untrusted sources.** The format is portable precisely because it has no sandbox. That cuts both ways.

If you want to submit a skill: open an issue. It will be read by a human. It may be declined. No explanation owed.

## Governance

Single maintainer. Submissions via issue. No roadmap, no committee, no versioning ceremony.

The enshittification-detector applies to this repo as much as anywhere else. If it ever requires a platform account to use, captures a community to extract from, or introduces a dependency it claimed to eliminate — file an issue and quote that back at me.

## Contact

Via GitHub. I will respond to interesting things. I am not a spam magnet.
