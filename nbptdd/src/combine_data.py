from dataclasses import dataclass
import pandas as pd


@dataclass
class CombineData():
    

    def load_df_from_dict(self, data_dict: dict) -> pd.DataFrame:
        if isinstance(data_dict, dict):
            df = pd.DataFrame(data_dict)
            df = self.__melt(df)
            return df
        else:
            return None


    def union_datasets(self, df_a: pd.DataFrame, df_b: pd.DataFrame) -> pd.DataFrame:
        if isinstance(df_a, pd.DataFrame) and isinstance(df_b, pd.DataFrame):
            return pd.concat([df_a, df_b])
        else:
            return None


    def __melt(self, df: pd.DataFrame) -> pd.DataFrame:
        df[['currency', 'code', 'mid']] = pd.DataFrame(df['rates'].tolist(), index=df.index)
        df = df.drop('rates', axis=1)
        return df
