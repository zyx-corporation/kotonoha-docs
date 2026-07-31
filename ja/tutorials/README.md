# Tutorials（チュートリアル）

この領域は、Kotonoha を学習しながら試すための段階的ガイドです。

初めて読む場合は、先に [はじめての Kotonoha](../start-here.md) と [初学者向け用語集](../glossary_for_beginners.md) を読むと理解しやすくなります。

英語版: [`../../en/tutorials/README.md`](../../en/tutorials/README.md)

## 最短ルート

まず動かすだけなら、次の 2 つで十分です。

| 順 | チュートリアル | 目的 |
| --- | --- | --- |
| 1 | [install_kotonoha_cli.md](install_kotonoha_cli.md) | `curl \| bash` で CLI を入れ、`kotonoha version` まで確認する |
| 2 | [first_cli_session.md](first_cli_session.md) | RDE skeleton と interchange envelope を体験する |

この段階では PostgreSQL、Obsidian、VS Code は不要です。

## 次に進むルート

CLI の最小体験が済んだら、目的に応じて進んでください。

| 目的 | チュートリアル | 到達点 |
| --- | --- | --- |
| 草案生成と検証を体験したい | [slm_demo_quickstart.md](slm_demo_quickstart.md) | ローカル SLM の草案を Kotonoha で検証する |
| MeaningDelta から草案を作りたい | [rde_draft_assistance.md](rde_draft_assistance.md) | M8 の CLI scaffold draft → validate → attach → human review を理解する |
| 検証済み草案を保存したい | [kotonoha_record_flow.md](kotonoha_record_flow.md) | DB-backed な Kotonoha record として保存する流れを理解する |

## 読まなくてもよいもの

チュートリアルを進めるだけなら、次は必須ではありません。

| 文書 | 位置づけ |
| --- | --- |
| [phase2_cli_acceptance_demo.md](../acceptance/phase2_cli_acceptance_demo.md) | リリース前の受入確認。学習用ではなく、終了コード・strict 検証を確認するための手順 |
| [cli_installer_implementation.md](../manual/cli_installer_implementation.md) | インストーラーのメンテナ向け実装手順 |
| [Release Train](../releases/README.md) | 配布 baseline とバージョン整合性の確認 |

## 関連（チュートリアル外）

| 文書 | 目的 |
| --- | --- |
| [読者別ラーニングパス](../learning-path.md) | 目的別の読み順を確認する |
| [install_obsidian_kotonoha_console.md](../manual/install_obsidian_kotonoha_console.md) | Obsidian プラグイン（GitHub Release） |
| [Manual](../manual/README.md) | 利用・運用の参照文書 |
| [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) | 厳密な意味・契約・適合条件の正本 |

## 配置メモ

チュートリアルは理解を優先し、細部を簡略化することがあります。厳密な意味・契約は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) を正とします。

旧 `docs/tutorials_ja/` は移行期間中も参照できますが、推奨配置はこの `ja/tutorials/` です。
