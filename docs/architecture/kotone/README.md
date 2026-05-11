# Kotone Architecture

Kotone の構成要素と関係を示す概念図を管理するディレクトリです。

## Documents

- [Kotone 概念図](./kotone_architecture_overview.html)

## Scope

この図は、Kotone の実装詳細ではなく、以下の概念的構成を示します。

- KMCS 上に主要モジュールを併置する
- KMCS 内部の各モジュールは KMCS Bus を介して必要時に相互接続される
- Sensor I/O と Audio I/O は外部デバイス側でも分離する
- Home Assistant は KMCS モジュールとして Sensor I/O フロントエンドの役割を持つ
- データベースは RDBMS に限定せず、状態・履歴・設定を保持する一般化された保存層として扱う

## Related issue

- #23
