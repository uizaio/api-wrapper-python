import uiza
from uiza import Connection
from uiza.api_resources.base.base import UizaBase
from uiza.exceptions import ClientException
from uiza.settings.config import settings
from uiza.utility.utility import set_url


class User(UizaBase):

    def __init__(self):
        self.connection = Connection(workspace_api_domain=uiza.workspace_api_domain, api_key=uiza.api_key)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.user.type,
            api_version=settings.uiza_api.user.version,
            api_sub_url=settings.uiza_api.user.sub_url
        )

    def list(self, **params):
        """
        Override method list of Uizabase
        :param params:
        """
        raise ClientException('User list method not found')

    def create(self, **data):
        """
        Override method create of Uizabase
        :param data:
        """
        raise ClientException('User create method not found')

    def update(self, **kwargs):
        """
        Override method update of Uizabase
        :param kwargs:
        """
        raise ClientException('User update method not found')

    def retrieve(self, id):
        """
        Override method retrieve of Uizabase
        :param id:
        """
        raise ClientException('User retrieve method not found')

    def delete(self, id):
        """
        Override method delete of Uizabase
        """
        raise ClientException('User delete method not found')

    # def login(self, email, password):
    #     """
    #     Login user function
    #     :param email: email of user
    #     :param password: password of user
    #     """
    #     self.connection.url = '{}/auth'.format(self.connection.url)
    #     data = self.connection.post(data={'email': email, 'password': password})
    #
    #     return data
    #
    # def check_token(self):
    #     """
    #     Check token user function
    #
    #     """
    #     self.connection.url = '{}/auth/check-token'.format(self.connection.url)
    #     data = self.connection.get()
    #
    #     return data
    #
    # def referral(self, user_id, total_referral):
    #     """
    #     Referral user function
    #     :param user_id: id of user
    #     :param total_referral: total referral
    #     """
    #     self.connection.url = '{}/referral'.format(self.connection.url)
    #     data = self.connection.post(data={'userId': user_id, 'totalReferral': total_referral})
    #
    #     return data
    #
    # def change_password(self, old_password, new_password):
    #     """
    #     Change password allows Admin or User update their current password.
    #     :param id: identifier of user need reset password
    #     :param old_password: current password
    #     :param new_password: new password (from a to Z, 6 to 25 characters)
    #     """
    #     self.connection.url = '{}/changePassword'.format(self.connection.url)
    #     data_body = dict(
    #         oldPassword=old_password,
    #         newPassword=new_password
    #     )
    #     data = self.connection.post(data=data_body)
    #
    #     return data
    #
    # def logout(self):
    #     """
    #     Log out an user
    #     """
    #     self.connection.url = '{}/logout'.format(self.connection.url)
    #     data = self.connection.post()
    #
    #     return data
