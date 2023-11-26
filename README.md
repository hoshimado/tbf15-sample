# 2章：配布パッケージの作成手順

「§2.3：作成時の依存関係の管理にpipを用いるケース」＞「§2.3.3： buildコマンドによる配布パッケージの作成
」で用いるサンプルコードです。



## §2.3.3： buildコマンドによる配布パッケージの作成

「リスト2.12：pyproject.tomlによる配布パッケージ作成用のフォルダー構成例」で提示のサンプルコードです。

「§2.2：解説に用いるサンプルパッケージの構成」の「リスト2.1：サンプルコードのパッケージ構成」に対して、buildコマンドでの配布パッケージ作成用にメタファイル等を追加したものとなります。

参考までに、動作確認時のコマンド一覧を以下へ記載します。

```
python -m pip install --upgrade build
python -m build
```



