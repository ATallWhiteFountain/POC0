import unittest
import datetime
import os
from pathlib import Path
from nbptdd.src.csv_output import CsvOutput
from nbptdd.src.combine_data import CombineData


class CsvOutputTest(unittest.TestCase):


    def setUp(self) -> None:
        self.produce_csv_output = CsvOutput()
        self.SOURCE_DICT = {'table': 'A', 'no': '233/A/NBP/2022', 'effectiveDate': '2022-12-02', 'rates': [{'currency': 'bat (Tajlandia)', 'code': 'THB', 'mid': 0.128}, {'currency': 'dolar amerykański', 'code': 'USD', 'mid': 4.4492}, {'currency': 'dolar australijski', 'code': 'AUD', 'mid': 3.0352}, {'currency': 'dolar Hongkongu', 'code': 'HKD', 'mid': 0.5719}, {'currency': 'dolar kanadyjski', 'code': 'CAD', 'mid': 3.3118}]}
        self.list_of_dicts = CombineData().get_list_of_dicts(self.SOURCE_DICT)
        self.path_to_output = str(Path('.').parent.absolute()) + '/output/'
        self.todays_date = str(datetime.date.today().strftime('%d-%m-%Y')) 


    def test_create_date_csv_filename_prefix_provided(self) -> None:
        prefix = 'this_is_test'
        filename = self.produce_csv_output.create_date_csv_filename(prefix)
        self.assertEqual(filename, f"{prefix}_{self.todays_date}.csv")


    def test_create_date_csv_filename_no_or_incorrect_prefix(self) -> None:
        filename = self.produce_csv_output.create_date_csv_filename()
        self.assertEqual(filename, f"currency_exchanges_{self.todays_date}.csv")


    def test_save_list_as_csv_success(self) -> None:
        filename = self.produce_csv_output.create_date_csv_filename()
        filepath = ''.join([self.path_to_output, filename])
        feedback = self.produce_csv_output.save_list_as_csv(self.list_of_dicts, filepath)
        self.assertTrue(feedback)
        self.assertIn(filename, os.listdir(self.path_to_output))


    def test_save_list_as_csv_bad_path(self) -> None:
        filename = self.produce_csv_output.create_date_csv_filename()
        filepath = ''.join(['nota/real/place/', filename])
        feedback = self.produce_csv_output.save_list_as_csv(self.list_of_dicts, filepath)
        self.assertIsNone(feedback)


    def test_save_list_as_csv_bad_filename(self) -> None:
        filepath = ''.join([self.path_to_output, 'some_gibberish'])
        feedback = self.produce_csv_output.save_list_as_csv(self.list_of_dicts, filepath)
        self.assertIsNone(feedback)


    def test_save_list_as_csv_bad_data(self) -> None:
        junk_list = ["yes", "no", -1, []]
        filename = self.produce_csv_output.create_date_csv_filename()
        filepath = ''.join([self.path_to_output, filename])
        feedback = self.produce_csv_output.save_list_as_csv(junk_list, filepath)
        self.assertIsNone(feedback)
