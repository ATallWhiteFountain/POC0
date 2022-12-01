import datetime

import requests
import pandas as pd


def get_table(resource_uri: str) -> dict:
    response = requests.get(resource_uri)
    return response.json()[0]


def get_df_from_table(table: dict) -> pd.DataFrame:
    return pd.DataFrame(table)


# uri do tabeli kursów aktualnie obowiązujących
TABLE_A_URI = "http://api.nbp.pl/api/exchangerates/tables/a?format=json/"
TABLE_B_URI = "http://api.nbp.pl/api/exchangerates/tables/b?format=json/"


# uzyskaj DataFrame'y
df_a = get_df_from_table(get_table(TABLE_A_URI))
df_b = get_df_from_table(get_table(TABLE_B_URI))

# sklej DataFrame'y
final_df = pd.concat([df_a, df_b])

# rozpakuj kolumnę 'rates' a następnie ją usuń
final_df[['currency', 'code', 'mid']] = pd.DataFrame(final_df['rates'].tolist(), index=final_df.index)
final_df = final_df.drop('rates', axis=1)

# string dzisiejszej daty na potrzeby nazwy pliku 
date_str = datetime.date.today().strftime('%d-%m-%Y')

# zapisz w formacie csv w working directory
final_df.to_csv(f"./output/exchange_rates_for_{date_str}.csv")
