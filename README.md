# 「初めてのPython配布パッケージ作成」本向けサンプルコード

本リポジトリでは、掲題の本に対するサンプルコードを提供しします。

掲題の本は下記で頒布中です。

* [技術書典オンラインマーケット内頒布ページ](https://techbookfest.org/product/8uuq2rQytjrEUNDp92RgGp)
* [BOOTH内頒布ページ](https://xingyanhuan.booth.pm/items/5266614)

（※作成中 at 2023-11-19）

# 説明文の素材（作成中）

2章2節：解説に用いるサンプルパッケージの構成

2.3.1 仮想環境 venv の作成

仮想環境に依存関係をインストールし、サンプルの動作確認


 * 天気の予想気温を取得するモジュール「@<code>{open_meteo_forecast_api.py}」
 ** @<code>{get()}
 *** Open-Meteo@<fn>{open-meteo}が提供するWeb APIを利用して、指定地点の向こう1週間の1h毎の予想気温を取得する関数
 *** 依存関係としてパッケージ「requests@<fn>{pkg-requests}」が必要
 * 取得した予想気温をインプットとして特性を出力するモジュール「@<code>{analyse_temperature.py}」
 ** @<code>{apply()}
 *** 与えられた気温の配列の特性を返す関数
 *** 依存関係としてパッケージ「numpy@<fn>{pkg-numpy}」が必要

//footnote[open-meteo][@<href>{https://open-meteo.com/}]
//footnote[pkg-requests][@<href>{https://pypi.org/project/requests/}]
//footnote[pkg-numpy][@<href>{https://numpy.org/}]

本サンプルはフラットレイアウトを採用します

なお、本サンプルコードを実行すると、予想気温が出力されます（実行方法は後述します）。

//list[example-output-of-sample-code][サンプルコードの実行例]{
tokyo
['2023-10-23T00:00', '2023-10-23T01:00', ..., '2023-10-29T23:00']
[13.2, 12.9, ... , 14.4]
//}


一時的にPythonコマンドにPATHを通す。

```
set PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python311
```

まず、サンプルコードを格納予定の任意のフォルダーに移動しコマンドラインを開きます。
Pythonに標準で含まれる機能を利用して仮想環境を作成するには、その位置でコマンドを実行します。

//list[create-venv][venvを利用して仮想環境を作成する]{
    python -m venv .venv
//}



python -m venv .venv

.venv\Scripts\activate

//list[activate-venv-win][仮想環境venvに入る（Windowsの場合）]{
    .venv\Scripts\activate
//}
//list[activate-venv-lnx][仮想環境venvに入る（Linuxの場合）]{
    source .venv/bin/activate
//}

//list[deactivate-venv][仮想環境venvを抜ける（Windows、Linux共に共通）]{
    deactivate
//}


pip list

python -m pip install requests numpy


python -m weatherforecast



