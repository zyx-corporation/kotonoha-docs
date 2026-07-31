# kotonoha-docs

**Public documentation for the Kotonoha ecosystem** that is **not** part of the normative Semantic Lineage System (SLS) specification.

This repository hosts user-facing and contributor-facing materials such as **beginner guides**, **concept explanations**, **manuals**, **tutorials**, **how-to guides**, **acceptance demos**, **reference papers**, and **supplementary docs**. Stable, review-facing technical specifications belong in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

## Start here

For Japanese readers, the beginner path now starts here:

- [はじめての Kotonoha](ja/start-here.md)
- [初学者向け用語集](ja/glossary_for_beginners.md)
- [読者別ラーニングパス](ja/learning-path.md)

The English beginner path is not yet fully mirrored. Until then, English readers should start with [en/README.md](en/README.md) and [en/concepts/kotonoha_concept_overview.md](en/concepts/kotonoha_concept_overview.md).

## Language roots

Reader-facing documentation is organized under repository-root language areas:

| Language | Area | Notes |
| --- | --- | --- |
| English | [`en/`](en/README.md) | English documentation area. Beginner mirror is pending. |
| Japanese | [`ja/`](ja/README.md) | 日本語ドキュメント領域。初学者向け導線を先行整備中。 |

The English and Japanese areas should normally use the same structure and contain translation pairs or equivalent companion documents. When one language leads temporarily, the corresponding location in the other language should link to the available source or state that translation is pending.

Historical material under [`docs/`](docs/README.md) remains available when needed, but new conceptual and explanatory documents should prefer `en/` and `ja/`.

## Quick trial path

For the current Japanese beginner flow:

| Step | Document | Goal |
| --- | --- | --- |
| 1 | [Kotonoha CLI のインストール](ja/tutorials/install_kotonoha_cli.md) | Run `kotonoha version` |
| 2 | [最初の CLI セッション](ja/tutorials/first_cli_session.md) | Try `kotonoha rde emit` and `validate --strict` |
| 3 | [RDE draft assistance quickstart](ja/tutorials/rde_draft_assistance.md) | Learn draft → validate → attach → human review |

PostgreSQL, Obsidian, VS Code, Release Train, and acceptance demos are not required for this first trial.

## Rendering and figures

Figures in this repository should generally be written as SVG. The default publication path is Markdown plus SVG references rendered to static HTML by [`tools/render_docs.py`](tools/render_docs.py). Direct HTML authoring is also allowed when layout, interaction, or print/PDF control requires it.

See [`docs/rendering_policy.md`](docs/rendering_policy.md) for the SVG-first figure policy and rendering workflow.

## What belongs here

| Kind | Preferred location | Notes |
| --- | --- | --- |
| Beginner guides | [`ja/start-here.md`](ja/start-here.md), [`ja/glossary_for_beginners.md`](ja/glossary_for_beginners.md), [`ja/learning-path.md`](ja/learning-path.md) | First entry points for newcomers. English mirrors are pending. |
| Conceptual explanations | `en/concepts/`, `ja/concepts/` | Reader-facing explanations of SLS, semantic lineage, ΔM, RDE, memory layer, and related concepts. |
| End-user and operator **manuals** | [`en/manual/`](en/manual/README.md), [`ja/manual/`](ja/manual/README.md) | Task-oriented reference. |
| **Tutorials** and learning paths | [`en/tutorials/`](en/tutorials/README.md), [`ja/tutorials/`](ja/tutorials/README.md) | Step-by-step guides for newcomers. |
| **Acceptance demos** | [`en/acceptance/`](en/acceptance/README.md), [`ja/acceptance/`](ja/acceptance/README.md) | Procedural validation checks; not tutorials. |
| **Method** | [`en/method/`](en/method/README.md), [`ja/method/`](ja/method/README.md) | How we build Kotonoha using SLS and RDE-style review; not the spec. |
| **Paper reference material** | [`ja/paper/`](ja/paper/README.md) | Academic papers and preprints as non-normative background material; not a substitute for `kotonoha-spec`. |
| Contribution workflow for this docs repo | [`CONTRIBUTING.md`](CONTRIBUTING.md) | Distinct from implementation contribution guides. |

## What does *not* belong here

- **Normative specifications**, schemas, or stability guarantees for implementers → [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).
- **Internal planning and non-public decisions** → not authored in repositories under this umbrella; collaborator-only workflows handle material that stays off the public web.

When documentation must align behavior across implementations, cite or summarize **`kotonoha-spec`** rather than duplicating normative text here.

## Related repositories

Public cross-references only.

| Repository | Role |
| --- | --- |
| [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | Canonical **public specifications** for SLS |
| [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) | OSS **core implementation** and developer docs tied to code |
| [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli) | Official **`kotonoha`** CLI ([definition](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md)) |
| **kotonoha-docs (this repository)** | **Non-specification** public documentation (manuals, tutorials, acceptance demos, guides, conceptual explanations, reference papers) |

## License

Unless otherwise stated in a specific file, repository content is licensed under the [Apache License 2.0](LICENSE).

## Links

- Repository: https://github.com/zyx-corporation/kotonoha-docs
- Japanese beginner start: [`ja/start-here.md`](ja/start-here.md)
- English docs: [`en/`](en/README.md)
- Japanese docs: [`ja/`](ja/README.md)
- Historical documentation index: [`docs/README.md`](docs/README.md)
- Rendering policy: [`docs/rendering_policy.md`](docs/rendering_policy.md)
- GitHub Projects (organization workflow): [`docs/github_projects_policy.md`](docs/github_projects_policy.md)
