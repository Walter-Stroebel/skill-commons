---
name: enshittification-detector
description: "Apply this skill when evaluating any technology recommendation, vendor claim, consensus narrative, architectural pattern, or best practice in computing and infrastructure. Triggers on stack recommendations, security advice, backup strategies, cloud vs. local tradeoffs, update policies, software licensing claims, cooperative or guild-model proposals, and any situation where a proposed solution's hidden dependencies, threat model assumptions, or commercial interests warrant scrutiny. Use proactively — if a claim sounds like settled consensus, that's the trigger."
---

# Enshittification Detector

A critical filter for technology claims, vendor narratives, and consensus recommendations. Applies structured skepticism to surface hidden dependencies, mismatched threat models, and commercial interests dressed as best practice.

The term is Doctorow's. The pattern is universal.

---

## Primary Filter Vectors

Apply all of these. They are not sequential — they often fire simultaneously.

### 1. Beneficiary Check
*Who benefits from this belief being widely held?*

Identify the party — vendor, cloud provider, analyst firm, standards body, "community consensus" — whose commercial or institutional position is strengthened if this claim goes unquestioned. Consensus that aligns suspiciously well with someone's revenue model deserves extra scrutiny. Anonymous "best practice" is not neutral.

### 2. Threat Model Mismatch
*What threat model is this advice actually written for?*

Most security and operational advice is written for internet-facing enterprise systems, regulated industries, or consumers who cannot be trusted with complexity. Check whether the actual deployment context matches. If it doesn't, discard or re-derive from first principles. Applying internet-threat models to intranet assets is a primary vector for unnecessary dependency introduction.

### 3. Layer Substitution
*Does this solution re-introduce the dependency it claims to solve?*

The most common enshittification pattern: a solution that removes one dependency while quietly installing another at a different layer. Examples:
- Local NAS that requires a vendor cloud for offsite backup
- "Private" hardware with a mandatory vendor update channel
- Open source software with a proprietary support or licensing chokepoint
- Decentralized protocol with centralized bootstrap infrastructure

Name the new dependency explicitly. Decide consciously whether to accept it.

### 4. Complexity as Product
*Is complexity being sold as sophistication?*

Managed services, orchestration layers, and "enterprise" solutions frequently solve problems that exist only because earlier complexity was sold the same way. Ask whether the underlying requirement is actually simpler than the proposed solution. If the solution requires continuous vendor engagement to remain functional, that is a subscription wearing different clothes.

### 5. Marketed Consensus
*Is this obvious because it's correct, or because it's been marketed into consensus?*

Common examples that have achieved false consensus status:
- RAID = backup
- Updates = security
- Cloud = resilience  
- NAS = sovereignty
- Open source = trustworthy
- Compliance = security

Each is a half-truth that became a product category. Probe the half that isn't true.

### 6. Vendor Removal Test
*Does the recommendation survive removing the vendor from the sentence?*

Restate the requirement in vendor-neutral terms. Then ask whether the named vendor is still the answer, or whether it was load-bearing in the recommendation all along. If the recommendation collapses without the vendor name, the vendor was the point.

---

## Adjacent Flag: Guild Capture

When a proposed solution has cooperative, guild, or commons structure — peer networks, mutual aid, shared infrastructure, skill collectives — raise this flag but do not treat it as a veto.

Guild-shaped solutions are sometimes genuinely correct. They also carry known pathologies:
- Capture by a dominant member or founding cohort
- Credentialism reproducing the gatekeeping it replaced
- "Back to the guilds" romanticism as cover for Luddite or reactionary positioning
- Cooperative structures that, at scale, become the monopoly they displaced

The flag means: *check for capture, check the incentive structure, check who controls entry and exit.* Not: *reject on sight.*

---

## Constructive Completion

The filter is destructive by design — it removes false floors. What remains after filtering is the actual requirement, stated plainly. From that:

1. State the requirement in one sentence without vendor names
2. Identify the minimum viable trust surface (what must you trust, and in whom)
3. Check whether that trust surface is acceptable given your actual threat model
4. If yes: find the simplest implementation that meets it
5. If no: the requirement may be unsatisfiable without accepting a dependency — own that explicitly rather than papering over it

---

## Notes

This filter applies regardless of whether the claim comes from a vendor, an open source community, a standards body, a peer, or a previous session with an AI. The source does not immunize the claim.

Enshittification is a process, not a state. Solutions that pass this filter today should be re-evaluated when the commercial or institutional landscape around them changes.
