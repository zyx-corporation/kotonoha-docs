# Kotonoha 構想概要

**Status:** informative (non-normative). Canonical semantics and conformance language live in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) — start with [introduction.md](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/introduction.md) and [introduction_ja.md](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/introduction_ja.md).

English companion: [`../../en/concepts/kotonoha_concept_overview.md`](../../en/concepts/kotonoha_concept_overview.md)

---

## 位置づけ

**Kotonoha** は、**Semantic Lineage System (SLS)** の中核概念として位置づけられる制度である。

Kotonoha は、単なる履歴管理、差分管理、ノート管理、AI 補助編集の仕組みではない。扱う対象は、文章やコードの変更そのものではなく、その変更によって生じる**意味の変化**である。

- **Git** は、何が変わったかを記録する。
- **Kotonoha** は、その変化によって何が保存され、何が変換され、何が補完され、何が失われ、どこに逸脱リスクが生まれたかを記録する。

この意味で、Kotonoha は**意味履歴の制度**である。

## RDE と「賢さ」

**RDE**（Resonant Deviation Evaluator）は、Kotonoha における意味変化監査の中核である。

RDE は、出力の正否を判定するだけの評価器ではない。危険な出力を禁止するだけの安全フィルタでもない。生成物や変更案が、元の議論・意図・価値・設計思想からどのように変化したかを観測し、その変化が許容された変換なのか、必要な補完なのか、危険な逸脱なのかを確認する。

ここで重要なのは、RDE が人間のいわゆる「賢さ」に近い働きを担う点である。

賢さとは、問題解決によって何が失われるかを見る能力であり、それを知能の次の振る舞いへフィードバックする能力である。曖昧さ、痛み、関係性、未解決性、責任の所在、少数の声、元の問いの射程——これらが言い換えや要約、実装上の便宜によって消えていないかを見落とさない。

したがって、RDE は知能の性能評価ではなく、**賢さの制度化**である。ただし RDE は**人間の承認・責任の代替ではない**（仕様上の人間権限は [`kotonoha-spec` introduction](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/introduction.md) を参照）。

## 素敵な知能

強い知能は問題を解く。高性能な知能は速く、広く、深く答える。しかし**素敵な知能**は、答えたあとに問う。

- この解決によって、何が見えなくなったか。
- この整理によって、元の痛みや曖昧さは雑に処理されていないか。
- この効率化によって、責任の所在は薄まっていないか。
- この一般化によって、個別の文脈は消えていないか。

Kotonoha が目指すのは、単に AI を便利にすることではない。知能が問題を解いたあとに、その解決によって失われたものを観測し、次の知的振る舞いへ戻すための構造である。

## Kotonoha における RDE レビュー

RDE レビューでは、少なくとも次を確認する（運用上の詳細は [Method](../method/README.md) を参照）。

1. **保存された要素**
2. **変換された要素**
3. **補完された要素**
4. **未解決のまま残した要素**
5. **失われた要素**
6. **逸脱リスク**
7. **次回更新方針**

従来の差分管理は追加・削除・変更を見る。意味の運用では、削除された文字列だけでなく、言い換えによって消えた曖昧さ、要約によって失われた射程、実装上の便宜によって隠れた理論的緊張も記録されなければならない。RDE はこの喪失を観測し、Kotonoha はその喪失を次の更新へ返す。

規範上の観測カテゴリと interchange は [`kotonoha-spec` SLS-4](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/rde-review-output.md) を正本とする。

## Git・Issue・Project との関係

| 仕組み | 主に残すもの |
| --- | --- |
| Git | 文字列の差分 |
| Issue | 未解決の作業 |
| Project | 作業の状態 |
| Kotonoha / SLS | 変更の意味、喪失、逸脱、責任 |

Kotonoha は Git、Issue、Project を否定しない。それらを利用しつつ、意味・喪失・逸脱・責任を扱う層を追加する。

## 運用原則（公開向け要約）

文書・仕様・実装・UI を更新するときは、次を意識する。

- 問題解決の成果だけでなく、その成果によって失われたものを確認する。
- 実装上の便宜を、理論的主張にすり替えない。
- 未検証の仮説を、実証済みの結論として扱わない。
- 元の議論の射程を、わかりやすさのために狭めすぎない。
- 人間の承認と責任の所在を、AI の評価結果で置き換えない。
- RDE レビューの結果を、次回更新方針へ明示的に戻す。

## 定式化（思想的メモ）

> RDE は、出力の正否を判定する装置ではない。  
> それは、問題解決によって失われた意味・文脈・関係・責任を観測し、その喪失を次の知的振る舞いへ戻すフィードバック構造である。

> 賢さとは、問題解決によって何が失われるかを見て、知能にフィードバックする能力である。

Kotonoha は、この賢さを意味履歴の制度として外在化する。

## 関連文書

| 文書 | 役割 |
| --- | --- |
| [`kotonoha-spec` introduction](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/introduction.md) | 用語・適合の規範 |
| [`kotonoha-spec` architecture](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/architecture.md) | 論理アーキテクチャ（informative 図を含む） |
| [sls_rde_development_method.md](../method/sls_rde_development_method.md) | プロジェクト自身への SLS + RDE 適用 |
| [kotonoha_architecture_terms.md](../../docs/architecture/kotonoha/kotonoha_architecture_terms.md) | バックエンド構成の概念用語 |
| [documentation-placement-policy](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/documentation-placement-policy.md) | `kotonoha-docs` と `kotonoha-spec` の配置 |

## 本ページの境界

- **含む:** 構想・動機・読者向けの概念整理。
- **含まない:** データモデル未決事項のトラッキング、Phase 計画、内部レビュー証跡（それらは公開 OSS の範囲外の計画文書に属する）。
- **誤読に注意:** 「賢さ」の比喩が強すぎると実装可能性が曖昧に見える。RDE を万能評価器や人間判断の代替と読んではならない。
