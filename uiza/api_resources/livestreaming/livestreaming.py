try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url
from uiza.exceptions import ClientException


class LiveStreaming(UizaBase):

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        super(LiveStreaming, self).__init__(connection, **kwargs)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.livestreaming.type,
            api_version=settings.uiza_api.livestreaming.version,
            api_sub_url=settings.uiza_api.livestreaming.sub_url
        )

    def list(self, **params):
        """

        :param params:
        :return:
        """
        raise ClientException('Livestreaming list method not found')

    def delete(self, id):
        """

        :param id:
        :return:
        """
        raise ClientException('Livestreaming delete method not found')

    def start_feed(self, id):
        """

        :param id:
        :return:
        """
        self.connection.url = '{}/feed'.format(self.connection.url)
        result = self.connection.post(dict(id=id))

        return result

    def stop_feed(self, id):
        """

        :param id:
        :return:
        """
        self.connection.url = '{}/feed'.format(self.connection.url)
        result = self.connection.put(dict(id=id))

        return result

    def get_view_feed(self,  id):
        """

        :param id:
        :return:
        """
        self.connection.url = '{}/tracking/current-view'.format(self.connection.url)
        query = '?{}'.format(urlencode({'id': id}))
        result = self.connection.get(query=query)

        return result

    def list_recorded(self):
        """

        :return:
        """
        self.connection.url = '{}/dvr'.format(self.connection.url)
        result = self.connection.get()

        return result

    def convert_into_vod(self, id):
        """

        :param id:
        :return:
        """
        self.connection.url = '{}/dvr/convert-to-vod'.format(self.connection.url)
        result = self.connection.post(dict(id=id))

        return result

    def delete_recorded(self, id):
        """

        :param id:
        :return:
        """
        self.connection.url = '{}/dvr'.format(self.connection.url)
        result = self.connection.delete(dict(id=id))

        return result
