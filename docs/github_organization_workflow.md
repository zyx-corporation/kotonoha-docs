# GitHub Organization workflow (short summary)

This page is a **public, abbreviated** companion to how the **Kotonoha (SLS)** Organization uses **GitHub Projects** and custom fields. It does **not** replace Issue or PR text as the source of completion criteria.

## Organization Project

- Use the **canonical cross-repository board** ([Kotonoha (SLS) — project #7](https://github.com/orgs/zyx-corporation/projects/7)) to track work across `kotonoha-spec`, `kotonoha-core`, `kotonoha-cli`, `kotonoha-docs`, and maintainer-only repos that participate on the same board.
- **One board row ≈ one trackable unit**, usually a linked **Issue** (or a PR when the body carries explicit acceptance criteria).
- Prefer **one** Project membership per item: do not duplicate the same Issue on both the Organization Project and a repository-only Project unless you state which is authoritative in the Issue body (see [`docs/github_projects_policy.md`](github_projects_policy.md)).

## Custom fields (meaning)

Align with the maintainers’ definitions:

| Field | Meaning (summary) |
| --- | --- |
| **Status** | Workflow stage (Backlog → In Progress → In Review → Done). **Done** implies the linked change is merged and the Issue acceptance criteria are met—not “we intend to finish”. |
| **Priority** | Relative urgency inside the team (e.g. P0–P3). |
| **Phase** | Development **phase 0–4** as used in the internal phase plan (concept → spec MVP → core → RDE productization → scale). Set **one primary Phase** per item; split child Issues if work spans phases. |
| **Area** | Coarse area (`docs`, `spec`, `core`, `ci`, …). |

**Phase vs milestone:** The **Phase** field is **not** the same as a GitHub **milestone** named e.g. “product MVP”. If both apply, say in the Issue how they relate.

## Truth order

1. Issue / PR description and comments (goals, done-when).  
2. Merged commits on the default branch (and tags when relevant).  
3. Project fields (snapshot for prioritization).  
4. Labels.

Do not treat the board as the only record of “done”.

## Related in this repo

- **[`docs/github_projects_policy.md`](github_projects_policy.md)** — participation and privacy boundary.  
- **[`docs/git_operation_rules.md`](git_operation_rules.md)** — Issue / branch / PR rules (Japanese; mirrored text).

Maintainers keep the **full operational rules** in the private planning repository; public docs stay free of internal-only URLs in Issue bodies when possible.
