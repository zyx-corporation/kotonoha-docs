# Method — KotonohaをSLS + RDEで構築する

このセクションは、Kotonohaプロジェクトが **Semantic Lineage System（SLS）** と **Resonant Deviation Evaluator（RDE）** 的レビューを、自身のエンジニアリングと文書化にどう適用するかを説明する。

このディレクトリには日本語版のMethod文書を置く。英語一次文書は [`docs/method/`](../method/README.md) に置く。

このセクションは **非規範的** であり、相互運用APIやスキーマを定義しない。それらは [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) に属する。

## Kotonoha Method 本文ドラフト

| 章 | 文書 | 状態 | 説明 |
| --- | --- | --- | --- |
| Chapter 0 | [システム・エンジニアリング初学者のための導入](chapter_00_intro_for_beginning_system_engineers.md) | draft / Japanese first | これまで何が問題だったのか、エンジニアリングは何をどう変えるのか、Kotonohaが何を担うのか。 |
| Chapter 1 | [タスク管理から意味統治へ](chapter_01_task_management_to_semantic_governance.md) | draft / Japanese first | Kotonoha Method が既存PMを意味統治へ拡張する理由。 |

## HTML / JS / SVG プロトタイプ

| 文書 | 説明 |
| --- | --- |
| [method_site/index.html](method_site/index.html) | 日本語版Kotonoha Methodの初期HTMLプロトタイプ。 |
| [sections/README.md](sections/README.md) | 章をセクションへ分割するための構成案。 |
| [assets/svg/semantic-transformation-flow.svg](assets/svg/semantic-transformation-flow.svg) | 要望から実装までの意味変化フロー図。 |

## 補助文書

| 文書 | 対応 | 説明 |
| --- | --- | --- |
| [Kotonoha Method — ドラフト骨子](kotonoha_method_outline.md) | [`docs/method/kotonoha_method_outline.md`](../method/kotonoha_method_outline.md) | SLSの制度的実装としてのKotonoha Methodの章立て案。 |
| [SLS + RDE 開発手法](sls_rde_development_method.md) | [`docs/method/sls_rde_development_method.md`](../method/sls_rde_development_method.md) | Kotonohaを進化させる際の実践、レビュー観点、ワークフロー習慣。 |
| [表現・公開展開方針](rendering_and_publication_policy.md) | future HTML / JS / SVG publication | HTML+JavaScript+SVG化、章のセクション分割、図表多用、紙媒体化を見据えた代替表現の方針。 |
| [ライセンス注記](LICENSE.md) | CC BY-NC-ND 4.0 | Kotonoha Method文書のライセンス注記。 |

## 執筆方針

- 章単位で、まず日本語版を執筆する。
- 日本語版の確認後、対応する英語版を [`docs/method/`](../method/README.md) に作成する。
- 英語版作成時には、単純翻訳ではなく、外部公開・国際読者向けに必要な補足と用語整理を行う。
- 将来的には、Markdown本文を基盤に、HTML、JavaScript、SVGによる読者向け表現へ発展させる。
- インタラクティブ表現を推奨する場合も、紙媒体化に備えて静的図表・表・脚注・代替説明を用意する。

## 想定読者

- [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)、[`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core)、`kotonoha-docs` のコントリビューター。
- レビューが単なる正誤確認ではなく、喪失・逸脱・未解決性を問う理由を理解したい読者。

## 他文書との関係

- **仕様** → [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)
- **実装** → [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core)
- **英語Method文書** → [`docs/method/`](../method/README.md)
- **運用マニュアルとチュートリアル** → [`docs/manual/`](../manual/README.md), [`docs/tutorials/`](../tutorials/README.md)

## ライセンス

特に個別ファイルで別途明記しない限り、このディレクトリ以下のKotonoha Method文書は **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International（CC BY-NC-ND 4.0）** で提供する。詳細は [LICENSE.md](LICENSE.md) を参照する。
