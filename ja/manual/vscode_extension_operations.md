# Kotonoha VS Code 拡張 — 操作マニュアル

VS Code / Cursor 上で **MeaningDelta（ΔM）・RDE・Review** を扱う [`kotonoha-vscode`](https://github.com/zyx-corporation/kotonoha-vscode) の利用手順です。

**仕様（非規範）:** [kotonoha-management M3 草案](https://github.com/zyx-corporation/kotonoha-management/blob/main/docs/29_m3_minimal_ui_spec_draft.md)  
**受け入れチェックリスト:** [kotonoha-vscode `docs/m3_acceptance.md`](https://github.com/zyx-corporation/kotonoha-vscode/blob/main/docs/m3_acceptance.md)  
**CLI 契約:** [`kotonoha-cli` `cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md)

英語版: [`../../en/manual/vscode_extension_operations.md`](../../en/manual/vscode_extension_operations.md)

---

## 1. 前提

| 項目 | 要件 |
| --- | --- |
| IDE | VS Code **1.85+** または Cursor |
| CLI | [`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) **≥ 0.2.4**（`status` / `delta` / `review` 付きビルド） |
| Core | **≥ 0.1.9**（CLI 経由） |
| PostgreSQL | サーバー起動済み・**空 DB 作成済み**・`kotonoha db migrate` 済み |
| ワークスペース | **Git リポジトリ**をフォルダとして開く（Extension 開発フォルダ単体ではない） |

### 1.1 データベース（migrate の前に必須）

`kotonoha db migrate` は **既存データベース内にテーブルを作る**だけです。DB・ユーザーの作成は別途必要です。

**Docker 例（`-p 5432:5432` 必須 — ホストから接続するため）:**

```bash
docker run -d --name kotonoha-pg \
  -e POSTGRES_USER=YOUR_USER \
  -e POSTGRES_PASSWORD='YOUR_PASSWORD' \
  -e POSTGRES_DB=YOUR_DB \
  -p 5432:5432 \
  postgres:16-alpine

export DATABASE_URL='postgres://YOUR_USER:YOUR_PASSWORD@localhost:5432/YOUR_DB'
kotonoha db migrate
```

`docker ps` で `0.0.0.0:5432->5432/tcp` を確認してください。ポート未公開だと Extension / CLI とも `connection or query failed` になります。

### 1.2 CLI ビルド（PATH に無い場合）

```bash
cd kotonoha-cli && cargo build --release
# フルパス例:
# /path/to/kotonoha-cli/target/release/kotonoha
```

古い `release` バイナリだと `status` サブコマンドが無い場合があります。更新後に再ビルドしてください。

---

## 2. 拡張の入手と起動

### 2.1 開発モード（F5）

1. **`kotonoha-vscode` リポジトリ**を IDE で開く（検証用 Git プロジェクトではない）。
2. `npm install && npm run compile`
3. **実行とデバッグ** → **Run Extension**（またはエディタにフォーカスして **F5**）。  
   **ターミナルにフォーカスしたまま F5 しても動きません。**
4. 開いた **Extension Development Host（別ウィンドウ）** で、検証用 repo を **ファイル → フォルダーを開く**。

### 2.2 設定（ワークスペース）

Extension Development Host 側で、**開いた Git プロジェクト**のワークスペース設定:

`Cmd+Shift+P` → **Preferences: Open Workspace Settings (JSON)**

```json
{
  "kotonoha.cliPath": "/path/to/kotonoha-cli/target/release/kotonoha",
  "kotonoha.databaseUrl": "postgres://USER:PASSWORD@localhost:5432/DBNAME",
  "kotonoha.decidedBy": "you@example.com"
}
```

- `databaseUrl` は **migrate と同じ完全 URL**（`@localhost:5432/DB名` まで）。
- **Git にコミットしない**。

任意: 検証 repo で `kotonoha init` → `.kotonoha/config.toml` ができる。

---

## 3. 画面構成

Activity Bar の **Kotonoha** アイコン → サイドバーに 3 パネル:

| パネル | 役割 |
| --- | --- |
| **Context** | Git / DB 状態、編集中ファイル・選択範囲 |
| **Meaning Delta** | ΔM 登録（`kotonoha delta create`） |
| **RDE & Review** | RDE 添付、Review、m2 export |

各パネル**タイトルバー左**の **Kotonoha アイコン**でサイドバーを開き直せます。右側に Refresh や他パネルへ移るボタンがあります。

---

## 4. ショートカット（既定）

| 操作 | macOS | Windows / Linux |
| --- | --- | --- |
| Kotonoha サイドバー | `Cmd+Alt+K` | `Ctrl+Alt+K` |
| Context パネル | `Cmd+Alt+Shift+C` | `Ctrl+Alt+Shift+C` |
| Meaning Delta パネル | `Cmd+Alt+Shift+M` | `Ctrl+Alt+Shift+M` |
| RDE & Review パネル | `Cmd+Alt+Shift+R` | `Ctrl+Alt+Shift+R` |
| Register ΔM（パネル表示） | `Cmd+Alt+Shift+D` | `Ctrl+Alt+Shift+D` |

変更: **キーボード ショートカット** で `kotonoha` を検索。

コマンドパレット（`Cmd+Shift+P`）でも `Kotonoha:` から同じ操作が選べます。

---

## 5. 基本ワークフロー

### 5.1 Context

1. 対象ファイルを開き、必要なら行を選択。
2. **Context** → **Refresh**。
3. `database: connected` を確認。

### 5.2 Meaning Delta

1. **Meaning Delta** を開く（ショートカット可）。
2. *Intended change* など入力（任意）。
3. **Register ΔM** → 成功時 **UUID** 表示。

### 5.3 RDE & Review

1. ターミナルで RDE JSON を用意:

   ```bash
   kotonoha rde emit | pbcopy
   ```

2. **Paste RDE from clipboard** または JSON ファイルで **Attach**。
3. **Refresh export preview** で assessment / 警告を確認。
4. **Approve** / Hold / Reject（人間責任の文言を確認）。
5. **Copy export (m2)** でクリップボードに JSON。

---

## 6. よくあるトラブル

| 症状 | 対処 |
| --- | --- |
| `unrecognized subcommand 'status'` | CLI を **再ビルド**（≥ 0.2.4）、`cliPath` を新バイナリに |
| `database: connection or query failed` | Docker の **`-p 5432:5432`**、`databaseUrl` の完全 URL、Postgres 起動 |
| `DATABASE_URL not set`（ターミナル） | `export DATABASE_URL=...` はターミナル専用。Extension は `kotonoha.databaseUrl` |
| パネルのアンカーが古い | ファイル切替後 **Refresh** またはショートカットでパネル再表示（自動更新あり） |
| F5 が効かない | **Run and Debug** から起動。`kotonoha-vscode` フォルダを開いているか確認 |

---

## 7. 関連資料

- [最初の CLI セッション](../tutorials/first_cli_session.md)
- [Phase 2 CLI 受け入れ](../acceptance/phase2_cli_acceptance_demo.md)
- [M2 CLI デモ](https://github.com/zyx-corporation/kotonoha-cli/blob/main/scripts/m2_acceptance_demo.sh)

---

## 改訂履歴

| 日付 | 内容 |
| --- | --- |
| 2026-05-20 | 初版（M3 操作・ショートカット・DB 前提） |
