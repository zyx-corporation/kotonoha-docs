# kotonoha-docs（日本語公開情報の入口）

## まず読む

Kotonoha を初めて知る人は、まず次のページから始めてください。

- [はじめての Kotonoha](ja/start-here.md)
- [初学者向け用語集](ja/glossary_for_beginners.md)
- [読者別ラーニングパス](ja/learning-path.md)

`kotonoha-docs` は、Kotonoha エコシステムの公開説明文書です。仕様の正本ではありません。厳密な意味・適合条件・スキーマ・安定性の定義は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) を参照してください。

## Kotonoha を一言でいうと

Kotonoha は、AI や人間が文章・仕様・コードを変更したときに、**何が変わったか**だけでなく、**その変更によって何が保存され、何が失われ、どこに意味のずれが生まれたか**を確認するための仕組みです。

Git は文字列の差分を残します。Kotonoha は、その差分の背後にある意味の変化を扱います。

## 5分で試す

ターミナルを使える人は、次の順で進めてください。

| 順 | 文書 | 到達点 |
| --- | --- | --- |
| 1 | [CLI インストール](ja/tutorials/install_kotonoha_cli.md) | `kotonoha version` が動く |
| 2 | [最初の CLI セッション](ja/tutorials/first_cli_session.md) | `kotonoha rde emit` と `validate --strict` を試す |

この段階では PostgreSQL、Obsidian、VS Code、Release Train、受入デモは不要です。

## 読者別の入口

| 目的 | 入口 |
| --- | --- |
| まず概要を知りたい | [はじめての Kotonoha](ja/start-here.md) |
| 用語を確認したい | [初学者向け用語集](ja/glossary_for_beginners.md) |
| 自分に合う読み順を選びたい | [読者別ラーニングパス](ja/learning-path.md) |
| 概念を深く理解したい | [Kotonoha 構想概要](ja/concepts/kotonoha_concept_overview.md) |
| 学習しながら試したい | [Tutorials](ja/tutorials/README.md) |
| 実運用の手順を見たい | [Manual](ja/manual/README.md) |
| 公開受入手順を確認したい | [Acceptance](ja/acceptance/README.md) |
| Release Train / 配布 baseline を確認したい | [Releases](ja/releases/README.md) |
| 研究背景を参照したい | [Paper](ja/paper/README.md) |

## プロジェクトの目的と範囲

`kotonoha-docs` の目的は、Kotonoha の概念、運用、学習手順を公開し、利用者やコミュニティが「何を目指しているか」「どこから始めるか」を短時間で把握できるようにすることです。

| 項目 | 内容 |
| --- | --- |
| 目的 | 概念、運用、学習手順を公開し、理解と参加のハードルを下げる |
| 目標 | 初学者が「理解する → 試す → 継続利用する」までの導線を明確にする |
| 範囲 | 規範仕様ではない説明文書、概念説明、マニュアル、チュートリアル、受入デモ、参考資料 |

## まだ読まなくてよいもの

初学者は、最初からすべてを読む必要はありません。

| 文書 | 後でよい理由 |
| --- | --- |
| `kotonoha-spec` | 仕様・適合性・スキーマが必要になってから読む |
| Release Train | バージョン整合性や配布 baseline を確認するときに読む |
| Acceptance demo | リリース確認・受入確認向けで、学習用ではない |
| CLI installer implementation | メンテナ向けの実装手順 |
| Paper | 背景思想や研究文脈を深く読むための長文 |

## 関連リポジトリ

| リポジトリ | 役割 |
| --- | --- |
| [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | 公開仕様の正本（normative） |
| [`kotonoha-core`](https://github.com/zyx-corporation/kotonoha-core) | OSS コア実装と開発者向け文書 |
| [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli) | 公式 CLI と CLI 定義 |
| **kotonoha-docs（本リポジトリ）** | 仕様外の公開説明文書（non-normative） |

## 言語案内

- 日本語: [`ja/`](ja/README.md)
- English: [`en/`](en/README.md)

両言語は、原則として同じ構造を保つ方針です。ただし、現在は日本語側の初学者向け導線を先行整備しています。

## 補足

- 図表のレンダリング方針: [`docs/rendering_policy.md`](docs/rendering_policy.md)
- 貢献手順: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- ライセンス: [Apache License 2.0](LICENSE)
