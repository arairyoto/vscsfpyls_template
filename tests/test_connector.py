import sys

sys.path.append('../src/')

import pytest

from lib.connector import Connector


@pytest.mark.parametrize('id,name', [
    ('1', '1'),
    ('id', 'name')
])
def test_put(ddb, id, name):
    conn = Connector(ddb)
    resp = conn.put(id, name)
    assert resp['ResponseMetadata']['HTTPStatusCode'] == 200

