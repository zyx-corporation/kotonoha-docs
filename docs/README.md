# Documentation index

Welcome to **kotonoha-docs**. These pages support readers and operators without replacing the canonical specification in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

## Current preferred language roots

Reader-facing documentation now uses repository-root language areas:

| Language | Preferred root |
| --- | --- |
| English | [`../en/`](../en/README.md) |
| Japanese | [`../ja/`](../ja/README.md) |

The historical `docs/` directory remains available as a compatibility and transition area. New reader-facing documents should prefer `en/` and `ja/` unless they are repository tooling, governance, or transitional notes.

## Migrated sections

| Legacy section | Preferred English location | Preferred Japanese location |
| --- | --- | --- |
| [`method/`](method/README.md) / [`method_ja/`](method_ja/README.md) | [`../en/method/`](../en/method/README.md) | [`../ja/method/`](../ja/method/README.md) |
| [`tutorials/`](tutorials/README.md) / [`tutorials_ja/`](tutorials_ja/README.md) | [`../en/tutorials/`](../en/tutorials/README.md) | [`../ja/tutorials/`](../ja/tutorials/README.md) |
| [`acceptance/`](acceptance/README.md) / [`acceptance_ja/`](acceptance_ja/README.md) | [`../en/acceptance/`](../en/acceptance/README.md) | [`../ja/acceptance/`](../ja/acceptance/README.md) |
| [`manual/`](manual/README.md) | [`../en/manual/`](../en/manual/README.md) | [`../ja/manual/`](../ja/manual/README.md) |

## Repository governance and tooling documents

| Document | Purpose |
| --- | --- |
| [Rendering policy](rendering_policy.md) | SVG-first rendering and HTML publication workflow. |
| [Git/Issue/PR workflow](git_operation_rules.md) | Organization-wide Issue/branch/PR rules (**Japanese**, this `docs/` file). |
| [GitHub Organization workflow](github_organization_workflow.md) | Short English summary of Organization **Projects** fields and truth order. |
| [GitHub Organization workflow（日本語）](github_organization_workflow_ja.md) | 上記の日本語版。 |
| [GitHub Projects policy](github_projects_policy.md) | Organization project-board usage policy. |

## Relationship to the specification

- **`kotonoha-spec`** holds normative definitions implementers rely on.
- **This repository** holds explanatory and procedural material. If there is a conflict, **`kotonoha-spec` wins**; update tutorials and acceptance demos here after specification changes when needed.
- **Tutorials** teach workflows and concepts.
- **Acceptance demos** validate public behavior for a phase; they are not learning tutorials.

## Contributing

See the top-level [CONTRIBUTING.md](../CONTRIBUTING.md).
