try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url
from uiza.exceptions import ClientException


class Callback(UizaBase):

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        super(Callback, self).__init__(connection, **kwargs)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.callback.type,
            api_version=settings.uiza_api.callback.version,
            api_sub_url=settings.uiza_api.callback.sub_url
        )

    def list(self, **params):
        """

        :param params:
        :return:
        """
        raise ClientException('Callback list method not found')
