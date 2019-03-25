import unittest
import mock
import uiza

from uiza.api_resources.user import User
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


class TestUserBaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestUserBaseTestCase, self).__init__(*args, **kwargs)
        uiza.workspace_api_domain = 'test domain'
        uiza.authorization = 'test api key'
        self.user_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.user_data_create = {
            'status': 1,
            'username': 'user_test',
            'email': 'user_test@uiza.io',
            'fullname': 'User Test',
            'avatar': 'https://exemple.com/avatar.jpeg',
            'dob': '05/15/2018',
            'gender': 0,
            'password': 'FMpsr<4[dGPu?B#u',
            'isAdmin': 1
        }
        self.user_data_update = dict(id=self.user_id, name='Test update')


class TestCreateUser(TestUserBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = User().create(**self.user_data_create)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            User().create(**self.user_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            User().create(**self.user_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            User().create(**self.user_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            User().create(**self.user_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            User().create(**self.user_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            User().create(**self.user_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            User().create(**self.user_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            User().create(**self.user_data_create)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestListUser(TestUserBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = User().list()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            User().list()
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            User().list()
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            User().list()
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            User().list()
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            User().list()
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            User().list()
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            User().list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            User().list()
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestRetrieveUser(TestUserBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = User().retrieve(id=self.user_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            User().retrieve(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            User().retrieve(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            User().retrieve(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            User().retrieve(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            User().retrieve(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            User().retrieve(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            User().retrieve(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            User().retrieve(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid_with_not_user_id(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            User().retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestUpdateUser(TestUserBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = User().update(**self.user_data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            User().update(**self.user_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            User().update(**self.user_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            User().update(**self.user_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            User().update(**self.user_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            User().update(**self.user_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            User().update(**self.user_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            User().update(**self.user_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            User().update(**self.user_data_update)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestDeleteUser(TestUserBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = User().delete(id=self.user_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            User().delete(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            User().delete(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            User().delete(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            User().delete(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            User().delete(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            User().delete(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            User().delete(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            User().delete(id=self.user_id)
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            User().delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestUpdatePasswordUser(TestUserBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = User().change_password(
            id = self.user_id,
            new_password='New password',
            old_password='Old password'
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            User().change_password(
                id=self.user_id,
                new_password='New password',
                old_password='Old password'
            )
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            User().change_password(
                id=self.user_id,
                new_password='New password',
                old_password='Old password'
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            User().change_password(
                id=self.user_id,
                new_password='New password',
                old_password='Old password'
            )
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            User().change_password(
                id=self.user_id,
                new_password='New password',
                old_password='Old password'
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            User().change_password(
                id=self.user_id,
                new_password='New password',
                old_password='Old password'
            )
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            User().change_password(
                id=self.user_id,
                new_password='New password',
                old_password='Old password'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            User().change_password(
                id=self.user_id,
                new_password='New password',
                old_password='Old password'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            User().change_password(
                id=self.user_id,
                new_password='New password',
                old_password='Old password'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')


class TestLogoutUser(TestUserBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = User().logout()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            User().logout()
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            User().logout()
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            User().logout()
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            User().logout()
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            User().logout()
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            User().logout()
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            User().logout()
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            User().logout()
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')
