# Obsidian Kotonoha Console — インストール

Obsidian 上で **提案・RDE 監査・人間承認** を行う [`obsidian-kotonoha-console`](https://github.com/zyx-corporation/obsidian-kotonoha-console) の導入手順です。

**正本（詳細）:** [obsidian-kotonoha-console `docs/install.ja.md`](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/install.ja.md)  
**English:** [`../../en/manual/install_obsidian_kotonoha_console.md`](../../en/manual/install_obsidian_kotonoha_console.md)

---

## 1. 前提

| 項目 | 要件 |
| --- | --- |
| Obsidian | 1.4.0 以上 |
| 入手方法 | [GitHub Release](https://github.com/zyx-corporation/obsidian-kotonoha-console/releases)（**v0.3.1 推奨**） |
| CLI backend（任意） | [CLI インストール](../tutorials/install_kotonoha_cli.md) 済み、`kotonoha >= 0.3.1` |

mock / http backend だけ使う場合、CLI は不要です。

---

## 2. 配置

```text
<vault>/.obsidian/plugins/kotonoha-console/
├── main.js
├── manifest.json
└── styles.css
```

Release zip（`obsidian-kotonoha-console-v0.3.0.zip`）を展開したら、フォルダ名を **`kotonoha-console`** にリネームして上記パスに置きます。

---

## 3. 有効化

1. Settings → Community plugins → **Restricted mode OFF**
2. **Kotonoha Console** を Enable
3. Settings → Kotonoha Console → Backend: 初回は `mock` 推奨

---

## 4. 次に読むもの

| 順 | 文書 | 内容 |
| --- | --- | --- |
| 1 | [CLI インストール](../tutorials/install_kotonoha_cli.md) | CLI backend を使う場合 |
| 2 | [obsidian-kotonoha-console README](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/README.md) | v0.3 の現在地・境界 |
| 3 | [dogfood 受け入れ](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/dogfood-acceptance.ja.md) | 手動確認チェックリスト |

---

## RDE note

Obsidian Console は **first usable UI** です。仕様正本は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)。`.kotonoha/` sidecar は local/plugin records であり complete SLS storage ではありません。
