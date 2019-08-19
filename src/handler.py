# -*- coding: utf-8 -*-
import os
import sys

import boto3
from lambda_decorators import json_http_resp, load_json_body

sys.path.append('./src/')

from lib.connector import Connector


# serverless-offlineのデフォルト設定で環境変数`IS_OFFLINE`に1が設定されている
if os.getenv('IS_OFFLINE'):
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
else:
    ddb = boto3.client('dynamodb')


@json_http_resp
@load_json_body
def put(event, context):
    print(event)
    id = event['body']['id']
    name = event['body']['name']
    conn = Connector(ddb)
    print(id, name)
    resp = conn.put(id, name)
    return resp
