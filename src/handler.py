# -*- coding: utf-8 -*-
import sys

import boto3
from lambda_decorators import json_http_resp, load_json_body

sys.path.append('./src/')

from lib.connector import Connector


ddb = boto3.client('dynamodb')

@json_http_resp
@load_json_body
def put(event, context):
    id = event['body']['id']
    name = event['body']['name']
    conn = Connector(ddb)
    resp = conn.put(id, name)
    return resp
