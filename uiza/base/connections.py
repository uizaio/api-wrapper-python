import re
import json

try:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import Request, urlopen
    from urllib2 import HTTPError

# from uiza.base.handle_errors import ServerException


class Connection(object):

    url = None

    def __init__(self, workspace_api_domain, api_key, **kwargs):
        """

        :param workspace_api_domain:
        :param api_key:
        :param kwargs:
        """
        self.auth_code = api_key
        self.headers = self._set_headers()
        self.workspace_api_domain = workspace_api_domain

    def get(self, query=''):
        """

        :param query:
        :return:
        """
        url = self._make_url(query)
        response_data, status_code = self._request_http(url)
        data = {}
        if response_data:
            try:
                data = json.loads(response_data)
            except Exception:
                return {}, status_code
        return data, status_code

    def post(self, data=None):
        """

        :param data:
        :return:
        """
        url = self._make_url_with_data(data=data, method='POST')
        response_data, status_code = self._request_http(url)
        data = {}
        if response_data:
            try:
                data = json.loads(response_data)
            except Exception:
                return {}, status_code
        return data, status_code

    def put(self, data):
        """

        :param data:
        :return:
        """
        url = self._make_url_with_data(data=data, method='PUT')
        response_data, status_code = self._request_http(url)
        if response_data:
            try:
                data = json.loads(response_data)
            except Exception:
                return {}, status_code
        return data, status_code

    def delete(self, data):
        """

        :param data:
        :return:
        """
        url = self._make_url_with_data(data=data, method='DELETE')
        response_data, status_code = self._request_http(url)
        if response_data:
            try:
                data = json.loads(response_data)
            except Exception:
                return {}, status_code
        return data, status_code

    def _make_url(self, query):
        """

        :param query:
        :return:
        """
        return Request('{}{}'.format(self.url, query), headers=self.headers)

    def _make_url_with_data(self, method, data=None):
        req_data = None
        if data:
            req_data = json.dumps(data).encode('utf8')
        try:
            request = Request(self.url, data=req_data, headers=self.headers, method=method)
        except TypeError:
            request = Request(self.url, data=req_data, headers=self.headers)
            request.get_method = lambda: method

        return request

    def _set_headers(self):
        """

        :return:
        """
        headers = {'Content-Type': 'application/json'}
        if self.auth_code:
            auth = {'Authorization': self.auth_code}
            headers.update(auth)

        return headers

    def _request_http(self, url):
        """

        :param url:
        :return:
        """
        try:
            response = urlopen(url)
            try:
                status_code = response.status
            except AttributeError:
                status_code = response.code

            response_data = response.read().decode('utf-8')
        except HTTPError as e:
            try:
                status_code = e.status
            except AttributeError:
                status_code = e.code

            response_data = e.read().decode('utf-8')

        # if status_code == 400:
        #     raise ServerException(ServerBaseErrors.ERR_UIZA_BAD_REQUEST)
        # elif status_code == 401:
        #     raise ServerException(ServerBaseErrors.ERR_UIZA_UNAUTHORIZED)
        # elif status_code == 404:
        #     raise ServerException(ServerBaseErrors.ERR_UIZA_NOT_FOUND)
        # elif status_code == 422:
        #     raise ServerException(ServerBaseErrors.ERR_UIZA_UNPROCESSABLE)
        # elif status_code == 500:
        #     raise ServerException(ServerBaseErrors.ERR_UIZA_INTERNAL_SERVER_ERROR)
        # elif status_code == 503:
        #     raise ServerException(ServerBaseErrors.ERR_UIZA_SERVICE_UNAVAILABLE)
        # elif re.match(r'^4[0-9]{2}$', str(status_code)):
        #     raise ServerException(ServerBaseErrors.ERR_UIZA_CLIENT_ERROR)
        # elif re.match(r'^5[0-9]{2}$', str(status_code)):
        #     raise ServerException(ServerBaseErrors.ERR_UIZA_SERVER_ERROR)

        return response_data, status_code
