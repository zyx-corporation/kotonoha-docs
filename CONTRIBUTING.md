# Contributing to kotonoha-docs

Thank you for helping improve public documentation for the Kotonoha ecosystem. This guide applies to **this repository** (`kotonoha-docs`). For contributing to the **specification**, use [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec). For contributing to **code**, use [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core).

## Principles

1. **Do not introduce normative behavior** here. If a change would define how implementations must behave, it belongs in `kotonoha-spec`. This repo may explain, summarize, and link to specifications.
2. **Prefer clarity over completeness** in tutorials; link out for edge cases.
3. **English-first** for new documents; add `*_ja.md` for Japanese translations aligned with the English source.

## Workflow

1. Open an **Issue** (or comment on an existing one) describing the doc gap: audience, scenario, and scope.
2. Open a **Pull Request** with focused changes. Large doc sets should be split when possible for review.
3. Use descriptive titles and explain **who the reader is** in the PR body.

## Style

- Use Markdown (`.md`). Prefer one topic per page where practical.
- Use relative links inside this repository; use absolute GitHub URLs only when linking across repositories.
- Diagrams: SVG or Mermaid in Markdown where supported; otherwise describe in text and link assets under `docs/assets/` when added.

## Organization layout

| Area | Path |
| --- | --- |
| Manual-style reference | [`docs/manual/`](docs/manual/README.md) |
| Tutorials | [`docs/tutorials/`](docs/tutorials/README.md) |
| Index | [`docs/README.md`](docs/README.md) |

## Reviews

Maintainers may request alignment with `kotonoha-spec` terminology. If you are unsure whether content is specification-level, ask in the Issue before investing in a large rewrite.

## GitHub Projects

See [`docs/github_projects_policy.md`](docs/github_projects_policy.md) for how this repo participates in organization Projects.
