#!/bin/bash

# パッケージ名（フォルダへのパス）
PKG_DIRNAME=./weatherforecast

# 作業フォルダ
WORKING_ENCODED_DISTPATH=./encoded_dist

# 実行開始の起点フォルダを記録
SCRIPT_ROOT_PATH=$(pwd)


# PKG化対象のPythonモジュールが格納されたフォルダ全体を、難読化
pyarmor gen --recursive --output $WORKING_ENCODED_DISTPATH   $PKG_DIRNAME



# 難読化後のPythonモジュールとランタイムが格納されたフォルダーへ、
# setup.pyによる配布パッケージの作成に必要なファイルをコピー
cp ./setup.py         $WORKING_ENCODED_DISTPATH/
cp ./requirements.txt $WORKING_ENCODED_DISTPATH/


# 難読化済みのPythonモジュールを用いて、配布パッケージ（Wheel形式）を作成
cd $WORKING_ENCODED_DISTPATH
python setup.py bdist_wheel



# ビルドを終えた成果物を、スクリプト√の`./dist`フォルダへ集約
mkdir $SCRIPT_ROOT_PATH/dist
cp ./dist/*   $SCRIPT_ROOT_PATH/dist/
cd $SCRIPT_ROOT_PATH



# ビルドの中間成果物を削除
# ※Debugしたい場合は、コメントアウトすること
rm -r $WORKING_ENCODED_DISTPATH


