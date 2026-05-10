# Phase 2 CLI walkthrough

This tutorial is a **hands-on acceptance-style demo** for the Phase 2 minimum surface of the [`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) CLI and [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core). It does not replace normative definitions in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

**Prerequisites:** Rust toolchain, optional PostgreSQL 16+ if you run persistence steps.

## 1. Build or install the CLI

From a checkout of `kotonoha-cli`:

```bash
cargo build --release
export PATH="$PWD/target/release:$PATH"
```

Confirm identity:

```bash
kotonoha version
```

Expect exit code **0** and two lines (CLI semver and targeted spec bundle per [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md)).

## 2. RDE interchange round-trip

Emit a minimal skeleton and validate it:

```bash
kotonoha rde emit | kotonoha rde validate --strict
echo $?
```

Expect **0**.

## 3. Core interchange envelope round-trip

```bash
kotonoha interchange emit | kotonoha interchange validate --strict
echo $?
```

Expect **0**.

## 4. Optional: PostgreSQL persistence

Start PostgreSQL (for example using [`docker-compose.yml`](https://github.com/zyx-corporation/kotonoha-core/blob/main/docker-compose.yml) from `kotonoha-core`):

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

Expect **0** and a UUID printed to stdout.

## 5. Validation failure (contract check)

Broken JSON should fail validation with exit code **2** (see `cli-definition.md`):

```bash
echo '{}' | kotonoha rde validate --strict
echo $?
```

Expect **2**.

---

## Where this fits

Internal governance ties this walkthrough to Phase 2 acceptance criteria (non-public [`kotonoha-management` doc](https://github.com/zyx-corporation/kotonoha-management/blob/main/docs/16_phase2_acceptance_demo.md)). For exact command names and exit codes, always prefer [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md).
