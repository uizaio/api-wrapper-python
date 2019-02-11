from typing import Any, Optional
from urllib import parse

from mappers.users import (
    GetUsersSchema,
    CreateUserSchema,
    UpdateUserSchema,
    UpdatePasswordUserSchema
)
from settings.config import settings
from uiza.base.connections import Connection
from uiza.base.decorators import validate_schema
from utility.utility import set_url


class Service(object):
    def __init__(self, connection: Connection, **kwargs):
        self.connection = connection

    def get_detail(self, id: str) -> Any:
        query = '?{}'.format(parse.urlencode({'id': id}))
        data = self.connection.get(query=query)

        return data

    def remove(self, id: str) -> Any:
        data = self.connection.delete(dict(id=id))

        return data


class User(Service):

    def __init__(self, connection: Connection, **kwargs):
        super(User, self).__init__(connection, **kwargs)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.user.type,
            api_version=settings.uiza_api.user.version,
            api_sub_url=settings.uiza_api.user.sub_url
        )

    @validate_schema(schema=GetUsersSchema)
    def get_users(self, params: Optional[dict] = None) -> Any:
        query = ''
        if params:
            query = '?{}'.format(parse.urlencode(params))
        data = self.connection.get(query=query)

        return data

    @validate_schema(schema=CreateUserSchema())
    def create(self, data: dict) -> Any:
        result = self.connection.post(data=data)

        return result

    @validate_schema(schema=UpdateUserSchema())
    def update(self, id: str, data: Optional[dict] = None) -> Any:
        data = self.connection.put(id=id, data=data)

        return data

    @validate_schema(schema=UpdatePasswordUserSchema())
    def update_password(self, id: str, data):
        self.connection.url = '{}/changepassword'.format(self.connection.url)
        data['id'] = id
        data = self.connection.put(id=id, data=data)

        return data

    def logout(self):
        self.connection.url = '{}/logout'.format(self.connection.url)
        data = self.connection.post()

        return data
