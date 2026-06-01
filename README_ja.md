# kotonoha-docs（日本語公開情報の入口）

## プロジェクトの目的と目標

Kotonoha は、AI 支援開発における意味変化を追跡可能にし、設計意図と実装のずれを監査可能にするための取り組みです。  
`kotonoha-docs` は、そのための公開ドキュメント入口として、利用者やコミュニティが「何を目指しているか」「どこから始めるか」を短時間で把握できるようにすることを目標とします。

- 目的: 概念、運用、学習手順を公開し、理解と参加のハードルを下げる
- 目標: 初学者が「理解する → 試す → 継続利用する」までの導線を明確にする
- 範囲: 規範仕様ではない説明文書（概念説明、マニュアル、チュートリアル、受入デモ、参考資料）

仕様の正本・規範定義は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) にあります。

## 最初に読む（プロジェクト理解）

- プロジェクト全体像: [`ja/README.md`](ja/README.md)
- 主要概念（SLS / semantic lineage / RDE など）: [`ja/concepts/README.md`](ja/concepts/README.md)
- 背景となる開発方法論: [`ja/method/README.md`](ja/method/README.md)

## はじめる（インストール・初回実行）

- **Release Train 2026-05（v0.3 baseline）:** [`ja/releases/kotonoha-release-train-2026-05.md`](ja/releases/kotonoha-release-train-2026-05.md)
- CLI インストール（`curl | bash`）: [`ja/tutorials/install_kotonoha_cli.md`](ja/tutorials/install_kotonoha_cli.md)
- Obsidian プラグイン（GitHub Release）: [`ja/manual/install_obsidian_kotonoha_console.md`](ja/manual/install_obsidian_kotonoha_console.md)
- 最初の CLI セッション: [`ja/tutorials/first_cli_session.md`](ja/tutorials/first_cli_session.md)
- クイックスタート（SLM デモ）: [`ja/tutorials/slm_demo_quickstart.md`](ja/tutorials/slm_demo_quickstart.md)
- 記録フロー（DB-backed、任意）: [`ja/tutorials/kotonoha_record_flow.md`](ja/tutorials/kotonoha_record_flow.md)
- インストーラー実装手順（メンテナ）: [`ja/manual/cli_installer_implementation.md`](ja/manual/cli_installer_implementation.md)
- CLI リポジトリ: [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli)

## 用途別ドキュメント導線

| 目的 | 読む場所 |
| --- | --- |
| 概念を理解したい | [`ja/concepts/`](ja/concepts/README.md) |
| 実運用の手順を見たい | [`ja/manual/`](ja/manual/README.md) |
| 学習しながら試したい | [`ja/tutorials/`](ja/tutorials/README.md) |
| 公開受入手順を確認したい | [`ja/acceptance/`](ja/acceptance/README.md) |
| Release Train / 配布 baseline | [`ja/releases/`](ja/releases/README.md) |
| 研究背景を参照したい | [`ja/paper/`](ja/paper/README.md) |

## 関連リポジトリ

| リポジトリ | 役割 |
| --- | --- |
| [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | 公開仕様の正本（normative） |
| [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) | OSS コア実装と開発者向け文書 |
| [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli) | 公式 CLI と CLI 定義 |
| **kotonoha-docs（本リポジトリ）** | 仕様外の公開説明文書（non-normative） |

## 言語案内

- 日本語: `ja/`
- 英語: `en/`（[English README](en/README.md)）

両言語は、原則として同じ構造を保つ方針です。

## 補足

- 図表のレンダリング方針: [`docs/rendering_policy.md`](docs/rendering_policy.md)
- 貢献手順: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- ライセンス: [Apache License 2.0](LICENSE)
