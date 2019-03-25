import uiza
from uiza import Connection
from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url


class Entity(UizaBase):

    def __init__(self):
        self.connection = Connection(workspace_api_domain=uiza.workspace_api_domain, api_key=uiza.authorization)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.entity.type,
            api_version=settings.uiza_api.entity.version,
            api_sub_url=settings.uiza_api.entity.sub_url
        )

    def search(self, keyword):
        """
        Search entity base on keyword entered
        :param keyword: keyword for search entity
        :return: tuple of list detail entity and status code
        """
        self.connection.url = '{}/search'.format(self.connection.url)
        params = dict(keyword=keyword)
        query = self.url_encode(params=params)
        data = self.connection.get(query=query)

        return data

    def publish(self, id):
        """
        Publish entity to CDN, use for streaming
        :param id: identifier of entity
        :return: tuple of response and status code
        """
        self.connection.url = '{}/publish'.format(self.connection.url)
        data = self.connection.post(data={'id': id})

        return data

    def get_status_publish(self, id):
        """
        Get status publish entity
        :param id: identifier of entity
        :return: tuple of status publish entity and status code
        """
        self.connection.url = '{}/publish/status'.format(self.connection.url)
        query = self.url_encode(params={'id': id})
        data = self.connection.get(query=query)

        return data

    def get_aws_upload_key(self):
        """
        Return the bucket temporary upload storage & key for upload
        :return:
        """
        aws_sub_url = 'admin/app/config/aws'
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.entity.type,
            api_version=settings.uiza_api.entity.version,
            api_sub_url=aws_sub_url
        )

        data = self.connection.get()

        return data
