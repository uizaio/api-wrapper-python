import unittest
import mock
import uiza

from uiza.api_resources.analytic import Analytic
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


class TestAnalyticBaseTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestAnalyticBaseTestCase, self).__init__(*args, **kwargs)
        uiza.workspace_api_domain = 'test domain'
        uiza.api_key = 'test api key'


class TestCreateAnalytic(TestAnalyticBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Analytic().create()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')


class TestRetrieveAnalytic(TestAnalyticBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_create_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Analytic().retrieve(id='test id')
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')


class TestUpdateAnalytic(TestAnalyticBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_update_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Analytic().update()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')


class TestDeleteAnalytic(TestAnalyticBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_delete_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Analytic().delete(id='test id')
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')


class TestListAnalytic(TestAnalyticBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_list_analytic_invalid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(ClientException) as context:
            Analytic().list()
        self.assertTrue(context.exception.__class__.__name__, 'ClientException')


class TestGetTotalLine(TestAnalyticBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Analytic().get_total_line(
            start_date='2018-11-01 20:00',
            end_date='2019-11-02 20:00',
            metric='rebuffer_count'
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Analytic().get_total_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Analytic().get_total_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Analytic().get_total_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Analytic().get_total_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Analytic().get_total_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Analytic().get_total_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Analytic().get_total_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Analytic().get_total_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_not_start_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_total_line(
                end_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_not_end_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_total_line(
                start_date='2019-11-02 20:00',
                metric='rebuffer_count'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_total_line_invalid_with_not_metric(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_total_line(
                end_date='2019-11-02 20:00',
                start_date='2019-11-02 20:00'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestGetType(TestAnalyticBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Analytic().get_type(
            start_date='2018-11-01 20:00',
            end_date='2019-11-02 20:00',
            type_filter='country'
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Analytic().get_type(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Analytic().get_type(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Analytic().get_type(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Analytic().get_type(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Analytic().get_type(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Analytic().get_type(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Analytic().get_type(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Analytic().get_type(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_not_start_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_type(
                end_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_not_end_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_type(
                start_date='2019-11-02 20:00',
                type_filter='country'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_type_invalid_with_not_type_filter(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_type(
                end_date='2019-11-02 20:00',
                start_date='2019-11-02 20:00'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')


class TestGetLine(TestAnalyticBaseTestCase):

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_valid(self, mock_request_http):
        mock_request_http.return_value = True, 200
        data = Analytic().get_line(
            start_date='2018-11-01 20:00',
            end_date='2019-11-02 20:00',
            type='video_startup_time'
        )
        self.assertEqual(data[1], 200)

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_status_code_400(self, mock_request_http):
        mock_request_http.return_value = True, 400
        with self.assertRaises(BadRequestError) as context:
            Analytic().get_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'BadRequestError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_status_code_401(self, mock_request_http):
        mock_request_http.return_value = True, 401
        with self.assertRaises(UnauthorizedError) as context:
            Analytic().get_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnauthorizedError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_status_code_404(self, mock_request_http):
        mock_request_http.return_value = True, 404
        with self.assertRaises(NotFoundError) as context:
            Analytic().get_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'NotFoundError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_status_code_422(self, mock_request_http):
        mock_request_http.return_value = True, 422
        with self.assertRaises(UnprocessableError) as context:
            Analytic().get_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'UnprocessableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_status_code_500(self, mock_request_http):
        mock_request_http.return_value = True, 500
        with self.assertRaises(InternalServerError) as context:
            Analytic().get_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'InternalServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_status_code_503(self, mock_request_http):
        mock_request_http.return_value = True, 503
        with self.assertRaises(ServiceUnavailableError) as context:
            Analytic().get_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServiceUnavailableError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_status_code_4xx(self, mock_request_http):
        mock_request_http.return_value = True, 412
        with self.assertRaises(ClientError) as context:
            Analytic().get_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ClientError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_status_code_5xx(self, mock_request_http):
        mock_request_http.return_value = True, 512
        with self.assertRaises(ServerError) as context:
            Analytic().get_line(
                start_date='2018-11-01 20:00',
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'ServerError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_not_start_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_line(
                end_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_not_end_date(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_line(
                start_date='2019-11-02 20:00',
                type='video_startup_time'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')

    @mock.patch('uiza.Connection._request_http')
    def test_get_line_invalid_with_not_type(self, mock_request_http):
        mock_request_http.return_value = True, 200
        with self.assertRaises(TypeError) as context:
            Analytic().get_line(
                start_date='2019-11-02 20:00',
                end_date='2019-11-02 20:00'
            )
        self.assertTrue(context.exception.__class__.__name__, 'TypeError')
