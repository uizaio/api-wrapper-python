import json
import urllib.request
import urllib.error
from typing import Optional

from typing import Any


class Connection(object):
    url = None

    def __init__(self, workspace_api_domain: str,
                 api_key: str, **kwargs):
        self.auth_code = api_key
        self.headers = self._set_headers()
        self.workspace_api_domain = workspace_api_domain

    def get(self, query: str = '') -> Any:
        url = self._make_url(query)
        response_data = self._request_http(url)
        data = {}
        if response_data:
            try:
                data = json.loads(response_data)
            except json.decoder.JSONDecodeError:
                return {}
        return data

    def post(self, data: Optional[dict] = None) -> Any:
        url = self._make_url_with_data(data=data)
        response_data = self._request_http(url)
        data = {}
        if response_data:
            try:
                data = json.loads(response_data)
            except json.decoder.JSONDecodeError:
                return {}
        return data

    def put(self, id: str, data: Optional[dict] = None) -> Any:
        url = self._make_url_with_data(id=id, data=data)
        response_data = self._request_http(url)
        if response_data:
            try:
                data = json.loads(response_data)
            except json.decoder.JSONDecodeError:
                return {}
        return data

    def delete(self, data: dict) -> Any:
        url = self._make_url_with_data(data=data)
        response_data = self._request_http(url)
        if response_data:
            try:
                data = json.loads(response_data)
            except json.decoder.JSONDecodeError:
                return {}
        return data

    def _make_url(self, query) -> urllib.request.Request:
        return urllib.request.Request('{}{}'.format(self.url, query))

    def _make_url_with_data(self, id: Optional[str] = None, data: Optional[dict] = None) -> urllib.request.Request:
        req_data = json.dumps(data).encode('utf8')

        if not id and data and ('id' not in data.keys()):
            url = urllib.request.Request(self.url, data=req_data, headers=self.headers, method='POST')
        elif id and data:
            url = urllib.request.Request(self.url, data=req_data, headers=self.headers, method='PUT')
        else:
            url = urllib.request.Request(self.url, data=req_data, headers=self.headers, method='DELETE')

        return url

    def _set_headers(self) -> dict:
        headers = {'Content-Type': 'application/json'}
        if self.auth_code:
            auth = {'Authorization': self.auth_code}
            headers.update(auth)

        return headers

    def _request_http(self, url: urllib.request.Request) -> Any:
        try:
            response = urllib.request.urlopen(url)
            if response.status == 200:
                pass
            elif response.status == 400:
                raise ValueError('Bad Request')
            elif response.status == 401:
                raise ValueError('Unauthorized')
            elif response.status == 404:
                raise ValueError('Not found')
            elif response.status == 422:
                raise ValueError('Unprocessable')
            elif response.status == 500:
                raise ValueError('Internal Server Error')
            elif response.status == 503:
                raise ValueError('Service Unavailable')

            response_data = response.read().decode('utf-8')

            return response_data

        except urllib.error.URLError as e:
            raise e
