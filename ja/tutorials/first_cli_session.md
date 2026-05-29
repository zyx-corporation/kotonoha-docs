# 最初の CLI セッション

[`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) CLI を**初めて触る**ためのセッションです。コマンドの意味と、Kotonoha の概念との関係を学びます。

**前提:** [Kotonoha CLI のインストール](install_kotonoha_cli.md) を完了し、ターミナルで `kotonoha version` が動くこと。

**English:** [../../en/tutorials/first_cli_session.md](../../en/tutorials/first_cli_session.md)

受入チェックリスト（終了コードの厳密確認）が必要な場合は [Phase 2 CLI 受入デモ](../acceptance/phase2_cli_acceptance_demo.md) を使います。本稿は学習用です。

---

## 学ぶこと

| 項目 | 説明 |
| --- | --- |
| CLI identity | どの CLI バージョンが、どの spec bundle を対象にしているか |
| RDE skeleton | 意味変化レビューを記録するための最小構造 |
| interchange envelope | ツール間でデータを交換するための輸送用の形 |
| 契約の参照先 | 厳密なコマンド定義はどこにあるか |

このチュートリアルでは **PostgreSQL は不要** です。

---

## 0. 準備確認

新しいターミナルで PATH が通っているか確認します。

```bash
kotonoha version
```

`command not found` となる場合は、[インストール手順](install_kotonoha_cli.md) の PATH 設定に戻ってください。

---

## 1. CLI の identity を確認する

```bash
kotonoha version
```

### なぜこれが重要か

Kotonoha では、**実装の振る舞い**と**規範仕様**を分離します。`version` は「このバイナリが何を対象にしているか」を示す入口です。ドキュメント・テスト・レビューが同じ契約を指しているか確認するために使います。

出力の厳密な規則は [cli-definition.md](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) を参照してください。

---

## 2. RDE skeleton を出力する

```bash
kotonoha rde emit
```

### RDE skeleton とは

生成・変換された内容が、元の意図をどう**保存・変形・補完・逸脱**したかを点検するための、レビュー向けの最小構造です。この段階で人を評価したり自動合否したりするものではありません。

### 検証する

```bash
kotonoha rde emit | kotonoha rde validate --strict
```

`validate` は、出力が期待される JSON 契約に合っているかを確認します。チュートリアルでは**形の理解**が目的です。

---

## 3. interchange envelope を出力する

```bash
kotonoha interchange emit
```

### interchange envelope とは

Kotonoha 関連データをツール間で渡すための**輸送用の形**です。理論全体でも完全な保存モデルでもありません。「何を受け渡しているか」について複数ツールが合意するための最小公開面です。

### 検証する

```bash
kotonoha interchange emit | kotonoha interchange validate --strict
```

**契約メモ（kotonoha-core 0.1.6 以降）:** トップレベルは `format` / `spec_bundle` / `lineage_unit` / `rde_document` など許可キーのみ。未定義フィールドがあると終了コード **2** になります。

### RDE skeleton との違い

| 種類 | 役割 |
| --- | --- |
| RDE skeleton | 意味変化の**レビュー**向け |
| interchange envelope | ツール間の**交換**向け |

---

## 4. 次に進む場所

| 目的 | 文書 |
| --- | --- |
| SLM 草案と検証の体験 | [slm_demo_quickstart.md](slm_demo_quickstart.md) |
| リリース確認 | [phase2_cli_acceptance_demo.md](../acceptance/phase2_cli_acceptance_demo.md) |
| コマンド契約 | [cli-definition.md](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) |
| 公開仕様 | [kotonoha-spec](https://github.com/zyx-corporation/kotonoha-spec) |

---

## RDE note

CLI は入口です。理論・方法論は仕様と [Method](../method/README.md) 文書にあります。本セッションは「コマンドが動く」ことと「何を表すか」の理解を目的とし、最終的な意味判断は人間の責務です。
