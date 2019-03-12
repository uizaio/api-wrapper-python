try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import uiza


class UizaBase(object):
    data_validated = None
    connection = None

    def create(self, **data):
        """
        Create data
        :param data: data body will be created
        """
        data_body = dict(appId=uiza.app_id)
        data_body.update(data)
        result = self.connection.post(data=data_body)
        try:
            query = self.url_encode(params={'id': result[0].id, 'appId': uiza.app_id})
            result = self.connection.get(query=query)
        except Exception:
            pass

        return result

    def update(self, **kwargs):
        """
        Update data
        :param kwargs: data body will be updated
        """
        data_body = dict(appId=uiza.app_id)
        if kwargs:
            data_body.update(kwargs)
        result = self.connection.put(data=data_body)
        try:
            query = self.url_encode(params={'id': result[0].id, 'appId': uiza.app_id})
            result = self.connection.get(query=query)
        except Exception:
            pass

        return result

    def list(self, **kwargs):
        """
        List data
        :param kwargs: params
        """
        params = dict(appId=uiza.app_id)
        if kwargs:
            params.update(kwargs)
        query = self.url_encode(params=params)
        result = self.connection.get(query=query)

        return result

    def retrieve(self, id):
        """
        Get detail
        :param id: id of object
        """
        query = self.url_encode(params={'id': id, 'appId': uiza.app_id})
        result = self.connection.get(query=query)

        return result

    def delete(self, id):
        """ata
        Delete data
        :param id: id of object
        :param appId: appId
        """
        result = self.connection.delete(dict(id=id, appId=uiza.app_id))

        return result

    def url_encode(self, params):
        return '?{}'.format(urlencode(params))
