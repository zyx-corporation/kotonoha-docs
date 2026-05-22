# LLM and SLM usage guide

This guide explains how Kotonoha uses large and small language models in user-facing workflows.

This document is public documentation, not a normative SLS specification. Exact RDE output semantics and validation rules are defined in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

Japanese counterpart: [`../../ja/manual/llm_slm_usage.md`](../../ja/manual/llm_slm_usage.md)

## Basic position

Kotonoha does not require a specific LLM provider or model.

LLMs or SLMs may generate candidate RDE drafts, but all such outputs must pass Kotonoha validation before attachment, persistence, or review use. Human approval remains outside LLM authority.

In short:

| Layer | Role |
| --- | --- |
| SLM / LLM | Draft generator, classifier assistant, JSON formatter |
| `kotonoha-core` / `kotonoha-cli` | Validation, persistence path, review record handling |
| Human reviewer | Final approval, hold, rejection, publication responsibility |

## Demo minimal profile: SLM

For demos, personal trials, and lightweight workflows, an SLM may be used as the **minimal demo profile**.

This is not a production requirement and not a normative SLS rule. It is a practical configuration example for low-cost, local-first, or quick-start usage.

Expected SLM roles:

- draft RDE category items;
- suggest short `summary` text;
- format candidate RDE JSON;
- identify obvious `lost` or `deviation_risk` items;
- assist note-level or single-file review;
- keep demo and low-cost workflows practical.

SLM output is never authoritative. It is only a draft.

## Example configuration profiles

The exact configuration format depends on the channel or implementation. The following examples describe intended profiles.

### Demo SLM profile

Use this for local demos, onboarding, personal notes, and short single-file reviews.

```yaml
kotonoha:
  ai:
    profile: demo-slm
    model_class: slm
    role: draft-only
    allowed_tasks:
      - rde_draft
      - category_suggestion
      - json_formatting
    validation_required: true
    validation_command: kotonoha rde validate --strict
    attach_requires_validated_json: true
    approval_authority: human
    escalation:
      on_source_context:
        - missing
        - partial
        - contested
      on_risk:
        - deviation_risk
      on_subject:
        - long_document
        - multi_document
        - publication_sensitive
```

### Hosted LLM escalation profile

Use this when the SLM draft is insufficient, the subject is long, or the review is conceptually or institutionally sensitive.

```yaml
kotonoha:
  ai:
    profile: hosted-llm-escalation
    model_class: llm
    role: draft-improvement
    allowed_tasks:
      - rde_draft_revision
      - ambiguity_review
      - lost_context_review
      - deviation_risk_review
    validation_required: true
    validation_command: kotonoha rde validate --strict
    approval_authority: human
```

### No-model profile

Use this when the user writes RDE observations manually.

```yaml
kotonoha:
  ai:
    profile: no-model
    model_class: none
    role: manual-review
    validation_required: true
    validation_command: kotonoha rde validate --strict
    approval_authority: human
```

These examples are documentation profiles. They do not define a required public configuration schema.

## When to escalate to a larger LLM or human review

Escalate beyond the demo SLM path when any of the following applies:

- the subject is long or spans multiple documents;
- source context is `missing`, `partial`, or `contested`;
- the review involves institutional responsibility, publication, legal, political, ethical, or safety-sensitive content;
- the RDE draft contains material `deviation_risk`;
- the meaning change depends on subtle philosophical, conceptual, or rhetorical structure;
- the user is unsure whether the generated review preserved the original intent.

A larger LLM may help produce a better draft, but human review remains required for approval.

## Validation gate

Before an RDE draft is attached, persisted, or used for review, run Kotonoha validation.

Typical command:

```bash
kotonoha rde validate --strict path/to/rde.json
```

The validator checks the machine-readable shape, required RDE categories, and closed vocabularies such as `source_context_status`. It does not prove that the semantic judgment is final or correct.

## Recommended workflow

1. Use an SLM, LLM, or manual process to draft an RDE review.
2. Inspect the draft as a human reviewer.
3. Validate the JSON with `kotonoha rde validate --strict`.
4. Attach the validated RDE output with `kotonoha rde attach` when appropriate.
5. Record a human decision with `kotonoha review approve`, `hold`, or `reject`.

## Provider examples

The following are examples of possible channels, not requirements:

- ChatGPT or a ChatGPT App / MCP client;
- Claude Desktop or Cursor through MCP;
- Gemini or another hosted LLM;
- Qwen or another local/open model;
- an organization-specific SLM.

Changing the model does not change RDE authority. The validated JSON and human review boundary are what matter.

## What not to do

Do not:

- treat raw LLM prose as the RDE record;
- treat an LLM-generated RDE as human approval;
- bypass `kotonoha` validation before attach or persistence;
- encode a provider-specific model as a public SLS requirement;
- let model convenience erase missing, partial, or contested source context.

## Summary

A safe demo profile is:

```text
Demo model profile: SLM
Role: draft-only assistant
Validation: kotonoha rde validate --strict
Escalation: larger LLM or human review when risk/context requires it
Final authority: human reviewer
```
