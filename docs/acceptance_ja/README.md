# 受入デモ

受入デモは、特定フェーズにおける Kotonoha の公開面が期待どおりに動作することを確認するための手順です。

これは**チュートリアルではありません**。見た目はウォークスルーに近い場合がありますが、主目的は学習ではなく検証です。つまり、コマンド、期待される終了コード、期待される出力、規範仕様へのリンクを確認します。

以下のような問いに答えるために、このセクションを使います。

- Phase 2 CLI の最小面は正常に動くか
- validate 系コマンドは期待される終了コードを返すか
- 任意の永続化パスは文書化されたセットアップで動くか
- どの公開動作が内部の受入チェックリストに紐づいているか

学習向けの資料は [チュートリアル](../tutorials_ja/README.md) を参照してください。

**English (primary):** [../acceptance/README.md](../acceptance/README.md)

## 公開中の受入デモ

| デモ | 説明 |
| --- | --- |
| [phase2_cli_acceptance_demo.md](phase2_cli_acceptance_demo.md) | Phase 2 CLI 受入デモ: `kotonoha version`、RDE / interchange validate、任意で PostgreSQL ストア |
