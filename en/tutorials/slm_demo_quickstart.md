# SLM demo quickstart

This tutorial shows a beginner-friendly path for running a small language model (SLM) locally and using it to draft an RDE review for Kotonoha.

This is a demo workflow. The SLM output is only a draft. Kotonoha validation and human review remain required.

Japanese counterpart: [`../../ja/tutorials/slm_demo_quickstart.md`](../../ja/tutorials/slm_demo_quickstart.md)

## Story: a small note before publishing

Imagine you are editing a short note before sharing it with a colleague or publishing it as a small article.

The note looks harmless. You only changed a few sentences. But you are not fully sure what changed in meaning.

Maybe the new version is clearer. Maybe it also removed an important hesitation. Maybe it made the claim sound stronger than you intended.

This is where Kotonoha helps.

In this tutorial, you will play the role of a writer reviewing a short note. A local SLM will act as a cheap draft assistant. It will try to describe what was preserved, changed, lost, or risky. Then Kotonoha will check whether the draft is a valid RDE review output. Finally, you will read it as the human reviewer.

The point is not to trust the SLM. The point is to make a first draft visible enough for you to review.

## Goal

By the end, you will have:

1. started a local SLM;
2. created a small note as the review subject;
3. asked the SLM to draft candidate RDE JSON;
4. validated the draft with `kotonoha rde validate --strict`;
5. reviewed the result as a human;
6. understood when to escalate to a larger LLM or deeper review.

## Assumptions

You have:

- macOS or Linux;
- a terminal;
- `kotonoha` CLI installed;
- a Git-backed or plain working directory;
- an SLM runtime such as Ollama.

If you do not have an SLM runtime yet, Ollama is a common local demo option. Other local SLM runtimes may also be used.

## Step 1 — Start or install an SLM runtime

The story begins with a small assistant running locally.

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

At this point, you have a local draft assistant. It is not an evaluator, not an approver, and not a source of truth.

## Step 2 — Prepare the note you want to review

Now create the note that will become the review subject.

```bash
mkdir -p kotonoha-demo
cd kotonoha-demo
cat > note.md <<'EOF'
# Draft note

Kotonoha records meaning changes. It helps users inspect what was preserved,
what changed, what was lost, and what should be reviewed next.
EOF
```

In a real workflow, this might be a paragraph from an essay, a README change, a research note, or an Obsidian draft.

For the tutorial, we keep it short so you can see the full loop.

## Step 3 — Ask the SLM for an RDE draft

Now ask the SLM to describe the note in Kotonoha's RDE format.

The SLM is not deciding whether the note is good. It is only preparing a candidate review record.

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

This is the first important boundary: the file is a draft, not a valid Kotonoha record yet.

## Step 4 — Validate the draft

Now Kotonoha checks the shape of the draft.

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

Validation does not mean the SLM was right. It only means the draft is shaped well enough to be reviewed.

## Step 5 — Read it as the human reviewer

Now the important part begins.

Even after validation succeeds, read the RDE draft yourself.

Ask:

- Did the draft preserve the intent of the note?
- Did it invent meaning that is not present?
- Did it miss any loss or ambiguity?
- Did it understate a deviation risk?
- Is the source context complete enough?

This is the second important boundary: Kotonoha helps you review meaning change, but it does not replace your responsibility.

## Step 6 — Optional: keep it as a Kotonoha record

Up to this point, `rde-draft.json` is still a temporary draft file.

If your goal is only to learn the workflow, you can stop at Step 5.
If you want to keep the draft as part of a Kotonoha record, you can continue into the CLI `delta create`, `rde attach`, and `review hold` flow.

Here, "keep it as a record" means creating a `delta` for the note, attaching the validated RDE draft to that delta, and recording a human review decision such as `hold`.

This step is optional. It is not required to run the quickstart.

The flow has three steps:

1. `delta create`: create a meaning-change record for the note.
2. `rde attach`: attach the validated RDE draft to that delta.
3. `review hold`: record a human decision to keep the review in a held state.

```bash
kotonoha delta create note.md
kotonoha rde attach --delta-id <DELTA_ID> --source-kind llm rde-draft.json
kotonoha review hold --delta-id <DELTA_ID> --decided-by "your-name"
```

Use `hold` while learning. Use `approve` only when you are intentionally recording a human approval.

In the story, `hold` means: "I have made the semantic change visible, but I am not ready to approve it yet."

## What the demo profile means

The `profile` shown here is not a required configuration file for running this quickstart.

It is a named usage policy that describes how the SLM is treated in this tutorial.

`demo-slm` means:

- The SLM is used for drafting only.
- SLM output is not an accepted Kotonoha record.
- Validation with `kotonoha rde validate --strict` is required.
- Passing validation does not mean the content is correct.
- Final judgment and approval authority remain with the human reviewer.

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

In the future, this form may be connected to a Kotonoha configuration file or profile registry. In this quickstart, however, you do not need to save this YAML in order to run the demo.

## When this story is enough

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

The story is simple:

A writer changes a note. A small model drafts a review. Kotonoha validates the shape. A human decides what it means.

The safe path is:

```text
SLM draft → Kotonoha validation → human review → attach / record decision
```
