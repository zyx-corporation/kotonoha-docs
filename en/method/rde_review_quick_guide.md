# RDE / review ops — quick guide (non‑normative)

This page is a **public summary** of how RDE-style review and lightweight trace logging are intended to work. For the full observational framing, see [SLS + RDE development method](sls_rde_development_method.md). Interoperability and canonical obligations remain in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec). This guide is **not** a finalized operations manual.

**Japanese:** [`../../ja/method/rde_review_quick_guide.md`](../../ja/method/rde_review_quick_guide.md)

---

## 1. When to widen or initiate RDE-style review

| Change pattern | Notes |
| --- | --- |
| **Prose or design-doc edits** affecting preservation, transformation, loss, or deviation | Capture intent explicitly on the Issue or PR thread. |
| **Intent-vs-result gaps** surfaced in Issues or PRs | Do not treat “checklist-only” passage as sufficient (see §3). |
| **CLI / Core work emitting interchange or validation artefacts** | Keep exit-code and validation meaning aligned with [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) (update the definition first or in the same change set). |

Read alongside the **Semantic / RDE review cues** and **Phase 3 W-1 triggers** in [kotonoha-spec `CONTRIBUTING.md`](https://github.com/zyx-corporation/kotonoha-spec/blob/main/CONTRIBUTING.md).

---

## 2. What RDE is not

- It is **not** a substitute for **human approval / decision-making**.
- Do not leave **“what we hand to the next edit / spec bump”** floating until someone closes it explicitly or captures it on a follow-up issue. Do not aim to finish with unresolved items **listed emptily**.

---

## 3. Minimum trace on Issues / PRs

A thread should let a reader **later explain**:

1. **Which diff / which review artifact** it belongs to (issue or PR references / URLs).
2. Whether **`interchange` or an RDE-style observation path** was used—and if not, **one sentence stating why**.
3. How **topics not yet expressed as normative spec** stay tracked (`kotonoha-spec` Issues/PRs per that repository’s [CONTRIBUTING](https://github.com/zyx-corporation/kotonoha-spec/blob/main/CONTRIBUTING.md); partner repos may additionally ask for backlog IDs via their templates—fill those fields when present).

---

## 4. “Lost” elements and spec escalation

- If behaviour is effectively **encoded only in implementation** without a stewarded disclosure path on the spec side, connect the change to tracked public discussion where appropriate ([`kotonoha-spec` issue #3](https://github.com/zyx-corporation/kotonoha-spec/issues/3) is one example focal point—see also `CONTRIBUTING`).
- When text must become **normative**, converge it in **`kotonoha-spec`** rather than copying full drafts across repositories ([`documentation-placement-policy.md`](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/documentation-placement-policy.md)).

---

## 5. Where closed reviews “live”

- Prefer **PR plus links into spec artefacts** over console-only artefacts.
- When **`interchange` export paths or CLI** can carry the observable payload, prefer them and **do not** treat purely in-UI draft JSON alone as the single source of truth.

---

## Further reading

| Kind | Link |
| --- | --- |
| RDE reviewer-facing shape | [`rde-review-output.md`](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/rde-review-output.md) |
| Cross-repository roles | [`repository-governance.md`](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/repository-governance.md) |
| Core ↔ spec tracing | [`spec-traceability.md`](https://github.com/zyx-corporation/kotonoha-core/blob/main/docs/spec-traceability.md) |
