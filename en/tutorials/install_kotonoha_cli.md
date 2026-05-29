# Install the Kotonoha CLI

Beginner-oriented install guide for the official `kotonoha` command.

**Next:** [First CLI session](first_cli_session.md)  
**Japanese:** [../../ja/tutorials/install_kotonoha_cli.md](../../ja/tutorials/install_kotonoha_cli.md)  
**Maintainer guide:** [../../ja/manual/cli_installer_implementation.md](../../ja/manual/cli_installer_implementation.md)

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash
export PATH="$HOME/.local/bin:$PATH"
kotonoha version
```

Pin a release:

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash -s -- --version v0.2.9
```

If no release binary exists for your platform, the installer falls back to `cargo install` (Rust required). See the Japanese tutorial for PATH and troubleshooting detail.
