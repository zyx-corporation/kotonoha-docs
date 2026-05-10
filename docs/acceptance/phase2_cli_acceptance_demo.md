# Phase 2 CLI acceptance demo

This document is a **hands-on acceptance demo** for the Phase 2 minimum surface of the [`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) CLI and [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core).

It is not a learning tutorial and does not replace normative definitions in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec). For a learning-oriented CLI introduction, see [First CLI session](../tutorials/first_cli_session.md).

**Japanese:** [../acceptance_ja/phase2_cli_acceptance_demo.md](../acceptance_ja/phase2_cli_acceptance_demo.md)

**Prerequisites:** Rust toolchain, optional PostgreSQL 16+ if you run persistence steps.

## Acceptance scope

This demo checks the following minimum behaviors:

- `kotonoha version` exits with code **0** and reports CLI/spec-bundle identity.
- RDE interchange skeleton emission validates in strict mode.
- Core interchange envelope emission validates in strict mode.
- Optional PostgreSQL persistence can migrate and store one envelope.
- Invalid JSON fails validation with the documented contract exit code.

## A. Build or install the CLI

From a checkout of `kotonoha-cli`:

```bash
cargo build --release
export PATH="$PWD/target/release:$PATH"
```

Confirm identity:

```bash
kotonoha version
```

Expected result: exit code **0** and two lines of output: CLI semver and targeted spec bundle per [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md).

## B. RDE interchange round-trip

Emit a minimal skeleton and validate it:

```bash
kotonoha rde emit | kotonoha rde validate --strict
echo $?
```

Expected result: **0**.

## C. Core interchange envelope round-trip

```bash
kotonoha interchange emit | kotonoha interchange validate --strict
echo $?
```

Expected result: **0**.

## D. Optional: PostgreSQL persistence

Start PostgreSQL, for example using [`docker-compose.yml`](https://github.com/zyx-corporation/kotonoha-core/blob/main/docker-compose.yml) from `kotonoha-core`:

```bash
cd /path/to/kotonoha-core
docker compose up -d
export DATABASE_URL=postgres://kotonoha:kotonoha@localhost:5432/kotonoha_dev
```

Apply migrations and store one envelope:

```bash
kotonoha db migrate
kotonoha interchange emit | kotonoha interchange store --strict
echo $?
```

Expected result: exit code **0** and one UUID printed to stdout.

## E. Validation failure contract check

Broken JSON should fail validation with exit code **2**. See [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) for command and exit-code contracts.

```bash
echo '{}' | kotonoha rde validate --strict
echo $?
```

Expected result: **2**.

## Automated script

The [`kotonoha-cli` repository](https://github.com/zyx-corporation/kotonoha-cli) ships [`scripts/phase2_acceptance_demo.sh`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/scripts/phase2_acceptance_demo.sh), which runs steps **A–E** from the internal acceptance checklist: `version`, round-trips, and exit **2** for invalid JSON.

Set `DATABASE_URL` to include **D** (`migrate` + `store`), matching CI on `main`.

## Governance note

Maintainers correlate this procedural demo with Phase 2 acceptance using material that intentionally stays outside public repositories. The reproducible public spine for this checklist is **`kotonoha-cli`** **[`phase2_acceptance_demo.sh`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/scripts/phase2_acceptance_demo.sh)** (including CI on **`kotonoha-cli` `main`**) plus **`kotonoha-docs`** [Phase 2 CLI walkthrough](https://github.com/zyx-corporation/kotonoha-docs/blob/main/docs/tutorials/phase2_cli_walkthrough.md).

For exact command names, schemas, and exit codes, always prefer public normative sources in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) and the CLI definition in [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli).
