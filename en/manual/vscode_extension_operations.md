# Kotonoha VS Code extension — operations manual

Task-oriented guide for [`kotonoha-vscode`](https://github.com/zyx-corporation/kotonoha-vscode) in VS Code / Cursor: **MeaningDelta**, **RDE**, and **Review** via the `kotonoha` CLI.

**Informative spec:** [kotonoha-management M3 draft](https://github.com/zyx-corporation/kotonoha-management/blob/main/docs/29_m3_minimal_ui_spec_draft.md)  
**Acceptance checklist:** [kotonoha-vscode `docs/m3_acceptance.md`](https://github.com/zyx-corporation/kotonoha-vscode/blob/main/docs/m3_acceptance.md)  
**CLI contract:** [`cli-definition.md`](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md)

日本語: [`../../ja/manual/vscode_extension_operations.md`](../../ja/manual/vscode_extension_operations.md)

---

## 1. Prerequisites

| Item | Requirement |
| --- | --- |
| IDE | VS Code **1.85+** or Cursor |
| CLI | [`kotonoha`](https://github.com/zyx-corporation/kotonoha-cli) **≥ 0.2.4** (with `status`, `delta`, `review`) |
| Core | **≥ 0.1.9** (via CLI) |
| PostgreSQL | Server running; **database created**; `kotonoha db migrate` applied |
| Workspace | Open a **Git repository** folder (not the extension sources alone) |

### 1.1 Database (before `db migrate`)

`kotonoha db migrate` creates tables **inside** an existing database. Create the role and database first.

**Docker example (requires `-p 5432:5432` for host access):**

```bash
docker run -d --name kotonoha-pg \
  -e POSTGRES_USER=YOUR_USER \
  -e POSTGRES_PASSWORD='YOUR_PASSWORD' \
  -e POSTGRES_DB=YOUR_DB \
  -p 5432:5432 \
  postgres:16-alpine

export DATABASE_URL='postgres://YOUR_USER:YOUR_PASSWORD@localhost:5432/YOUR_DB'
kotonoha db migrate
```

Confirm `0.0.0.0:5432->5432/tcp` in `docker ps`.

### 1.2 CLI build

```bash
cd kotonoha-cli && cargo build --release
```

Rebuild if `status` is reported as an unknown subcommand (stale binary).

---

## 2. Running the extension

### 2.1 Development (F5)

1. Open the **`kotonoha-vscode`** repo in the IDE.
2. `npm install && npm run compile`
3. **Run and Debug** → **Run Extension** (or **F5** with focus in the editor — not the terminal).
4. In the **Extension Development Host** window, **File → Open Folder** on your Git project.

### 2.2 Workspace settings (EDH)

```json
{
  "kotonoha.cliPath": "/path/to/kotonoha-cli/target/release/kotonoha",
  "kotonoha.databaseUrl": "postgres://USER:PASSWORD@localhost:5432/DBNAME",
  "kotonoha.decidedBy": "you@example.com"
}
```

Use the **same full URL** as for `db migrate`. Do not commit secrets.

---

## 3. UI layout

Activity bar **Kotonoha** → three sidebar panels: **Context**, **Meaning Delta**, **RDE & Review**.

Each panel title bar has a **Kotonoha** icon (reopen sidebar) and contextual actions (Refresh, panel jumps).

---

## 4. Default keyboard shortcuts

| Action | macOS | Windows / Linux |
| --- | --- | --- |
| Show Kotonoha sidebar | `Cmd+Alt+K` | `Ctrl+Alt+K` |
| Context panel | `Cmd+Alt+Shift+C` | `Ctrl+Alt+Shift+C` |
| Meaning Delta panel | `Cmd+Alt+Shift+M` | `Ctrl+Alt+Shift+M` |
| RDE & Review panel | `Cmd+Alt+Shift+R` | `Ctrl+Alt+Shift+R` |
| Register ΔM (focus) | `Cmd+Alt+Shift+D` | `Ctrl+Alt+Shift+D` |

Rebind under **Keyboard Shortcuts** (`kotonoha`). Command Palette: `Kotonoha:` commands.

---

## 5. Basic workflow

1. **Context** → Refresh → `database: connected`
2. **Meaning Delta** → Register ΔM → note UUID
3. **RDE & Review** → paste/file attach → Review → Copy export (m2)

See the Japanese manual for step-by-step troubleshooting tables (same content).

---

## Revision

| Date | Change |
| --- | --- |
| 2026-05-20 | Initial M3 operations + shortcuts + DB bootstrap |
