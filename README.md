## Description
VSCode×Serverless Framework×Python×localstackの開発環境テンプレート

## OS
Windows10

## Requirements
- AWS CLI installed
- Node.js 8.10+ installed
- Python 3.6 installed
- Docker installed
- pipenv installed
```
$ pip install pipenv
```
- Serverless Framework installed
```
$ npm i serverless -g
```
## Setup
### localstack
```
$ git clone https://github.com/localstack/localstack.git
```
※他ディレクトリにクローン
### Pythonモジュール
```
$ export PIPENV_VENV_IN_PROJECT=1
$ pipenv sync
```
### Node.jsモジュール
```
$ npm i
```
## Test
### localstack起動
localstackをクローンしたディレクトリに移り、localstackを起動
```
$ export COMPOSE_CONVERT_WINDOWS_PATHS=1
$ cd path/to/localstack
$ docker-compose up
```
※別プロセスで実行
### ローカルデプロイ
localstackにデプロイ（AWSにはデプロイされません）
```
$ sls deploy --stage local --region {REGION} --profile {PROFILE}
```
- REGION：任意のAWSリージョンを入力
- PROFILE：任意のプロファイル名を入力（どのプロファイルであっても問題ありません）
### 環境変数設定
Lambdaで環境変数を使用している場合は、環境変数を設定
```
$ export TABLE_NAME=user
```
### テスト実行
```
$ cd tests
$ pytest -v
```
## Build and Deploy
```
$ sls deploy --stage {STAGE} --region {REGION} --profile {PROFILE}
```
- STAGE：ステージ名（dev, stg, prod, ...）
- REGION：AWSリージョン
- PROFILE：プロファイル名