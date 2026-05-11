# Kotonoha ドキュメント — 日本語

ここは Kotonoha エコシステムの日本語ドキュメント領域です。

`kotonoha-docs` は説明・手順・学習用の公開文書を置く場所です。SLS の規範的要求は定義しません。仕様の正本は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) にあります。

英語版対応: [`../en/README.md`](../en/README.md)

## セクション

| セクション | 目的 | 移行期間中の現行参照元 |
| --- | --- | --- |
| [Method](method/README.md) | プロジェクト自身が SLS + RDE をどう適用するか | `docs/method_ja/` と対応 |
| [Manual](manual/README.md) | 利用・運用の参照文書 | 現時点では `docs/manual/` を参照 |
| [Tutorials](tutorials/README.md) | 学習向けの段階的ガイド | `docs/tutorials_ja/` と対応 |
| [Acceptance demos](acceptance/README.md) | 公開動作を確認する検証向け手順 | `docs/acceptance_ja/` と対応 |

## 配置ルール

概念説明・補助説明・学習用文書は、原則としてこのリポジトリに置きます。厳密な意味、適合性、スキーマ、バージョン規則が必要な場合は、規範本文を重複させず [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) へリンクします。

## 移行メモ

既存の `docs/` ディレクトリは移行互換のため当面残します。新規の日本語読者向け文書は `ja/` ツリーを優先し、対応する英語版を `en/` 側に置くことを原則とします。
