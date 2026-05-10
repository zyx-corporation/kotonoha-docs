# GitHub Organization のワークフロー（短い要約）

**English (primary):** [github_organization_workflow.md](github_organization_workflow.md)

本ページは、**Kotonoha（SLS）** Organization が **GitHub Projects** とカスタムフィールドをどう使うかについての**公開向け・簡略版**である。**完了条件の正本は Issue／PR の本文**であり、本ページでは置き換えない。

## Organization Project

- **組織横断の正規ボード**（[Kotonoha (SLS) — project #7](https://github.com/orgs/zyx-corporation/projects/7)）で、`kotonoha-spec`、`kotonoha-core`、`kotonoha-cli`、`kotonoha-docs`、および同じボードに参加する運用用リポジトリの作業を追う。
- **ボードの 1 行 ≒ 1 つの追跡単位**であり、通常はリンクされた **Issue**（本文に完了条件が明示された PR のみのケースは例外可）。
- **同じ Issue を Organization Project とリポジトリ専用 Project の両方に載せない**。載せる場合は Issue 本文でどちらを正とするかを書く（[`docs/github_projects_policy.md`](github_projects_policy.md)）。

## カスタムフィールド（意味の整理）

メンテナ側の定義に合わせる：

| フィールド | 意味（要約） |
| --- | --- |
| **Status** | 進行段階（Backlog → In Progress → In Review → Done）。**Done** は、リンク先の変更がマージされ Issue の受け入れ条件を満たした状態を指し、「いずれ終わらせる」という意図だけではない。 |
| **Priority** | チーム内での緊急度の相対値（例: P0〜P3）。 |
| **Phase** | 内部フェーズ計画における開発 **フェーズ 0〜4**（観念整理 → 公開仕様 MVP → Core 最小 → RDE 運用の製品化 → 拡張）。**主に効く Phase を 1 つ**設定する。複数フェーズにまたがるときは子 Issue に分割してよい。 |
| **Area** | 粗い領域（`docs`、`spec`、`core`、`ci` など）。 |

**Phase とマイルストーン：** Projects の **Phase** は、GitHub の **マイルストーン**（例:「製品 MVP」）と**同じものではない**。両方あてはまるときは Issue 本文で関係を書く。

## 真実の優先順位

1. Issue／PR の説明とコメント（目的・完了条件）。  
2. 既定ブランチへのマージ済みコミット（必要ならタグ）。  
3. Project のフィールド（優先付け用のスナップショット）。  
4. ラベル。

ボードだけを「完了」の記録として扱わない。

## このリポジトリ内の関連文書

- **[`docs/github_projects_policy.md`](github_projects_policy.md)** — 参加のしかたと公開境界。  
- **[`docs/git_operation_rules.md`](git_operation_rules.md)** — Issue／ブランチ／PR のルール（日本語・複製）。

運用上の**詳細ルールの正本**は計画用リポジトリ側で保守する。公開向け Issue 本文には、可能な範囲で内部専用 URL を載せない。
