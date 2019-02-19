try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url


class Category(UizaBase):

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        super(Category, self).__init__(connection, **kwargs)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.category.type,
            api_version=settings.uiza_api.category.version,
            api_sub_url=settings.uiza_api.category.sub_url
        )
        self.category_relation_url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.category.type,
            api_version=settings.uiza_api.category.version,
            api_sub_url='media/entity/related/metadata'
        )

    def create_relation(self, **data):
        """

        :param data:
        :return:
        """
        self.connection.url = self.category_relation_url
        result = self.connection.post(data)

        return result

    def delete_relation(self, **data):
        """

        :param data:
        :return:
        """
        self.connection.url = self.category_relation_url
        result = self.connection.delete(data)

        return result
