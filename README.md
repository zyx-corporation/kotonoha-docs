# kotonoha-docs

**Public documentation for the Kotonoha ecosystem** that is **not** part of the normative Semantic Lineage System (SLS) specification.

This repository hosts user-facing and contributor-facing materials such as **manuals**, **tutorials**, **how-to guides**, and **supplementary docs**. Stable, review-facing technical specifications belong in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

**Japanese:** [README_ja.md](README_ja.md)

## What belongs here

| Kind | Typical location | Notes |
| --- | --- | --- |
| End-user and operator **manuals** | [`docs/manual/`](docs/manual/README.md) | Task-oriented reference (installation, configuration, operations). |
| **Tutorials** and learning paths | [`docs/tutorials/`](docs/tutorials/README.md) | Step-by-step guides for newcomers. |
| **Contribution** workflow for *this docs repo* | [`CONTRIBUTING.md`](CONTRIBUTING.md) | Distinct from implementation contribution guides in [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core). |
| **Method** (SLS + RDE in our own process) | [`docs/method/`](docs/method/README.md) | How we build Kotonoha using semantic-lineage and RDE-style review—*not* the spec. |
| Other **non-normative** public docs | [`docs/README.md`](docs/README.md) | Glossaries for readers, FAQs, migration notes—without locking API or schema semantics. |

## What does *not* belong here

- **Normative specifications**, schemas, or stability guarantees for implementers → [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).
- **Internal planning, drafts, and non-public decisions** → private [`kotonoha-management`](https://github.com/zyx-corporation/kotonoha-management) (access-controlled).

When documentation must align behavior across implementations, cite or summarize **`kotonoha-spec`** rather than duplicating normative text here.

## Related repositories

Public cross-references only.

| Repository | Role |
| --- | --- |
| [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | Canonical **public specifications** for SLS |
| [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) | OSS **core implementation** and developer docs tied to code |
| **kotonoha-docs (this repository)** | **Non-specification** public documentation (manuals, tutorials, guides) |

## Language policy

**English is the default** for files in this repository. Japanese or other translations may be added alongside the English source. When you add a translation, keep English primary and use the `*_ja.md` suffix for Japanese files (for example, `README.md` / `README_ja.md`).

## License

Unless otherwise stated in a specific file, repository content is licensed under the [Apache License 2.0](LICENSE).

## Links

- Repository: https://github.com/zyx-corporation/kotonoha-docs
- Documentation index: [`docs/README.md`](docs/README.md)
- GitHub Projects (organization workflow): [`docs/github_projects_policy.md`](docs/github_projects_policy.md)
