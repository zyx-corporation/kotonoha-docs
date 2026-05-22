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

## デフォルト最小選択: SLM

個人利用や軽量ワークフローでは、デフォルト最小選択として SLM を使ってかまいません。

SLM に期待する役割は次の通りです。

- RDE category item の草案作成。
- 短い `summary` 文の提案。
- RDE JSON候補の整形。
- 明らかな `lost` または `deviation_risk` の抽出補助。
- ノート単位、単一ファイル単位のレビュー補助。
- local-first または低コスト運用の実用化。

SLM 出力は権威ではありません。あくまで草案です。

## 大きなLLMまたは人間レビューへ上げる場合

次のいずれかに該当する場合、デフォルトSLM経路から、大きなLLMまたは人間レビューへ上げます。

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

1. SLMまたはLLMでRDE review草案を作る。
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

最も安全なdefaultは次の通りです。

```text
Default model: SLM
Role: draft-only assistant
Validation: kotonoha rde validate --strict
Escalation: larger LLM or human review when risk/context requires it
Final authority: human reviewer
```
