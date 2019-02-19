import unittest
import mock

from uiza import Connection
from uiza.api_resources.storage import Storage
from uiza.exceptions import ClientException


class TestIntegration(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIntegration, self).__init__(*args, **kwargs)
        self.storage_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.storage_data = {
            "name":"FTP Uiza test 4",
            "description":"FTP of Uiza, use for transcode",
            "storageType":"ftp",
            "host":"ftp-example.uiza.io"
        }
        connection = Connection(workspace_api_domain='example.com', api_key='abcd1234')
        self.storage = Storage(connection=connection)

    @mock.patch('uiza.Connection._request_http')
    def test_create_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.storage.create(**self.storage_data)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.storage.retrieve(id=self.storage_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            self.storage.retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data_update = dict(id=self.storage_id, name='Test update')
        data = self.storage.update(**data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.storage.delete(id=self.storage_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_storage_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.storage.delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_storage_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.storage.list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')
