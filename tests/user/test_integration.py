import unittest
import mock

from uiza.api_resources.base.connections import Connection
from uiza.api_resources.user.user import User


class TestIntegration(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIntegration, self).__init__(*args, **kwargs)
        self.user_id = '37d6706e-be91-463e-b3b3-b69451dd4752'
        self.user_data = {
            "status":1,
            "username":"user_test",
            "email":"user_test@uiza.io",
            "fullname":"User Test",
            "avatar":"https://exemple.com/avatar.jpeg",
            "dob":"05/15/2018",
            "gender":0,
            "password":"FMpsr<4[dGPu?B#u",
            "isAdmin":1
        }
        connection = Connection(workspace_api_domain='example.com', api_key='abcd1234')
        self.user = User(connection=connection)

    @mock.patch('uiza.Connection._request_http')
    def test_create_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.user.create(**self.user_data)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.user.retrieve(id=self.user_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_user_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(Exception) as context:
            self.user.retrieve()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_list_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.user.list()
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_update_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data_update = dict(id=self.user_id, name='Test update')
        data = self.user.update(**data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.user.delete(id=self.user_id)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_delete_user_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.user.delete()
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_update_password_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data_update = dict(id=self.user_id, newPassword='New password', oldPassword='Old password')
        data = self.user.update_password(**data_update)
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_logout_user_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data_update = dict(id=self.user_id, newPassword='New password', oldPassword='Old password')
        data = self.user.logout()
        self.assertEqual(data[1], 200)
