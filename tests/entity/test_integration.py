import unittest
import mock

from uiza.api_resources.base.connections import Connection
from uiza.api_resources.entity.entity import Entity


class TestIntegration(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIntegration, self).__init__(*args, **kwargs)
        self.entity_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.entity_data = {
            "name": "Sample Video Python1",
            "url": "https://example.com/video.mp4",
            "inputType": "http",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'\''s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "shortDescription": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
            "poster": "https://example.com/picture001.jpeg",
            "thumbnail": "https://example.com/picture002.jpeg",
            "extendMetadata": {
                "movie_category": "action",
                "imdb_score": 8.8,
                "published_year": "2018"
            },
            "embedMetadata": {
                "artist": "John Doe",
                "album": "Album sample",
                "genre": "Pop"
            },
            "metadataIds": ["16a9e425-efb0-4360-bd92-8d49da111e88"]
        }
        connection = Connection(workspace_api_domain='example.com', api_key='abcd1234')
        self.entity = Entity(connection=connection)

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.entity.create(**self.entity_data)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.entity.retrieve(id=self.entity_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            self.entity.retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.entity.list()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data_update = dict(id=self.entity_id, name='Test update')
        data = self.entity.update(**data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.entity.delete(id=self.entity_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_entity_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.entity.delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.entity.search(keyword='test_keyword')
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.entity.publish(id=self.entity_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.entity.get_status_publish_entity(id=self.entity_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_entity_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.entity.get_status_publish_entity()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.entity.get_aws_upload_key()
        self.assertEqual(data[1], 200)
