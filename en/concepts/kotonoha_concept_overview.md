# Kotonoha concept overview

**Status:** informative (non-normative). Canonical semantics and conformance language live in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) — start with [introduction.md](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/introduction.md).

Japanese companion: [`../../ja/concepts/kotonoha_concept_overview.md`](../../ja/concepts/kotonoha_concept_overview.md)

---

## Positioning

**Kotonoha** is the institutional framing at the centre of the **Semantic Lineage System (SLS)**.

Kotonoha is not merely version history, diff management, note-taking, or AI-assisted editing. It concerns **changes in meaning** that arise when text or code changes—not the lexical change alone.

- **Git** records *what changed*.
- **Kotonoha** records *what was preserved, transformed, complemented, left unresolved, lost, and where deviation risk appeared* because of that change.

In that sense, Kotonoha is an **institution for semantic lineage**.

## RDE and “wisdom”

The **Resonant Deviation Evaluator (RDE)** is the core of meaning-change auditing in Kotonoha.

RDE is not only a pass/fail scorer. It is not only a safety filter. It observes how a generated artefact or proposed change relates to prior discussion, intent, values, and design rationale—and whether the shift is an acceptable transformation, a needed complement, or a dangerous drift.

What matters here is that RDE carries work similar to what people have called **wisdom**: seeing what problem-solving **removes** from view—ambiguity, pain, relationships, unresolved tension, accountability, minority voices, the original question’s scope—and feeding that back into the next intelligent act.

RDE is therefore institutionalised **wisdom**, not a benchmark of raw intelligence. It does **not** replace human approval or accountability (see human authority in [`kotonoha-spec` introduction](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/introduction.md)).

## “Wonderful” intelligence

Strong intelligence solves problems. High-performance intelligence answers quickly, broadly, and deeply. **Wonderful** intelligence asks afterward:

- What became invisible because of this solution?
- Was original pain or ambiguity brushed aside for clarity?
- Did accountability thin out through efficiency?
- Did generalisation erase particular context?

Kotonoha is not only about making AI convenient. It is a structure for observing what was lost when intelligence solved a problem—and returning that loss to the next act of thought.

## RDE review in Kotonoha

An RDE-style review checks at least the following (operational detail: [Method](../method/README.md)):

1. **Preserved elements**
2. **Transformed elements**
3. **Complemented elements**
4. **Intentionally unresolved elements**
5. **Lost elements**
6. **Deviation risk**
7. **Next update policy**

Traditional diffs show additions, deletions, and edits. In semantic operation, what matters is not only deleted strings: ambiguity lost in paraphrase, scope lost in summary, theoretical tension hidden for implementation convenience must also be visible. RDE observes that loss; Kotonoha routes it into the next update.

Normative observation categories and interchange: [`kotonoha-spec` SLS-4](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/rde-review-output.md).

## Relationship to Git, Issues, and projects

| Mechanism | Primarily records |
| --- | --- |
| Git | String-level deltas |
| Issues | Open work |
| Projects | Work state |
| Kotonoha / SLS | Meaning, loss, drift, accountability |

Kotonoha does not replace Git, Issues, or project boards. It uses them and adds a layer for meaning, loss, drift, and responsibility.

## Operating principles (public summary)

When updating documents, specifications, implementations, or UI:

- Confirm what was lost through success, not only what was achieved.
- Do not swap implementation convenience for theoretical claims.
- Do not treat unverified hypotheses as established conclusions.
- Do not narrow the original discussion’s scope only for readability.
- Do not replace human approval and accountability with AI evaluation output.
- Route RDE review results explicitly into the next update policy.

## Formulation (conceptual memo)

> RDE is not a device that judges correctness of output alone.  
> It is feedback that observes meaning, context, relationships, and accountability lost through problem-solving—and returns that loss to the next intelligent behaviour.

> Wisdom is the ability to see what problem-solving removes—and to feed that back to intelligence.

Kotonoha externalises that wisdom as an institution for semantic lineage.

## Related documents

| Document | Role |
| --- | --- |
| [`kotonoha-spec` introduction](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/introduction.md) | Normative terms and conformance |
| [`kotonoha-spec` architecture](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/architecture.md) | Logical architecture (includes informative figures) |
| [sls_rde_development_method.md](../method/sls_rde_development_method.md) | How the programme applies SLS + RDE |
| [kotonoha_architecture_terms.md](../../docs/architecture/kotonoha/kotonoha_architecture_terms.md) | Backend concept vocabulary |
| [documentation-placement-policy](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/documentation-placement-policy.md) | Placement between `kotonoha-docs` and `kotonoha-spec` |

## Boundaries of this page

- **Includes:** vision, motivation, reader-facing concept framing.
- **Excludes:** internal phase plans, unresolved schema tracking, and private review artefacts (outside public OSS planning docs).
- **Misreadings to avoid:** metaphorical “wisdom” overstated as vague implementation; RDE read as omniscient scorer or substitute for human judgment.
