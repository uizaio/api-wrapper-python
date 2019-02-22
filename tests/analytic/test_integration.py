import unittest
import mock

from uiza import Connection
from uiza.api_resources.analytic import Analytic
from uiza.exceptions import ClientException


class TestIntegration(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIntegration, self).__init__(*args, **kwargs)
        connection = Connection(workspace_api_domain='example.com', api_key='abcd1234')
        self.analytic = Analytic()

    @mock.patch('uiza.Connection._request_http')
    def test_create_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.analytic.create()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')

    @mock.patch('uiza.Connection._request_http')
    def test_retrieve_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.analytic.retrieve(id='test id')
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')

    @mock.patch('uiza.Connection._request_http')
    def test_update_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.analytic.update()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')

    @mock.patch('uiza.Connection._request_http')
    def test_delete_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.analytic.delete(id='test id')
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')

    @mock.patch('uiza.Connection._request_http')
    def test_list_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            self.analytic.list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')

    @mock.patch('uiza.Connection._request_http')
    def test_total_line_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.analytic.get_total_line(
            start_date='2018-11-01 20:00',
            end_date='2019-11-02 20:00',
            metric='rebuffer_count'
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_total_line_invalid_with_not_start_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.analytic.get_total_line(
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


    @mock.patch('uiza.Connection._request_http')
    def test_total_line_invalid_with_not_end_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.analytic.get_total_line(
                start_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


    @mock.patch('uiza.Connection._request_http')
    def test_total_line_invalid_with_not_metric(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.analytic.get_total_line(
                end_date='2019-11-02 20:00',
                start_date='2019-11-02 20:00'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.analytic.get_type(
            start_date='2018-11-01 20:00',
            end_date='2019-11-02 20:00',
            type_filter='country'
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_not_start_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.analytic.get_type(
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_not_end_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.analytic.get_type(
                start_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_not_metric(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.analytic.get_type(
                end_date='2019-11-02 20:00',
                start_date='2019-11-02 20:00'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = self.analytic.get_line(
            start_date='2018-11-01 20:00',
            end_date='2019-11-02 20:00',
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_not_start_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.analytic.get_line(
                end_date='2019-11-02 20:00'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_not_end_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            self.analytic.get_line(
                start_date='2019-11-02 20:00'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')
