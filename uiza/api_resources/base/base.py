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
        try:
            query = '?{}'.format(urlencode({'id': result[0].id}))
            result = self.connection.get(query=query)
        except Exception:
            pass

        return result

    def update(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        result = self.connection.put(data=kwargs)
        try:
            query = '?{}'.format(urlencode({'id': result[0].id}))
            result = self.connection.get(query=query)
        except Exception:
            pass

        return result

    def list(self, **params):
        """

        :param params:
        :return:
        """
        query = ''
        if params:
            query = '?{}'.format(urlencode(params))
        result = self.connection.get(query=query)

        return result

    def retrieve(self, id):
        """

        :param id:
        :return:
        """
        query = '?{}'.format(urlencode({'id': id}))
        result = self.connection.get(query=query)

        return result

    def delete(self, id):
        """

        :return:
        """
        result = self.connection.delete(dict(id=id))

        return result
