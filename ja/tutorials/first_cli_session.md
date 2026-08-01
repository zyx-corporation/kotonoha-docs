# 最初の CLI セッション

このチュートリアルでは、`kotonoha` CLI を使って、Kotonoha の最小部品を確認します。

目的は、難しい理論を理解することではありません。まずは、Kotonoha が次の 3 つを扱う道具だと手で確認します。

| 確認するもの | 何のためか |
| --- | --- |
| CLI identity | 自分が使っている `kotonoha` コマンドが、どの仕様・バージョンを前提にしているか確認する |
| RDE skeleton | 意味の変化を点検するための空のレビュー用紙を出す |
| interchange envelope | Kotonoha のデータを、CLI・UI・他ツール間で受け渡すための封筒を出す |

つまり、このページで行うことは「Kotonoha で意味レビューを書く前に、CLI が出せる最小の形を確認する」ことです。

**前提:** [Kotonoha CLI のインストール](install_kotonoha_cli.md) を完了し、ターミナルで `kotonoha version` が動くこと。

**English:** [../../en/tutorials/first_cli_session.md](../../en/tutorials/first_cli_session.md)

受入チェックリスト（終了コードの厳密確認）が必要な場合は [Phase 2 CLI 受入デモ](../acceptance/phase2_cli_acceptance_demo.md) を使います。本稿は学習用です。

---

## このセッションで作るイメージ

たとえば、AI に仕様書を要約させたとします。

そのとき、普通のレビューでは「要約が読みやすいか」「重要なことが残っているか」を人間が見ます。

Kotonoha では、そこにもう一段加えて、次のようなことを記録できる形にします。

| 観点 | 例 |
| --- | --- |
| 保存された要素 | 「人間が最終承認する」という原則は残っている |
| 変換された要素 | 長い議論を短い仕様説明に変えた |
| 補完された要素 | 元文にはなかった注意書きを足した |
| 失われた要素 | 未解決だった論点が、解決済みに見える形になった |
| 逸脱リスク | AI の判断を人間承認の代替に見せてしまう |

このようなレビューを書くために、まず空の点検票を CLI から出してみます。それが `kotonoha rde emit` です。

さらに、その点検票を別のツールへ渡すための封筒も確認します。それが `kotonoha interchange emit` です。

このチュートリアルでは **PostgreSQL は不要** です。Obsidian や VS Code も不要です。

---

## 0. 準備確認

新しいターミナルで PATH が通っているか確認します。

```bash
kotonoha version
```

`command not found` となる場合は、[インストール手順](install_kotonoha_cli.md) の PATH 設定に戻ってください。

---

## 1. CLI identity を確認する

まず、使っている CLI の身元を確認します。

```bash
kotonoha version
```

### 何を確認しているか

ここで確認しているのは、「この `kotonoha` コマンドが何者か」です。

Kotonoha では、実装と仕様を分けます。CLI が新しくても、参照している仕様 bundle が古い場合があります。逆に、仕様が更新されていても、手元の CLI が古い場合もあります。

そのため、最初に `version` を見ます。

### なぜ必要か

RDE レビューや interchange の形式は、仕様と対応している必要があります。どの CLI がどの仕様を前提にしているかを確認しないままレビューすると、後で「この JSON はどのバージョンの形なのか」が分からなくなります。

つまり、`version` は単なるバージョン表示ではなく、レビュー記録の出所確認です。

出力の厳密な規則は [cli-definition.md](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) を参照してください。

---

## 2. RDE skeleton を出力する

次に、意味変化レビューの空のひな形を出します。

```bash
kotonoha rde emit
```

### 何を出しているか

これは、RDE レビューを書くための最小構造です。

ここでは、まだ実際のレビュー内容は書きません。まず「Kotonoha では、意味変化をこのような形で記録する」という空の点検票を見ます。

### 何のために使うか

AI が文章を要約した、仕様を変更した、コードを生成した、レビューコメントを反映した。そうしたときに、単に「良い / 悪い」を見るのではなく、次を確認するために使います。

| 観点 | 問い |
| --- | --- |
| 保存 | 元の意図や制約は残っているか |
| 変換 | 表現や構造はどう変わったか |
| 補完 | 元にはなかった情報を足していないか |
| 未解決 | 決まっていない論点を残せているか |
| 喪失 | 要約や実装で消えた意味はないか |
| 逸脱 | 元の設計思想から危険にずれていないか |

この段階では、人を評価したり、AI 出力を自動合否したりするものではありません。人間がレビューするための記録用紙です。

### 形を検証する

出力したひな形が、期待される形に合っているかを確認します。

```bash
kotonoha rde emit | kotonoha rde validate --strict
```

`validate` は意味の正しさを判定するものではありません。JSON の形が期待される契約に合っているかを確認します。

ここで確認しているのは、「レビュー用紙の中身が正しいか」ではなく、「レビュー用紙として読める形になっているか」です。

---

## 3. interchange envelope を出力する

次に、ツール間で受け渡すための封筒を出します。

```bash
kotonoha interchange emit
```

### 何を出しているか

interchange envelope は、Kotonoha 関連データを複数のツール間で渡すための共通形式です。

RDE skeleton はレビュー用紙です。interchange envelope は、そのレビュー用紙や関連情報を入れて運ぶ封筒です。

| 種類 | たとえ | 役割 |
| --- | --- | --- |
| RDE skeleton | レビュー用紙 | 意味変化を点検するための構造 |
| interchange envelope | 封筒 | レビュー用紙や関連データをツール間で渡すための構造 |

### 何のために使うか

CLI だけで完結するなら、封筒はまだ必要に見えないかもしれません。

しかし、Kotonoha は CLI、Obsidian、VS Code、将来の UI、他のレビュー支援ツールと接続することを想定しています。そのとき、各ツールが勝手な形式でデータを渡すと、意味レビューの履歴が壊れます。

そのため、ツール間で受け渡す最小形式として interchange envelope を使います。

### 形を検証する

```bash
kotonoha interchange emit | kotonoha interchange validate --strict
```

**契約メモ（kotonoha-core 0.1.6 以降）:** interchange envelope は strict JSON として検証されます。トップレベルは `format` / `spec_bundle` / `lineage_unit` / `rde_document` など許可されたキーのみで、`lineage_unit` の中も `id` / `prior_unit_id` 以外の未定義フィールドは拒否されます。未定義フィールドがあると `kotonoha interchange validate --strict` は終了コード **2** で失敗します。

この検証も、意味の正しさではなく形式の確認です。

---

## 4. ここまでで分かったこと

このセッションで確認したことは、次の 3 つです。

| コマンド | 分かったこと |
| --- | --- |
| `kotonoha version` | 手元の CLI がどの仕様・バージョンを前提にしているか |
| `kotonoha rde emit` | 意味変化レビューの空のひな形を出せること |
| `kotonoha interchange emit` | レビュー関連データをツール間で渡す封筒を出せること |

まだ実際の意味レビューは行っていません。ここでは、Kotonoha の最小部品を確認しただけです。

次の段階では、AI や SLM が作った草案を検証し、人間が確認する流れに進みます。

---

## 5. 次に進む場所

| 目的 | 文書 |
| --- | --- |
| SLM 草案と検証の体験 | [slm_demo_quickstart.md](slm_demo_quickstart.md) |
| Kotonoha record として保存する流れ | [kotonoha_record_flow.md](kotonoha_record_flow.md) |
| リリース確認 | [phase2_cli_acceptance_demo.md](../acceptance/phase2_cli_acceptance_demo.md) |
| コマンド契約 | [cli-definition.md](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) |
| 公開仕様 | [kotonoha-spec](https://github.com/zyx-corporation/kotonoha-spec) |

---

## RDE note

このチュートリアルは、Kotonoha の理論をすべて説明するものではありません。

ここで行ったのは、意味レビューの前提になる 3 つの形を確認することです。

1. どの CLI / 仕様で作業しているかを確認する。
2. 意味変化レビューの空のひな形を出す。
3. そのレビュー情報をツール間で運ぶ封筒を出す。

最終的な意味判断は CLI ではなく人間の責務です。CLI は、その判断を記録し、検証し、他のツールへ渡せる形にするための入口です。
