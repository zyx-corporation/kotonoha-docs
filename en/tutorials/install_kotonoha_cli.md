# Install the Kotonoha CLI

Beginner-oriented install guide for the official `kotonoha` command.

**Next:** [First CLI session](first_cli_session.md)  
**Japanese:** [../../ja/tutorials/install_kotonoha_cli.md](../../ja/tutorials/install_kotonoha_cli.md)  
**Version policy:** [../manual/cli_version_policy.md](../manual/cli_version_policy.md)  
**Maintainer guide:** [../../ja/manual/cli_installer_implementation.md](../../ja/manual/cli_installer_implementation.md)

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash
export PATH="$HOME/.local/bin:$PATH"
kotonoha version
```

Pin a release:

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash -s -- --version v0.3.1
```

If no release binary exists for your platform, the installer falls back to `cargo install` (Rust required). See the Japanese tutorial for PATH and troubleshooting detail.

---

## Next reading

| Order | Document | Content |
| --- | --- | --- |
| 1 | [first_cli_session.md](first_cli_session.md) | First RDE / interchange session |
| 2 | [slm_demo_quickstart.md](slm_demo_quickstart.md) | Local SLM and draft validation |
| — | [install_obsidian_kotonoha_console.md](../manual/install_obsidian_kotonoha_console.md) | Obsidian plugin (UI) |
| — | [phase2_cli_acceptance_demo.md](../acceptance/phase2_cli_acceptance_demo.md) | Release verification (separate from learning) |

---

## RDE note

Installation is an **entry point**, not Kotonoha theory itself. Meaning audit and normative definitions live in [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) and each tool's contract docs.
