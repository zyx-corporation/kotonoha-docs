# Kotonoha ドキュメント — 日本語

## はじめての方へ

このページは、`kotonoha-docs` リポジトリの日本語公開文書（`ja/`）の入口です。

Kotonoha を初めて知る人は、まず次の順で読んでください。

| 順 | 文書 | 目的 |
| --- | --- | --- |
| 1 | [はじめての Kotonoha](start-here.md) | Kotonoha が何をする仕組みかを理解する |
| 2 | [初学者向け用語集](glossary_for_beginners.md) | RDE / SLS / interchange などの用語をざっくり理解する |
| 3 | [読者別ラーニングパス](learning-path.md) | 自分の目的に合う読み順を選ぶ |

この 3 つを読めば、最初から仕様正本、受入デモ、Release Train、長文論文を読む必要はありません。

## Kotonoha の位置づけ

Kotonoha は、AI 支援開発や文書更新における **意味の変化** を追跡し、設計意図と成果物のずれを監査可能にする取り組みです。

| 観点 | Git 等の従来の記録 | Kotonoha が問うこと |
| --- | --- | --- |
| 変更の記録 | 何が変わったか | その変化で何が起きたか |
| 対象 | 差分・履歴 | 保存、変形、補完、喪失、逸脱、不確実性 |
| 目的 | 再現・マージ | 意味履歴としての追跡と再合意 |

中核概念は **Semantic Lineage System（SLS）** と **Resonant Deviation Evaluator（RDE）** です。ただし、初学者は最初から厳密な仕様定義を読む必要はありません。

## まず試す

ターミナルを使える場合は、次の順で進めます。

| 順 | 文書 | 到達点 |
| --- | --- | --- |
| 1 | [Kotonoha CLI のインストール](tutorials/install_kotonoha_cli.md) | `kotonoha version` が動く |
| 2 | [最初の CLI セッション](tutorials/first_cli_session.md) | `kotonoha rde emit` と `validate --strict` を試す |
| 3 | [SLM デモクイックスタート](tutorials/slm_demo_quickstart.md) | 草案生成と検証の流れを体験する |

この段階では PostgreSQL、Obsidian、VS Code は必須ではありません。

## 読者別導線

| 読者 | 入口 |
| --- | --- |
| 初めて来た人 | [はじめての Kotonoha](start-here.md) |
| 用語で迷った人 | [初学者向け用語集](glossary_for_beginners.md) |
| 自分に合う読み順を選びたい人 | [読者別ラーニングパス](learning-path.md) |
| CLI を試したい人 | [Tutorials](tutorials/README.md) |
| Obsidian / VS Code で使いたい人 | [Manual](manual/README.md) |
| 開発やレビューに参加したい人 | [Method](method/README.md) |
| リリース確認をしたい人 | [Acceptance](acceptance/README.md) |
| 配布 baseline を確認したい人 | [Releases](releases/README.md) |
| 背景思想を読みたい人 | [Paper](paper/README.md) |

## 文書一覧

各ブロックは **説明（本文）** と **索引（表）** に分けています。パスは `ja/` からの相対パスです。

### 初学者向け入口

| 文書 | 内容 |
| --- | --- |
| [start-here.md](start-here.md) | Kotonoha を初めて読む人のための入口 |
| [glossary_for_beginners.md](glossary_for_beginners.md) | 初学者向けの用語説明 |
| [learning-path.md](learning-path.md) | 読者別の読み進め方 |

### 概念（Concepts）

Kotonoha / SLS / RDE の構想と用語を説明します。規範定義の代替ではありません。

| 文書 | 内容 |
| --- | --- |
| [kotonoha_concept_overview.md](concepts/kotonoha_concept_overview.md) | 非規範要約（意味履歴、RDE の役割、人間承認） |
| [README.md](concepts/README.md) | 概念領域の索引・関連リンク |

### チュートリアル（Tutorials）

学習向けの段階的手順です。厳密な契約より理解を優先します。

| 文書 | 内容 |
| --- | --- |
| [install_kotonoha_cli.md](tutorials/install_kotonoha_cli.md) | `curl \| bash` による CLI 導入 |
| [first_cli_session.md](tutorials/first_cli_session.md) | `version` / `rde emit` / `interchange emit` の入門 |
| [slm_demo_quickstart.md](tutorials/slm_demo_quickstart.md) | ローカル SLM → 検証 → 人間レビューの体験 |
| [kotonoha_record_flow.md](tutorials/kotonoha_record_flow.md) | 検証済み RDE 草案を DB-backed な Kotonoha record として保存 |
| [README.md](tutorials/README.md) | チュートリアル領域の索引 |

### マニュアル（Manual）

利用・運用の参照文書です。前提条件と手順を中心に記述します。

| 文書 | 内容 |
| --- | --- |
| [install_obsidian_kotonoha_console.md](manual/install_obsidian_kotonoha_console.md) | Obsidian プラグイン — GitHub Release からの手動インストール |
| [vscode_extension_operations.md](manual/vscode_extension_operations.md) | CLI・DB・ワークスペース、ΔM / RDE / Review 操作 |
| [llm_slm_usage.md](manual/llm_slm_usage.md) | 草案生成、validation、人間による最終判断の分離 |
| [cli_installer_implementation.md](manual/cli_installer_implementation.md) | CLI インストーラーのメンテナ向け実装手順 |
| [README.md](manual/README.md) | マニュアル領域の索引 |

### 方法論（Method）

プロジェクト自身が SLS + RDE をどう適用するかを説明します。公開ドラフト・事例・運用要約を含みます。

| 文書 | 内容 |
| --- | --- |
| [kotonoha_method_outline.md](method/kotonoha_method_outline.md) | 方法論の骨子（タスクではなく意味・責任の系列として統治） |
| [sls_rde_development_method.md](method/sls_rde_development_method.md) | 仕様・実装・文書化への dogfooding 事例 |
| [rde_review_quick_guide.md](method/rde_review_quick_guide.md) | いつ RDE を検討するかの公開向け要約 |
| [README.md](method/README.md) | Method 領域の索引 |

### 受入デモ（Acceptance）

公開動作の検証手順です。リリース確認・受入テスト向けであり、初学者向けチュートリアルではありません。

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
