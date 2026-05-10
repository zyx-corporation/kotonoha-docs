# Documentation index

Welcome to **kotonoha-docs**. These pages support readers and operators without replacing the canonical specification in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

## Sections

| Section | Purpose |
| --- | --- |
| [Method](method/README.md) | How Kotonoha development applies **SLS + RDE** in practice (non-normative). |
| [Method Japanese](method_ja/README.md) | 日本語版のMethod文書。 |
| [Manual](manual/README.md) | Reference-style topics (setup, operations, troubleshooting). |
| [Tutorials](tutorials/README.md) | Guided learning paths and hands-on exercises. |
| [Tutorials (Japanese)](tutorials_ja/README.md) | 日本語チュートリアル（`docs/tutorials_ja/`）。 |
| [Acceptance demos](acceptance/README.md) | Procedural validation checks with expected commands, outputs, and exit codes. |
| [Acceptance demos (Japanese)](acceptance_ja/README.md) | 日本語の受入デモ手順（`docs/acceptance_ja/`）。 |
| Git / Issue / PR | [git_operation_rules.md](git_operation_rules.md) | Organization-wide Git workflow (Japanese; mirrored from **`kotonoha-management` canonical** [`04_git_operation_rules.md`](https://github.com/zyx-corporation/kotonoha-management/blob/main/docs/04_git_operation_rules.md)). |

## Relationship to the specification

- **`kotonoha-spec`** holds normative definitions implementers rely on.
- **This repository** holds explanatory and procedural material. If there is a conflict, **`kotonoha-spec` wins**; update tutorials and acceptance demos here after specification changes when needed.
- **Tutorials** teach workflows and concepts.
- **Acceptance demos** validate public behavior for a phase; they are not learning tutorials.

## Contributing

See the top-level [CONTRIBUTING.md](../CONTRIBUTING.md).
