# -*- coding: utf-8 -*-
import boto3
import pytest


@pytest.fixture(scope='session')
def ddb():
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    return ddb
