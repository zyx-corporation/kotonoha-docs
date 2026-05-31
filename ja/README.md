# Kotonoha ドキュメント — 日本語

## このページについて

本ページは、`kotonoha-docs` リポジトリの **日本語公開文書**（`ja/`）の入口です。対象読者は、利用者、コミュニティ参加者、新規のコントリビュータです。

ここに置く文書は **非規範**（informative）です。概念の説明、運用手順、学習ガイド、受入確認、研究背景の参考資料を扱います。API・スキーマ・適合要件の正本は別リポジトリに置き、本領域では重複定義しません。

## Kotonoha の位置づけ

Kotonoha は、AI 支援開発における **意味の変化** を追跡し、設計意図と成果物のずれを監査可能にする取り組みです。

| 観点 | Git 等の従来の記録 | Kotonoha が問うこと |
| --- | --- | --- |
| 変更の記録 | 何が変わったか | その変化で何が起きたか |
| 対象 | 差分・履歴 | 保存、変形、暗黙補完、逸脱、不確実性 |
| 目的 | 再現・マージ | 意味履歴としての追跡と再合意 |

中核概念は **Semantic Lineage System（SLS）** と **Resonant Deviation Evaluator（RDE）** です。詳細は「概念」セクションの文書を参照してください。

## 上位入口と言語

| 種別 | パス |
| --- | --- |
| リポジトリ全体（目的・目標・導線） | [README_ja.md](../README_ja.md) |
| 英語ドキュメント領域 | [en/README.md](../en/README.md) |
| 規範仕様（正本） | [kotonoha-spec](https://github.com/zyx-corporation/kotonoha-spec) |

## 読み進め方

用途に応じて、次の順序を目安にしてください。各段階の文書パスは下表のとおりです。

| 段階 | 目的 | 文書 |
| --- | --- | --- |
| 1 | 構想を把握する | [kotonoha_concept_overview.md](concepts/kotonoha_concept_overview.md) |
| 1b | 配布 baseline（Release Train）を確認する | [kotonoha-release-train-2026-05.md](releases/kotonoha-release-train-2026-05.md) |
| 2 | CLI をインストールする | [install_kotonoha_cli.md](tutorials/install_kotonoha_cli.md) |
| 3 | CLI を手で試す（DB 不要） | [first_cli_session.md](tutorials/first_cli_session.md) |
| 4 | SLM 草案と検証の流れを体験する | [slm_demo_quickstart.md](tutorials/slm_demo_quickstart.md) |
| 5 | Obsidian で提案・RDE・承認を使う | [install_obsidian_kotonoha_console.md](manual/install_obsidian_kotonoha_console.md) |
| 6 | VS Code で ΔM / RDE / Review を使う | [vscode_extension_operations.md](manual/vscode_extension_operations.md) |
| 7 | リリース前の最小動作を確認する | [phase2_cli_acceptance_demo.md](acceptance/phase2_cli_acceptance_demo.md) |

段階 1 のあと、背景を深く読む場合は [kotonoha_concept.md](paper/kotonoha_concept.md)（暫定版 v0.1）へ進みます。段階 6 は学習用チュートリアルとは目的が異なり、終了コードと strict 検証を確認する手順です。

## 文書一覧

各ブロックは **説明（本文）** と **索引（表）** に分けています。パスは `ja/` からの相対パスです。

### 概念（Concepts）

Kotonoha / SLS / RDE の構想と用語を説明します。規範定義の代替ではありません。

| 文書 | 内容 |
| --- | --- |
| [kotonoha_concept_overview.md](concepts/kotonoha_concept_overview.md) | 短い非規範要約（意味履歴、RDE の役割、人間承認） |
| [README.md](concepts/README.md) | 概念領域の索引・関連リンク |

### 方法論（Method）

プロジェクト自身が SLS + RDE をどう適用するかを説明します。公開ドラフト・事例・運用要約を含みます。

| 文書 | 内容 |
| --- | --- |
| [kotonoha_method_outline.md](method/kotonoha_method_outline.md) | 方法論の骨子（タスクではなく意味・責任の系列として統治） |
| [sls_rde_development_method.md](method/sls_rde_development_method.md) | 仕様・実装・文書化への dogfooding 事例 |
| [rde_review_quick_guide.md](method/rde_review_quick_guide.md) | いつ RDE を検討するかの公開向け要約 |
| [README.md](method/README.md) | Method 領域の索引（HTML プロトタイプへのリンク含む） |

### マニュアル（Manual）

利用・運用の参照文書です。前提条件と手順を中心に記述します。

| 文書 | 内容 |
| --- | --- |
| [install_obsidian_kotonoha_console.md](manual/install_obsidian_kotonoha_console.md) | Obsidian プラグイン — GitHub Release からの手動インストール |
| [vscode_extension_operations.md](manual/vscode_extension_operations.md) | CLI・DB・ワークスペース、ΔM / RDE / Review 操作 |
| [llm_slm_usage.md](manual/llm_slm_usage.md) | 草案生成、validation、人間による最終判断の分離 |
| [cli_installer_implementation.md](manual/cli_installer_implementation.md) | CLI インストーラーのメンテナ向け実装手順 |
| [README.md](manual/README.md) | マニュアル領域の索引 |

### チュートリアル（Tutorials）

学習向けの段階的手順です。厳密な契約より理解を優先します。

| 文書 | 内容 |
| --- | --- |
| [install_kotonoha_cli.md](tutorials/install_kotonoha_cli.md) | `curl \| bash` による CLI 導入 |
| [first_cli_session.md](tutorials/first_cli_session.md) | `version` / `rde emit` / `interchange emit` の入門 |
| [slm_demo_quickstart.md](tutorials/slm_demo_quickstart.md) | ローカル SLM → 検証 → 人間レビューの体験 |
| [README.md](tutorials/README.md) | チュートリアル領域の索引 |

### 受入デモ（Acceptance）

公開動作の検証手順です。リリース確認・受入テスト向けです。

| 文書 | 内容 |
| --- | --- |
| [phase2_cli_acceptance_demo.md](acceptance/phase2_cli_acceptance_demo.md) | CLI + Core 最小面、strict 検証、任意の永続化 |
| [README.md](acceptance/README.md) | 受入デモ領域の索引 |

### Release Train

モジュール横断の配布 baseline と commit / stability tier の一覧です。

| 文書 | 内容 |
| --- | --- |
| [kotonoha-release-train-2026-05.md](releases/kotonoha-release-train-2026-05.md) | 2026-05 / v0.3 train — First UI hardening baseline |
| [README.md](releases/README.md) | Release Train 領域の索引 |

### 論文・長文（Paper）

研究背景・設計思想の参考資料です。normative ではありません。

| 文書 | 内容 |
| --- | --- |
| [kotonoha_concept.md](paper/kotonoha_concept.md) | 概要より詳しい背景・論点（暫定 v0.1） |
| [README.md](paper/README.md) | 論文・PDF / LaTeX の取り扱い方針 |

## エコシステムリポジトリ

実装と仕様は、次のリポジトリに分離しています。

| リポジトリ | 役割 |
| --- | --- |
| [kotonoha-spec](https://github.com/zyx-corporation/kotonoha-spec) | 公開仕様の正本（normative） |
| [kotonoha-core](https://github.com/zyx-corporation/kotonoha-core) | OSS コア実装 |
| [kotonoha-cli](https://github.com/zyx-corporation/kotonoha-cli) | 公式 CLI（契約: `docs/cli-definition.md`） |
| [obsidian-kotonoha-console](https://github.com/zyx-corporation/obsidian-kotonoha-console) | Obsidian プラグイン（first usable UI） |
| [kotonoha-vscode](https://github.com/zyx-corporation/kotonoha-vscode) | VS Code / Cursor 拡張（M3 最小 UI） |

## 配置方針

- **説明・手順・学習資料** → `kotonoha-docs`（本リポジトリ）
- **意味・適合性・スキーマ・バージョン規則** → `kotonoha-spec`（リンクのみ、本文の重複禁止）

規範が必要な箇所では、説明文書に定義を書き足さず、仕様正本への参照で足りるようにしてください。
