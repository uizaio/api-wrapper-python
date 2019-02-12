from typing import Any
from urllib import parse

from uiza.base.connections import Connection


class UizaBase(object):
    def __init__(self, connection: Connection, **kwargs):
        self.connection = connection

    def get_detail(self, id: str) -> Any:
        query = '?{}'.format(parse.urlencode({'id': id}))
        data = self.connection.get(query=query)

        return data

    def remove(self, id: str) -> Any:
        data = self.connection.delete(dict(id=id))

        return data
