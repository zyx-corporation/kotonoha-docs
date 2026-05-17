# kotonoha-docs（日本語概要）

**Semantic Lineage System（SLS）の仕様に含まれない**、利用者・コミュニティ向けの**公開ドキュメント**を置くリポジトリです。

仕様の正本・規範的な定義は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) にあります。本リポジトリは **概念説明**、**マニュアル**、**チュートリアル**、**ハウツー**、**受入デモ**、**参考論文**、**補助的な説明**など、normative ではない公開文書を対象とします。

## 言語ルート

読者向けドキュメントは、リポジトリ直下の言語別領域に配置します。

| 言語 | 領域 | 備考 |
| --- | --- | --- |
| English | [`en/`](en/README.md) | 英語ドキュメント領域 |
| Japanese | [`ja/`](ja/README.md) | 日本語ドキュメント領域 |

英語版と日本語版は、原則として同じ構造と同じ内容の翻訳・対応文書を持つようにします。

既存の [`docs/`](docs/README.md) は必要に応じて履歴・補助資料として参照できますが、新規の概念説明・補助説明は `en/` と `ja/` を優先します。

**English:** [en/README.md](en/README.md)

## レンダリングと図表

本リポジトリの図は、原則として SVG で記述します。標準の公開経路は、Markdown から SVG を参照し、[`tools/render_docs.py`](tools/render_docs.py) で静的 HTML に変換する方式です。レイアウト、インタラクション、印刷/PDF制御が必要な場合は、HTML 直書きも許容します。

SVG-first の図表方針とレンダリング手順は [`docs/rendering_policy.md`](docs/rendering_policy.md) を参照してください。

## 置くもの／置かないもの（要約）

### 置くもの

- 概念説明
  - 例: SLS、semantic lineage、ΔM、RDE、memory layer、auditability などの説明
  - [`en/concepts/`](en/concepts/README.md), [`ja/concepts/`](ja/concepts/README.md)（[#42](https://github.com/zyx-corporation/kotonoha-docs/issues/42)）
- 利用・運用のマニュアル
  - 例: [`en/manual/`](en/manual/README.md), [`ja/manual/`](ja/manual/README.md)
- 学習用チュートリアル
  - 例: [`en/tutorials/`](en/tutorials/README.md), [`ja/tutorials/`](ja/tutorials/README.md)
- 受入デモなど、仕様外の確認手順
  - 例: [`en/acceptance/`](en/acceptance/README.md), [`ja/acceptance/`](ja/acceptance/README.md)
- FAQ、移行メモ、ハウツー、補助的な説明
- 開発**手法**の説明
  - 例: [`en/method/`](en/method/README.md), [`ja/method/`](ja/method/README.md)
  - ただし、これは仕様正本ではなく、説明・手順の層です。
- **参考論文・プレプリント**
  - 配置: [`ja/paper/README.md`](ja/paper/README.md)
  - 背景理解・研究文脈・設計思想を補助する参考資料であり、normative ではありません。
- 本リポジトリへの貢献手順
  - [`CONTRIBUTING.md`](CONTRIBUTING.md)

### 置かないもの

- 実装者向けの **規範仕様・スキーマ・安定インターフェースの定義**
  - 仕様の正本は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) に置きます。
- 非公開の計画・草案……公開リポジトリでは書かず、提携コントリビューター向けにはメンテナ側のチャネルで個別に案内があります。

## 関連リポジトリ

| リポジトリ | 役割 |
| --- | --- |
| [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | SLS の **公開仕様**（正本） |
| [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) | OSS **コア実装** とコードに紐づく開発者向け文書 |
| [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli) | 公式 **`kotonoha`** CLI（[`CLI 定義`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md)） |
| **kotonoha-docs（本リポジトリ）** | **仕様外**の公開ドキュメント（マニュアル・チュートリアル・受入デモ・概念説明・参考論文等） |

## 言語方針

リポジトリ直下の言語別領域は以下です。

- `en/`: 英語
- `ja/`: 日本語

両領域は、原則として同じ構造を持つようにします。一方の言語が先行する場合は、対応するもう一方の場所に、既存文書へのリンクまたは翻訳待ちである旨を示します。

## ライセンス

特記なき限り [Apache License 2.0](LICENSE) とします。
