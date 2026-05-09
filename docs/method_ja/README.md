# Method — KotonohaをSLS + RDEで構築する

このセクションは、Kotonohaプロジェクトが **Semantic Lineage System（SLS）** と **Resonant Deviation Evaluator（RDE）** 的レビューを、自身のエンジニアリングと文書化にどう適用するかを説明する。

このディレクトリには日本語版のMethod文書を置く。英語一次文書は [`docs/method/`](../method/README.md) に置く。

このセクションは **非規範的** であり、相互運用APIやスキーマを定義しない。それらは [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) に属する。

| 文書 | 対応 | 説明 |
| --- | --- | --- |
| [Kotonoha Method — ドラフト骨子](kotonoha_method_outline.md) | [`docs/method/kotonoha_method_outline.md`](../method/kotonoha_method_outline.md) | SLSの制度的実装としてのKotonoha Methodの章立て案。 |
| [SLS + RDE 開発手法](../method/sls_rde_development_method_ja.md) | [`docs/method/sls_rde_development_method.md`](../method/sls_rde_development_method.md) | Kotonohaを進化させる際の実践、レビュー観点、ワークフロー習慣。 |

## 想定読者

- [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)、[`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core)、`kotonoha-docs` のコントリビューター。
- レビューが単なる正誤確認ではなく、喪失・逸脱・未解決性を問う理由を理解したい読者。

## 他文書との関係

- **仕様** → [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)
- **実装** → [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core)
- **英語Method文書** → [`docs/method/`](../method/README.md)
- **運用マニュアルとチュートリアル** → [`docs/manual/`](../manual/README.md), [`docs/tutorials/`](../tutorials/README.md)
