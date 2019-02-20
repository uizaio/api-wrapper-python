try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url


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

    def update_password(self, id, old_password, new_password):
        """
        Update password allows Admin or User update their current password.
        :param id: identifier of user need reset password
        :param old_password: current password
        :param new_password: new password (from a to Z, 6 to 25 characters)
        :return: tuple of id of user and status code
        """
        self.connection.url = '{}/changepassword'.format(self.connection.url)
        data_body = dict(
            id=id,
            oldPassword=old_password,
            newPassword=new_password
        )
        data = self.connection.post(data=data_body)

        return data

    def logout(self):
        """
        Log out an user
        :return: message
        """
        self.connection.url = '{}/logout'.format(self.connection.url)
        data = self.connection.post()

        return data
