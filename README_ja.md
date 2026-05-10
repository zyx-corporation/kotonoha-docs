# kotonoha-docs（日本語概要）

**Semantic Lineage System（SLS）の仕様に含まれない**、利用者・コミュニティ向けの**公開ドキュメント**を置くリポジトリです。

仕様の正本・規範的な定義は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) にあります。本リポジトリは **マニュアル**、**チュートリアル**、**ハウツー**、**受入デモ**、**補助的な説明**など、normative ではない公開文書を対象とします。

**English:** [README.md](README.md)

## 置くもの／置かないもの（要約）

### 置くもの

- 利用・運用のマニュアル
  - 例: [`docs/manual/`](docs/manual/README.md)
- 学習用チュートリアル
  - 例: [`docs/tutorials_ja/`](docs/tutorials_ja/README.md)
- 受入デモなど、仕様外の確認手順
  - 例: [`docs/acceptance_ja/`](docs/acceptance_ja/README.md)
- FAQ、移行メモ、ハウツー、補助的な説明
- 開発**手法**の説明
  - 例: SLS + RDE を自プロセスにどう当てるか
  - 例: [`docs/method/`](docs/method/README.md)
  - ただし、これは仕様正本ではなく、説明・手順の層です。
- 本リポジトリへの貢献手順
  - [`CONTRIBUTING.md`](CONTRIBUTING.md)

### 置かないもの

- 実装者向けの **規範仕様・スキーマ・安定インターフェースの定義**
  - 仕様の正本は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) に置きます。
- 非公開の計画・草案
  - private `kotonoha-management` で管理します。

## 関連リポジトリ

| リポジトリ | 役割 |
| --- | --- |
| [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | SLS の **公開仕様**（正本） |
| [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) | OSS **コア実装** とコードに紐づく開発者向け文書 |
| [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli) | 公式 **`kotonoha`** CLI（[`CLI 定義`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md)） |
| **kotonoha-docs（本リポジトリ）** | **仕様外**の公開ドキュメント（マニュアル・チュートリアル・受入デモ等） |

## 言語方針

原則 **英語** を正とします。日本語版は英語の横に `*_ja.md` で追加します。

## ライセンス

特記なき限り [Apache License 2.0](LICENSE) とします。
