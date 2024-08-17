# udemy-langchain

## 実行手順

### 1. Python のバージョンの確認

以下のコマンドで、Poetry で実行できる Python のバージョンを確認してください。

```console
poetry run python --version
```

[.tool-verisons](.tool-versions) に書かれたバージョンが表示されれば問題ありません。

> **Note**
> もしも想定外のバージョンが表示された場合、以下の手順を試してください。
>
> - `poetry env list` コマンドで、poetry で作成した環境を表示
> - `poetry env remove 3.10` などのコマンドで環境を一通り削除
> - `poetry env use $(which python)` コマンドを実行

### 2. パッケージのインストール

以下のコマンドで、Poetry を使って Python パッケージをインストールしてください。

```console
poetry install
```

### 3. `.env` ファイルの作成

以下のような内容で、`.env` ファイルを作成してください。

```
OPENAI_API_KEY=<your-openai-api-key>
GRADIO_USERNAME=oshima
GRADIO_PASSWORD=oshimapassword
APP_ENV=local
```

### 4. 実行

Gradio の Web アプリケーションを起動する場合、以下のコマンドを実行してください。

```console
poetry run python src/gradio_app.py
```
