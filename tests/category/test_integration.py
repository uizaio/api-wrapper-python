import unittest
import mock

from uiza import Connection
from uiza.api_resources.category import Category


class TestIntegration(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIntegration, self).__init__(*args, **kwargs)
        self.category_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.category_data = {
            "name":"Folder sample python 3",
            "type":"tag",
            "description":"Folder description",
            "orderNumber":1,
            "icon":"https://exemple.com/icon.png"
        }
        connection = Connection(workspace_api_domain='example.com', api_key='abcd1234')
        self.category = Category(connection=connection)
        self.category_relation_data = {
            "entityId": 'eb578480-6311-4534-b00e-7c7ffbce8283',
            "metadataIds": ["29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0"]
        }

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.category.create(**self.category_data)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.category.retrieve(id=self.category_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            self.category.retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.category.list()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data_update = dict(id=self.category_id, name='Test update')
        data = self.category.update(**data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.category.delete(id=self.category_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.category.delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.category.create_relation(**self.category_relation_data)
        self.assertEqual(data[1], 200)


    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.category.delete_relation(**self.category_relation_data)
        self.assertEqual(data[1], 200)
