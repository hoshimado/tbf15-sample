# 付録

## 付録B：本書で利用するPython環境のインストール方法

「§B.1：WindowsでのPython環境の作り」に記載の、
「そのコマンドラインを閉じるまでは、一時的にPythonコマンドにPATHが通った状態」とするための
コマンドは以下です。

```
set PATH=%PATH%;%USERPROFILE%\AppData\Local\Programs\Python\Python311
```

「§B.2：LinuxでのPython環境の作り方」に記載の、Dockerfileファイルは以下です。

* [Dockerfile](./docker/Dockerfile)



## 付録C：パッケージ化の前にソース難読化を実施する（Pyarmor）

「§C.2：Setup()関数による配布パッケージの作成手順」に記載の
「リストC.1：Pyarmorで難読化したのちにsetup.pyで配布パッケージを作成する」
のシェルスクリプトは以下です。

* [build_whl_by_setuppy_with_pyarmor.sh](./examples/build_whl_by_setuppy_with_pyarmor.sh)

「§C.3：poetryコマンドによる配布パッケージの作成手順」に記載の
「リストC.3：Pyarmorで難読化したのちにpoetryで配布パッケージを作成する」
のシェルスクリプトは以下です。

* [build_whl_by_poetry_with_pyarmor.sh](./examples/build_whl_by_poetry_with_pyarmor.sh)

その際に用いる、キー追記後のpyporject.tomlファイルは以下です。

* [Pyarmorを考慮したpyproject.toml](./examples/pyproject.toml)



## 付録D：配布パッケージ化をGitHub Actionsで自動化する（CI 構築）

本節に記載のワークフローファイルは以下です。

* [リストD.1：setup.pyを用いた配布パッケージの作成のワークフロー](./examples/python-package-legacy.yml)
* [リストD.2：poetryを用いた配布パッケージの作成のワークフロー](./examples/python-package-poetry.yml)
* [リストD.3：poetryを用いた配布パッケージの作成を、難読化込みで実施するワークフロー](./examples/python-package-poetry-with-pyarmor.yml)




