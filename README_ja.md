# kotonoha-docs（日本語概要）

**Semantic Lineage System（SLS）の仕様に含まれない**、利用者・コミュニティ向けの**公開ドキュメント**を置くリポジトリです。

仕様の正本・規範的な定義は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) にあります。本リポジトリは **マニュアル**、**チュートリアル**、**ハウツー**、**受入デモ**、**補助的な説明**など、normative ではない公開文書を対象とします。

**English:** [README.md](README.md)

## 置くもの／置かないもの（要約）

| 種別 | 場所 | 備考 |
| --- | --- | --- |
| 利用・運用のマニュアル | [`docs/manual/`](docs/manual/README.md) | インストール、設定、運用、トラブルシュートなどの参照文書。 |
| 学習用チュートリアル | [`docs/tutorials_ja/`](docs/tutorials_ja/README.md) | 初学者向けの段階的な学習導線。 |
| 受入デモ | [`docs/acceptance_ja/`](docs/acceptance_ja/README.md) | 期待コマンド、出力、終了コードを確認する手順。チュートリアルではない。 |
| 開発手法 | [`docs/method/`](docs/method/README.md) | SLS + RDE を自プロセスにどう当てるか。仕様正本ではない。 |
| 本リポジトリへの貢献手順 | [`CONTRIBUTING.md`](CONTRIBUTING.md) | 実装リポジトリ向けの貢献手順とは分ける。 |

## 置かないもの

- 実装者向けの **規範仕様・スキーマ・安定インターフェースの定義** → [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)
- 非公開の計画・草案 → private [`kotonoha-management`](https://github.com/zyx-corporation/kotonoha-management)

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
