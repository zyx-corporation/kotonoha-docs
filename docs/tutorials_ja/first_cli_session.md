# 最初の CLI セッション

本チュートリアルは、[`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) CLI を学ぶための最初のセッションです。

最初に実行するコマンドの意味と、それらが Kotonoha の概念とどう関係するかを説明します。これは受入チェックリストではありません。期待される終了コードを含むリリース確認が必要な場合は、[Phase 2 CLI 受入デモ](../acceptance_ja/phase2_cli_acceptance_demo.md) を参照してください。

**English (primary):** [../tutorials/first_cli_session.md](../tutorials/first_cli_session.md)

## 学ぶこと

このチュートリアルを終えると、以下を理解できるようになります。

- CLI の identity を確認する方法
- CLI が対象 spec bundle を報告する理由
- RDE skeleton が何を表すか
- interchange envelope が何を表すか
- 厳密なコマンド契約をどこで確認するか

## 前提

- Rust ツールチェーン
- [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli) のチェックアウト

このチュートリアルでは PostgreSQL は不要です。

## 1. CLI をビルドする

`kotonoha-cli` をチェックアウトしたディレクトリで:

```bash
cargo build --release
export PATH="$PWD/target/release:$PATH"
```

これで、ローカルの `kotonoha` コマンドをシェルから使えるようになります。

## 2. CLI の identity を確認する

実行します。

```bash
kotonoha version
```

重要なのは、単にコマンドが動くことだけではありません。CLI は、自分自身と、対象とする仕様バンドルを識別できる必要があります。

Kotonoha では、実装の振る舞いと規範仕様を分離します。この分離は、ドキュメント、テスト、将来の実装が、どの公開契約について話しているのかを明確にするために重要です。

正確な出力規則は [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) を参照してください。

## 3. RDE skeleton を出力する

実行します。

```bash
kotonoha rde emit
```

RDE skeleton は、意味変化レビューを記録するための最小構造です。この段階で、人を判断したりユーザーをスコアリングしたりするわけではありません。生成・変換された内容が元の意図をどのように保存し、変換し、補完し、あるいは逸脱するかを点検するための形を準備します。

次に検証します。

```bash
kotonoha rde emit | kotonoha rde validate --strict
```

validate は、出力された構造が期待される契約に合っているかを確認します。チュートリアルでは形の理解が目的です。受入デモでは、期待される終了コードの確認が目的です。

## 4. interchange envelope を出力する

実行します。

```bash
kotonoha interchange emit
```

interchange envelope は、Kotonoha 関連データをツール間で交換するための輸送用の形です。これは理論全体でも、完全な保存モデルでもありません。複数のツールが「何を受け渡しているのか」について合意するための最小公開面です。

検証します。

```bash
kotonoha interchange emit | kotonoha interchange validate --strict
```

**契約メモ：** **`kotonoha-core`** **0.1.6** 以降、interchange エンベロープには **許可されるトップレベルキーのみ**（`format`、`spec_bundle`、`lineage_unit`、`rde_document`）。**`lineage_unit`** オブジェクトにも **`id` と `prior_unit_id` だけ** が許されます。未定義のフィールドがあると検証が失敗し（`interchange validate` で終了コード **2**）、仕様側で vocabulary を追記したバージョンを待つ運用になります。

RDE skeleton と interchange envelope の違いは重要です。

- RDE skeleton: 意味変化を点検するためのレビュー向け構造
- Interchange envelope: ツール間でデータを移動するための交換向け構造

## 5. 次に進む場所

Phase 2 の振る舞いをリリース確認やレビュー目的で検証したい場合は、以下を使います。

- [Phase 2 CLI 受入デモ](../acceptance_ja/phase2_cli_acceptance_demo.md)

厳密なコマンド名、出力規則、終了コード契約が必要な場合は、以下を参照してください。

- [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md)
- [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)

## RDE note

このチュートリアルでは、CLI を理論そのものとして提示しないようにしています。CLI は入口です。理論は、仕様、method 文書、今後の semantic-lineage workflow にあります。
