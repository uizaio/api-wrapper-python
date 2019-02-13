try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.base.base import UizaBase
from settings.config import settings
from utility.utility import set_url
from uiza.entity.handle_errors import EntitiesErrors


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

    def search(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.connection.url = '{}/search'.format(self.connection.url)
        query = ''
        if kwargs:
            query = '?{}'.format(urlencode(kwargs))
        data = self.connection.get(query=query)

        return data

    def publish(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        self.connection.url = '{}/publish'.format(self.connection.url)
        data = self.connection.post(data=kwargs)

        return data

    def get_status_publish_entity(self, id):
        """

        :param kwargs:
        :return:
        """
        self.connection.url = '{}/publish/status'.format(self.connection.url)
        query = '?{}'.format(urlencode({'id': id}))
        data = self.connection.get(query=query)

        return data

    def get_aws_upload_key(self):
        """

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
