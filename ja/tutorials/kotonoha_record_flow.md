# Kotonoha record flow quickstart

この文書は、検証済みの RDE 草案を DB-backed な Kotonoha record として残すための最小手順です。

**前提:** [SLM デモ quickstart](slm_demo_quickstart.md) で `rde-draft.json` を作成し、`kotonoha rde validate --strict` に通していること。

英語版: [`../../en/tutorials/kotonoha_record_flow.md`](../../en/tutorials/kotonoha_record_flow.md)

## この文書で扱うこと

この文書では、次を扱います。

1. ローカル PostgreSQL を用意する。
2. `DATABASE_URL` を設定する。
3. `kotonoha db migrate` を実行する。
4. `delta create` で MeaningDelta record の器を作る。
5. `rde attach` で検証済み RDE 草案を添付する。
6. `review hold` で人間の判断を記録する。
7. `export` で記録を確認する。

この文書は本番 DB 運用ガイドではありません。パスワード、権限、バックアップ、ネットワーク公開範囲は、本番利用時に別途設計してください。

## DBなしでできること / DBが必要になること

[SLM quickstart](slm_demo_quickstart.md) の Step 1〜5 は DB なしで実行できます。

```text
note.md
  ↓
SLM が rde-draft.json を作る
  ↓
kotonoha rde validate --strict rde-draft.json
  ↓
レビュー可能な形の草案
```

一方、この文書で扱う record flow は DB を使います。

```text
kotonoha delta create note.md
  ↓
MeaningDelta record ID = DELTA_ID

kotonoha rde attach --delta-id "$DELTA_ID" rde-draft.json
  ↓
RDE assessment attached

kotonoha review hold --delta-id "$DELTA_ID"
  ↓
Human review decision recorded
```

## 前提

| 項目 | 説明 |
| --- | --- |
| `kotonoha` CLI | インストール済みで `kotonoha version` が動くこと |
| Git repository | `delta create` は現行 CLI では Git repository 内で実行する |
| PostgreSQL | record flow を保存するために必要 |
| Docker | 任意。ローカル PostgreSQL を簡単に起動する場合に使用 |
| `DATABASE_URL` | Kotonoha CLI が接続する PostgreSQL URL |
| `note.md` | 対象ノート |
| `rde-draft.json` | validate 済みの RDE 草案 |

## Step 1 — ローカル PostgreSQL を起動する

Docker が使える場合は、次のように PostgreSQL を起動できます。

```bash
docker run --name kotonoha-postgres \
  -e POSTGRES_USER=kotonoha \
  -e POSTGRES_PASSWORD=kotonoha \
  -e POSTGRES_DB=kotonoha \
  -p 5432:5432 \
  -d postgres:16
```

既に同名コンテナが存在する場合は、次で起動できます。

```bash
docker start kotonoha-postgres
```

これはローカル検証用です。本番用の設定ではありません。

## Step 2 — DATABASE_URL を設定する

```bash
export DATABASE_URL="postgres://kotonoha:kotonoha@localhost:5432/kotonoha"
```

確認します。

```bash
echo "$DATABASE_URL"
```

## Step 3 — DB migration を実行する

```bash
kotonoha db migrate
```

状態を確認します。

```bash
kotonoha status
```

## Step 4 — note.md と rde-draft.json を確認する

```bash
ls -la note.md rde-draft.json
kotonoha rde validate --strict rde-draft.json
```

ここで validation が成功している必要があります。

## Step 5 — delta record を作る

`delta create` は、ここまでの草案や Obsidian sidecar 履歴を自動的に取り込む操作ではありません。

まず `note.md` に対する MeaningDelta の器を DB に作ります。現行 CLI では、主に Git commit、file path、diff reference、任意の observation を保存します。`--observation` を指定しない場合、observation は空です。

```bash
DELTA_ID=$(kotonoha delta create note.md)
echo "$DELTA_ID"
```

`DELTA_ID` は任意に決める値ではありません。`kotonoha delta create note.md` が出力する UUID です。

### 任意: observation を添える

必要であれば、delta 作成時に簡単な observation を渡せます。

```bash
cat > observation.json <<'EOF'
{
  "note": "SLM quickstart demo delta",
  "source": "note.md",
  "intent": "Create a delta anchor before attaching validated RDE draft"
}
EOF

DELTA_ID=$(kotonoha delta create note.md --observation observation.json)
echo "$DELTA_ID"
```

この observation は RDE review output そのものではありません。RDE 草案は次の `rde attach` で明示的に添付します。

## Step 6 — RDE 草案を delta に添付する

```bash
kotonoha rde attach --delta-id "$DELTA_ID" --source-kind llm --strict rde-draft.json
```

これは、validate 済みの `rde-draft.json` を、先ほど作った delta に明示的に添付する操作です。

## Step 7 — review decision を記録する

学習中は `hold` を使うのが安全です。

```bash
kotonoha review hold --delta-id "$DELTA_ID" --decided-by "your-name"
```

`hold` は、「意味変化を見える形にはしたが、まだ承認する段階ではない」という判断です。

`approve` は、人間として承認を記録する意図がある場合だけ使います。

## Step 8 — export して確認する

```bash
kotonoha export --delta-id "$DELTA_ID" --format m2
```

必要ならファイルに保存します。

```bash
kotonoha export --delta-id "$DELTA_ID" --format m2 --out record-export.json
```

## Obsidian sidecar との関係

Obsidian Console の `.kotonoha/` sidecar は、ローカル UI 上の proposal / audit / review 記録です。

この CLI record flow では、sidecar を自動的に DB record へ取り込むわけではありません。

この文書で添付するのは、明示的に指定した `rde-draft.json` です。

```text
Obsidian sidecar
  = Console UI のローカル証跡

DB-backed record flow
  = delta create / rde attach / review hold で明示的に保存する記録
```

sidecar と DB record の相関や export 連携は、今後の統合課題です。

## よくあるエラー

### `DATABASE_URL is not set`

`DATABASE_URL` が設定されていません。

```bash
export DATABASE_URL="postgres://kotonoha:kotonoha@localhost:5432/kotonoha"
```

### database connection failed

PostgreSQL が起動していない、または接続 URL が間違っています。

```bash
docker ps
docker start kotonoha-postgres
```

### delta create requires a Git repository

現行 CLI の `delta create` は Git repository 内で実行します。

```bash
git init
git add note.md
git commit -m "demo note"
```

または、既存の Git repository 内で手順を実行してください。

### relation/table does not exist

migration が未実行の可能性があります。

```bash
kotonoha db migrate
```

## RDE 的な境界

### 保存された要素

SLM は草案作成専用です。validation と人間レビューは必須です。

### 変換された要素

一時ファイルとしての RDE 草案を、DB-backed な Kotonoha record に接続します。

### 補完された要素

`delta create`、`rde attach`、`review hold` の意味と、`DELTA_ID` の扱いを明示します。

### 未解決の要素

本格的な PostgreSQL 運用、Obsidian sidecar と DB record の同期、M6 export との相関は、この文書の範囲外です。

### 逸脱リスク

`delta create` を、意味変化を自動評価する操作と誤解してはいけません。これはまず、記録の器を作る操作です。

## 要約

安全な流れは次です。

```text
SLM draft
  → validate
  → delta create
  → rde attach
  → human review
  → export
```
