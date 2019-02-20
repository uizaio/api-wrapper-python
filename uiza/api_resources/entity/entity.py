try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url


class Entity(UizaBase):

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        super(Entity, self).__init__(connection, **kwargs)
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
        query = '?{}'.format(urlencode(params))
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

    def get_status_publish_entity(self, id):
        """
        Get status publish entity
        :param id: identifier of entity
        :return: tuple of status publish entity and status code
        """
        self.connection.url = '{}/publish/status'.format(self.connection.url)
        query = '?{}'.format(urlencode({'id': id}))
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
