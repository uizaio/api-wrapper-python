try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.base.base import UizaBase
from settings.config import settings
from utility.utility import set_url


class User(UizaBase):

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        super(User, self).__init__(connection, **kwargs)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.user.type,
            api_version=settings.uiza_api.user.version,
            api_sub_url=settings.uiza_api.user.sub_url
        )

    def update_password(self, **data):
        """

        :param data:
        :return:
        """
        self.connection.url = '{}/changepassword'.format(self.connection.url)
        data = self.connection.post(data=data)

        return data

    def logout(self):
        """

        :return:
        """
        self.connection.url = '{}/logout'.format(self.connection.url)
        data = self.connection.post()

        return data
