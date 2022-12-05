from typing import Optional
from nbptdd.src.api_client import ApiClient
from nbptdd.src.combine_data import CombineData
from nbptdd.src.produce_csv_output import ProduceCsvOutput


def store_currency_exchanges(tables: list) -> Optional[str]:
    api_client = ApiClient()
    api_client.get(tables[0])
    data_dict_a = api_client.getDictData()
    api_client = ApiClient()
    api_client.get(tables[1])
    data_dict_b = api_client.getDictData()
    combine_data = CombineData()
    df_a = combine_data.load_df_from_dict(data_dict_a)
    df_b = combine_data.load_df_from_dict(data_dict_b)
    final_df = combine_data.union_datasets(df_a, df_b)
    produce_csv_output = ProduceCsvOutput()
    return produce_csv_output.save_df(final_df, './output/', 'currency_exchange.csv')

if __name__ == '__main__':
    TABLE_A_URI = "http://api.nbp.pl/api/exchangerates/tables/a?format=json/"
    TABLE_B_URI = "http://api.nbp.pl/api/exchangerates/tables/b?format=json/"
    tables = [TABLE_A_URI, TABLE_B_URI]
    result = store_currency_exchanges(tables)
    print('task completed', result)
