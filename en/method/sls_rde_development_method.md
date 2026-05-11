# SLS + RDE development method (for Kotonoha itself)

This document explains how the **Kotonoha** programme uses **Semantic Lineage System (SLS)** ideas and **Resonant Deviation Evaluator (RDE)**–style review **as a development method**—not only as concepts implemented *eventually* in software. It is descriptive public guidance. For normative technical definitions, see [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

---

## 1. Purpose

**Dogfooding the mindset:** we aim to build Kotonoha in a way that already embodies what SLS and RDE stand for:

- Treat meaningful change as more than text diffs.
- Record **what was preserved, transformed, complemented, left unresolved, lost, and where deviation risks appear**, and route learning into **next steps**.

This method applies to **specification text**, **code**, **public docs** (`kotonoha-docs`), and cross-repo coordination.

---

## 2. Core terms (working-level)

| Term | Short meaning in this method |
| --- | --- |
| **SLS** | An institutional layer for **semantic lineage**: tracing meaning, loss, and responsibility across changes—not replacing Git, Issues, or projects, but complementing them. |
| **RDE review** | A structured review that inspects a change along **observation categories** (below), not only “does it build?” or “is it correct?” |
| **ΔM (semantic change)** | Change in intent, scope, tension, or value—not merely characters added or removed. |

RDE is **not** framed here as a scorecard, universal safety filter, or substitute for human judgment and accountability.

---

## 3. RDE observation categories (applied to daily work)

When reviewing an Issue, PR, or doc revision, participants ask—not necessarily in order—whether the following are **explicit enough** for someone revisiting the thread later:

1. **Preserved elements** — Intent, constraints, or commitments that remain intentionally intact.
2. **Transformed elements** — Where wording or structure changed and meaning was carried over in altered form (vs silent drift).
3. **Complemented elements** — New explanations, assumptions, or structure that were not present before.
4. **Intentionally unresolved elements** — Deliberately deferred tensions, ambiguity, or open questions (distinct from “not yet started”).
5. **Lost elements / loss** — Ambiguity, pain, responsibility, or questions that **vanished** through summarisation, refactoring, or simplification—not only deleted lines in a diff.
6. **Deviation risk** — Risk of unacceptable drift: metaphor overload, narrowing RDE to tooling concerns, or swapping strategic nuance for implementation convenience.
7. **Next update policy** — What should feed the **next** edit, design decision, or publication step (not a one-off TODO).

In practice, **no change is required to fill every category with prose**. The bar is **conscious visibility**: critical loss or deviation should not be invisible to future readers.

---

## 4. Semantic lineage vs Git / Issues / Projects

| Mechanism | What it captures well | What SLS + RDE add in method |
| --- | --- | --- |
| **Git** | Text diffs, commits, branches | Articulating **why** the meaning of the change matters for lineage—not inferring “loss” from deletions alone. |
| **Issues** | Open work, discussion threads | Surfacing **unresolved** and **lost** dimensions that ticket closure might erase. |
| **Projects (boards)** | Status and prioritisation | Keeping **completion criteria** in Issues/PRs, not only column moves—see each repo’s contributor guidance. |

The method insists: **Git shows what changed; RDE-oriented review asks what the change *did* to meaning and obligation.**

---

## 5. Repository roles (how the method routes work)

| Repository | Role in this method |
| --- | --- |
| [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | Hosts **review-facing, normative** public specification text. Changes here should remain traceable to discussion and migration notes where helpful. |
| [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) | **Implementation** aligned with spec; PRs bridge behaviour back to spec sections when behaviour changes. |
| **`kotonoha-docs` (this repo)** | **Non-normative** explanations, manuals, tutorials, and **this method**—must not silently redefine spec semantics. |
| Internal planning / pre-public drafts | Handled **outside** public repos (organisation policy); promotion into `kotonoha-spec` or public docs follows explicit readiness checks. |

---

## 6. Lifecycle habits (lightweight)

**Authors**

- State **intent** and **non-goals** for substantive PRs.
- Call out **known trade-offs** and **deferred** items instead of hiding them in diff noise.
- When promoting material toward public spec, avoid internal codenames and private-repo dependencies in public text.

**Reviewers**

- Use the **seven categories** as prompts where the change is conceptual, editorial, or architectural.
- Push back when **loss** or **scope shrink** looks accidental—especially for RDE itself (do not narrow “RDE” to a linter or gadget).

**Maintainers**

- Keep **drift risks** (metaphor, operational narrowing, etc.) visible in recurring reviews—aligned with project governance where applicable.

---

## 7. What this method is not

- **Not a substitute** for [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec): behaviour contracts stay in the specification.
- **Not** a guarantee that automated tooling implements full RDE today: the method can apply **before** tooling catches up.
- **Not** unique to one repo: adapt Issue/PR templates per repository while keeping the same conceptual spine.

---

## 8. Further reading (public)

- [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) — canonical definitions as they stabilise.
- [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) — implementation and developer-facing notes.
- [`CONTRIBUTING.md`](../../CONTRIBUTING.md) in this repo — how to contribute to **documentation** here.

---

## Changelog

| Date | Change |
| --- | --- |
| 2026-05-10 | Initial publication of this method overview. |
