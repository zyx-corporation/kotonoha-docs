# Phase 2 CLI ウォークスルー

本チュートリアルは、[`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) CLI と [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) の Phase 2 最小面に対する **手を動かす受入デモ風**の手順です。[`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) の規範的定義には代わりません。

**English (primary):** [../tutorials/phase2_cli_walkthrough.md](../tutorials/phase2_cli_walkthrough.md)

**前提:** Rust ツールチェーン。永続化手順を実行する場合は任意で PostgreSQL 16 以上。

## 1. CLI のビルドまたはインストール

`kotonoha-cli` をチェックアウトしたディレクトリで:

```bash
cargo build --release
export PATH="$PWD/target/release:$PATH"
```

動作確認:

```bash
kotonoha version
```

終了コード **0** と、2 行の出力（CLI のセマバと、[`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) に沿った spec バンドル）が得られる想定です。

## 2. RDE interchange の往復

最小スケルトンを出力し検証します。

```bash
kotonoha rde emit | kotonoha rde validate --strict
echo $?
```

**0** になる想定です。

## 3. Core interchange envelope の往復

```bash
kotonoha interchange emit | kotonoha interchange validate --strict
echo $?
```

**0** になる想定です。

## 4. 任意: PostgreSQL 永続化

PostgreSQL を起動します（例: `kotonoha-core` の [`docker-compose.yml`](https://github.com/zyx-corporation/kotonoha-core/blob/main/docker-compose.yml) を利用）。

```bash
cd /path/to/kotonoha-core
docker compose up -d
export DATABASE_URL=postgres://kotonoha:kotonoha@localhost:5432/kotonoha_dev
```

マイグレーション適用と、envelope を1件ストアします。

```bash
kotonoha db migrate
kotonoha interchange emit | kotonoha interchange store --strict
echo $?
```

終了コード **0** と、標準出力に UUID が1行出る想定です。

## 5. 検証失敗（契約チェック）

壊れた JSON は **`cli-definition.md`** に従い終了コード **2** で検証失敗する想定です。

```bash
echo '{}' | kotonoha rde validate --strict
echo $?
```

**2** になる想定です。

## 自動スクリプト（任意）

[`kotonoha-cli` リポジトリ](https://github.com/zyx-corporation/kotonoha-cli) には [`scripts/phase2_acceptance_demo.sh`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/scripts/phase2_acceptance_demo.sh) があり、内部の受入チェックリストにある手順 **A–E**（`version`、往復、無効 JSON で終了コード **2**）を実行します。`DATABASE_URL` を設定すると **D**（migrate + store）を含められ、`main` の CI と同様のセットアップにできます。

---

## 位置づけ

社内運用では、本ウォークスルーが Phase 2 の受入基準に紐づきます（非公開の [`kotonoha-management` 文書](https://github.com/zyx-corporation/kotonoha-management/blob/main/docs/16_phase2_acceptance_demo.md)）。コマンド名や終了コードの厳密さは、常に [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) を優先してください。
