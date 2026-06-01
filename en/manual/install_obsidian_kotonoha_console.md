# Obsidian Kotonoha Console — Installation

Install guide for [`obsidian-kotonoha-console`](https://github.com/zyx-corporation/obsidian-kotonoha-console) on Obsidian.

**Canonical detail:** [obsidian-kotonoha-console `docs/install.md`](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/install.md)  
**Japanese:** [`../../ja/manual/install_obsidian_kotonoha_console.md`](../../ja/manual/install_obsidian_kotonoha_console.md)

---

## Prerequisites

| Item | Requirement |
| --- | --- |
| Obsidian | 1.4.0+ |
| Source | [GitHub Release v0.3.0](https://github.com/zyx-corporation/obsidian-kotonoha-console/releases/tag/v0.3.0) |
| CLI backend (optional) | [Install Kotonoha CLI](../tutorials/install_kotonoha_cli.md), `kotonoha >= 0.3.1` |

---

## Install path

```text
<vault>/.obsidian/plugins/kotonoha-console/
├── main.js
├── manifest.json
└── styles.css
```

After unzipping **`kotonoha-console-v0.3.0.zip`**, place `kotonoha-console/` under `.obsidian/plugins/`.

---

## Enable

1. Settings → Community plugins → **Restricted mode OFF**
2. Enable **Kotonoha Console**
3. Settings → Backend: `mock` for UI-only; see [backend setup](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/backend-setup.md) for CLI / HTTP orchestrator

See [`docs/backend-setup.md`](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/backend-setup.md) and [`docs/install.md`](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/install.md).
