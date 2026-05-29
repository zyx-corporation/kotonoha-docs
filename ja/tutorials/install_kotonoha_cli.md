# Kotonoha CLI のインストール

このチュートリアルは、**はじめて `kotonoha` コマンドを使う人**向けです。ターミナル（macOS の「ターミナル」、Linux のシェル）が開ければ進められます。**Rust や Git の知識は不要**です（インストーラーが必要に応じてソースからビルドします）。

**次のステップ:** インストール後は [最初の CLI セッション](first_cli_session.md) へ進んでください。

**English:** [../../en/tutorials/install_kotonoha_cli.md](../../en/tutorials/install_kotonoha_cli.md)  
**メンテナ向け実装手順:** [../manual/cli_installer_implementation.md](../manual/cli_installer_implementation.md)

---

## このチュートリアルで行うこと

| 段階 | 内容 |
| --- | --- |
| 1 | 公式インストーラーを実行する |
| 2 | `kotonoha` が使えるように PATH を通す |
| 3 | `kotonoha version` で動作確認する |

## 前提

| 項目 | 必要か |
| --- | --- |
| macOS または Linux | はい |
| インターネット接続 | はい |
| Rust（事前インストール） | いいえ（バイナリ配布が無い場合のみ、インストーラーが自動で `cargo install` を試します） |
| PostgreSQL | いいえ（この段階では不要） |

---

## 1. インストーラーを実行する

次の**1行**をターミナルに貼り付けて Enter を押します。

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash
```

### 何が起きているか

| 部分 | 意味 |
| --- | --- |
| `curl -fsSL` | インターネットからスクリプトを安全に取得する |
| `install.sh` | Kotonoha 公式のインストールスクリプト |
| `\| bash` | 取得したスクリプトを実行する |

インストーラーは次を試します。

1. **GitHub Releases** からお使いの OS 向けバイナリをダウンロード（速い）
2. バイナリが無い場合は **`cargo install`** でビルド（数分かかることがあります）

### バージョンを指定したい場合

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash -s -- --version v0.2.9
```

### インストール先を変えたい場合

既定は `~/.local/bin` です。

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash -s -- --dir "$HOME/.local"
```

---

## 2. PATH を通す

インストール先が `~/.local/bin` のとき、**新しいターミナル**で次を実行するか、シェル設定ファイルに追記します。

```bash
export PATH="$HOME/.local/bin:$PATH"
```

| シェル | 追記するファイル（例） |
| --- | --- |
| bash | `~/.bashrc` |
| zsh（macOS 既定） | `~/.zprofile` または `~/.zshrc` |

追記する1行:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

設定を読み直す例（zsh）:

```bash
source ~/.zprofile
```

---

## 3. 動作確認

```bash
kotonoha version
```

**期待:** エラーなく終了し、CLI のバージョンと対象 spec bundle に関する行が表示される。

表示されない場合（`command not found`）:

1. 手順 2 の PATH を再度確認する
2. 別ターミナルウィンドウを開き直す
3. それでも失敗する場合は [トラブルシューティング](#トラブルシューティング) を参照

---

## トラブルシューティング

| 症状 | 対処 |
| --- | --- |
| `command not found: kotonoha` | PATH に `~/.local/bin` が含まれているか確認 |
| バイナリ取得に失敗し cargo が始まる | Rust が未インストールなら [rustup.rs](https://rustup.rs/) で Rust を入れてから再実行、または `KOTONOHA_INSTALL_METHOD=cargo` を明示 |
| 企業プロキシで curl が失敗 | プロキシ設定をしたうえで再試行、または [ソースからビルド](https://github.com/zyx-corporation/kotonoha-cli/blob/main/README_ja.md) |
| 厳密な終了コード・出力形式 | [cli-definition.md](https://github.com/zyx-corporation/kotonoha-cli/blob/main/docs/cli-definition.md) |

cargo のみで入れたい場合:

```bash
curl -fsSL https://raw.githubusercontent.com/zyx-corporation/kotonoha-cli/main/scripts/install.sh | bash -s -- --method cargo
```

---

## 次に読むもの

| 順 | 文書 | 内容 |
| --- | --- | --- |
| 1 | [first_cli_session.md](first_cli_session.md) | RDE / interchange の初回体験 |
| 2 | [slm_demo_quickstart.md](slm_demo_quickstart.md) | ローカル SLM と草案検証 |
| — | [phase2_cli_acceptance_demo.md](../acceptance/phase2_cli_acceptance_demo.md) | リリース確認（学習とは別目的） |

---

## RDE note

インストールは **Kotonoha の理論そのものではなく入口** です。意味監査・規範定義は [`kotonoha-spec`](https://github.com/zyx-corporation/kotonoha-spec) と各ツールの契約文書にあります。インストールログは懲罰目的ではなく、導入と再現のための手順です。
