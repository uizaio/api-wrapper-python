import unittest
import mock
import uiza

from uiza.api_resources.livestreaming import LiveStreaming
from uiza.exceptions import (
    BadRequestError,
    UnauthorizedError,
    NotFoundError,
    UnprocessableError,
    InternalServerError,
    ServiceUnavailableError,
    ClientError,
    ServerError,
    ClientException
)


class TestLiveStreamingBaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestLiveStreamingBaseTestCase, self).__init__(*args, **kwargs)
        uiza.workspace_api_domain = 'test domain'
        uiza.api_key = 'test api key'
        self.live_streaming_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.live_streaming_data_create = {
            'name': 'test event python 1',
            'mode': 'push',
            'encode': 1,
            'dvr': 1,
            'linkStream': [
                'https://playlist.m3u8'
            ],
            'resourceMode': 'single'
        }
        self.live_streaming_data_update = {
            'id': self.live_streaming_id,
            'name': 'test event python 2',
            'mode': 'push',
            'encode': 1,
            'dvr': 1,
            'linkStream': [
                'https://playlist.m3u8'
            ],
            'resourceMode': 'single'
        }


class TestCreateLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().create(**self.live_streaming_data_create)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().create(**self.live_streaming_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().create(**self.live_streaming_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().create(**self.live_streaming_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().create(**self.live_streaming_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().create(**self.live_streaming_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().create(**self.live_streaming_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().create(**self.live_streaming_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().create(**self.live_streaming_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestRetrieveLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().retrieve(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_live_streaming_invalid_with_not_live_streaming_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            LiveStreaming().retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestUpdateLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().update(**self.live_streaming_data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().update(**self.live_streaming_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().update(**self.live_streaming_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().update(**self.live_streaming_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().update(**self.live_streaming_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().update(**self.live_streaming_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().update(**self.live_streaming_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().update(**self.live_streaming_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().update(**self.live_streaming_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestListLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_live_streaming_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            LiveStreaming().list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')


class TestDeleteLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_delete_live_streaming_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            LiveStreaming().delete(id='test id')
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')


class TestStartFeedLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().start_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_start_feed_live_streaming_invalid_with_not_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            LiveStreaming().start_feed()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestStopFeedLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().stop_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_stop_feed_live_streaming_invalid_with_not_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            LiveStreaming().stop_feed()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestGetViewFeedLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().get_view_feed(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_view_feed_live_streaming_invalid_with_not_live_streaming_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            LiveStreaming().get_view_feed()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestConvertIntoVODLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().convert_into_vod(id=self.live_streaming_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_convert_into_vod_live_streaming_invalid_with_not_live_streaming_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            LiveStreaming().convert_into_vod()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestListRecordedLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().list_recorded()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().list_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().list_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().list_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().list_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().list_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().list_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().list_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_recorded_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().list_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestDeleteRecordedLiveStreaming(TestLiveStreamingBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            LiveStreaming().delete_recorded(id='Test id recorded')
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_recorded_live_streaming_invalid_with_not_live_streaming_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            LiveStreaming().delete_recorded()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')
