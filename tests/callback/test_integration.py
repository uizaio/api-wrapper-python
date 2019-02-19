import unittest
import mock

from uiza import Connection
from uiza.api_resources.callback import Callback
from uiza.exceptions import ClientException


class TestIntegration(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIntegration, self).__init__(*args, **kwargs)
        self.callback_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.callback_data = {
            "url":"https://callback-url-python.uiza.co",
            "method":"GET"
        }
        connection = Connection(workspace_api_domain='example.com', api_key='abcd1234')
        self.callback = Callback(connection=connection)

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.callback.create(**self.callback_data)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.callback.retrieve(id=self.callback_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            self.callback.retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data_update = dict(id=self.callback_id, name='Test update')
        data = self.callback.update(**data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.callback.delete(id=self.callback_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.callback.delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_callback_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.callback.list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')
