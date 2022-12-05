import unittest
import datetime
import os
from pathlib import Path
import pandas as pd
from nbptdd.src.produce_csv_output import ProduceCsvOutput

# > saved file must be csv, must have human-readable run date

class ProduceCsvOutputTest(unittest.TestCase):

    def setUp(self) -> None:
        self.produce_csv_output = ProduceCsvOutput()
        self.SOURCE_DF = pd.DataFrame({'table': 'A', 'no': '233/A/NBP/2022', 'effectiveDate': '2022-12-02', 'rates': [{'currency': 'bat (Tajlandia)', 'code': 'THB', 'mid': 0.128}, {'currency': 'dolar amerykański', 'code': 'USD', 'mid': 4.4492}, {'currency': 'dolar australijski', 'code': 'AUD', 'mid': 3.0352}, {'currency': 'dolar Hongkongu', 'code': 'HKD', 'mid': 0.5719}, {'currency': 'dolar kanadyjski', 'code': 'CAD', 'mid': 3.3118}]})
        self.path_to_output = str(Path('.').parent.absolute()) + '/output/'
        self.todays_date = str(datetime.date.today().strftime('%d-%m-%Y')) 

    def test_save_df_not_a_df(self) -> None:
        result = self.produce_csv_output.save_df(-1, self.path_to_output, 'test.csv')
        self.assertEqual(result, None)

    def test_save_df_bad_path(self) -> None:
        result = self.produce_csv_output.save_df(self.SOURCE_DF, -1, 'test.csv')
        self.assertEqual(result, None)

    def test_save_df_bad_filename(self) -> None:
        result = self.produce_csv_output.save_df(self.SOURCE_DF, self.path_to_output, -1)
        self.assertEqual(result, None)

    def test_save_df_success(self) -> None:
        result = self.produce_csv_output.save_df(self.SOURCE_DF, self.path_to_output, 'test.csv')
        self.assertIsInstance(result, str)
        self.assertIn(f"test_{self.todays_date}.csv", os.listdir(self.path_to_output))

    def test_save_df_is_saved_file_csv(self) -> None:
        saved_file_filename = self.produce_csv_output.save_df(self.SOURCE_DF, self.path_to_output, 'test.csv')
        self.assertTrue(".csv" in saved_file_filename)

    def test_saved_file_has_human_readable_run_date(self) -> None:
        result = self.produce_csv_output.save_df(self.SOURCE_DF, self.path_to_output, 'test.csv')
        self.assertTrue(self.todays_date in result)
