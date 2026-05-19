# Paper — 論文・長文アーティファクト

このディレクトリは、Kotonoha / SLS に関連する査読付き論文、プレプリント、その他の学術的な長文成果物を管理する日本語ドキュメント領域です。

本領域の文書は、実装者向けの規範本文ではなく、背景理解・研究文脈・設計思想を補助するための参考資料です。正本となる技術定義は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) にあります。

## 取り扱い方針

- 論文・プレプリント・長文原稿は、規範仕様ではなく参考資料として扱います。
- `kotonoha-spec` にある技術定義を正本とします。
- PDF、LaTeXソース、長文原稿などを追加するときは、ライセンスと由来を同じ変更、または文書 front matter に明記してください。
- 大きなバイナリや投稿用成果物を追加する場合は、Issue 起点で追加してください。

## Contents

| File | Description |
| --- | --- |
| [`kotonoha_concept.md`](kotonoha_concept.md) | **構想長文正本（暫定版 v0.1・非規範）**。M0 概念固定の公開向け Markdown。内部計画は [`kotonoha-management` `27`](https://github.com/zyx-corporation/kotonoha-management/blob/main/docs/27_kotonoha_concept_development_plan.md) が参照する。 |
| [`kotonoha_concept.tex`](kotonoha_concept.tex) / [`kotonoha_concept.pdf`](kotonoha_concept.pdf) | 同上テーマの LaTeX / PDF（`md` と内容は暫定版で追随調整予定）。短い要約は [`../concepts/kotonoha_concept_overview.md`](../concepts/kotonoha_concept_overview.md)。 |
| RDE position paper v0.6.3 | RDE の背景理解・研究文脈・設計思想を補助する参考資料。LaTeX source (`ltjsarticle`) は大きいため、必要に応じて安全な方法で別途配置する。 |

## Notes

このセクションは `ja/` 配下の日本語ドキュメント構造に合わせて配置します。英語版または投稿先別の配置が必要になった場合は、別途 `en/paper/` もしくは成果物専用ディレクトリを設けます。
