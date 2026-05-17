---
title: "🧩 Kotonoha Architecture Concept Terminology"
created: "2026-05-12T00:55:00+09:00"
updated: "2026-05-12T00:55:00+09:00"
author: "Tomoyuki Kano <tomyuk@zyxcorp.jp>"
tags: [kotonoha, architecture, rde, semantic-lineage, relation-store, audit]
links: []
source_type: "chatgpt"
source_id: "kotonoha-architecture-terms-2026-05-12"
document_type: "architecture_terms"
status: "draft"
---
# 🧩 Kotonoha Architecture Concept Terminology

この文書は、Kotonoha アーキテクチャ概念図に対応する構成要素・概念用語の定義表である。

Kotonoha は、外部入力を単に分類・要約するシステムではなく、入力から生じる出来事を `MeaningEvent` として正規化し、関係履歴、意味変化 ΔM、RDE 評価、Policy Boundary、監査ログを通じて、人間が判断可能な形へ整える意味監査バックエンドとして位置づける。

## 1. 全体構造

```text
External Sources
  ↓
Event Normalizer
  ↓
MeaningEvent
  ↓
Meaning Event Bus
  ↓
Meaning Extractor / Relation Resolver / ΔM Detector
  ↓
RDE Evaluator
  ↓
Policy Boundary
  ↓
Action Proposal
  ↓
Human Review
  ↓
relation_store / lineage_store / audit_log
```

## 2. 概念用語一覧

| 用語 | 種別 | 定義 | 主な入力 | 主な出力 | 責任範囲 |
|---|---|---|---|---|---|
| 入力ソース | 外部入力 | Kotonoha に流入する意味イベントの発生源。 | Mail / IMAP、Slack、Calendar API、Docs、Obsidian、GitHub Issues、Sensor Events | 生データ、イベント通知、会話、予定、文書変更、センサーイベント | 外部世界の出来事を提供する。意味判断はしない。 |
| Event Normalizer | 正規化層 | 外部入力を共通形式の `MeaningEvent` に変換する層。 | メール本文、Slack投稿、予定、Issue、文書差分、センサーイベント | `MeaningEvent` | 入力形式の差異を吸収する。意味評価・最終判断は行わない。 |
| MeaningEvent | 中間表現 | Kotonoha 内部で扱う標準イベント単位。 | 正規化済みイベント | 各処理モジュールへの入力 | 「誰が・何を・どの文脈で・いつ発生させたか」を保持する。 |
| Meaning Event Bus | 内部連携基盤 | 各処理モジュールを疎結合に接続するイベントバス。 | `MeaningEvent`、解析結果、評価結果、フィードバック | 各モジュールへのイベント配信 | point-to-point 接続を避け、必要時に相互接続する。 |
| Meaning Extractor | 意味抽出層 | イベントから意図・要求・論点・感情的含意を抽出する。 | `MeaningEvent`、本文、会話文脈 | intent、request、topic、stance、unresolved_points | 発話行為と意味要素を抽出する。最終判断はしない。 |
| Relation Resolver | 関係解決層 | イベントがどの人物・組織・案件・関係履歴に属するかを解決する。 | `MeaningEvent`、送信者、過去履歴、文書・タスク文脈 | relation_id、actor、context、project、role | 関係主体と文脈を同定する。 |
| ΔM Detector | 意味差分検出層 | 前回状態との差分として意味変化 ΔM を検出する。 | 現在の意味状態、過去の意味状態、relation_store、lineage_store | ΔM summary、change_type、risk_hint | 何が変化したかを抽出する。変化の許容性判断は RDE に渡す。 |
| RDE Evaluator | 意味逸脱評価層 | 意味変化が保存・変換・補完・逸脱のどれに当たるかを評価する。 | ΔM、元文脈、生成案、過去判断、関係履歴 | preserved、authorized_transformation、inferred_extension、suspicious_drift、critical_distortion | 意味変化の監査を担う。Policy の代替ではない。 |
| Policy Boundary | 権限・安全境界 | どの操作が許可されるか、人間承認が必要かを判定する。 | RDE結果、操作候補、権限、リスク、ユーザー設定 | allow、require_review、block、escalate | 実行可能性と介入境界を制御する。 |
| Action Proposal | 行動提案層 | Kotonoha の判断結果を、通知・下書き・タスク化などの候補へ変換する。 | 意味抽出結果、RDE評価、Policy判定、関係文脈 | 返信下書き、Slack通知、予定候補、タスク候補、レビュー依頼 | 実行ではなく、原則として「提案」を生成する。 |
| Human Review | 人間確認層 | Kotonoha の判断・提案を人間が確認・修正・承認する。 | Action Proposal、RDE理由、未解決点、信頼度 | approve、reject、edit、defer | 判断主体を人間側に残す。 |
| Feedback Loop | 学習・補正循環 | 人間の承認・却下・修正を関係履歴や監査ログへ戻す循環。 | Human Review の結果 | relation update、policy adjustment、future hint | Kotonoha の判断傾向を継続的に補正する。 |
| relation_store | 永続ストア | 人物・組織・案件・文脈に関する関係履歴を保持する。 | relation_id、actor、trust、stability、context_affinity、判断履歴 | 関係状態、参照文脈、更新候補 | 関係の変化と継続性を保存する。 |
| lineage_store | 永続ストア | 意味状態と意味変化の系列を保持する。 | MeaningEvent、meaning_state、ΔM、文書・会話履歴 | 過去状態、意味差分履歴、分岐・統合履歴 | SLS 的な意味履歴を保存する。 |
| audit_log | 永続ストア | 判断・評価・提案・承認の来歴を記録する。 | RDE結果、Policy判定、Action Proposal、人間操作 | 監査証跡、説明可能な判断履歴 | 後から「なぜそう判断したか」を追跡可能にする。 |
| 出力先 | 外部出力 | Kotonoha の提案や監査結果を人間・外部ツールへ渡す先。 | Action Proposal、Audit Report、承認済み操作 | Mail Draft、Slack Notice、Calendar Task、Audit Report | 実行・通知・提示の受け皿。 |
| Mail Draft | 出力先 | メール返信案を生成・提示する。 | Action Proposal、文脈、未解決点 | 返信下書き | 自動送信ではなく、原則として下書き生成を担う。 |
| Slack Notice | 出力先 | Slack 上で必要な通知・要約・確認依頼を行う。 | Action Proposal、チーム文脈 | 通知、確認依頼、要約 | 組織内の暗黙合意や未解決点を可視化する。 |
| Calendar Task | 出力先 | 予定候補・タスク候補へ変換する。 | 期限、依頼、会議文脈、優先度 | カレンダー候補、ToDo、リマインド | 時間・責任・依存関係を扱う。 |
| Audit Report | 出力先 | 判断理由・意味変化・介入境界を報告する。 | audit_log、RDE結果、Policy判定 | 監査レポート、説明文 | 監査可能性を人間に返す。 |

## 3. 重要な責任分離

### 3.1 RDE Evaluator と Policy Boundary

`RDE Evaluator` と `Policy Boundary` は混同してはならない。

- `RDE Evaluator` は、意味変化が妥当か、補完が過剰ではないか、元の意図から危険に逸脱していないかを評価する。
- `Policy Boundary` は、その評価結果を踏まえて、実際に通知・下書き・タスク作成・外部送信などを許可してよいかを裁定する。

つまり、RDE は意味の監査層であり、Policy Boundary は実行・介入の境界層である。

### 3.2 Action Proposal と自律実行

`Action Proposal` は、原則として自律実行ではない。

Kotonoha は「勝手に処理する秘書」ではなく、「監査可能な判断材料を整える秘書層」として設計する。自動送信、自動削除、外部投稿、予定確定、権限変更などの強い操作は、`Policy Boundary` と `Human Review` によって明示的に制御されるべきである。

## 4. RDE 差異検証

### 保存された要素

- Kotonoha を意味監査バックエンドとして扱う設計思想
- `MeaningEvent`、ΔM、RDE、relation_store、lineage_store、audit_log の中核構造
- 人間判断を奪わず、判断可能性を高めるという原則

### 変換された要素

- アーキテクチャ概念図を、設計レビューで参照可能な用語一覧表へ変換した
- 図上の要素を、責任範囲・入出力・境界の観点から再定義した

### 補完された要素

- RDE と Policy Boundary の責任分離
- Action Proposal と自律実行の分離
- Feedback Loop の明示

### 未解決のまま残した要素

- 各モジュールの具体的 API スキーマ
- `MeaningEvent` の正式 JSON / YAML schema
- relation_store / lineage_store / audit_log の物理実装方式
- Policy Boundary における権限モデル

### 逸脱リスク

- Kotonoha が「意味監査層」ではなく、単なる自律エージェント基盤として誤読されること
- RDE が Policy や Safety Filter と混同されること
- Action Proposal が自動実行前提として実装されること

### 次回更新方針

次回は、`MeaningEvent` の最小スキーマ、RDE評価結果の分類スキーマ、Action Proposal の承認フローを別文書として分離する。

## 5. Related

- Issue: #27
- Kotonoha 構想（非規範）: [`ja/concepts/kotonoha_concept_overview.md`](../../../ja/concepts/kotonoha_concept_overview.md) / [English](../../../en/concepts/kotonoha_concept_overview.md)
