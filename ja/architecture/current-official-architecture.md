# Kotonoha 現在の公式構成

Kotonoha は、単一アプリケーションではなく、仕様、共通実装、CLI、UIアダプタからなる多層システムとして整理する。

Normative source（英語正本）: [`kotonoha-spec` `docs/current-official-architecture.md`](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/current-official-architecture.md)

## 現在の優先順位

1. `kotonoha-spec` を正本とする。
2. `kotonoha-cli` を first stable runtime とする。
3. `obsidian-kotonoha-console` を first usable UI として dogfood する。
4. `kotonoha-vscode` は thin Developer Console として育てる。
5. orchestrator / MCP / gateway / web console は、上記が安定してから拡張する。

## リポジトリの役割

| Repository | 役割 |
| --- | --- |
| `kotonoha-spec` | frontmatter、sidecar、handoff、RDE audit、project/principal identity の正本 |
| `kotonoha-core` | 共通実装ロジック |
| `kotonoha-cli` | 安定実行基盤 |
| `obsidian-kotonoha-console` | 文脈・レビュー・RDE監査の first usable UI |
| `kotonoha-vscode` | CLI/Core に接続する開発者向け thin UI |
| `kotonoha-docs` | 利用者・開発者向け文書 |
| `kotonoha-management` | 計画・issue統制 |
| `kotonoha-orchestrator` | RDE/orchestration backend |
| `kotonoha-mcp` | MCP連携 |
| `kotonoha-gateway` | gateway / integration boundary |
| `kotonoha-web-console` | 将来のWeb UI候補 |

## 設計上の注意

`kotonoha-vscode` は AI coding agent ではない。

`obsidian-kotonoha-console` は CLI の代替ではない。

`kotonoha-cli` は仕様正本ではない。

仕様正本は `kotonoha-spec` である。

## 現在の焦点

現在の焦点は、機能を増やすことではなく、次の4点を安定させることにある。

- 仕様正本の明確化
- CLI 実行基盤の安定化
- Obsidian UI の dogfood
- VSCode UI の thin adapter 化

## CLI 推奨バージョン

| 区分 | バージョン |
| --- | --- |
| 推奨 | **v0.3.1** |
| 最小（standalone CLI） | v0.3.0 |
| 最小（Obsidian / VSCode） | v0.3.1 |

詳細・更新方針: [CLI 推奨バージョン](../manual/cli_version_policy.md)

`kotonoha-cli` は実行基盤であり仕様正本ではない。契約の正本は `kotonoha-spec` である。

## 関連

- CLI 推奨バージョン: [cli_version_policy.md](../manual/cli_version_policy.md)
- Obsidian dogfood: [`obsidian-kotonoha-console` `docs/dogfood-acceptance.ja.md`](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/dogfood-acceptance.ja.md)
- VSCode thin console: [`kotonoha-vscode` `docs/thin-developer-console.ja.md`](https://github.com/zyx-corporation/kotonoha-vscode/blob/main/docs/thin-developer-console.ja.md)
