# LLM / SLM 利用ガイド

この文書は、Kotonoha が利用者向けワークフローの中で、大規模言語モデル（LLM）および小規模言語モデル（SLM）をどのように扱うかを説明します。

この文書は公開ドキュメントであり、normative な SLS 仕様ではありません。RDE output の厳密な意味定義とvalidation ruleは [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) で定義されます。

英語版対応: [`../../en/manual/llm_slm_usage.md`](../../en/manual/llm_slm_usage.md)

## 基本方針

Kotonoha は、特定の LLM provider または model を要求しません。

LLM または SLM は RDE 草案を生成してよいですが、その出力は attach、永続化、レビュー利用の前に Kotonoha の検証を通過しなければなりません。人間による承認は LLM の権限外にあります。

要約すると、役割分担は次の通りです。

| 層 | 役割 |
| --- | --- |
| SLM / LLM | 草案生成、分類補助、JSON整形補助 |
| `kotonoha-core` / `kotonoha-cli` | validation、永続化経路、review record handling |
| Human reviewer | 最終承認、保留、却下、公開責任 |

## profileとは何か（定義・所在・適用）

この文書でいう `profile` は、Kotonoha のAI利用における**運用方針の名前付きセット**です。
例: `demo-slm`、`hosted-llm-escalation`、`no-model`。

先に重要点をまとめると次の通りです。

- これは **SLS仕様そのもの** ではなく、実装・運用で使う方針名です。
- この文書にあるYAMLは **説明用サンプル** であり、共通の必須設定ファイルを定義しません。
- 実際の「どこに書くか」は、利用している実装（CLIラッパー、MCP連携、社内オーケストレーション等）の設定方式に従います。

### どこにあるか

公開リポジトリでは、`profile` はまずこの文書の「設定プロファイル例」に記述された**ドキュメント上の定義**として存在します。
つまり、ここに書かれた `demo-slm` は「組み込み済み固定プロファイル」を指すのではなく、利用者が自分の運用設定へ写経・対応づけるための参照です。

### どう適用されるか

適用の実態は、利用側が `profile` 名に対応するポリシーを設定することです。典型的には次を固定します。

1. モデルの役割（例: `draft-only`）。
2. 検証ゲート（例: `kotonoha rde validate --strict` を必須化）。
3. 承認権限（例: 最終承認は人間）。
4. エスカレーション条件（`missing` / `partial` / `contested`、高リスク、長文など）。

要するに `profile` は「実行可能な設定ファイルの単一仕様」ではなく、運用境界を揃えるための方針ラベルです。

## デモ最小プロファイル: SLM

デモ、個人試用、軽量ワークフローでは、SLMを **デモ最小プロファイル** として使ってかまいません。

これはproduction requirementでも、normativeなSLS ruleでもありません。低コスト、local-first、quick-start用途の実用的な設定例です。

SLMに期待する役割は次の通りです。

- RDE category item の草案作成。
- 短い `summary` 文の提案。
- RDE JSON候補の整形。
- 明らかな `lost` または `deviation_risk` の抽出補助。
- ノート単位、単一ファイル単位のレビュー補助。
- デモおよび低コスト運用の実用化。

SLM 出力は権威ではありません。あくまで草案です。

## 設定プロファイル例

正確な設定形式は、channelまたはimplementationに依存します。以下は意図を示す設定例です。

### Demo SLM profile

local demo、onboarding、個人ノート、短い単一ファイルreview向けです。

```yaml
kotonoha:
  ai:
    profile: demo-slm
    model_class: slm
    role: draft-only
    allowed_tasks:
      - rde_draft
      - category_suggestion
      - json_formatting
    validation_required: true
    validation_command: kotonoha rde validate --strict
    attach_requires_validated_json: true
    approval_authority: human
    escalation:
      on_source_context:
        - missing
        - partial
        - contested
      on_risk:
        - deviation_risk
      on_subject:
        - long_document
        - multi_document
        - publication_sensitive
```

### Hosted LLM escalation profile

SLM草案が不十分な場合、対象が長い場合、概念的・制度的にsensitiveなreviewに使います。

```yaml
kotonoha:
  ai:
    profile: hosted-llm-escalation
    model_class: llm
    role: draft-improvement
    allowed_tasks:
      - rde_draft_revision
      - ambiguity_review
      - lost_context_review
      - deviation_risk_review
    validation_required: true
    validation_command: kotonoha rde validate --strict
    approval_authority: human
```

### No-model profile

利用者がRDE observationを手動で書く場合に使います。

```yaml
kotonoha:
  ai:
    profile: no-model
    model_class: none
    role: manual-review
    validation_required: true
    validation_command: kotonoha rde validate --strict
    approval_authority: human
```

これらはdocumentation profileです。必須のpublic configuration schemaを定義するものではありません。

## 大きなLLMまたは人間レビューへ上げる場合

次のいずれかに該当する場合、demo SLM経路から、大きなLLMまたは人間レビューへ上げます。

- 対象が長文、または複数文書にまたがる。
- source context が `missing`、`partial`、または `contested` である。
- 制度的責任、公開、法務、政治、倫理、安全上重要な内容を含む。
- RDE草案に重要な `deviation_risk` が含まれる。
- 意味変化が、微妙な哲学的・概念的・修辞的構造に依存している。
- 生成されたreviewが元の意図を保存しているか、利用者が確信できない。

大きなLLMは、より良い草案生成を助けることがあります。しかし、承認には人間レビューが必要です。

## Validation gate

RDE草案をattach、永続化、レビュー利用する前に、Kotonoha validationを実行します。

典型的なコマンドは次の通りです。

```bash
kotonoha rde validate --strict path/to/rde.json
```

validatorは、機械可読なshape、必須RDE category、`source_context_status` などのclosed vocabularyを検査します。ただし、そのsemantic judgmentが最終的に正しいことを証明するものではありません。

## 推奨ワークフロー

1. SLM、LLM、または手動でRDE review草案を作る。
2. 人間が草案を読む。
3. `kotonoha rde validate --strict` でJSONを検証する。
4. 必要に応じて、検証済みRDE outputを `kotonoha rde attach` でattachする。
5. `kotonoha review approve`、`hold`、`reject` のいずれかで人間判断を記録する。

## Provider例

以下は利用可能なchannelの例であり、要求ではありません。

- ChatGPT または ChatGPT App / MCP client。
- Claude Desktop または Cursor through MCP。
- Gemini または他のhosted LLM。
- Qwen または他のlocal/open model。
- 組織固有のSLM。

モデルを変更しても、RDEの権威は変わりません。重要なのは、検証済みJSONと人間レビュー境界です。

## 避けるべきこと

次を避けます。

- LLMの自由文章をそのままRDE recordとして扱う。
- LLM生成RDEを人間承認として扱う。
- attachまたは永続化の前に `kotonoha` validationを迂回する。
- provider固有のmodelをpublic SLS requirementとして埋め込む。
- modelの便利さによって、missing、partial、contested なsource contextを見えなくする。

## 要約

安全なdemo profileは次の通りです。

```text
Demo model profile: SLM
Role: draft-only assistant
Validation: kotonoha rde validate --strict
Escalation: larger LLM or human review when risk/context requires it
Final authority: human reviewer
```
