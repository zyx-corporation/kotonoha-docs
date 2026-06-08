# 読者別ラーニングパス

Kotonoha の文書は、概念、チュートリアル、マニュアル、受入デモ、研究背景に分かれています。最初から全部読む必要はありません。自分の目的に合う入口から進んでください。

## まず全員におすすめ

最初は、次の 2 つだけで十分です。

1. [はじめての Kotonoha](start-here.md)
2. [初学者向け用語集](glossary_for_beginners.md)

そのあと、目的別に進みます。

## 使ってみたい人

CLI を入れて、最小動作を試すルートです。PostgreSQL や Obsidian は不要です。

| 順 | 文書 | 到達点 |
| --- | --- | --- |
| 1 | [Kotonoha CLI のインストール](tutorials/install_kotonoha_cli.md) | `kotonoha version` が動く |
| 2 | [最初の CLI セッション](tutorials/first_cli_session.md) | `kotonoha rde emit` と `validate --strict` を試す |
| 3 | [SLM デモクイックスタート](tutorials/slm_demo_quickstart.md) | 草案生成と検証の流れを体験する |

## Obsidian で使いたい人

ノート環境の中で Kotonoha Console を使うルートです。まず CLI の最小理解を済ませてから進むことを推奨します。

| 順 | 文書 | 到達点 |
| --- | --- | --- |
| 1 | [はじめての Kotonoha](start-here.md) | 何をする仕組みか理解する |
| 2 | [最初の CLI セッション](tutorials/first_cli_session.md) | RDE skeleton と interchange の役割を知る |
| 3 | [Obsidian Kotonoha Console のインストール](manual/install_obsidian_kotonoha_console.md) | Obsidian で提案・RDE・承認の入口を使う |

## 開発に参加したい人

仕様と実装の境界を理解し、CLI や UI の変更に関わるルートです。

| 順 | 文書 | 到達点 |
| --- | --- | --- |
| 1 | [はじめての Kotonoha](start-here.md) | プロジェクトの目的を理解する |
| 2 | [Kotonoha 構想概要](concepts/kotonoha_concept_overview.md) | SLS / RDE / 人間承認の位置づけを理解する |
| 3 | [Method](method/README.md) | プロジェクト自身の SLS + RDE 適用方法を知る |
| 4 | [CLI インストーラー実装手順](manual/cli_installer_implementation.md) | インストーラー保守の前提を知る |
| 5 | [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | 仕様正本を確認する |

## リリース確認・受入確認をしたい人

学習ではなく、公開動作の確認を行うルートです。

| 順 | 文書 | 到達点 |
| --- | --- | --- |
| 1 | [Release Train](releases/README.md) | 対象 baseline を確認する |
| 2 | [Phase 2 CLI 受入デモ](acceptance/phase2_cli_acceptance_demo.md) | 終了コード・strict 検証・任意永続化を確認する |
| 3 | [CLI version policy](manual/cli_version_policy.md) | バージョン整合性を確認する |

## 思想・研究背景を読みたい人

Kotonoha がなぜ必要なのか、背景にある意味監査や制度設計を読むルートです。

| 順 | 文書 | 到達点 |
| --- | --- | --- |
| 1 | [Kotonoha 構想概要](concepts/kotonoha_concept_overview.md) | 構想の中心を理解する |
| 2 | [Kotonoha Method Outline](method/kotonoha_method_outline.md) | 方法論としての位置づけを理解する |
| 3 | [RDE Review Quick Guide](method/rde_review_quick_guide.md) | レビュー観点を理解する |
| 4 | [Paper](paper/README.md) | 長文・研究背景へ進む |

## 迷ったときの判断

| 状況 | 進む先 |
| --- | --- |
| 何から読めばよいかわからない | [はじめての Kotonoha](start-here.md) |
| 用語が難しい | [初学者向け用語集](glossary_for_beginners.md) |
| まず動かしたい | [Kotonoha CLI のインストール](tutorials/install_kotonoha_cli.md) |
| 仕様が必要 | [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) |
| リリース確認が必要 | [Acceptance](acceptance/README.md) |
| 背景思想を読みたい | [Paper](paper/README.md) |

## このページの境界

このページは、学習順序を案内するための非規範ドキュメントです。コマンドの正確な挙動、スキーマ、適合条件、安定性 tier は、各実装リポジトリまたは [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) を確認してください。
