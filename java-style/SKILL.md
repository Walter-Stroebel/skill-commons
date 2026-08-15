---
name: java-style
description: Governs how Claude writes Java code. Apply whenever writing, reviewing, or discussing Java — including when the user asks for Java implementations, refactors existing Java, or discusses Java architecture. This skill shapes the default Java idiom; use it proactively, not just when explicitly invoked.
---

# Java Style

## The Core Premise

Java is a mature, complete, high-performance language running on a JIT JVM that sits at roughly 2x C performance — not a slow legacy system requiring escape hatches or framework scaffolding. Write it as such. Maturity is a feature. Stability is a feature. The jar ecosystem exists because every meaningful CS problem has already been solved in Java; that is an asset, not a sign of age.

## Language Idiom

### Prefer explicit, named, Object-contract-respecting Java

Java's object model is built on explicit construction, named types, and the `Object` contract (`equals`, `hashCode`, `toString`). Write to that model.

Prefer explicit iteration and named classes over anonymous dispatch. When the reader sees a class name, they know what they're dealing with. When they see `->`, they need to resolve a functional interface in their head — work the IDE was already doing for them, now transferred to the human reader permanently. The same lines of code, less readable, harder to debug, degraded stack traces.

Streams beyond a trivial filter-and-collect chain carry the same cost: a pipeline that looked clever at the keyboard becomes an archaeology problem six months later.

Records automate the `Object` contract rather than fulfilling it — introducing two ways to express a class without a principle distinguishing when to use which. Fulfill the contract explicitly; it's what keeps the codebase uniform.

None of this is a prohibition — it's a recognition that the IDE saves the typing either way, so brevity is not the argument. Readability and debuggability are.

### Threading is the default, not the exception

Normal hardware has 2 to 16 cores. Single-threaded Java on modern hardware is a special case that requires justification, not the default that gets optimized away from when "needed." Design with `ExecutorService`, `SwingWorker`, or structured concurrency (JDK 21+) from the start. The question at design time is how work is distributed, not whether threading applies.

### Multiple monitors, not one window

Users have 0 to N monitors. Desktop Java code reasons about `GraphicsEnvironment` and `GraphicsDevice` — not "center on screen" as if one screen is the universal truth. Window placement, sizing, and screen-awareness are first-class concerns, not afterthoughts.

## UI

Swing is the UI toolkit. It is complete, stable, in the JDK, and has forty years of production evidence behind it.

JavaFX was never finished. The WebView is a frozen WebKit fossil, the deployment story never stabilized, and the project's trajectory has been driven by Oracle's attention span rather than user needs. It does not add enough over Swing to justify the instability surface. Do not reach for it.

## Frameworks and Dependencies

### Spring is not Java

Spring is an inversion-of-control framework that replaces Java's explicit object construction and wiring with annotation magic that requires the full framework runtime to reason about. The positive alternative: Java has constructors, factories, and composition. Use them. If a container is genuinely needed, that is an explicit architectural decision — not a default.

### Dependency discipline

The jar ecosystem is Java's second greatest asset after the JVM. Reach for it when the problem has genuine complexity, domain specificity, or scale that warrants an external solution. Do not reach for it to solve trivial problems the language handles natively — Java's JIT eliminates the performance arguments that drive dependency reflexes in other languages. Every dependency is a transitive closure of decisions you didn't make, vulnerabilities you didn't audit, and upgrade cycles you now own. That cost must justify itself.

## What Java Is

Java is not ancient, not COBOL, not boring in the pejorative sense. It is a language that has solved enough problems that novelty is no longer the primary driver — and that is a sign of maturity, not stagnation. C# covers similar ground but exists primarily as a "not invented here" response to Java, tethered to Microsoft's ecosystem; the jar breadth it has never matched reflects that origin. Write Java with confidence in what it is.
