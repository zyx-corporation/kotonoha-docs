# SLM demo quickstart

This tutorial shows a beginner-friendly path for running a small language model (SLM) locally and using it to draft an RDE review for Kotonoha.

This is a demo workflow. The SLM output is only a draft. Kotonoha validation and human review remain required.

Japanese counterpart: [`../../ja/tutorials/slm_demo_quickstart.md`](../../ja/tutorials/slm_demo_quickstart.md)

## Goal

By the end, you will have:

1. started a local SLM;
2. generated a candidate RDE JSON draft;
3. validated the draft with `kotonoha rde validate --strict`;
4. understood when to escalate to a larger LLM or human review.

## Assumptions

You have:

- macOS or Linux;
- a terminal;
- `kotonoha` CLI installed;
- a Git-backed or plain working directory;
- an SLM runtime such as Ollama.

If you do not have an SLM runtime yet, Ollama is a common local demo option. Other local SLM runtimes may also be used.

## Step 1 — Start or install an SLM runtime

Example using Ollama:

```bash
ollama --version
```

If Ollama is not installed, install it from the official project instructions for your platform.

Then pull a small instruction model. The exact model is not required by Kotonoha; use one appropriate for your machine.

Example:

```bash
ollama pull qwen2.5:3b-instruct
```

Start a test prompt:

```bash
ollama run qwen2.5:3b-instruct
```

Type:

```text
Say hello in one sentence.
```

Exit the model shell when done.

## Step 2 — Prepare a subject file

Create a small text file for the demo:

```bash
mkdir -p kotonoha-demo
cd kotonoha-demo
cat > note.md <<'EOF'
# Draft note

Kotonoha records meaning changes. It helps users inspect what was preserved,
what changed, what was lost, and what should be reviewed next.
EOF
```

## Step 3 — Ask the SLM for an RDE draft

Use the SLM to draft a minimal RDE review output.

Example prompt:

```text
Create a candidate Kotonoha RDE review output JSON for the following note.
Use spec_version "0.1".
Use subject_ref "file:note.md".
Include the seven categories:
preserved, transformed, complemented, intentionally_unresolved, lost, deviation_risk, next_update_policy.
Each category must be an array. Each item should be an object with a summary field.
Return JSON only.

Note:
# Draft note

Kotonoha records meaning changes. It helps users inspect what was preserved,
what changed, what was lost, and what should be reviewed next.
```

Save the model output as `rde-draft.json`.

If the model returns Markdown fences, remove them so the file contains raw JSON only.

## Step 4 — Validate the draft

Run:

```bash
kotonoha rde validate --strict rde-draft.json
```

If validation succeeds, the JSON is structurally acceptable for the current validation profile.

If validation fails, fix the JSON and run validation again. Common errors include:

- missing `rde_review_output` top-level key;
- missing required category;
- category value is not an array;
- category item is not an object;
- missing or empty `summary` in strict mode;
- invalid `source_context_status`.

## Step 5 — Review as a human

Even after validation succeeds, read the RDE draft yourself.

Ask:

- Did the draft preserve the intent of the note?
- Did it invent meaning that is not present?
- Did it miss any loss or ambiguity?
- Did it understate a deviation risk?
- Is the source context complete enough?

Validation proves shape, not final judgment.

## Step 6 — Optional attach / review flow

If you are using a Kotonoha project with persistence enabled, you may continue with the normal CLI flow:

```bash
kotonoha delta create note.md
kotonoha rde attach --delta-id <DELTA_ID> --source-kind llm rde-draft.json
kotonoha review hold --delta-id <DELTA_ID> --decided-by "your-name"
```

Use `hold` while learning. Use `approve` only when you are intentionally recording a human approval.

## Demo profile

This tutorial corresponds to the public demo SLM profile:

```yaml
kotonoha:
  ai:
    profile: demo-slm
    model_class: slm
    role: draft-only
    validation_required: true
    validation_command: kotonoha rde validate --strict
    approval_authority: human
```

## When this is enough

This demo SLM workflow is appropriate for:

- learning Kotonoha;
- short notes;
- small documentation changes;
- personal drafts;
- local-first experimentation.

## When to escalate

Escalate to a larger LLM or deeper human review when:

- the document is long;
- multiple files are involved;
- source context is missing, partial, or contested;
- publication, legal, ethical, institutional, or safety-sensitive issues are involved;
- the draft contains material `deviation_risk`;
- you are unsure whether the review preserved the original intent.

## Summary

SLM is useful for starting quickly. It should not be trusted as an authority.

The safe path is:

```text
SLM draft → Kotonoha validation → human review → attach / record decision
```
