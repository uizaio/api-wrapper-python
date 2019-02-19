import unittest
import mock

from uiza import Connection
from uiza.api_resources.livestreaming import LiveStreaming
from uiza.exceptions import ClientException


class TestIntegration(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIntegration, self).__init__(*args, **kwargs)
        self.livestream_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.livestream_data = {
            "name":"test event python 1",
            "mode":"push",
            "encode":1,
            "dvr":1,
            "linkStream":[
                "https://playlist.m3u8"
            ],
            "resourceMode":"single"
        }
        connection = Connection(workspace_api_domain='example.com', api_key='abcd1234')
        self.livestream = LiveStreaming(connection=connection)

    @mock.patch('uiza.Connection._request_http')
    def test_create_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.livestream.create(**self.livestream_data)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.livestream.retrieve(id=self.livestream_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_livestream_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            self.livestream.retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data_update = dict(id=self.livestream_id, name='Test update')
        data = self.livestream.update(**data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_list_livestream_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.livestream.list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_livestream_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.livestream.delete(id=self.livestream_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.livestream.start_feed(self.livestream_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_livestream_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.livestream.start_feed()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.livestream.stop_feed(self.livestream_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_livestream_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.livestream.stop_feed()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.livestream.get_view_feed(self.livestream_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_livestream_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.livestream.get_view_feed()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.livestream.convert_into_vod(self.livestream_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_livestream_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.livestream.convert_into_vod()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.livestream.delete_recorded(self.livestream_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_livestream_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.livestream.delete_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_livestream_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.livestream.list_recorded()
        self.assertEqual(data[1], 200)
