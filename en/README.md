# Kotonoha documentation — English

This is the English documentation area for the Kotonoha ecosystem.

`kotonoha-docs` contains explanatory and procedural material. It does **not** define normative SLS requirements. Canonical specifications belong in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec).

Japanese counterpart: [`../ja/README.md`](../ja/README.md)

## Sections

| Section | Purpose | Current source during migration |
| --- | --- | --- |
| [Method](method/README.md) | How the project applies SLS + RDE in its own work | Mirrors `docs/method/` |
| [Manual](manual/README.md) | Reference-style usage and operation topics | Mirrors `docs/manual/` |
| [Tutorials](tutorials/README.md) | Learning-oriented step-by-step guides | Mirrors `docs/tutorials/` |
| [Acceptance demos](acceptance/README.md) | Validation-oriented public behavior checks | Mirrors `docs/acceptance/` |

## Placement rule

Conceptual and explanatory documents should normally live under this repository. When exact semantics, conformance, schemas, or versioning rules are needed, link to [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) instead of duplicating normative text.

## Migration note

The historical `docs/` directory remains available during migration. New reader-facing English documents should prefer the `en/` tree and keep the corresponding Japanese location under `ja/` aligned where possible.
