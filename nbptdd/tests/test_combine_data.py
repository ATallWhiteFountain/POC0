import unittest
from nbptdd.src.combine_data import CombineData


class CombineDataTest(unittest.TestCase):


    def setUp(self) -> None:
        self.combine_data = CombineData()
        self.SOURCE_DICT_A = {'table': 'A', 'no': '233/A/NBP/2022', 'effectiveDate': '2022-12-02', 'rates': [{'currency': 'bat (Tajlandia)', 'code': 'THB', 'mid': 0.128}, {'currency': 'dolar amerykański', 'code': 'USD', 'mid': 4.4492}, {'currency': 'dolar australijski', 'code': 'AUD', 'mid': 3.0352}, {'currency': 'dolar Hongkongu', 'code': 'HKD', 'mid': 0.5719}, {'currency': 'dolar kanadyjski', 'code': 'CAD', 'mid': 3.3118}]}
        self.SOURCE_DICT_B = {'table': 'B', 'no': '048/B/NBP/2022', 'effectiveDate': '2022-11-30', 'rates': [{'currency': 'afgani (Afganistan)', 'code': 'AFN', 'mid': 0.050971}, {'currency': 'ariary (Madagaskar)', 'code': 'MGA', 'mid': 0.001032}, {'currency': 'balboa (Panama)', 'code': 'PAB', 'mid': 4.5066}, {'currency': 'birr etiopski', 'code': 'ETB', 'mid': 0.0842}, {'currency': 'dinar algierski', 'code': 'DZD', 'mid': 0.032478}]}
        self.desired_headers = ['table', 'no', 'effectiveDate', 'currency', 'code', 'mid']


    def test_combine_data_get_list_of_dicts_dict_provided(self) -> None:
        list_of_dicts = self.combine_data.get_list_of_dicts(self.SOURCE_DICT_A)
        headers = [list(item.keys()) for item in list_of_dicts]

        self.assertEqual(len(list_of_dicts), 5)
        self.assertCountEqual(headers, 5*[self.desired_headers])


    def test_combine_data_get_list_of_dicts_no_dict(self) -> None:
        list_of_dicts = self.combine_data.get_list_of_dicts("Not a dictionary")
        self.assertIsNone(list_of_dicts)


    def test_combine_data_union_dicts_two_lists_of_dicts(self) -> None:
        list_a = self.combine_data.get_list_of_dicts(self.SOURCE_DICT_A)
        list_b = self.combine_data.get_list_of_dicts(self.SOURCE_DICT_B)
        product_list = self.combine_data.union_dicts(list_a, list_b)

        types = [isinstance(item, dict) for item in product_list]

        self.assertEqual(len(product_list), 10)
        self.assertCountEqual(types, 10*[True])


    def test_combine_data_union_dicts_one_list_of_dicts(self) -> None:
        list_a = self.combine_data.get_list_of_dicts(self.SOURCE_DICT_A)
        dict_b = self.SOURCE_DICT_B
        product_list = self.combine_data.union_dicts(list_a, dict_b)

        self.assertIsNone(product_list)


    def test_combine_data_union_dicts_no_list_of_dicts(self) -> None:
        dict_a = self.SOURCE_DICT_A
        dict_b = self.SOURCE_DICT_B
        product_list = self.combine_data.union_dicts(dict_a, dict_b)

        self.assertIsNone(product_list)
