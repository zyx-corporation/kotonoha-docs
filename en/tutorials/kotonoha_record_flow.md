# Kotonoha record flow quickstart

This document shows the minimal path for storing a validated RDE draft as a DB-backed Kotonoha record.

It assumes that you have completed the [SLM demo quickstart](slm_demo_quickstart.md), created `rde-draft.json`, and validated it with `kotonoha rde validate --strict`.

Japanese counterpart: [`../../ja/tutorials/kotonoha_record_flow.md`](../../ja/tutorials/kotonoha_record_flow.md)

## What this document covers

This document walks through:

1. starting a local PostgreSQL instance;
2. setting `DATABASE_URL`;
3. running `kotonoha db migrate`;
4. creating a MeaningDelta record container with `delta create`;
5. attaching the validated RDE draft with `rde attach`;
6. recording a human review decision with `review hold`;
7. confirming the record with `export`.

This is not a production database operations guide. Design credentials, permissions, backups, and network exposure separately for production use.

## DB-free vs DB-backed

Steps 1–5 of the [SLM quickstart](slm_demo_quickstart.md) run without a database.

```text
note.md
  ↓
SLM produces rde-draft.json
  ↓
kotonoha rde validate --strict rde-draft.json
  ↓
a draft ready for human review
```

This document covers the optional DB-backed record flow:

```text
kotonoha delta create note.md
  ↓
MeaningDelta record ID = DELTA_ID

kotonoha rde attach --delta-id "$DELTA_ID" rde-draft.json
  ↓
RDE assessment attached

kotonoha review hold --delta-id "$DELTA_ID"
  ↓
Human review decision recorded
```

## Prerequisites

| Item | Description |
| --- | --- |
| `kotonoha` CLI | installed; `kotonoha version` works |
| Git repository | `delta create` currently requires a Git repository |
| PostgreSQL | required to persist the record flow |
| Docker | optional; convenient way to start local PostgreSQL |
| `DATABASE_URL` | PostgreSQL URL the Kotonoha CLI connects to |
| `note.md` | the note under review |
| `rde-draft.json` | validated RDE draft |

## Step 1 — Start local PostgreSQL

If Docker is available, start PostgreSQL with:

```bash
docker run --name kotonoha-postgres \
  -e POSTGRES_USER=kotonoha \
  -e POSTGRES_PASSWORD=kotonoha \
  -e POSTGRES_DB=kotonoha \
  -p 5432:5432 \
  -d postgres:16
```

If a container with the same name already exists:

```bash
docker start kotonoha-postgres
```

This is for local verification only, not production configuration.

## Step 2 — Set DATABASE_URL

```bash
export DATABASE_URL="postgres://kotonoha:kotonoha@localhost:5432/kotonoha"
```

Verify:

```bash
echo "$DATABASE_URL"
```

## Step 3 — Run DB migration

```bash
kotonoha db migrate
```

Check status:

```bash
kotonoha status
```

## Step 4 — Confirm note.md and rde-draft.json

```bash
ls -la note.md rde-draft.json
kotonoha rde validate --strict rde-draft.json
```

Validation must succeed before you continue.

## Step 5 — Create a delta record

`delta create` does **not** automatically ingest earlier drafts or Obsidian sidecar history.

It first creates a MeaningDelta container in the DB for `note.md`. The current CLI mainly stores the Git commit, file path, diff reference, and an optional observation. Without `--observation`, observation is empty.

```bash
DELTA_ID=$(kotonoha delta create note.md)
echo "$DELTA_ID"
```

`DELTA_ID` is not a value you choose manually. It is the UUID printed by `kotonoha delta create note.md`.

### Optional: attach an observation

```bash
cat > observation.json <<'EOF'
{
  "note": "SLM quickstart demo delta",
  "source": "note.md",
  "intent": "Create a delta anchor before attaching validated RDE draft"
}
EOF

DELTA_ID=$(kotonoha delta create note.md --observation observation.json)
echo "$DELTA_ID"
```

This observation is not a substitute for the RDE review output. Attach the RDE draft explicitly in the next step with `rde attach`.

## Step 6 — Attach the RDE draft to the delta

```bash
kotonoha rde attach --delta-id "$DELTA_ID" --source-kind llm --strict rde-draft.json
```

This explicitly attaches the validated `rde-draft.json` to the delta you created above.

## Step 7 — Record a review decision

While learning, `hold` is the safer default:

```bash
kotonoha review hold --delta-id "$DELTA_ID" --decided-by "your-name"
```

`hold` means: you have made the semantic change visible, but you are not ready to approve it yet.

Use `approve` only when you intentionally record human approval.

## Step 8 — Export and verify

```bash
kotonoha export --delta-id "$DELTA_ID" --format m2
```

To save to a file:

```bash
kotonoha export --delta-id "$DELTA_ID" --format m2 --out record-export.json
```

## Obsidian sidecar relationship

Obsidian Console `.kotonoha/` sidecar files are local proposal / audit / review traces in the UI.

This CLI record flow does **not** automatically import sidecar data into DB records.

You attach the explicitly specified `rde-draft.json`.

```text
Obsidian sidecar
  = local trace in the Console UI

DB-backed record flow
  = records saved explicitly via delta create / rde attach / review hold
```

Correlating sidecar and DB records, and tighter export integration, remain future work.

## Common errors

### `DATABASE_URL is not set`

Set the connection URL:

```bash
export DATABASE_URL="postgres://kotonoha:kotonoha@localhost:5432/kotonoha"
```

### database connection failed

PostgreSQL may be stopped, or the URL may be wrong.

```bash
docker ps
docker start kotonoha-postgres
```

### delta create requires a Git repository

Run `delta create` inside a Git repository:

```bash
git init
git add note.md
git commit -m "demo note"
```

Or run the steps inside an existing repository.

### relation/table does not exist

Migrations may not have run:

```bash
kotonoha db migrate
```

## RDE boundaries

### Preserved elements

The SLM remains draft-only. Validation and human review remain required.

### Authorized transformations

A temporary RDE draft file becomes connected to a DB-backed Kotonoha record.

### Inferred extensions

This document explains `delta create`, `rde attach`, `review hold`, and how to use `DELTA_ID`.

### Unresolved elements

Production PostgreSQL operations, Obsidian sidecar ↔ DB record sync, and M6 export correlation are out of scope.

### Drift risks

Do not treat `delta create` as automatic semantic evaluation. It first creates a record container.

## Summary

The safe path:

```text
SLM draft
  → validate
  → delta create
  → rde attach
  → human review
  → export
```
