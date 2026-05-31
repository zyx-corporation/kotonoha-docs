# Kotonoha CLI Recommended Version

**Updated:** 2026-05-29  
**Audience:** users, UI adapter maintainers, release verification

Normative source: [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec)  
CLI implementation: [`kotonoha-cli`](https://github.com/zyx-corporation/kotonoha-cli)

Japanese: [`../../ja/manual/cli_version_policy.md`](../../ja/manual/cli_version_policy.md)

---

## Current policy

| Scope | Version | Notes |
| --- | --- | --- |
| **Recommended** | **v0.3.1** | GitHub Latest (as of 2026-05-29) |
| **Minimum (standalone CLI)** | v0.3.0 | Stable runtime from M6 Team Mode onward |
| **Minimum (Obsidian CLI backend)** | v0.3.1 | Requires M6 export profile and status env |
| **Minimum (VSCode extension)** | v0.3.1 | Context export and status integration |

For new installs, pin **v0.3.1**:

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash -s -- --version v0.3.1
```

See [Install Kotonoha CLI](../tutorials/install_kotonoha_cli.md).

---

## UI adapter compatibility

| UI / mode | CLI required | Requirement |
| --- | --- | --- |
| `obsidian-kotonoha-console` — backend **cli** | Yes | ≥ v0.3.1 (`rde emit` / `rde validate`; optional `context export`) |
| `obsidian-kotonoha-console` — **mock** / **http** | No | Orchestrator or mock RDE |
| `kotonoha-vscode` | Yes | ≥ v0.3.1 via `kotonoha.cliPath` |

UI adapters follow CLI/Core behavior and do not redefine the spec. See [Current official architecture](../architecture/current-official-architecture.md) (Japanese; English normative overview lives in `kotonoha-spec`).

---

## Verification

```bash
kotonoha version
```

Expected: clean exit with CLI version and target spec bundle lines.

---

## Update policy

1. **Recommended** tracks GitHub Latest after compatibility checks.
2. When **minimum** versions rise, update this document, the informative section in `kotonoha-spec`, and each UI repo compatibility note in the same cycle.
3. Breaking changes require contract updates in `kotonoha-spec`. **CLI release numbers are not normative spec.**

---

## RDE note

Version pinning is **operational compatibility guidance**. Meaning audit, frontmatter, sidecar, and RDE output contracts remain canonical in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec). The CLI is the first stable runtime that executes against the spec; its version tag does not define semantics.

---

## Related

| Document | Role |
| --- | --- |
| [install_kotonoha_cli.md](../tutorials/install_kotonoha_cli.md) | Installation |
| [current-official-architecture.md](../architecture/current-official-architecture.md) | Layered architecture (JA) |
| [Obsidian CLI compatibility](https://github.com/zyx-corporation/obsidian-kotonoha-console/blob/main/docs/cli-runtime-compatibility.md) | Obsidian Console |
| [VSCode thin console](https://github.com/zyx-corporation/kotonoha-vscode/blob/main/docs/thin-developer-console.md) | VSCode extension |

Governance: [kotonoha-management #167](https://github.com/zyx-corporation/kotonoha-management/issues/167)
