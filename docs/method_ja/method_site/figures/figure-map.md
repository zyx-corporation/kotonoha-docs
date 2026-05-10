# Kotonoha Method 図表対応表

Status: draft / non-normative

この文書は、Kotonoha Method のHTML / JS / SVG展開において、各章・各セクションに対応する図表を管理するための対応表である。

目的は、図表を単なる装飾ではなく、本文の論理構造を支える教材要素として設計することである。

---

## 1. 図表設計原則

各図表は、少なくとも次を満たす。

- 対応する章・セクションを持つ。
- 本文のどの論点を支えるかが明確である。
- SVG内に `title` と `desc` を含む。
- HTML側に `figcaption` を持つ。
- 印刷/PDF用の静的説明を持つ。
- 色だけに依存しない。
- インタラクティブ化する場合も、静的版が同じ意味内容を保持する。

---

## 2. 既存図表

| Figure ID | SVG | 対応章 | 対応セクション | 目的 | 状態 |
| --- | --- | --- | --- | --- | --- |
| Figure 0-1 | `engineering-transformation-loss.svg` | Chapter 0 | 0.2 / 0.5 | エンジニアリングが願望・暗黙知・属人的判断を構造へ変換し、その過程で喪失が生じることを示す。 | SVG作成済み / HTML図表索引掲載済み |
| Figure 0-2 / 1-1 | `semantic-transformation-flow.svg` | Chapter 0 / Chapter 1 | 0.8 / 1.1 | 要望からIssue、仕様、実装、文書への変換過程で意味が変化することを示す。 | SVG作成済み / トップHTML・図表索引掲載済み |
| Figure 1-2 | `task-vs-semantic-completion.svg` | Chapter 1 | 1.4 | タスク完了と意味完了の違いを示す。 | SVG作成済み / 図表索引掲載済み |

---

## 3. 次に作成する図表候補

| Figure ID | 対応章 | 対応セクション | 図表案 | 目的 | 優先度 |
| --- | --- | --- | --- | --- | --- |
| Figure 1-3 | Chapter 1 | 1.3 | Git diff vs Semantic lineage 比較図 | Gitがファイル差分を示す一方、意味履歴には意図・喪失・責任が必要であることを示す。 | 高 |
| Figure 1-4 | Chapter 1 | 1.8 | 責任再収束フロー | 人間、AI、レビュー、CI、文書が分散的に関与した後、承認点と記録へ再収束する構造を示す。 | 高 |
| Figure 1-5 | Chapter 1 | 1.5 / 1.6 | AI生成物の昇格フロー | AI生成物が draft / hypothesis / reviewed / accepted / published へ移る流れを示す。 | 高 |
| Figure 2-1 | Chapter 2 | TBD | 中核語彙関係図 | 意味、意図、成果物、判断、責任、ΔM、保存、変換、補完、喪失、逸脱の関係を示す。 | 中 |
| Figure 2-2 | Chapter 2 | TBD | RDE観測カテゴリ図 | preserved / transformed / complemented / unresolved / loss / drift risk / next update policy の関係を示す。 | 中 |

---

## 4. HTML埋め込み方針

章本文HTMLへ図表を埋め込む際は、次の構造を標準とする。

```html
<section class="card figure-card" aria-labelledby="figure-x-title">
  <p class="section-label">Figure X</p>
  <h2 id="figure-x-title">図表タイトル</h2>
  <p>本文上の導入説明。</p>
  <figure>
    <img src="../../assets/svg/example.svg" alt="図表の意味を説明する代替テキスト。" />
    <figcaption>図X: 図表タイトル。</figcaption>
  </figure>
  <div class="text-view">
    <h3>印刷/PDF用の静的説明</h3>
    <p>図表の意味内容を文章で説明する。</p>
  </div>
</section>
```

---

## 5. 今後の注意

図表を増やすほど、本文と図表の対応関係が壊れやすくなる。したがって、図表を追加したら、次を同時に更新する。

- 図表SVG本体
- 図表索引 `method_site/figures/index.html`
- この対応表
- 対応する章HTML
- 必要に応じて章Markdown本文

図表は本文の後付けではなく、意味理解を支える構造部品として扱う。
