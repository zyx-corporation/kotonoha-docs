# Kotonoha Release Train 2026-05

**テーマ:** First UI hardening and convergence baseline  
**公開日:** 2026-05-31  
**English:** [`../../en/releases/kotonoha-release-train-2026-05.md`](../../en/releases/kotonoha-release-train-2026-05.md)

---

## 概要

本 Release Train は、**単一 repo の release を Kotonoha 全体の配布単位へ拡張**したものです。各モジュールは **個別の実バージョン** を保持します。バージョン番号を無理に揃えません。

| 配布ラベル | 意味 |
| --- | --- |
| **Kotonoha Release Train 2026-05** | 2026年5月時点の First UI hardening ベースライン |
| **v0.3 train** | Obsidian first UI hardening と CLI runtime parity を中心とした世代 |

---

## 第一配布対象（Included Components）

| Component | Version / Ref | Commit (short) | Role | Stability |
| --- | --- | --- | --- | --- |
| [obsidian-kotonoha-console](https://github.com/zyx-corporation/obsidian-kotonoha-console) | **v0.3.0** | [`10a9d6c`](https://github.com/zyx-corporation/obsidian-kotonoha-console/commit/10a9d6c830440a51ca47160d107697867a2e60f9) | First usable UI | **Stable (UI)** |
| [kotonoha-cli](https://github.com/zyx-corporation/kotonoha-cli) | **v0.3.1** | [`1e99139`](https://github.com/zyx-corporation/kotonoha-cli/commit/1e9913971f653fe45a07224678b93304a30adc77) | First stable runtime | **Stable (runtime)** |
| [kotonoha-spec](https://github.com/zyx-corporation/kotonoha-spec) | main @ train cut | [`3e72ad5`](https://github.com/zyx-corporation/kotonoha-spec/commit/3e72ad54d68e4f2d4db2b3664c2a70df656e0bd8) | Normative source | **Normative** |
| [kotonoha-core](https://github.com/zyx-corporation/kotonoha-core) | **v0.1.16** | [`b345756`](https://github.com/zyx-corporation/kotonoha-core/commit/b345756b57f2242c4158aea0f552d3c1b5f1c18f) | Shared implementation layer | **Stable (library)** |
| [kotonoha-orchestrator](https://github.com/zyx-corporation/kotonoha-orchestrator) | api **v0.1.0** @ train cut | [`9b079d1`](https://github.com/zyx-corporation/kotonoha-orchestrator/commit/9b079d131b6f147230289cd9370d669ce4414591) | Stable adapter for `/v1/rde/evaluate` | **Stable adapter (partial)** |
| [kotonoha-vscode](https://github.com/zyx-corporation/kotonoha-vscode) | **v0.1.0** @ train cut | [`ddefd33`](https://github.com/zyx-corporation/kotonoha-vscode/commit/ddefd33a0757015b0c86e59b1872fa39987bdc16) | Thin Developer Console (M3) | **Stable (extension)** |
| [kotonoha-docs](https://github.com/zyx-corporation/kotonoha-docs) | main @ train cut | [`d0e4b53`](https://github.com/zyx-corporation/kotonoha-docs/commit/d0e4b537f86fd0a5fc4741daaf13f3dee45903fe) | Documentation entrypoint | **Informative** |

### バイナリ配布あり

| Component | GitHub Release | Install |
| --- | --- | --- |
| obsidian-kotonoha-console | [v0.3.0](https://github.com/zyx-corporation/obsidian-kotonoha-console/releases/tag/v0.3.0) | [install_obsidian_kotonoha_console.md](../manual/install_obsidian_kotonoha_console.md) |
| kotonoha-cli | [v0.3.1](https://github.com/zyx-corporation/kotonoha-cli/releases/tag/v0.3.1) | [install_kotonoha_cli.md](../tutorials/install_kotonoha_cli.md) |

Obsidian 配置パス: `<vault>/.obsidian/plugins/kotonoha-console/`（zip 展開後は `kotonoha-console` へリネーム）

---

## 第二配布対象（Expansion layer — 同梱説明のみ）

[kotonoha-spec MCP/gateway expansion boundary](https://github.com/zyx-corporation/kotonoha-spec) に従い、以下は **今回の正式安定配布物ではない**。参照 commit のみ固定します。

| Component | Commit (short) | Role | Train 上の位置づけ |
| --- | --- | --- | --- |
| [kotonoha-mcp](https://github.com/zyx-corporation/kotonoha-mcp) | [`b8c7d74`](https://github.com/zyx-corporation/kotonoha-mcp/commit/b8c7d7438d1bb23d42dbea7d5d402ee7e629a572) | MCP integration skeleton | Expansion / experimental |
| [kotonoha-gateway](https://github.com/zyx-corporation/kotonoha-gateway) | [`3421949`](https://github.com/zyx-corporation/kotonoha-gateway/commit/34219491b48f2534e26da19e7dbd7932210c2fb8) | Gateway expansion | Expansion / experimental |
| [kotonoha-web-console](https://github.com/zyx-corporation/kotonoha-web-console) | [`b11c68d`](https://github.com/zyx-corporation/kotonoha-web-console/commit/b11c68dacbb39b3988425bc9a86171eee21b4b90) | Web console workflows | Expansion / experimental |

---

## Stable / Experimental Boundary

### Stable（本 train で daily-use を期待してよい）

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
- sidecar ↔ CLI/M6 export correlation（v0.4）
- advanced partial apply UX（v0.4）

---

## v0.3 Epic 対応（obsidian-kotonoha-console）

| Issue | 内容 |
| --- | --- |
| #38 | Audit engine labeling |
| #39 | CLI backend dogfood parity |
| #40 | Note I/O completion |
| #41 | Sidecar spec alignment |
| #42 | Settings / connection UX |
| #43 | Release v0.3.0 |

Parent: [kotonoha-management#168](https://github.com/zyx-corporation/kotonoha-management/issues/168)

---

## RDE check

### Preserved Elements

v0.3 train の主役は **Obsidian first UI hardening** である。Kotonoha は spec-first、human-reviewed、RDE-auditable のまま。

### Authorized Transformations

単一 repo release から **Release Train** への拡張。CLI / spec / core / orchestrator / docs との互換性を一枚で示す。

### Inferred Extensions

Engine labeling、sidecar validation、CLI parity、Note I/O hardening が v0.3 acceptance criteria として必須化。

### Unresolved Elements

MCP / gateway / web-console をいつ正式配布物に昇格させるか。Git context export、partial apply UX、sidecar/export correlation（v0.4）。

### Drift Risks

- expansion layer を「正式安定版」と誤認すること
- `/v1/proposals/generate` を stable と誤認すること
- local / CLI audit を full RDE と誤認すること
- `.kotonoha/` sidecar を complete SLS storage と誤認すること

### Next Revision Policy

v0.3.x は corrective hardening のみ。Release Train 2026-05 は v0.4 epic 開始まで改訂しない（緊急修正を除く）。

---

## 関連

- [obsidian v0.3 dogfood record](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/v0.3-dogfood-record.ja.md)
- [CLI version policy](../manual/cli_version_policy.md)
- [orchestrator API stability boundary](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/orchestrator-api-stability-boundary.md)
