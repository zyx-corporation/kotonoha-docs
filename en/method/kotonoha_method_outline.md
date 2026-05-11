# Kotonoha Method — draft outline

Status: draft / non-normative

This document sketches the initial structure for **Kotonoha Method**: a project management and governance method derived from the Semantic Lineage System (SLS) perspective.

It is a public draft. It does not define APIs, data schemas, or interoperability requirements. Normative technical definitions belong in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

---

## 1. Working definition

**Kotonoha Method is the institutional implementation of SLS.**

More precisely, it is a method for governing projects as evolving lineages of **meaning, decisions, artifacts, and responsibility**, especially in human-AI collaborative work.

Where the surrounding concepts separate concerns as follows:

| Layer | Role |
| --- | --- |
| **SLS** | Records and traces semantic lineage: how meanings, decisions, and artifacts change over time. |
| **RDE** | Evaluates semantic change: what was preserved, transformed, complemented, unresolved, lost, or at risk of drift. |
| **Kotonoha Method** | Institutionalizes those practices as project routines, review habits, decision protocols, and responsibility structures. |
| **Kotonoha Console** | Provides a human-facing interface for observing, editing, reviewing, and governing semantic lineage. |

A shorter formulation:

> SLS records semantic lineage; RDE evaluates semantic deviation; Kotonoha Method turns both into an institutional practice.

---

## 2. Why this method is needed

Modern project management is good at tracking tasks, owners, deadlines, and status. It is weaker at tracking how meaning changes when requirements, documents, code, and AI-generated outputs evolve together.

In AI-assisted projects, this weakness becomes critical:

- A task may be marked complete while the original intent has narrowed.
- A generated draft may be fluent while silently replacing an unresolved tension with a false conclusion.
- A refactor may improve structure while losing the rationale that made the design safe.
- A project board may show progress while responsibility has become too diffuse to be accountable.

Kotonoha Method treats these as first-class project risks.

The method does not replace Git, Issues, Pull Requests, or project boards. It adds an institutional layer that asks:

- What meaning changed?
- Was the change authorized by the project intent?
- What was preserved, transformed, complemented, deferred, or lost?
- Who or what structure can take responsibility for the consequence of the change?

---

## 3. Core principles

### 3.1 Meaning before throughput

Speed is valuable only when the project can still explain what changed and why. AI-assisted acceleration must not erase semantic accountability.

### 3.2 Intent preservation

Every substantial change should preserve, explicitly transform, or explicitly reject the prior intent. Silent replacement of intent is treated as drift.

### 3.3 Authorized transformation

Not all change is loss. A change may be valid when it transforms an idea into a new form while preserving its responsibility-bearing structure.

### 3.4 Explicit unresolvedness

Open tensions should remain visible. Marking uncertainty as complete is more dangerous than leaving a question open.

### 3.5 Responsibility recapture

Even when responsibility is distributed across humans, tools, documents, and agents, the project must define how consequences reconverge into accountable structures.

### 3.6 Tool independence

The method should work with GitHub, Obsidian, local files, issue trackers, or future SLS-native tooling. The concepts should not depend on a single product.

### 3.7 Non-scoring governance

The method uses structured review, but it should not collapse into simplistic scoring. RDE-style observations are prompts for judgment, not substitutes for judgment.

---

## 4. Draft chapter structure

### Part I — Foundations

#### Chapter 1. From task management to semantic governance

Explains why task completion alone is insufficient for AI-assisted and meaning-heavy projects. Introduces the gap between operational progress and semantic continuity.

Key topics:

- Limits of conventional project management
- AI-generated acceleration and semantic drift
- Meaning, obligation, and institutional memory
- Why Git history is necessary but insufficient

#### Chapter 2. Core vocabulary

Defines the working terms needed to use the method without overloading the public SLS specification.

Key topics:

- Semantic lineage
- ΔM / semantic change
- Intent, artifact, decision, and responsibility
- Preserved / transformed / complemented / unresolved / lost / drift risk
- Institutional implementation

#### Chapter 3. SLS, RDE, and Kotonoha Method

Positions the method in relation to the broader Kotonoha ecosystem.

Key topics:

- SLS as semantic lineage infrastructure
- RDE as semantic deviation evaluation
- Kotonoha Method as institutional implementation
- Kotonoha Console as operational interface
- Boundary between method guidance and normative specification

---

### Part II — Project lifecycle

#### Chapter 4. Project charter as semantic anchor

Describes how a project begins by recording not only goals, but also non-goals, forbidden substitutions, and responsibility assumptions.

Key topics:

- Intent statement
- Non-goals
- Design constraints
- Success and failure conditions
- What must not be lost

#### Chapter 5. Issue design for semantic traceability

Explains how Issues should carry intent, context, scope, and review expectations, rather than merely being task containers.

Key topics:

- Issue as a semantic unit
- Acceptance criteria vs semantic preservation criteria
- Dependencies and lineage links
- Open questions and deferred tensions
- When to split or merge issues

#### Chapter 6. Pull Request review with RDE prompts

Defines a lightweight review routine for conceptual, architectural, documentation, and code changes.

Key topics:

- Preserved elements
- Authorized transformations
- Inferred extensions
- Unresolved elements
- Loss and suspicious drift
- Critical distortion
- Next update policy

#### Chapter 7. Decision records and semantic lineage notes

Introduces decision records as a bridge between Git commits, issue discussions, and SLS-style lineage.

Key topics:

- Why a decision was made
- What alternatives were rejected
- What assumptions remain unstable
- What future reviewers should inspect
- How decisions should be revised

---

### Part III — Artifacts and workflows

#### Chapter 8. Documents as evolving meaning states

Treats documents as living semantic states rather than static outputs.

Key topics:

- Draft, review, publication, and revision states
- Preventing LLM-generated document corruption
- Capturing summary loss
- Handling translations and bilingual drift
- Public vs internal material

#### Chapter 9. Code as institutional behavior

Frames implementation not as isolated code completion, but as behavior that must remain aligned with specification, method, and responsibility.

Key topics:

- Spec-to-code traceability
- Tests as behavioral commitments
- Refactoring and semantic preservation
- Implementation convenience vs conceptual narrowing
- Regression as semantic loss

#### Chapter 10. AI-assisted generation protocol

Defines how LLM outputs should enter the project without being mistaken for validated decisions.

Key topics:

- Prompt context and source-of-truth boundaries
- Draft status for AI-generated content
- Human review obligations
- RDE pass before promotion
- Preventing false closure and excessive confidence

#### Chapter 11. Project boards and milestones

Clarifies how GitHub Projects or equivalent boards should support, but not replace, semantic governance.

Key topics:

- Status columns as operational views
- Milestones as semantic checkpoints
- Completion criteria
- Deferred work visibility
- Board movement vs meaning movement

---

### Part IV — Governance and responsibility

#### Chapter 12. Responsibility recapture model

Develops the institutional principle that responsibility may be distributed during work, but consequences must reconverge into accountable structures.

Key topics:

- Distributed responsibility
- Human-AI collaboration and accountability
- Review ownership
- Maintainer obligations
- Escalation and freeze points

#### Chapter 13. Drift patterns and countermeasures

Catalogues recurring forms of semantic drift and how the method should detect or mitigate them.

Key topics:

- Stronger claim than evidence supports
- Tool convenience becoming theory
- Metaphor replacing mechanism
- Internal assumptions leaking into public docs
- Unresolved tensions converted into polished prose

#### Chapter 14. Review cadence and institutional memory

Describes recurring review practices that keep lineage visible over time.

Key topics:

- Weekly or milestone-level semantic review
- Drift review
- Publication readiness review
- Migration review after specification changes
- Retrospective as lineage repair

---

### Part V — Adoption model

#### Chapter 15. Minimal adoption

Defines the smallest useful version of Kotonoha Method for a small team or solo project.

Key topics:

- Intent note
- RDE checklist
- Issue and PR templates
- Decision log
- Lightweight review rhythm

#### Chapter 16. Team adoption

Explains how to use the method across a small organization or multi-repository project.

Key topics:

- Shared vocabulary
- Cross-repo lineage
- Maintainer roles
- Review responsibilities
- Project board conventions

#### Chapter 17. SLS-native adoption

Describes the future state where tooling can record and inspect semantic lineage directly.

Key topics:

- Kotonoha Console
- SLS-native links
- Semantic diffs
- RDE-assisted review
- Human approval and audit trails

---

## 5. Proposed templates

Future drafts should include operational templates.

### 5.1 Project charter template

```markdown
# Project charter

## Intent

## Non-goals

## What must not be lost

## Success conditions

## Failure conditions

## Responsibility structure

## Open questions
```

### 5.2 Issue template

```markdown
## Intent

## Context / lineage

## Scope

## Non-goals

## Acceptance criteria

## Semantic preservation criteria

## Open questions
```

### 5.3 Pull Request RDE note

```markdown
## Preserved elements

## Authorized transformations

## Inferred extensions

## Unresolved elements

## Loss / drift risks

## Next update policy
```

### 5.4 Decision record template

```markdown
# Decision record: <title>

## Context

## Decision

## Alternatives considered

## Expected semantic change

## Risks

## Revisit condition
```

---

## 6. Initial scope boundaries

This draft intentionally avoids claiming that Kotonoha Method is already a complete formal method.

Out of scope for the initial public draft:

- Complete SLS data model
- Full RDE automation
- Universal project management replacement
- Quantitative scoring of meaning change
- Claims about organizational safety without empirical validation

The initial target is practical: make meaning loss, semantic drift, and responsibility diffusion visible enough to manage.

---

## 7. Next drafting tasks

- Decide whether the main public essay should use the subtitle **Semantic Project Management** or **Meaning-Aware Project Governance**.
- Add examples from documentation editing, code review, and AI-generated draft review.
- Prepare issue and PR templates aligned with this method.
- Add a minimal adoption guide for small teams.
- Keep internal-only planning artefacts out of this public doc chain; expose ideas at the concept level rather than cloning proprietary planning verbatim.
- Keep the method clearly non-normative relative to `kotonoha-spec`.

---

## 8. Working punchlines

- **Kotonoha Method is SLS made institutional.**
- **Git records textual change; Kotonoha Method governs semantic change.**
- **RDE asks what a change did to meaning; Kotonoha Method asks how the project takes responsibility for that change.**
- **A project is not only a task graph. It is a lineage of meanings, decisions, and obligations.**
