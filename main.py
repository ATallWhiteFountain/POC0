from nbptdd.src.api_client import ApiClient
from nbptdd.src.combine_data import CombineData
from nbptdd.src.csv_output import CsvOutput


def store_currency_exchanges(tables: list) -> str:
    api_client = ApiClient()
    api_client.get(tables[0])
    data_dict_a = api_client.getJsonDictData()
    api_client = ApiClient()
    api_client.get(tables[1])
    data_dict_b = api_client.getJsonDictData()
    combine_data = CombineData()
    df_a = combine_data.get_list_of_dicts(data_dict_a)
    df_b = combine_data.get_list_of_dicts(data_dict_b)
    final_df = combine_data.union_dicts(df_a, df_b)
    produce_csv_output = CsvOutput()
    filename = produce_csv_output.create_date_csv_filename()
    filepath = f"./output/{filename}"
    if produce_csv_output.save_list_as_csv(final_df, filepath):
        return True
    else:
        return False


if __name__ == '__main__':
    TABLE_A_URI = "http://api.nbp.pl/api/exchangerates/tables/a?format=json/"
    TABLE_B_URI = "http://api.nbp.pl/api/exchangerates/tables/b?format=json/"
    tables = [TABLE_A_URI, TABLE_B_URI]
    result = store_currency_exchanges(tables)
    print('task completed', result)
