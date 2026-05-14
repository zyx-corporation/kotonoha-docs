# RDE／レビュー運用ガイド（短文・非規範）

公開向けの**要約**である。詳しい観測カテゴリと背景は [SLS + RDE に基づく開発手法](sls_rde_development_method.md)、相互運用上の規範は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) を正とする。**確定した運用規程や内部ドラフトではない**。

**English:** [`../../en/method/rde_review_quick_guide.md`](../../en/method/rde_review_quick_guide.md)

---

## 1. RDE／レビューを検討するタイミング（目安）

| 変化の例 | メモ |
| --- | --- |
| **文言・設計ドキュメント**の変更で、保存／変換／喪失／逸脱のどれかが動くとき | PR／Issue で意図を言語化する。 |
| **意図と結果のギャップ**が Issue／PR で話題になるとき | チェックリスト通過のみで終わらせない（下記§3）。 |
| **CLI／コアが interchange または検証結果を出す**変更 | [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) の終了コード・エラー意味と矛盾させない（定義側を先または同時に更新）。 |

[kotonoha-spec の CONTRIBUTING](https://github.com/zyx-corporation/kotonoha-spec/blob/main/CONTRIBUTING.md) にある **Semantic／RDE レビュー観点**と併せて読む。

---

## 2. RDE に期待しないこと

- **承認・採決の代替**にならない。
- 「次回更新方針」を**誰かがクローズまたは次 Issue で文章化するまで**宙に浮かせない。**未解決だけを書いて締める**ことを目的にしない。

---

## 3. PR／Issue に残すトレース（最低ライン）

次が**後から読み手に説明できる**状態を、暫定的な合格として使える。

1. **どの差分・どのレビュー**についての議論か（Issue／PR の番号または URL）。
2. **interchange や RDE 観測経路**を使ったか。使わないときは、その**理由が一文**で書けるか。
3. **まだ規範に載らない論点**は、[kotonoha-spec](https://github.com/zyx-corporation/kotonoha-spec) の Issue／PR で追跡する（手順の粒度は同リポジトリの [CONTRIBUTING](https://github.com/zyx-corporation/kotonoha-spec/blob/main/CONTRIBUTING.md)、[Git 運用ルール（日本語）](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/git_operation_rules.md) などに従う）。各パートナーリポのテンプレートが「関連バックログ ID」などを求める場合はそれに応じる。

---

## 4. 喪失（lost）と仕様昇格の扱い

- **実装だけで決め打ち**したときは、公開側での追跡・議論への接続を検討する（追跡の例: [`kotonoha-spec` issue #3](https://github.com/zyx-corporation/kotonoha-spec/issues/3)）。
- **normative** が必要になったタイミングでは **`kotonoha-spec` に集約**し、短文運用説明でも規範本文を重複複製しない（配置方針: [`documentation-placement-policy.md`](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/documentation-placement-policy.md)）。

---

## 5. レビューの正本（実務メモ）

- **クローズ済みレビュー**は PR と仕様側リンクへ寄せる。
- **`interchange` の export と CLI が使えるならそれを優先**し、UI 内だけのドラフト JSON を単独の正本にしない。

---

## 参照

| 種別 | リンク |
| --- | --- |
| RDE 出力の形（規範／参照） | [`rde-review-output.md`](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/rde-review-output.md) |
| リポ間の役割 | [`repository-governance.md`](https://github.com/zyx-corporation/kotonoha-spec/blob/main/docs/repository-governance.md) |
| コア側トレース | [`spec-traceability.md`](https://github.com/zyx-corporation/kotonoha-core/blob/main/docs/spec-traceability.md) |
