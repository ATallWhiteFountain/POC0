from dataclasses import dataclass
import datetime
import csv
import os


@dataclass
class CsvOutput():
    
    def save_list_as_csv(self, list_of_dicts: list[dict], filename_path: str) -> str:

        if (isinstance(list_of_dicts, list) and 
            isinstance(list_of_dicts[0], dict) and
            self.__is_valid_filepath(filename_path)):

            with open(filename_path, 'w') as f:
                w = csv.DictWriter(f, list_of_dicts[0].keys())
                w.writeheader()
                for row in list_of_dicts:                                               
                    if isinstance(row, dict):
                        w.writerow(row)                             
                return w
        else:
            return None


    def create_date_csv_filename(self, prefix: str = 'currency_exchanges') -> str:
        current_date = str(datetime.date.today().strftime('%d-%m-%Y'))
        if not isinstance(prefix, str):
            prefix = 'currency_exchanges'
        return f"{prefix}_{current_date}.csv"


    def __is_valid_filepath(self, filename_path: str) -> bool:
        filename = filename_path.split('/')[-1]
        path = filename_path.replace(filename, '')
        if ('csv' in filename 
            and str(datetime.date.today().strftime('%d-%m-%Y')) in filename
            and os.path.exists(path)):
            return True
        else:
            return False
