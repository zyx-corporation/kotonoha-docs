# SLM デモ quickstart

このチュートリアルは、小規模言語モデル（SLM）をローカルで起動し、Kotonoha用のRDE review草案を作るための初心者向け手順です。

これはデモ用ワークフローです。SLM出力はあくまで草案です。Kotonoha validationと人間レビューは必須です。

英語版対応: [`../../en/tutorials/slm_demo_quickstart.md`](../../en/tutorials/slm_demo_quickstart.md)

## 目的

この手順を終えると、次ができるようになります。

1. ローカルSLMを起動する。
2. RDE JSON草案を生成する。
3. `kotonoha rde validate --strict` で草案を検証する。
4. どの時点で大きなLLMまたは人間レビューへ上げるべきかを理解する。

## 前提

以下を前提とします。

- macOS または Linux。
- terminalを使えること。
- `kotonoha` CLIがインストール済みであること。
- Git管理された作業ディレクトリ、または通常の作業ディレクトリがあること。
- OllamaなどのSLM runtimeを使えること。

SLM runtimeがまだない場合、Ollamaはローカルデモ用の一般的な選択肢です。他のlocal SLM runtimeでも構いません。

## Step 1 — SLM runtimeを起動または確認する

Ollamaを使う例です。

```bash
ollama --version
```

Ollamaが入っていない場合は、公式手順に従って利用環境へインストールしてください。

次に、小さめのinstruction modelを取得します。Kotonohaは特定モデルを要求しません。利用するマシンに合うものを選びます。

例:

```bash
ollama pull qwen2.5:3b-instruct
```

テスト起動します。

```bash
ollama run qwen2.5:3b-instruct
```

次のように入力します。

```text
Say hello in one sentence.
```

確認できたらmodel shellを終了します。

## Step 2 — 対象ファイルを用意する

デモ用の小さなテキストファイルを作成します。

```bash
mkdir -p kotonoha-demo
cd kotonoha-demo
cat > note.md <<'EOF'
# Draft note

Kotonoha records meaning changes. It helps users inspect what was preserved,
what changed, what was lost, and what should be reviewed next.
EOF
```

## Step 3 — SLMにRDE草案を作らせる

SLMに最小RDE review outputを作らせます。

プロンプト例:

```text
Create a candidate Kotonoha RDE review output JSON for the following note.
Use spec_version "0.1".
Use subject_ref "file:note.md".
Include the seven categories:
preserved, transformed, complemented, intentionally_unresolved, lost, deviation_risk, next_update_policy.
Each category must be an array. Each item should be an object with a summary field.
Return JSON only.

Note:
# Draft note

Kotonoha records meaning changes. It helps users inspect what was preserved,
what changed, what was lost, and what should be reviewed next.
```

モデルの出力を `rde-draft.json` として保存します。

Markdownのコードフェンスが付いている場合は削除し、ファイルには生のJSONだけを残します。

## Step 4 — 草案を検証する

次を実行します。

```bash
kotonoha rde validate --strict rde-draft.json
```

validationが成功すれば、そのJSONは現在のvalidation profileに対して構造上受け入れ可能です。

validationに失敗した場合は、JSONを修正して再実行します。よくあるエラーは次です。

- top-level key `rde_review_output` がない。
- 必須categoryがない。
- category valueがarrayではない。
- category itemがobjectではない。
- strict modeで `summary` がない、または空である。
- `source_context_status` が不正である。

## Step 5 — 人間が読む

validationが成功しても、RDE草案は必ず自分で読みます。

確認します。

- 草案はノートの意図を保存しているか。
- 存在しない意味を発明していないか。
- 喪失や曖昧さを見落としていないか。
- 逸脱リスクを軽く扱いすぎていないか。
- source contextは十分か。

validationはshapeを確認するものであり、最終判断を証明するものではありません。

## Step 6 — 任意: attach / review flow

永続化が有効なKotonoha projectを使っている場合は、通常のCLI flowへ進めます。

```bash
kotonoha delta create note.md
kotonoha rde attach --delta-id <DELTA_ID> --source-kind llm rde-draft.json
kotonoha review hold --delta-id <DELTA_ID> --decided-by "your-name"
```

学習中は `hold` を使うのが安全です。`approve` は、人間として承認を記録する意図がある場合だけ使います。

## Demo profile

このチュートリアルは、公開ガイド上のdemo SLM profileに対応します。

```yaml
kotonoha:
  ai:
    profile: demo-slm
    model_class: slm
    role: draft-only
    validation_required: true
    validation_command: kotonoha rde validate --strict
    approval_authority: human
```

## この手順で十分な場合

このdemo SLM workflowは、次に向いています。

- Kotonohaの学習。
- 短いノート。
- 小さなドキュメント変更。
- 個人草稿。
- local-firstな実験。

## escalationすべき場合

次の場合は、大きなLLMまたは深い人間レビューへ上げます。

- 文書が長い。
- 複数ファイルが関係する。
- source contextがmissing、partial、contestedである。
- 公開、法務、倫理、制度、安全上sensitiveな内容を含む。
- 草案に重要な `deviation_risk` がある。
- 元の意図を保存しているか確信できない。

## 要約

SLMはすばやく始めるために有用です。しかし、権威として信頼してはいけません。

安全な流れは次です。

```text
SLM draft → Kotonoha validation → human review → attach / record decision
```
