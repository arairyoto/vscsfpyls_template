# -*- coding: utf-8 -*-
import os


TABLE_NAME = os.getenv('TABLE_NAME')


class Connector:
    def __init__(self, ddb):
        self._ddb = ddb

    def put(self, id, name):
        return self._ddb.put_item(
            TableName=TABLE_NAME,
            Item={
                'id': {
                    'S': id
                },
                'name': {
                    'S': name
                }
            }
        )

    def get(self, id):
        return self._ddb.get_item(
            TableName=TABLE_NAME,
            Key={
                'id': {
                    'S': id
                }
            }
        )