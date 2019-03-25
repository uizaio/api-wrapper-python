import uiza
from uiza import Connection
from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url
from uiza.exceptions import ClientException


class Analytic(UizaBase):

    def __init__(self):
        self.connection = Connection(workspace_api_domain=uiza.workspace_api_domain, api_key=uiza.authorization)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.analytic.type,
            api_version=settings.uiza_api.analytic.version,
            api_sub_url=settings.uiza_api.analytic.sub_url
        )

    def list(self, **params):
        """
        Override method list of Uizabase
        :param params:
        :return: Raise error when get method list
        """
        raise ClientException('Callback list method not found')

    def create(self, **data):
        """
        Override method create of Uizabase
        :param data:
        :return: Raise error when get method create
        """
        raise ClientException('Callback create method not found')

    def update(self, **kwargs):
        """
        Override method update of Uizabase
        :param kwargs:
        :return: Raise error when get method update
        """
        raise ClientException('Callback update method not found')

    def retrieve(self, id):
        """
        Override method retrieve of Uizabase
        :param id:
        :return: Raise error when get method retrieve
        """
        raise ClientException('Callback retrieve method not found')

    def delete(self, id):
        """
        Override method delete of Uizabase
        :return: Raise error when get method delete
        """
        raise ClientException('Callback delete method not found')

    def get_total_line(self, start_date, end_date, metric):
        """
        Get total line
        :param start_date: start date
        :param end_date: end date
        :param metric: get metric from https://docs.uiza.io/#analytic-metrics
        :return:
        """
        params = dict(
            start_date=start_date,
            end_date=end_date,
            metric=metric
        )
        self.connection.url = '{}/total-line-v2'.format(self.connection.url)
        query = self.url_encode(params=params)
        result = self.connection.get(query=query)

        return result

    def get_type(self, start_date, end_date, type_filter):
        """
        Get data base on 4 type of filter: country, device, title, player
        :param start_date: start date
        :param end_date: end date
        :param type_filter: filter are country, device, title, player
        :return:
        """
        params = dict(
            start_date=start_date,
            end_date=end_date,
            type_filter=type_filter
        )
        self.connection.url = '{}/type'.format(self.connection.url)
        query = self.url_encode(params=params)
        result = self.connection.get(query=query)

        return result

    def get_line(self, start_date, end_date, type):
        """
        Get data grouped by hour
        :param start_date: start date
        :param end_date: end date
        :param type: type
        :return:
        """
        params = dict(
            start_date=start_date,
            end_date=end_date,
            type=type
        )
        self.connection.url = '{}/line'.format(self.connection.url)
        query = self.url_encode(params=params)
        result = self.connection.get(query=query)

        return result
