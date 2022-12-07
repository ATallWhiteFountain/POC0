from dataclasses import dataclass
import datetime
import pandas as pd


@dataclass
class ProduceCsvOutput():
    
    
    def save_df(self, df: pd.DataFrame, dir_path: str, filename: str) -> str:
        if isinstance(df, pd.DataFrame) and isinstance(dir_path, str) and isinstance(filename, str):
            filename = self.__create_filename(filename)
            df.to_csv(dir_path + filename)
            return filename
        else:
            return None


    def __create_filename(self, prefix: str) -> str:
        todays_date = str(datetime.date.today().strftime('%d-%m-%Y'))
        if ".csv" not in prefix:
            return f"{prefix}'_'{todays_date}.csv"
        else:
            return f"{prefix.split('.csv')[0]}_{todays_date}.csv"
