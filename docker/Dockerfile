FROM python:3.9-alpine3.18 
# https://github.com/docker-library/python/blob/8f971d595fff0cc134370916a069bfedc5887308/3.9/alpine3.18/Dockerfile


# curlコマンドの導入と、本書で配布パッケージの作成に利用するパッケージのインストール
RUN apk --no-cache add curl \
 && curl -sSL https://install.python-poetry.org | python3 - \
 && echo 'export PATH=$PATH:/root/.local/bin' >> ~/.bashrc \
 && /root/.local/bin/poetry config virtualenvs.in-project true \
 && pip install pyarmor \
 && pip install --upgrade setuptools wheel \
 && pip install --upgrade build \
 && python -m pip install --upgrade pip


# 対話的なシェルに対して、明示的に環境変数PATHへ/root/.local/binを追加
ENV PATH="${PATH}:/root/.local/bin"
