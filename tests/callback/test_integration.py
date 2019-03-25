import unittest
import mock
import uiza

from uiza.api_resources.callback import Callback
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


class TestCallbackBaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCallbackBaseTestCase, self).__init__(*args, **kwargs)
        uiza.workspace_api_domain = 'test domain'
        uiza.authorization = 'test api key'
        self.callback_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.callback_data_create = {
            "url": "https://callback-url-python.uiza.co",
            "method": "GET"
        }
        self.callback_data_update = dict(id=self.callback_id, name='Test update')


class TestCreateCallback(TestCallbackBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Callback().create(**self.callback_data_create)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Callback().create(**self.callback_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Callback().create(**self.callback_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Callback().create(**self.callback_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Callback().create(**self.callback_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Callback().create(**self.callback_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Callback().create(**self.callback_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Callback().create(**self.callback_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_callback_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Callback().create(**self.callback_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestRetrieveCallback(TestCallbackBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Callback().retrieve(id=self.callback_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Callback().retrieve(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Callback().retrieve(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Callback().retrieve(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Callback().retrieve(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Callback().retrieve(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Callback().retrieve(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Callback().retrieve(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Callback().retrieve(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_callback_invalid_with_not_callback_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            Callback().retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestUpdateCallback(TestCallbackBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Callback().update(**self.callback_data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Callback().update(**self.callback_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Callback().update(**self.callback_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Callback().update(**self.callback_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Callback().update(**self.callback_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Callback().update(**self.callback_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Callback().update(**self.callback_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Callback().update(**self.callback_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_callback_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Callback().update(**self.callback_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestDeleteCallback(TestCallbackBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Callback().delete(id=self.callback_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Callback().delete(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Callback().delete(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Callback().delete(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Callback().delete(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Callback().delete(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Callback().delete(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Callback().delete(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Callback().delete(id=self.callback_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_callback_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Callback().delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestListCallback(TestCallbackBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_storage_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Callback().list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')
