import re
import json

try:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import Request, urlopen
    from urllib2 import HTTPError

from uiza.exceptions import (
    BadRequestError,
    UnauthorizedError,
    NotFoundError,
    UnprocessableError,
    InternalServerError,
    ServiceUnavailableError,
    ClientError,
    ServerError,
    ServerBaseErrors
)


class ResponseObject(object):
    dict = None  # type: dict

    def __init__(self, d):
        self.dict = d
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [ResponseObject(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, ResponseObject(b) if isinstance(b, dict) else b)


class Connection(object):
    url = None

    def __init__(self, workspace_api_domain, api_key, **kwargs):
        """
        Handle the Uiza connection
        :param workspace_api_domain: workspace api domain of uiza account
        :param api_key: private key of uiza account
        :param kwargs:
        """
        self.auth_code = api_key
        self.headers = self._set_headers()
        self.workspace_api_domain = workspace_api_domain

    def get(self, query=''):
        """
        Handle request GET
        :param query: params of request GET
        :return: obj and status code after request
        """
        url = self._make_url(query)
        response_data, status_code = self._request_http(url)
        status_code = self._filter_error_status_code(status_code=status_code, response_data=response_data)
        data = {}
        if response_data:
            data = self._get_response_obj(response_data=response_data)
        return data, status_code

    def post(self, data=None):
        """
        Handle request POST
        :param data: data body of request POST
        :return:
        """
        url = self._make_url_with_data(data=data, method='POST')
        response_data, status_code = self._request_http(url)
        status_code = self._filter_error_status_code(status_code=status_code, response_data=response_data)
        data = {}
        if response_data:
            data = self._get_response_obj(response_data=response_data)
        return data, status_code

    def put(self, data):
        """
        Handle request PUT
        :param data: data body of request PUT
        :return: obj and status code after request
        """
        url = self._make_url_with_data(data=data, method='PUT')
        response_data, status_code = self._request_http(url)
        status_code = self._filter_error_status_code(status_code=status_code, response_data=response_data)
        if response_data:
            data = self._get_response_obj(response_data=response_data)
        return data, status_code

    def delete(self, data):
        """
        Handle request DELETE
        :param data: data body of request DELETE
        :return: obj and status code after request
        """
        url = self._make_url_with_data(data=data, method='DELETE')
        response_data, status_code = self._request_http(url)
        status_code = self._filter_error_status_code(status_code=status_code, response_data=response_data)
        data = {}
        if response_data:
            data = self._get_response_obj(response_data=response_data)
        return data, status_code

    def _make_url(self, query):
        """
        Make Request urllib/urllib2 with query
        :param query: query of method GET
        :return: Request object
        """
        return Request('{}{}'.format(self.url, query), headers=self.headers)

    def _make_url_with_data(self, method, data=None):
        """
        Make Request urllib/urllib2 with body data
        :param method: method of request. It include POST, PUT, DELETE
        :param data: boday data of request
        :return: Request object
        """
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
        Set header of request
        :return:
        """
        headers = {'Content-Type': 'application/json'}
        if self.auth_code:
            auth = {'Authorization': self.auth_code}
            headers.update(auth)

        return headers

    def _request_http(self, url):
        """
        Start request to Uiza server
        :param url: Request obj
        :return: string response, status code
        """
        message_error = None
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

        return response_data, status_code

    def _filter_error_status_code(self, status_code, response_data):
        """
        Filter error code if status code in [400, 401, 404, 422, 500, 503, 4xx, 5xx]
        :param status_code: status code
        :param response_data: response
        :return:
        """
        if status_code == 200:
            return status_code

        message_error = None
        response_obj = self._get_message_error(response_data)
        if response_obj:
            message_error = response_obj.get('message')

        if status_code == 400:
            if not message_error:
                message_error = ServerBaseErrors.ERR_UIZA_BAD_REQUEST
            raise BadRequestError(message_error)
        elif status_code == 401:
            if not message_error:
                message_error = ServerBaseErrors.ERR_UIZA_UNAUTHORIZED
            raise UnauthorizedError(message_error)
        elif status_code == 404:
            if not message_error:
                message_error = ServerBaseErrors.ERR_UIZA_NOT_FOUND
            raise NotFoundError(message_error)
        elif status_code == 422:
            if not message_error:
                message_error = ServerBaseErrors.ERR_UIZA_UNPROCESSABLE
            raise UnprocessableError(message_error)
        elif status_code == 500:
            if not message_error:
                message_error = ServerBaseErrors.ERR_UIZA_INTERNAL_SERVER_ERROR
            raise InternalServerError(message_error)
        elif status_code == 503:
            if not message_error:
                message_error = ServerBaseErrors.ERR_UIZA_SERVICE_UNAVAILABLE
            raise ServiceUnavailableError(message_error)
        elif re.match(r'^4[0-9]{2}$', str(status_code)):
            raise ClientError(ServerBaseErrors.ERR_UIZA_CLIENT_ERROR)
        elif re.match(r'^5[0-9]{2}$', str(status_code)):
            raise ServerError(ServerBaseErrors.ERR_UIZA_SERVER_ERROR)

        return status_code

    def _get_response_obj(self, response_data):
        """
        Convert from string to object of response
        :param response_data: string response
        :return: dict null, object or list object
        """
        try:
            response_dict = json.loads(response_data)
            data = response_dict.get('data')
            if not data:
                return {}

            if isinstance(data, dict):
                return ResponseObject(response_dict.get('data'))

            if isinstance(data, list):
                return [ResponseObject(item) for item in data]
        except Exception:
            return {}

    def _get_message_error(self, response_data):
        """
        Get message error from response data
        :param response_data: string response
        :return: dict
        """
        try:
            response_dict = json.loads(response_data)
            return response_dict
        except Exception:
            return {}
