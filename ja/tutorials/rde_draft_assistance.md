# RDE draft assistance quickstart

このチュートリアルでは、既存の MeaningDelta から RDE review の候補を作る M8 の流れを説明します。

大事な境界はひとつです。`kotonoha rde draft` はレビューを書く支援です。意味的に正しいと判定するものでも、attach するものでも、承認するものでも、公開を許可するものでもありません。

英語版: [`../../en/tutorials/rde_draft_assistance.md`](../../en/tutorials/rde_draft_assistance.md)

## いつ使うか

すでに MeaningDelta record があり、`preserved`、`lost`、`transformed`、`intentionally_unresolved`、`next_update_policy` などの RDE category を書き始めたいときに使います。

空の RDE ひな形だけが欲しい場合は、こちらで十分です。

```bash
kotonoha rde emit
```

## 前提

| 項目 | 理由 |
| --- | --- |
| PostgreSQL と `DATABASE_URL` | `rde draft` は既存 MeaningDelta を読むため |
| `kotonoha db migrate` 実行済み | 必要なテーブルが存在する必要があるため |
| `DELTA_ID` | `kotonoha delta create` が返す UUID |

## Step 1 — attach 可能な draft を作る

```bash
kotonoha rde draft --delta-id "$DELTA_ID" > rde-draft.json
```

標準出力は top-level `rde_review_output` を持つ通常の RDE JSON です。そのまま validation や attach に渡せます。

## Step 2 — strict validation する

```bash
kotonoha rde validate --strict rde-draft.json
```

validation は JSON の形が受け入れ可能であることを示すだけです。レビュー内容が意味的に正しいことを保証しません。

## Step 3 — evidence として attach する

```bash
kotonoha rde attach --delta-id "$DELTA_ID" --strict --source-kind cli rde-draft.json
```

attach は `rde_assessments` row を保存します。これはレビュー証跡であって、判断そのものではありません。

## Step 4 — 人間レビューを記録する

学習中は `approve` より `hold` のほうが安全です。

```bash
kotonoha review hold --delta-id "$DELTA_ID" --decided-by "your-name"
```

`approve` は、人間として承認を記録する意図がある場合だけ使ってください。

## 任意 — provenance wrapper を含める

別チャネルで source metadata や boundary flag も運びたい場合は、次を使います。

```bash
kotonoha rde draft --delta-id "$DELTA_ID" --wrap
```

wrapped form は provenance を運ぶための形です。`rde validate` / `rde attach` に渡すときは内側の `rde_review_output` を取り出すか、標準の unwrapped 出力を使ってください。

## 安全な理解

```text
draft
  → validate
  → attach
  → human review
  → export / console observation
```

この状態を混ぜないでください。流暢な draft でも、まだ candidate にすぎません。

