try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url
from uiza.exceptions import ClientException


class Analytic(UizaBase):

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        super(Analytic, self).__init__(connection, **kwargs)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.analytic.type,
            api_version=settings.uiza_api.analytic.version,
            api_sub_url=settings.uiza_api.analytic.sub_url
        )

    def list(self, **params):
        """

        :param params:
        :return:
        """
        raise ClientException('Callback list method not found')

    def create(self, **data):
        """

        :param data:
        :return:
        """
        raise ClientException('Callback create method not found')

    def update(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        raise ClientException('Callback update method not found')

    def retrieve(self, id):
        """

        :param id:
        :return:
        """
        raise ClientException('Callback retrieve method not found')

    def delete(self, id):
        """

        :return:
        """
        raise ClientException('Callback delete method not found')

    def get_total_line(self, start_date, end_date, metric):
        """

        :param start_date:
        :param end_date:
        :param metric:
        :return:
        """
        params = dict(
            start_date=start_date,
            end_date=end_date,
            metric=metric
        )
        self.connection.url = '{}/total-line-v2'.format(self.connection.url)
        query = '?{}'.format(urlencode(params))
        result = self.connection.get(query=query)

        return result

    def get_type(self, start_date, end_date, type_filter):
        """

        :param start_date:
        :param end_date:
        :param type_filter:
        :return:
        """
        params = dict(
            start_date=start_date,
            end_date=end_date,
            type_filter=type_filter
        )
        self.connection.url = '{}/type'.format(self.connection.url)
        query = '?{}'.format(urlencode(params))
        result = self.connection.get(query=query)

        return result

    def get_line(self, start_date, end_date):
        """

        :param start_date:
        :param end_date:
        :return:
        """
        params = dict(
            start_date=start_date,
            end_date=end_date
        )
        self.connection.url = '{}/line'.format(self.connection.url)
        query = '?{}'.format(urlencode(params))
        result = self.connection.get(query=query)

        return result
