# First CLI session

This tutorial is a learning-oriented first session with the [`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) CLI.

It explains what the first commands mean and how they relate to Kotonoha concepts. It is not an acceptance checklist. If you need release-facing validation with expected exit codes, see the [Phase 2 CLI acceptance demo](../acceptance/phase2_cli_acceptance_demo.md).

**Japanese:** [../../ja/tutorials/first_cli_session.md](../../ja/tutorials/first_cli_session.md)

## What you will learn

By the end of this tutorial, you should understand:

- how to confirm the CLI identity;
- why the CLI reports a targeted spec bundle;
- what an RDE skeleton represents;
- what an interchange envelope represents;
- where to look for exact command contracts.

## Prerequisites

- Rust toolchain
- A checkout of [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli)

You do not need PostgreSQL for this tutorial.

## 1. Build the CLI

From a checkout of `kotonoha-cli`:

```bash
cargo build --release
export PATH="$PWD/target/release:$PATH"
```

This makes the local `kotonoha` command available in your shell.

## 2. Confirm CLI identity

Run:

```bash
kotonoha version
```

The important idea is not only that the command runs. The CLI should identify both itself and the specification bundle it targets.

Kotonoha separates implementation behavior from normative specification. That separation matters because documentation, tests, and future implementations must know which public contract they are discussing.

For exact output rules, see [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md).

## 3. Emit an RDE skeleton

Run:

```bash
kotonoha rde emit
```

An RDE skeleton is a minimal structured form for recording meaning-change review. At this stage, you are not judging a person or scoring a user. You are preparing a shape for inspecting how generated or transformed content may preserve, transform, extend, or drift from an original intent.

Now validate it:

```bash
kotonoha rde emit | kotonoha rde validate --strict
```

Validation checks whether the emitted structure conforms to the expected contract. In a tutorial, the purpose is to understand the shape. In an acceptance demo, the purpose is to confirm the expected exit code.

## 4. Emit an interchange envelope

Run:

```bash
kotonoha interchange emit
```

An interchange envelope is a transport shape for exchanging Kotonoha-related data across tools. It is not the full theory and not the full storage model. It is the minimal public surface that lets different tools agree on what is being passed.

Validate it:

```bash
kotonoha interchange emit | kotonoha interchange validate --strict
```

**Contract note:** validating with **`kotonoha-core` ≥ 0.1.6** rejects **extra JSON keys** at the interchange **top level** (only `format`, `spec_bundle`, `lineage_unit`, `rde_document`) and rejects unknown keys beside `id` / `prior_unit_id` inside **`lineage_unit`** (exit **2** from `interchange validate`). Prefer extending the recorded vocabulary via spec-tracked revisions rather than ad-hoc envelope fields.

The difference between the RDE skeleton and the interchange envelope is important:

- RDE skeleton: a review-oriented structure for meaning-change inspection.
- Interchange envelope: an exchange-oriented structure for moving data between tools.

## 5. Where to go next

If you want to verify Phase 2 behavior for release or review, use:

- [Phase 2 CLI acceptance demo](../acceptance/phase2_cli_acceptance_demo.md)

If you need exact command names, output rules, and exit-code contracts, use:

- [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md)
- [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)

## RDE note

This tutorial intentionally avoids presenting the CLI as the theory itself. The CLI is an entry point. The theory lives in the specification, method documents, and future semantic-lineage workflows.
