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

## Default minimal choice: SLM

For personal and lightweight workflows, the default minimal model choice may be an SLM.

Expected SLM roles:

- draft RDE category items;
- suggest short `summary` text;
- format candidate RDE JSON;
- identify obvious `lost` or `deviation_risk` items;
- assist note-level or single-file review;
- keep local-first or low-cost workflows practical.

SLM output is never authoritative. It is only a draft.

## When to escalate to a larger LLM or human review

Escalate beyond the default SLM path when any of the following applies:

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

1. Use an SLM or LLM to draft an RDE review.
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

The safest default is:

```text
Default model: SLM
Role: draft-only assistant
Validation: kotonoha rde validate --strict
Escalation: larger LLM or human review when risk/context requires it
Final authority: human reviewer
```
