import unittest
from nbptdd.src.api_client import ApiClient


class ApiClientTest(unittest.TestCase):
    

    def setUp(self) -> None:
        self.api_client = ApiClient()
        self.CORRECT_URI = "http://api.nbp.pl/api/exchangerates/tables/a?format=json/"
        self.WRONG_URI = "http://api.nbp.pl/a?format=json/"


    def test_http_get_correct_uri_status(self) -> None:
        response_data = self.api_client.get(self.CORRECT_URI)
        self.assertEqual(response_data, 200)


    def test_http_get_wrong_uri_status(self) -> None:
        response_data = self.api_client.get(self.WRONG_URI)
        self.assertNotEqual(response_data, 200)


    def test_http_get_dict_success(self) -> None:
        self.api_client.get(self.CORRECT_URI)
        dict_data = self.api_client.getDictData()
        self.assertIsInstance(dict_data, dict)


    def test_http_get_dict_failure(self) -> None:
        dict_data = self.api_client.getDictData()
        self.assertEqual(dict_data, None)
