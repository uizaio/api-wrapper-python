import unittest
import mock
import uiza

from uiza.api_resources.entity import Entity
from uiza.exceptions import (
    BadRequestError,
    UnauthorizedError,
    NotFoundError,
    UnprocessableError,
    InternalServerError,
    ServiceUnavailableError,
    ClientError,
    ServerError
)


class TestEntityBaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEntityBaseTestCase, self).__init__(*args, **kwargs)
        uiza.workspace_api_domain = 'test domain'
        uiza.authorization = 'test api key'
        self.entity_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.entity_data_create = {
            "name": "Sample Video Python",
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
        self.entity_data_update = dict(id=self.entity_id, name='Test update')


class TestCreateEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().create(**self.entity_data_create)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().create(**self.entity_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().create(**self.entity_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().create(**self.entity_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().create(**self.entity_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().create(**self.entity_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().create(**self.entity_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().create(**self.entity_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_entity_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().create(**self.entity_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestRetrieveEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().retrieve(id=self.entity_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().retrieve(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().retrieve(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().retrieve(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().retrieve(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().retrieve(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().retrieve(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().retrieve(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().retrieve(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_entity_invalid_with_not_entity_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            Entity().retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestUpdateEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().update(**self.entity_data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().update(**self.entity_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().update(**self.entity_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().update(**self.entity_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().update(**self.entity_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().update(**self.entity_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().update(**self.entity_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().update(**self.entity_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_storage_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().update(**self.entity_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestDeleteEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().delete(id=self.entity_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().delete(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().delete(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().delete(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().delete(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().delete(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().delete(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().delete(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().delete(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_not_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Entity().delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestListEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().list()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().list()
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().list()
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().list()
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().list()
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().list()
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().list()
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_entity_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().list()
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestSearchEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().search(keyword='Test keyword')
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().search(keyword='Test keyword')
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().search(keyword='Test keyword')
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().search(keyword='Test keyword')
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().search(keyword='Test keyword')
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().search(keyword='Test keyword')
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().search(keyword='Test keyword')
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().search(keyword='Test keyword')
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().search(keyword='Test keyword')
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_search_entity_invalid_with_not_keyword(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Entity().search()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestPublishEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().publish(self.entity_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().publish(self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().publish(self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().publish(self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().publish(self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().publish(self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().publish(self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().publish(self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().publish(self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_publish_entity_invalid_with_not_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Entity().publish()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestGetPublishStatusEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().get_status_publish(id=self.entity_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().get_status_publish(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().get_status_publish(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().get_status_publish(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().get_status_publish(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().get_status_publish(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().get_status_publish(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().get_status_publish(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().get_status_publish(id=self.entity_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_publish_status_invalid_with_not_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            Entity().get_status_publish()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestGetAWSUploadKeyEntity(TestEntityBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Entity().get_aws_upload_key()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Entity().get_aws_upload_key()
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Entity().get_aws_upload_key()
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Entity().get_aws_upload_key()
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Entity().get_aws_upload_key()
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Entity().get_aws_upload_key()
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Entity().get_aws_upload_key()
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Entity().get_aws_upload_key()
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_aws_upload_key_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Entity().get_aws_upload_key()
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')
