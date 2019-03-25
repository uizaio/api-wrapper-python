import uiza
from uiza import Connection
from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url
from uiza.exceptions import ClientException


class Storage(UizaBase):

    def __init__(self):
        self.connection = Connection(workspace_api_domain=uiza.workspace_api_domain, api_key=uiza.authorization)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.storage.type,
            api_version=settings.uiza_api.storage.version,
            api_sub_url=settings.uiza_api.storage.sub_url
        )

    def list(self, **params):
        """
        Override method list of Uizabase
        :param params:
        :return: Raise error when get method list
        """
        raise ClientException('Storage list method not found')

    def create(self, **data):
        """
        Override method create of Uizabase
        :param params:
        :return: Raise error when get method list
        """
        raise ClientException('Storage create method not found')

    def delete(self, id):
        """
        Override method create of Uizabase
        :param params:
        :return: Raise error when get method list
        """
        raise ClientException('Storage delete method not found')

    def add(self, **data):
        """
        Add storage
        :param data: data body will be created
        :return: tuple of data created and status code
        """
        result = self.connection.post(data=data)
        try:
            query = self.url_encode(params={'id': result[0].id})
            result = self.connection.get(query=query)
        except Exception:
            pass

        return result

    def remove(self, id):
        """
        Remove storage
        :return: tuple of id removed and status code
        """
        result = self.connection.delete(dict(id=id))

        return result
