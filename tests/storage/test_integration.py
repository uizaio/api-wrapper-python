import unittest
import mock
import uiza

from uiza.api_resources.storage import Storage
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


class TestStorageBaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestStorageBaseTestCase, self).__init__(*args, **kwargs)
        uiza.workspace_api_domain = 'test domain'
        uiza.authorization = 'test api key'
        self.storage_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.storage_data_create = {
            'name': 'FTP Uiza test 4',
            'description': 'FTP of Uiza, use for transcode',
            'storageType': 'ftp',
            'host': 'ftp-example.uiza.io'
        }

        self.storage_data_update = {
            'id': '37d6706e-be91-463e-b3b3-b69451dd4752',
            'name': 'FTP Uiza test 5',
            'description': 'FTP of Uiza, use for transcode',
            'storageType': 'ftp',
            'host': 'ftp-example.uiza.io'
        }


class TestAddStorage(TestStorageBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Storage().add(**self.storage_data_create)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Storage().add(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Storage().add(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Storage().add(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Storage().add(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Storage().add(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Storage().add(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Storage().add(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_add_storage_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Storage().add(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestRetrieveStorage(TestStorageBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Storage().retrieve(id=self.storage_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Storage().retrieve(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Storage().retrieve(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Storage().retrieve(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Storage().retrieve(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Storage().retrieve(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Storage().retrieve(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Storage().retrieve(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Storage().retrieve(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_storage_invalid_with_not_storage_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            Storage().retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestUpdateStorage(TestStorageBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Storage().update(**self.storage_data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Storage().update(**self.storage_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Storage().update(**self.storage_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Storage().update(**self.storage_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Storage().update(**self.storage_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Storage().update(**self.storage_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Storage().update(**self.storage_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Storage().update(**self.storage_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Storage().update(**self.storage_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestRemoveStorage(TestStorageBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Storage().remove(id=self.storage_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Storage().remove(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Storage().remove(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Storage().remove(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Storage().remove(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Storage().remove(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Storage().remove(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Storage().remove(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Storage().remove(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_remove_storage_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Storage().remove()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestListStorage(TestStorageBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_storage_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Storage().list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')


class TestCreateStorage(TestStorageBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_storage_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Storage().create(**self.storage_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')

class TestDeleteStorage(TestStorageBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_delete_storage_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Storage().delete(id=self.storage_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')
