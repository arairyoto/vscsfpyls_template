## Description
VSCode×Serverless Framework×Python×localstackの開発環境テンプレート

## OS
Windows10

## Requirements
- AWS CLI installed
- Node.js 8.10+ installed
- Python 3.6 installed
- pipenv installed
```
$ pip install pipenv
```
- Serverless Framework installed
```
$ npm i serverless -g
```
## Setup
### Pythonモジュール
```
$ export PIPENV_VENV_IN_PROJECT=1
$ pipenv sync
```
### Node.jsモジュール
```
$ npm i
```
### serverless-dynamodb-local
```
$ sls dynamodb install
```
## Debug
### serverless-offline起動
```
$ sls offline start --stage local --region {REGION} --profile {PROFILE}
```
- REGION：任意のAWSリージョンを入力
- PROFILE：任意のプロファイル名を入力（どのプロファイルであっても問題ありません）
### APIリクエスト
http://localhost:3000にリクエストを送信
## Test
### serverless-offline起動
```
$ sls offline start --stage local --region {REGION} --profile {PROFILE}
```
- REGION：任意のAWSリージョンを入力
- PROFILE：任意のプロファイル名を入力（どのプロファイルであっても問題ありません）
※別プロセスで駆動
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