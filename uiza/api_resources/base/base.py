try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class UizaBase(object):

    data_validated = None
    connection = None

    def create(self, **data):
        """
        Create data
        :param data: data body will be created
        :return: tuple of data created and status code
        """
        result = self.connection.post(data=data)
        try:
            query = self.url_encode(params={'id': result[0].id})
            result = self.connection.get(query=query)
        except Exception:
            pass

        return result

    def update(self, **kwargs):
        """
        Update data
        :param kwargs: data body will be updated
        :return: tuple of data updated and status code
        """
        result = self.connection.put(data=kwargs)
        try:
            query = self.url_encode(params={'id': result[0].id})
            result = self.connection.get(query=query)
        except Exception:
            pass

        return result

    def list(self, **params):
        """
        List data
        :param params: params
        :return: tuple of data exist and status code
        """
        query = ''
        if params:
            query = self.url_encode(params=params)
        result = self.connection.get(query=query)

        return result

    def retrieve(self, id):
        """
        Get detail
        :param id: id of object
        :return: tuple of data and status code
        """
        query = self.url_encode(params={'id': id})
        result = self.connection.get(query=query)

        return result

    def delete(self, id):
        """ata
        Delete data
        :return: tuple of id removed and status code
        """
        result = self.connection.delete(dict(id=id))

        return result

    def url_encode(self, params):
        return '?{}'.format(urlencode(params))
