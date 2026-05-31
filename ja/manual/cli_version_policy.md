# Kotonoha CLI 推奨バージョン

**更新日:** 2026-05-29  
**対象:** 利用者・UI アダプタ開発者・リリース確認担当

Normative source（仕様正本）: [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)  
CLI 実装: [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli)

English: [`../../en/manual/cli_version_policy.md`](../../en/manual/cli_version_policy.md)

---

## 現在の推奨

| 区分 | バージョン | 備考 |
| --- | --- | --- |
| **推奨（recommended）** | **v0.3.1** | GitHub Latest（2026-05-29 時点） |
| **最小（standalone CLI）** | v0.3.0 | M6 Team Mode 以降の安定実行基盤 |
| **最小（Obsidian CLI backend）** | v0.3.1 | M6 export profile / status env を前提 |
| **最小（VSCode 拡張）** | v0.3.1 | context export / status 連携を前提 |

新規インストールは **v0.3.1** を指定してください。

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash -s -- --version v0.3.1
```

詳細: [CLI インストール](../tutorials/install_kotonoha_cli.md)

---

## UI アダプタとの関係

| UI / モード | CLI 要否 | 要件 |
| --- | --- | --- |
| `obsidian-kotonoha-console` — backend **cli** | 必須 | ≥ v0.3.1（`rde emit` / `rde validate`、任意で `context export`） |
| `obsidian-kotonoha-console` — **mock** / **http** | 不要 | orchestrator または mock RDE |
| `kotonoha-vscode` | 必須 | ≥ v0.3.1（`kotonoha.cliPath` 経由） |

UI アダプタは CLI/Core の振る舞いに従い、仕様を再定義しない。詳細は [現在の公式構成](../architecture/current-official-architecture.md)。

---

## 確認方法

```bash
kotonoha version
```

期待: エラーなく終了し、CLI バージョンと対象 spec bundle に関する行が表示される。

---

## 更新方針

1. **推奨バージョン**は、互換性確認後に GitHub Latest を反映する。
2. **最小バージョン**を上げるときは、同一サイクルで本書・`kotonoha-spec` の informative 節・各 UI リポジトリの互換メモを更新する。
3. 破壊的変更は `kotonoha-spec` の契約更新とセットで扱う。**CLI の実装バージョンは normative spec ではない。**

---

## RDE note

CLI バージョン固定は **運用上の互換ガイド** である。意味監査・frontmatter・sidecar・RDE 出力契約の正本は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) にある。CLI は first stable runtime として spec に従う実行面であり、バージョン番号そのものが仕様を定義しない。

---

## 関連

| 文書 | 内容 |
| --- | --- |
| [install_kotonoha_cli.md](../tutorials/install_kotonoha_cli.md) | インストール手順 |
| [current-official-architecture.md](../architecture/current-official-architecture.md) | 多層構成と優先順位 |
| [obsidian CLI 互換メモ](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/cli-runtime-compatibility.md) | Obsidian Console |
| [VSCode thin console](https://github.com/zyx-corporation/kotonoha-vscode/blob/main/docs/thin-developer-console.ja.md) | VSCode 拡張 |

Governance: [kotonoha-management #167](https://github.com/zyx-corporation/kotonoha-management/issues/167)
