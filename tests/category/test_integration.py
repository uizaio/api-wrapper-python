import unittest
import mock
import uiza

from uiza.api_resources.category import Category
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


class TestCategoryBaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCategoryBaseTestCase, self).__init__(*args, **kwargs)
        uiza.workspace_api_domain = 'test domain'
        uiza.authorization = 'test api key'
        self.category_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.category_data_create = {
            'name':'Folder sample python 3',
            'type':'tag',
            'description':'Folder description',
            'orderNumber':1,
            'icon':'https://exemple.com/icon.png'
        }
        self.category_data_update = dict(id=self.category_id, name='Test update')


class TestCreateCategory(TestCategoryBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Category().create(**self.category_data_create)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Category().create(**self.category_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Category().create(**self.category_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Category().create(**self.category_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Category().create(**self.category_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Category().create(**self.category_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Category().create(**self.category_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Category().create(**self.category_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_category_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Category().create(**self.category_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestRetrieveCategory(TestCategoryBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Category().retrieve(id=self.category_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Category().retrieve(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Category().retrieve(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Category().retrieve(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Category().retrieve(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Category().retrieve(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Category().retrieve(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Category().retrieve(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Category().retrieve(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_category_invalid_with_not_category_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            Category().retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestUpdateCategory(TestCategoryBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Category().update(**self.category_data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Category().update(**self.category_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Category().update(**self.category_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Category().update(**self.category_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Category().update(**self.category_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Category().update(**self.category_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Category().update(**self.category_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Category().update(**self.category_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_category_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Category().update(**self.category_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestDeleteCategory(TestCategoryBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Category().delete(id=self.category_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Category().delete(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Category().delete(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Category().delete(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Category().delete(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Category().delete(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Category().delete(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Category().delete(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Category().delete(id=self.category_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_category_invalid_not_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Category().delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestListCategory(TestCategoryBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Category().list()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Category().list()
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Category().list()
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Category().list()
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Category().list()
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Category().list()
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Category().list()
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Category().list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_category_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Category().list()
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestCreateRelationCategory(TestCategoryBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Category().create_relation(
            entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
            metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_not_entity_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Category().create_relation(
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_relation_category_invalid_not_metadata_ids(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Category().create_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestDeleteRelationCategory(TestCategoryBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Category().delete_relation(
            entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
            metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_not_entity_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Category().delete_relation(
                metadata_ids=['29f7b6ba-e2a7-4d4b-8026-30828d0a1bb0']
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_relation_category_invalid_not_metadata_ids(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Category().delete_relation(
                entity_id='eb578480-6311-4534-b00e-7c7ffbce8283',
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')
