# SLM デモ quickstart

小規模言語モデル（SLM）をローカルで起動し、Kotonoha 用の RDE review **草案**を作る初心者向け手順です。

**前提:** [CLI のインストール](install_kotonoha_cli.md) と [最初の CLI セッション](first_cli_session.md) を完了していること。

これはデモ用ワークフローです。SLM 出力は草案であり、Kotonoha の validation と人間レビューは必須です。

英語版: [`../../en/tutorials/slm_demo_quickstart.md`](../../en/tutorials/slm_demo_quickstart.md)

## 物語: 公開前の小さなノート

あなたが短いノートを編集している場面を想像してください。誰かに共有する前、あるいは小さな記事として公開する前の草稿です。

見た目には、たいした変更ではありません。数行を書き換えただけです。けれども、その変更で意味がどう変わったのかは、少し不安です。

新しい文はわかりやすくなったかもしれません。けれども同時に、必要なためらいや、未解決の問いを消してしまったかもしれません。あるいは、自分が意図したよりも強い主張に見えてしまうかもしれません。

ここでKotonohaを使います。

このチュートリアルでは、あなたは短いノートを確認する書き手です。local SLMは、安価な草案作成係として働きます。SLMは、何が保存され、何が変わり、何が失われ、どこにリスクがあるかを、まず粗く書き出します。その後、Kotonohaがその草案がRDE review outputとして検証可能な形になっているかを確認します。最後に、人間であるあなたが内容を読みます。

目的はSLMを信頼することではありません。最初の草案を、レビューできる程度に見える形へ出すことです。

## 目的

この手順を終えると、次ができるようになります。

1. ローカルSLMを起動する。
2. レビュー対象となる小さなノートを作る。
3. SLMにRDE JSON草案を作らせる。
4. `kotonoha rde validate --strict` で草案を検証する。
5. 人間として結果を読む。
6. どの時点で大きなLLMまたは深い人間レビューへ上げるべきかを理解する。

## 前提

| 項目 | 説明 |
| --- | --- |
| OS | macOS または Linux |
| ターミナル | コピー＆ペーストでコマンドを実行できること |
| `kotonoha` CLI | [install_kotonoha_cli.md](install_kotonoha_cli.md) 済み（`kotonoha version` が動くこと） |
| 作業ディレクトリ | 任意のフォルダ（Git 管理は任意） |
| SLM runtime | Ollama など（未導入なら Step 1 で準備） |

SLM runtime がまだない場合、Ollama はローカルデモ向けの一般的な選択肢です。他の local SLM でも構いません。

## Step 1 — SLM runtimeを起動または確認する

物語は、小さな助手をローカルで起動するところから始まります。

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

日本語での草案作成では、次を目安にすると安定しやすくなります。

- 推奨: `qwen2.5:7b-instruct`（日本語の指示追従と要約が比較的安定）
- 軽量優先: `qwen2.5:3b-instruct`（メモリが限られる環境向け）

テスト起動します。

```bash
ollama run qwen2.5:3b-instruct
```

次のように入力します。

```text
Say hello in one sentence.
```

確認できたらmodel shellを終了します。

この時点で、local draft assistant が用意できました。ただし、それは評価者ではなく、承認者でもなく、正本でもありません。

## Step 2 — レビューしたいノートを用意する

次に、レビュー対象となるノートを作ります。

```bash
mkdir -p kotonoha-demo
cd kotonoha-demo
cat > note.md <<'EOF'
# Draft note

Kotonoha records meaning changes. It helps users inspect what was preserved,
what changed, what was lost, and what should be reviewed next.
EOF
```

実際のワークフローでは、これはエッセイの一段落、READMEの変更、研究メモ、Obsidianの草稿かもしれません。

チュートリアルでは、流れ全体が見えるように短くしています。

## Step 3 — SLMにRDE草案を作らせる

次に、SLMにこのノートをKotonohaのRDE形式で説明させます。

SLMは、このノートが良いか悪いかを決めるわけではありません。候補となるreview recordを準備するだけです。

プロンプト例:

```text
次のノートに対する Kotonoha RDE review output の候補JSONを作成してください。
トップレベルは次の厳密な形にしてください:
{
  "rde_review_output": {
    "spec_version": "0.1",
    "subject_ref": "file:note.md",
    "categories": {
      "preserved": [],
      "transformed": [],
      "complemented": [],
      "intentionally_unresolved": [],
      "lost": [],
      "deviation_risk": [],
      "next_update_policy": []
    }
  }
}
spec_version は "0.1" を使用してください。
subject_ref は "file:note.md" を使用してください。
次の7カテゴリを含めてください:
preserved, transformed, complemented, intentionally_unresolved, lost, deviation_risk, next_update_policy.
各カテゴリは配列にしてください。各要素は summary フィールドを持つオブジェクトにしてください。
JSONのみを返し、トップレベルキーは "rde_review_output" にしてください。

ノート:
# Draft note

Kotonoha records meaning changes. It helps users inspect what was preserved,
what changed, what was lost, and what should be reviewed next.
```

モデルの出力を `rde-draft.json` として保存します。

Ollamaへ明示的にプロンプトを渡してファイル保存する例:

```bash
cat > rde-prompt.txt <<'EOF'
次のノートに対する Kotonoha RDE review output の候補JSONを作成してください。
トップレベルは次の厳密な形にしてください:
{
  "rde_review_output": {
    "spec_version": "0.1",
    "subject_ref": "file:note.md",
    "categories": {
      "preserved": [],
      "transformed": [],
      "complemented": [],
      "intentionally_unresolved": [],
      "lost": [],
      "deviation_risk": [],
      "next_update_policy": []
    }
  }
}
spec_version は "0.1" を使用してください。
subject_ref は "file:note.md" を使用してください。
次の7カテゴリを含めてください:
preserved, transformed, complemented, intentionally_unresolved, lost, deviation_risk, next_update_policy.
各カテゴリは配列にしてください。各要素は summary フィールドを持つオブジェクトにしてください。
JSONのみを返し、トップレベルキーは "rde_review_output" にしてください。

ノート:
# Draft note

Kotonoha records meaning changes. It helps users inspect what was preserved,
what changed, what was lost, and what should be reviewed next.
EOF

ollama run qwen2.5:7b-instruct < rde-prompt.txt > rde-draft.json
```

Markdownのコードフェンスが付いている場合は削除し、ファイルには生のJSONだけを残します。

ここが最初の重要な境界です。このファイルは草案であり、まだ有効なKotonoha recordではありません。

## Step 4 — 草案を検証する

ここでKotonohaが草案のshapeを確認します。

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

validationが成功しても、SLMが正しかったという意味ではありません。レビュー可能な形に整った、という意味です。

## Step 5 — 人間として読む

ここからが重要です。

validationが成功しても、RDE草案は必ず自分で読みます。

確認します。

- 草案はノートの意図を保存しているか。
- 存在しない意味を発明していないか。
- 喪失や曖昧さを見落としていないか。
- 逸脱リスクを軽く扱いすぎていないか。
- source contextは十分か。

ここが二つ目の重要な境界です。Kotonohaは意味変化のレビューを助けますが、あなたの責任を置き換えるものではありません。

## Step 6 — 任意: Kotonoha の記録として残す

### Step 1〜5 と Step 6 の違い

- **Step 1〜5:** DB なしで、SLM 草案を作り、RDE JSON の形を検証する。
- **Step 6:** 検証済み草案を DB 上の Kotonoha record として残したい場合だけ進む（任意）。

ここまでの手順では、`rde-draft.json` はまだ一時的な草案ファイルです。学習だけが目的なら、Step 5 までで十分です。

### 3コマンドがそれぞれ何をするか

| 操作 | 役割 |
| --- | --- |
| `delta create` | `note.md` に対する **MeaningDelta の器（アンカー）** を DB に作る |
| `rde attach` | Step 3〜4 で作って検証した `rde-draft.json` を、その delta に **明示的に** 添付する |
| `review hold` | 人間として「保留」の review decision を DB に **明示的に** 記録する |

`delta create` は、ここまでの sidecar や一時ファイルの履歴を自動的に取り込む操作ではありません。まず `note.md` に対する delta record を DB に作り、その後 `rde attach` によって検証済みの `rde-draft.json` を明示的に添付します。

### `delta create` が実際に保存するもの

`kotonoha delta create note.md` は、意味変化の中身を深く計算して保存する操作ではありません。主に次を保存します。

- 現在の Git commit
- ファイルパス（`note.md`）
- line range または `diff_ref`（未指定時は `unstaged:note.md` など）
- project / principal ID（環境変数があれば）
- `observation`（`--observation` を渡さなければ空の `{}`）
- 空の `source_context`

**この時点では入りません:** SLM の `rde-draft.json`、validation 結果、Obsidian Console の sidecar、ノート全文のスナップショット。これらは別操作です。

`delta create` には **Git リポジトリ** と **`DATABASE_URL`** が必要です（[CLI インストール](install_kotonoha_cli.md) および [最初の CLI セッション](first_cli_session.md) を参照）。

### Obsidian Console の sidecar との関係

Obsidian Console の `.kotonoha/`（`proposals/`、`audit/`、`reviews/`）は、Console 上の proposal / audit / review の **ローカル証跡** です。この quickstart の CLI flow では sidecar ではなく `rde-draft.json` を明示的に `rde attach` します。sidecar と DB record の自動同期は、この手順の対象外です。

### `<DELTA_ID>` の決め方

`<DELTA_ID>` は任意の文字列ではありません。`delta create` が標準出力に出す **UUID**（`meaning_deltas.id`）です。

```bash
DELTA_ID=$(kotonoha delta create note.md)
kotonoha rde attach --delta-id "$DELTA_ID" --source-kind llm rde-draft.json
kotonoha review hold --delta-id "$DELTA_ID" --decided-by "your-name"
```

任意の補助情報を delta 作成時に残したい場合は `--observation` を使えます（RDE 草案そのものの代わりにはなりません。RDE は `rde attach` で添付します）。

```bash
cat > observation.json <<'EOF'
{
  "note": "SLM quickstart demo delta",
  "source": "note.md",
  "intent": "Create a delta anchor before attaching validated RDE draft"
}
EOF

DELTA_ID=$(kotonoha delta create note.md --observation observation.json)
kotonoha rde attach --delta-id "$DELTA_ID" --source-kind llm rde-draft.json
kotonoha review hold --delta-id "$DELTA_ID" --decided-by "your-name"
```

学習中は `hold` を使うのが安全です。`approve` は、人間として承認を記録する意図がある場合だけ使います。

この物語の中で `hold` は、「意味変化を見える形にはしたが、まだ承認する段階ではない」という意味です。

## Demo profile は何を表しているか

この節の `profile` は、この quickstart を実行するために必須の設定ファイルではありません。

ここでは、このチュートリアルでの SLM の扱いを「利用ポリシー」として名前付きで表しています。

`demo-slm` は次を意味します。

- SLM は草案作成専用である。
- SLM 出力は承認済み Kotonoha record ではない。
- `kotonoha rde validate --strict` による validation が必要である。
- validation が成功しても、内容が正しいとは限らない。
- 最終判断と承認権限は人間に残る。

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

将来、この形式は Kotonoha の設定ファイルや profile registry に接続される可能性があります。ただし、この quickstart では、この YAML を保存しなくても手順を実行できます。

## この物語で十分な場合

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

物語は単純です。

書き手がノートを変更する。小さなモデルがレビュー草案を書く。Kotonohaがshapeを検証する。人間がその意味を判断する。

安全な流れは次です。

```text
SLM draft → Kotonoha validation → human review → attach / record decision
```
