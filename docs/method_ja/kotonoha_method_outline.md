# Kotonoha Method — ドラフト骨子

Status: draft / non-normative

この文書は、**Kotonoha Method** の初期構成案である。Kotonoha Method は、Semantic Lineage System（SLS）の観点から導かれる、プロジェクト管理およびガバナンスの方法論として位置づける。

この文書は公開ドラフトであり、API、データスキーマ、相互運用性要件を定義するものではない。規範的な技術仕様は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) に置く。

---

## 1. 作業定義

**Kotonoha Method は、SLS の制度的実装である。**

より正確には、人間とAIが協働するプロジェクトにおいて、プロジェクトを単なるタスク集合ではなく、**意味・判断・成果物・責任の変化系列**として統治するための方法論である。

周辺概念との関係は次のように整理する。

| 層 | 役割 |
| --- | --- |
| **SLS** | 意味・判断・成果物が時間の中でどう変化したかを記録し、意味の系譜を追跡する。 |
| **RDE** | 意味変化を評価し、保存・変換・補完・未解決・喪失・逸脱リスクを見分ける。 |
| **Kotonoha Method** | それらをプロジェクト運営、レビュー習慣、意思決定手順、責任構造として制度化する。 |
| **Kotonoha Console** | 意味の系譜を観察・編集・レビュー・統治するための人間向けUIを提供する。 |

短く言えば、次のように表現できる。

> SLS は意味の系譜を記録する。RDE は意味の逸脱を評価する。Kotonoha Method は、その両者を制度的実践に変換する。

---

## 2. なぜこの方法論が必要か

一般的なプロジェクト管理は、タスク、担当者、期限、ステータスを追跡することに長けている。一方で、要求、文書、コード、AI生成物が同時に変化するプロジェクトにおいて、**意味がどのように変化したか**を追跡する力は弱い。

AI支援プロジェクトでは、この弱点が深刻化する。

- タスクは完了しているが、当初の意図が狭められている。
- 生成されたドラフトは流暢だが、未解決の緊張を偽の結論で置き換えている。
- リファクタリングにより構造は改善されたが、設計を安全にしていた理由が失われている。
- プロジェクトボード上では進捗しているが、責任が拡散しすぎて引き受け不能になっている。

Kotonoha Method は、これらをプロジェクト上の一次的リスクとして扱う。

この方法論は、Git、Issue、Pull Request、プロジェクトボードを置き換えない。むしろ、それらに次の問いを追加する制度的レイヤーである。

- どの意味が変化したのか。
- その変化はプロジェクトの意図によって許可されているのか。
- 何が保存され、何が変換され、何が補完され、何が延期され、何が失われたのか。
- その変化の帰結を、誰が、またはどの構造が引き受けるのか。

---

## 3. 中核原則

### 3.1 スループットより意味

速度は重要である。しかし、その変化が何であり、なぜ起きたのかを説明できない速度は危険である。AIによる加速は、意味上の説明責任を消してはならない。

### 3.2 意図の保存

重要な変更は、先行する意図を保存するか、明示的に変換するか、明示的に拒否する必要がある。沈黙のうちに意図を置換することは逸脱として扱う。

### 3.3 許可された変換

すべての変化が喪失ではない。ある変化は、責任を引き受けうる構造を保ったまま、アイデアを別の形式へ移す正当な変換でありうる。

### 3.4 未解決性の明示

未解決の緊張は可視化されたまま残すべきである。不確実性を完了済みに見せかけることは、問いを開いたままにすることより危険である。

### 3.5 責任の再収束

作業中の責任は、人間、ツール、文書、AIエージェントのあいだに分散しうる。しかし、帰結は引き受け可能な構造へ再収束しなければならない。

### 3.6 ツール非依存

この方法論は、GitHub、Obsidian、ローカルファイル、Issue tracker、将来のSLSネイティブツールのいずれでも機能すべきである。概念は特定プロダクトへ閉じない。

### 3.7 非スコアリング型ガバナンス

構造化レビューは用いるが、単純なスコアリングには還元しない。RDE的観察項目は判断の代替ではなく、判断を支えるプロンプトである。

---

## 4. 章立て案

### Part I — 基礎

#### Chapter 1. タスク管理から意味統治へ

タスク完了だけでは、AI支援・意味集約型プロジェクトを管理しきれない理由を説明する。運用上の進捗と意味的連続性の差異を導入する。

主題:

- 従来型プロジェクト管理の限界
- AI生成による加速と意味ドリフト
- 意味、責務、制度的記憶
- なぜGit履歴だけでは不十分なのか

#### Chapter 2. 中核語彙

公開SLS仕様を過剰に先取りせず、方法論として必要な作業語彙を定義する。

主題:

- 意味の系譜
- ΔM / 意味変化
- 意図、成果物、判断、責任
- 保存・変換・補完・未解決・喪失・逸脱リスク
- 制度的実装

#### Chapter 3. SLS、RDE、Kotonoha Method

Kotonohaエコシステムにおける方法論の位置を整理する。

主題:

- 意味系譜基盤としてのSLS
- 意味逸脱評価としてのRDE
- 制度的実装としてのKotonoha Method
- 運用インターフェースとしてのKotonoha Console
- 方法論ガイドと規範的仕様の境界

---

### Part II — プロジェクトライフサイクル

#### Chapter 4. 意味アンカーとしてのプロジェクト憲章

プロジェクト開始時に、目標だけでなく、非目標、置換してはならないもの、責任に関する前提を記録する。

主題:

- Intent statement
- Non-goals
- 設計制約
- 成功条件と失敗条件
- 失ってはならないもの

#### Chapter 5. 意味追跡可能性を持つIssue設計

Issueを単なるタスク容器ではなく、意図、文脈、範囲、レビュー期待を保持する単位として扱う。

主題:

- 意味単位としてのIssue
- Acceptance criteria と semantic preservation criteria
- 依存関係とlineage link
- 未解決の問いと延期された緊張
- Issueを分割・統合すべき条件

#### Chapter 6. RDEプロンプトによるPull Requestレビュー

概念変更、アーキテクチャ変更、文書変更、コード変更に対する軽量なレビュー手順を定義する。

主題:

- 保存された要素
- 許可された変換
- 推論された補完
- 未解決の要素
- 喪失と疑わしい逸脱
- 重大な歪曲
- 次回更新方針

#### Chapter 7. Decision Record と意味系譜ノート

Decision Record を、Git commit、Issue議論、SLS的lineageを接続する橋として導入する。

主題:

- なぜその判断が行われたのか
- どの代替案が退けられたのか
- どの前提がまだ不安定か
- 将来のレビューで何を見るべきか
- 判断はどのように改訂されるべきか

---

### Part III — 成果物とワークフロー

#### Chapter 8. 変化する意味状態としての文書

文書を静的な出力ではなく、生きた意味状態として扱う。

主題:

- Draft、review、publication、revision の状態
- LLM生成文書の腐食を防ぐ
- 要約による喪失の捕捉
- 翻訳とバイリンガルドリフト
- 公開資料と内部資料の境界

#### Chapter 9. 制度的振る舞いとしてのコード

実装を孤立したコード完了ではなく、仕様・方法論・責任と整合すべき振る舞いとして扱う。

主題:

- 仕様からコードへの追跡可能性
- 行動上の約束としてのテスト
- リファクタリングと意味保存
- 実装上の便宜と概念の矮小化
- 回帰を意味喪失として見る

#### Chapter 10. AI支援生成プロトコル

LLM出力を、検証済み判断と誤認せずにプロジェクトへ取り込むための手順を定義する。

主題:

- プロンプト文脈と source of truth の境界
- AI生成物のドラフト状態
- 人間レビューの責務
- 昇格前のRDE確認
- 偽の完了と過剰な確信の防止

#### Chapter 11. Project board と Milestone

GitHub Projects 等のボードは意味統治を支えるが、置き換えないことを明確にする。

主題:

- 運用ビューとしてのStatus column
- 意味上のcheckpointとしてのMilestone
- 完了条件
- 延期された作業の可視化
- Board movement と meaning movement の違い

---

### Part IV — ガバナンスと責任

#### Chapter 12. 責任再収束モデル

作業中の責任は分散しうるが、帰結は引き受け可能な構造へ再収束しなければならないという制度原則を展開する。

主題:

- 分散された責任
- 人間とAIの協働における説明責任
- レビュー所有権
- Maintainer の責務
- Escalation と freeze point

#### Chapter 13. ドリフトパターンと対抗策

反復して現れる意味ドリフトの形式と、その検出・緩和方法を整理する。

主題:

- 証拠より強い主張
- ツール都合の理論化
- 比喩による機構の置換
- 内部前提の公開文書への漏出
- 未解決の緊張が洗練された文章により閉じられる問題

#### Chapter 14. レビュー周期と制度的記憶

時間の中でlineageを可視化し続けるための反復的レビュー実践を説明する。

主題:

- 週次またはmilestone単位のsemantic review
- Drift review
- Publication readiness review
- 仕様変更後のmigration review
- Lineage repair としてのretrospective

---

### Part V — 導入モデル

#### Chapter 15. 最小導入

小規模チームまたは個人プロジェクトで使える最小構成を定義する。

主題:

- Intent note
- RDE checklist
- Issue / PR templates
- Decision log
- 軽量レビューリズム

#### Chapter 16. チーム導入

小規模組織または複数リポジトリを持つプロジェクトでの使い方を説明する。

主題:

- 共通語彙
- Cross-repo lineage
- Maintainer role
- Review responsibility
- Project board convention

#### Chapter 17. SLSネイティブ導入

将来的に、ツールが意味系譜を直接記録・検査できる状態を説明する。

主題:

- Kotonoha Console
- SLS-native link
- Semantic diff
- RDE-assisted review
- Human approval と audit trail

---

## 5. テンプレート案

今後のドラフトでは、運用テンプレートを追加する。

### 5.1 Project charter template

```markdown
# Project charter

## Intent

## Non-goals

## What must not be lost

## Success conditions

## Failure conditions

## Responsibility structure

## Open questions
```

### 5.2 Issue template

```markdown
## Intent

## Context / lineage

## Scope

## Non-goals

## Acceptance criteria

## Semantic preservation criteria

## Open questions
```

### 5.3 Pull Request RDE note

```markdown
## Preserved elements

## Authorized transformations

## Inferred extensions

## Unresolved elements

## Loss / drift risks

## Next update policy
```

### 5.4 Decision record template

```markdown
# Decision record: <title>

## Context

## Decision

## Alternatives considered

## Expected semantic change

## Risks

## Revisit condition
```

---

## 6. 初期スコープ境界

このドラフトは、Kotonoha Method がすでに完成した形式的方法であるとは主張しない。

初期公開ドラフトで扱わないもの:

- 完全なSLSデータモデル
- RDEの完全自動化
- 汎用プロジェクト管理の全面的置換
- 意味変化の定量スコアリング
- 実証なしの組織安全性主張

初期目標は実践的である。すなわち、意味喪失、意味ドリフト、責任拡散を、管理可能な程度に可視化することである。

---

## 7. 次回ドラフト作業

- 公開本文の副題を **Semantic Project Management** とするか、**Meaning-Aware Project Governance** とするか決める。
- 文書編集、コードレビュー、AI生成ドラフトレビューの具体例を追加する。
- この方法論に沿ったIssue templateとPR templateを準備する。
- 小規模チーム向けのminimal adoption guideを追加する。
- privateな `kotonoha-management` の計画情報を露出せずに、概念だけを公開文書へ接続する。
- `kotonoha-spec` に対して、この方法論が非規範的であることを明確に保つ。

---

## 8. 作業中のパンチライン

- **Kotonoha Method は、SLS を制度に変える。**
- **Git はテキストの変化を記録する。Kotonoha Method は意味の変化を統治する。**
- **RDE は変更が意味に何をしたかを問う。Kotonoha Method は、その変化の帰結をプロジェクトがどう引き受けるかを問う。**
- **プロジェクトは単なるタスクグラフではない。意味、判断、責務の系譜である。**
