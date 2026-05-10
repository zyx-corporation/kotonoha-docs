# GitHub Projects (organization workflow)

This repository participates in **zyx-corporation** GitHub **Organization Projects** alongside the public **`kotonoha`** repositories [**`kotonoha-spec`**](https://github.com/zyx-corporation/kotonoha-spec), [**`kotonoha-core`**](https://github.com/zyx-corporation/kotonoha-core), **kotonoha-docs (this repository)**, and [**`kotonoha-cli`**](https://github.com/zyx-corporation/kotonoha-cli).

## Canonical cross-repository board

Organization **Project [Kotonoha (SLS)](https://github.com/orgs/zyx-corporation/projects/7)** (**#7**) tracks work across the public **`kotonoha`** repositories above **and** private operational repositories that participate on the same board (maintainer workspace—**do not** embed internal playbook URLs or private-repo hyperlinks in public Issues). Use Issues and PRs in each repository; add or reference items on the Project for status and priority. The Project README on GitHub duplicates repository links and **lists configured views** (per-repo filters, board, open items).

## Project views (#7)

These views are configured on the board ([project](https://github.com/orgs/zyx-corporation/projects/7)):

| View | Layout | Filter / intent |
| --- | --- | --- |
| [View 1](https://github.com/orgs/zyx-corporation/projects/7/views/1) | Table | All items (rename to *Overview* in the UI if you prefer). |
| [Board (Status)](https://github.com/orgs/zyx-corporation/projects/7/views/2) | Board | Kanban by Status. |
| [kotonoha-spec](https://github.com/orgs/zyx-corporation/projects/7/views/3) | Table | `repo:zyx-corporation/kotonoha-spec` |
| [kotonoha-core](https://github.com/orgs/zyx-corporation/projects/7/views/4) | Table | `repo:zyx-corporation/kotonoha-core` |
| [kotonoha-cli](https://github.com/orgs/zyx-corporation/projects/7/views/5) | Table | `repo:zyx-corporation/kotonoha-cli` |
| [kotonoha-docs](https://github.com/orgs/zyx-corporation/projects/7/views/6) | Table | `repo:zyx-corporation/kotonoha-docs` |
| [View 10](https://github.com/orgs/zyx-corporation/projects/7/views/10) | Table | Private planning-repository slice on the board — keep internal naming out of public Issues |
| [Open items](https://github.com/orgs/zyx-corporation/projects/7/views/8) | Table | `is:open` |

If a legacy view still filters `kotonoha-project`, remove it in the Project UI (API update for views is limited). Configuration uses the REST API `POST /orgs/zyx-corporation/projectsV2/7/views` with header `X-GitHub-Api-Version: 2026-03-10`.

## For contributors

- Use **GitHub Issues** to propose documentation gaps and **Pull Requests** to submit changes.
- **Completion criteria** live in the Issue and PR bodies (and merged content), not only in a board column.
- Maintainers may mirror progress on shared Organization Projects (status, priority). If an Item is marked **Done** on a board, the linked Issue should reflect the same outcome (typically after the PR is merged).

## Language

Issues and PRs in this repository follow the repository **English-first** policy (see the top-level `README.md`).

## Privacy / public boundary

Do not require private repository names or internal-only codenames in public Issue or documentation text. Keep public artifacts reviewable without access to private repos.

For maintainer-only operational detail on Project fields and triage, follow maintainer-directed channels rather than exporting internal playbook text into Issues.
