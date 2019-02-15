try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class UizaBase(object):

    data_validated = None

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        self.connection = connection

    def create(self, **data):
        """

        :param data:
        :return:
        """
        result = self.connection.post(data=data)

        return result

    def update(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        data = self.connection.put(data=kwargs)

        return data

    def list(self, **params):
        """

        :param params:
        :return:
        """
        query = ''
        if params:
            query = '?{}'.format(urlencode(params))
        data = self.connection.get(query=query)

        return data

    def retrieve(self, id):
        """

        :param id:
        :return:
        """
        query = '?{}'.format(urlencode({'id': id}))
        data = self.connection.get(query=query)

        return data

    def delete(self, id):
        """

        :return:
        """
        data = self.connection.delete(dict(id=id))

        return data
