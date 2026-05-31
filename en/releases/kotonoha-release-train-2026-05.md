# Kotonoha Release Train 2026-05

**Theme:** First UI hardening and convergence baseline  
**Published:** 2026-05-31  
**Japanese:** [`../../ja/releases/kotonoha-release-train-2026-05.md`](../../ja/releases/kotonoha-release-train-2026-05.md)

---

## Overview

This Release Train extends **single-repo releases** into a **Kotonoha-wide distribution unit**. Each module keeps its **own version number**; versions are not forced to align.

| Label | Meaning |
| --- | --- |
| **Kotonoha Release Train 2026-05** | First UI hardening baseline as of May 2026 |
| **v0.3 train** | Obsidian first UI hardening + CLI runtime parity generation |

---

## Primary distribution (Included Components)

| Component | Version / Ref | Commit (short) | Role | Stability |
| --- | --- | --- | --- | --- |
| [obsidian-kotonoha-console](https://github.com/zyx-corporation/obsidian-kotonoha-console) | **v0.3.0** | [`10a9d6c`](https://github.com/zyx-corporation/obsidian-kotonoha-console/commit/10a9d6c830440a51ca47160d107697867a2e60f9) | First usable UI | **Stable (UI)** |
| [kotonoha-cli](https://github.com/zyx-corporation/kotonoha-cli) | **v0.3.1** | [`1e99139`](https://github.com/zyx-corporation/kotonoha-cli/commit/1e9913971f653fe45a07224678b93304a30adc77) | First stable runtime | **Stable (runtime)** |
| [kotonoha-spec](https://github.com/zyx-corporation/kotonoha-spec) | main @ train cut | [`3e72ad5`](https://github.com/zyx-corporation/kotonoha-spec/commit/3e72ad54d68e4f2d4db2b3664c2a70df656e0bd8) | Normative source | **Normative** |
| [kotonoha-core](https://github.com/zyx-corporation/kotonoha-core) | **v0.1.16** | [`b345756`](https://github.com/zyx-corporation/kotonoha-core/commit/b345756b57f2242c4158aea0f552d3c1b5f1c18f) | Shared implementation layer | **Stable (library)** |
| [kotonoha-orchestrator](https://github.com/zyx-corporation/kotonoha-orchestrator) | api **v0.1.0** @ train cut | [`9b079d1`](https://github.com/zyx-corporation/kotonoha-orchestrator/commit/9b079d131b6f147230289cd9370d669ce4414591) | Stable adapter for `/v1/rde/evaluate` | **Stable adapter (partial)** |
| [kotonoha-vscode](https://github.com/zyx-corporation/kotonoha-vscode) | **v0.1.0** @ train cut | [`ddefd33`](https://github.com/zyx-corporation/kotonoha-vscode/commit/ddefd33a0757015b0c86e59b1872fa39987bdc16) | Thin Developer Console (M3) | **Stable (extension)** |
| [kotonoha-docs](https://github.com/zyx-corporation/kotonoha-docs) | main @ train cut | [`d0e4b53`](https://github.com/zyx-corporation/kotonoha-docs/commit/d0e4b537f86fd0a5fc4741daaf13f3dee45903fe) | Documentation entrypoint | **Informative** |

### Binary releases

| Component | GitHub Release | Install |
| --- | --- | --- |
| obsidian-kotonoha-console | [v0.3.0](https://github.com/zyx-corporation/obsidian-kotonoha-console/releases/tag/v0.3.0) | [install_obsidian_kotonoha_console.md](../manual/install_obsidian_kotonoha_console.md) |
| kotonoha-cli | [v0.3.1](https://github.com/zyx-corporation/kotonoha-cli/releases/tag/v0.3.1) | [install_kotonoha_cli.md](../tutorials/install_kotonoha_cli.md) |

Obsidian install path: `<vault>/.obsidian/plugins/kotonoha-console/` (rename zip folder to `kotonoha-console` after unzip).

---

## Secondary (Expansion layer — reference only)

Per [kotonoha-spec MCP/gateway expansion boundary](https://github.com/zyx-corporation/kotonoha-spec), these are **not formal stable distribution targets** in this train. Commits are pinned for reference.

| Component | Commit (short) | Role | Train status |
| --- | --- | --- | --- |
| [kotonoha-mcp](https://github.com/zyx-corporation/kotonoha-mcp) | [`b8c7d74`](https://github.com/zyx-corporation/kotonoha-mcp/commit/b8c7d7438d1bb23d42dbea7d5d402ee7e629a572) | MCP integration skeleton | Expansion / experimental |
| [kotonoha-gateway](https://github.com/zyx-corporation/kotonoha-gateway) | [`3421949`](https://github.com/zyx-corporation/kotonoha-gateway/commit/34219491b48f2534e26da19e7dbd7932210c2fb8) | Gateway expansion | Expansion / experimental |
| [kotonoha-web-console](https://github.com/zyx-corporation/kotonoha-web-console) | [`b11c68d`](https://github.com/zyx-corporation/kotonoha-web-console/commit/b11c68dacbb39b3988425bc9a86171eee21b4b90) | Web console workflows | Expansion / experimental |

---

## Stable / Experimental Boundary

### Stable (daily-use expectations in this train)

- `kotonoha-cli` **v0.3.1**
- `obsidian-kotonoha-console` **v0.3.0**
- orchestrator `/health`
- orchestrator `/v1/agents`
- orchestrator `/v1/rde/evaluate`

### Experimental / deferred

- `/v1/proposals/generate` — best-effort
- local rule-based / CLI interchange skeleton — **not full RDE evaluation**
- MCP integration
- gateway expansion
- web-console workflows
- sidecar ↔ CLI/M6 export correlation (v0.4)
- advanced partial apply UX (v0.4)

---

## RDE check

### Preserved Elements

The v0.3 train centers on **Obsidian first UI hardening**. Kotonoha remains spec-first, human-reviewed, and RDE-auditable.

### Authorized Transformations

Extension from single-repo release to **Release Train** documentation with cross-module compatibility in one view.

### Drift Risks

- Treating expansion layer repos as formally stable
- Mistaking `/v1/proposals/generate` for stable behavior
- Mistaking local/CLI audit paths for full RDE evaluation
- Mistaking `.kotonoha/` sidecars for complete SLS storage

### Next Revision Policy

Revise Release Train 2026-05 only for corrective v0.3.x hardening. Deeper integration belongs to the v0.4 epic.

---

## Related

- [obsidian v0.3 dogfood record](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/v0.3-dogfood-record.ja.md)
- [CLI version policy](../manual/cli_version_policy.md)
