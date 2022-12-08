import unittest
from nbptdd.src.api_client import ApiClient


class ApiClientTest(unittest.TestCase):
    

    def setUp(self) -> None:
        self.api_client = ApiClient()
        self.CORRECT_URI = "http://api.nbp.pl/api/exchangerates/tables/a?format=json/"
        self.XML_URI = "http://api.nbp.pl/api/exchangerates/tables/a?format=xml"
        self.WRONG_URI = "http://api.nbp.pl/a?format=json/"


    def test_http_get_correct_uri_status(self) -> None:
        response_data = self.api_client.get(self.CORRECT_URI)
        self.assertEqual(response_data, 200)


    def test_http_get_wrong_uri_status(self) -> None:
        response_data = self.api_client.get(self.WRONG_URI)
        self.assertNotEqual(response_data, 200)


    def test_http_get_json_dict_data_success(self) -> None:
        self.api_client.get(self.CORRECT_URI)
        dict_data = self.api_client.getJsonDictData()
        self.assertIsInstance(dict_data, dict)


    def test_http_get_json_dict_data_not_a_json_raises_exception(self) -> None:
        self.api_client.get(self.XML_URI)
        dict_data = self.api_client.getJsonDictData()
        self.assertIsNone(dict_data)
