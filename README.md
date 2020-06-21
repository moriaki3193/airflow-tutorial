# Airflow Tutorial

## Setup

### gitignore ファイルの生成
```shell
# gitignore.io から Python の gitignore ファイルを生成する
% curl -L http://www.gitignore.io/api/python > .gitignore
```

### Python 仮想環境の作成
[Python Docs : 仮想環境の作成](https://docs.python.org/ja/3/library/venv.html)を参考に Python の仮想環境を作成する。

#### 1. pyenv のインストール
このリポジトリ以下で利用する Python のバージョンを取得するために、 [pyenv](https://github.com/pyenv/pyenv) を使用する（インストール方法についてはリンク先を参照する）。

#### 2. Python のバージョンの指定
```shell
# .python-version が作成される
% pyenv local 3.7.5

# 有効になっているバージョンの確認
% python -V
Python 3.7.5
```

#### 3. 仮想環境の初期化
```shell
# .venv という名称のフォルダが作成される
% python -m venv .venv

# 仮想環境を有効にする : fish users
% source .venv/bin/activate.fish
```

### Airflow 開発環境の構築
[Airflow : Home / Installation](https://airflow.apache.org/docs/stable/installation.html) に記載されている手順を参考にローカル開発環境を設定する。

#### OPTIONAL 仮想環境の確認
作成した仮想環境に対する Python のパスが呼び出されていることを確認する。

```shell
# .venv 以下の Python が呼び出されていることを確認する
% which python
path/to/airflow-tutorial/.venv/bin/python
```

#### 1. Airflow のインストール
```shell
% pip install apache-airflow
```

#### 2. データベースの初期化
> Airflow ではタスクを実行する前にデータベースを初期化する必要があります。Airflow で実験を行うあるいは学習しているだけの場合には、デフォルト設定としての SQLite を指定したまま利用することができます。 SQLite を利用したくない場合には、[データベースバックエンドを初期化する](https://airflow.apache.org/docs/stable/howto/initialize-database.html)を参考にその他のデータベースの設定を行ってください。

```shell
# 仮想環境内の Airflow CLI を参照していることを確認
% which airflow

# データベースの初期化 : ユーザホームの airflow ディレクトリに SQLite データベースが作成される
% airflow initdb
DB: sqlite:////Users/msaigusa/airflow/airflow.db
[2020-06-21 19:18:19,607] {db.py:378} INFO - Creating tables
...
...
...
WARNI [airflow.utils.log.logging_mixin.LoggingMixin] cryptography not found - values will not be stored encrypted.
Done.
```
