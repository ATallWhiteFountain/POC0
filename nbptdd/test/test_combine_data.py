import unittest
import pandas as pd
from nbptdd.src.combine_data import CombineData


class CombineDataTest(unittest.TestCase):

    def setUp(self) -> None:

        self.combine_data = CombineData()

        self.SOURCE_DICT_A = {'table': 'A', 'no': '233/A/NBP/2022', 'effectiveDate': '2022-12-02', 'rates': [{'currency': 'bat (Tajlandia)', 'code': 'THB', 'mid': 0.128}, {'currency': 'dolar amerykański', 'code': 'USD', 'mid': 4.4492}, {'currency': 'dolar australijski', 'code': 'AUD', 'mid': 3.0352}, {'currency': 'dolar Hongkongu', 'code': 'HKD', 'mid': 0.5719}, {'currency': 'dolar kanadyjski', 'code': 'CAD', 'mid': 3.3118}]}

        self.SOURCE_DICT_B = {'table': 'B', 'no': '048/B/NBP/2022', 'effectiveDate': '2022-11-30', 'rates': [{'currency': 'afgani (Afganistan)', 'code': 'AFN', 'mid': 0.050971}, {'currency': 'ariary (Madagaskar)', 'code': 'MGA', 'mid': 0.001032}, {'currency': 'balboa (Panama)', 'code': 'PAB', 'mid': 4.5066}, {'currency': 'birr etiopski', 'code': 'ETB', 'mid': 0.0842}, {'currency': 'dinar algierski', 'code': 'DZD', 'mid': 0.032478}]}


    def test_load_data_df_from_dict_dict_provided(self) -> None:
        result = self.combine_data.load_df_from_dict(self.SOURCE_DICT_A)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertCountEqual(list(result.columns), ['table', 'no', 'effectiveDate', 'currency', 'code', 'mid'])

    def test_load_data_df_from_dict_no_dict_provided(self) -> None:
        result = self.combine_data.load_df_from_dict(-1)
        self.assertEqual(result, None)

    def test_combine_data_two_correct_args(self) -> None:
        arg_a = self.combine_data.load_df_from_dict(self.SOURCE_DICT_A)
        arg_b = self.combine_data.load_df_from_dict(self.SOURCE_DICT_B)
        result = self.combine_data.union_datasets(arg_a, arg_b)
        self.assertEqual(result.shape[0], 5+5)
        self.assertIn('effectiveDate', list(result.columns))

    def test_combine_data_incorrect_args(self) -> None:
        result = self.combine_data.union_datasets(-1, 'no')
        self.assertEqual(result, None)
