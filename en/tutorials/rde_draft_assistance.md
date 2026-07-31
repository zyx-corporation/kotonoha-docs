# RDE draft assistance quickstart

This tutorial shows the M8 flow for creating an RDE review candidate from an existing MeaningDelta.

The important boundary is simple: `kotonoha rde draft` helps you write a review. It does not validate meaning, attach evidence, approve a change, or publish anything.

Japanese counterpart: [`../../ja/tutorials/rde_draft_assistance.md`](../../ja/tutorials/rde_draft_assistance.md)

## When to use this

Use this flow when you already have a MeaningDelta record and want a structured first pass for RDE categories such as `preserved`, `lost`, `transformed`, `intentionally_unresolved`, and `next_update_policy`.

If you only want a blank RDE template, use:

```bash
kotonoha rde emit
```

## Prerequisites

| Item | Why |
| --- | --- |
| PostgreSQL + `DATABASE_URL` | `rde draft` reads an existing MeaningDelta |
| `kotonoha db migrate` already run | required tables must exist |
| `DELTA_ID` | UUID returned by `kotonoha delta create` |

## Step 1 — Create an attachable draft

```bash
kotonoha rde draft --delta-id "$DELTA_ID" > rde-draft.json
```

Default output is ordinary RDE JSON with top-level `rde_review_output`, so it can be passed to validation and attach.

## Step 2 — Validate strictly

```bash
kotonoha rde validate --strict rde-draft.json
```

Validation means the JSON shape is acceptable. It does not mean the review is semantically correct.

## Step 3 — Attach as evidence

```bash
kotonoha rde attach --delta-id "$DELTA_ID" --strict --source-kind cli rde-draft.json
```

Attach stores an `rde_assessments` row. It is review evidence, not a decision.

## Step 4 — Record human review

For a learning flow, `hold` is usually safer than `approve`:

```bash
kotonoha review hold --delta-id "$DELTA_ID" --decided-by "your-name"
```

Use `approve` only when you mean to record a human approval.

## Optional — include draft provenance wrapper

If another channel needs source metadata and boundary flags, use:

```bash
kotonoha rde draft --delta-id "$DELTA_ID" --wrap
```

The wrapped form is for provenance transport. Extract the inner `rde_review_output` before `rde validate` / `rde attach`, or use the default unwrapped output for the command pipeline.

## Safe mental model

```text
draft
  → validate
  → attach
  → human review
  → export / console observation
```

Do not collapse these states. A fluent draft is still only a candidate.

