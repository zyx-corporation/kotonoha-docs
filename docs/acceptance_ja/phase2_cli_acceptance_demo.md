# Phase 2 CLI 受入デモ

本ドキュメントは、[`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) CLI と [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) の Phase 2 最小面に対する**手を動かす受入デモ**です。

これは学習用チュートリアルではなく、[`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) の規範的定義にも代わりません。CLI を学ぶための導入は [最初の CLI セッション](../tutorials_ja/first_cli_session.md) を参照してください。

**English (primary):** [../acceptance/phase2_cli_acceptance_demo.md](../acceptance/phase2_cli_acceptance_demo.md)

**前提:** Rust ツールチェーン。永続化手順を実行する場合は任意で PostgreSQL 16 以上。

## 受入範囲

このデモでは、以下の最小動作を確認します。

- `kotonoha version` が終了コード **0** で終了し、CLI / spec bundle の識別情報を出力する
- RDE interchange skeleton の出力が strict mode で検証に通る
- Core interchange envelope の出力が strict mode で検証に通る
- 任意で PostgreSQL 永続化により migrate と envelope 1件の store ができる
- 無効な JSON が、文書化された契約終了コードで検証失敗する

## A. CLI のビルドまたはインストール

`kotonoha-cli` をチェックアウトしたディレクトリで:

```bash
cargo build --release
export PATH="$PWD/target/release:$PATH"
```

動作確認:

```bash
kotonoha version
```

期待結果: 終了コード **0**。さらに、CLI のセマバと [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) に沿った対象 spec bundle の2行が出力されます。

## B. RDE interchange の往復

最小スケルトンを出力し検証します。

```bash
kotonoha rde emit | kotonoha rde validate --strict
echo $?
```

期待結果: **0**。

## C. Core interchange envelope の往復

```bash
kotonoha interchange emit | kotonoha interchange validate --strict
echo $?
```

期待結果: **0**。

## D. 任意: PostgreSQL 永続化

PostgreSQL を起動します。例として `kotonoha-core` の [`docker-compose.yml`](https://github.com/zyx-corporation/kotonoha-core/blob/main/docker-compose.yml) を使います。

```bash
cd /path/to/kotonoha-core
docker compose up -d
export DATABASE_URL=postgres://kotonoha:kotonoha@localhost:5432/kotonoha_dev
```

マイグレーション適用と、envelope を1件 store します。

```bash
kotonoha db migrate
kotonoha interchange emit | kotonoha interchange store --strict
echo $?
```

期待結果: 終了コード **0**。標準出力に UUID が1行出ます。

## E. 検証失敗の契約チェック

壊れた JSON は終了コード **2** で検証失敗する想定です。コマンドと終了コードの契約は [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) を参照してください。

```bash
echo '{}' | kotonoha rde validate --strict
echo $?
```

期待結果: **2**。

## 自動スクリプト

[`kotonoha-cli` リポジトリ](https://github.com/zyx-corporation/kotonoha-cli) には [`scripts/phase2_acceptance_demo.sh`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/scripts/phase2_acceptance_demo.sh) があり、内部の受入チェックリストにある手順 **A–E**（`version`、往復、無効 JSON で終了コード **2**）を実行します。

`DATABASE_URL` を設定すると **D**（`migrate` + `store`）を含められ、`main` の CI と同様のセットアップにできます。

## ガバナンス上の位置づけ

メンテナは社内向けのチェックリストで Phase 2 受入の整合も取っているが、その本文は公開リポジトリには複製しない。公開で再現可能な根据は、この手順および **[Phase 2 CLI チュートリアル](https://github.com/zyx-corporation/kotonoha-docs/blob/main/docs/tutorials/phase2_cli_walkthrough.md)**、**[`phase2_acceptance_demo.sh`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/scripts/phase2_acceptance_demo.sh)**（CI）を正とすること。

コマンド名、スキーマ、終了コードの厳密さは、常に [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) の公開規範ソースと [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli) の CLI 定義を優先してください。
