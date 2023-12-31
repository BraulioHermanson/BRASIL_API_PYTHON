# https://fred.stlouisfed.org/docs/api/fred/
import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()
key = os.getenv("API_KEY")

URL = f"https://api.stlouisfed.org/fred/series/search?search_text=brazil&api_key={key}&file_type=json"

resposta_busca = requests.get(URL)

# print(resposta_busca.json()["seriess"][-1])

# Paginacao
LIMITE = 3
OFFSET = 3
URL_LIMITE = f"https://api.stlouisfed.org/fred/series/search?search_text=brazil&api_key={key}&file_type=json&limit={LIMITE}&offset={OFFSET}"
resposta_busca_limite = requests.get(URL_LIMITE)
# print(resposta_busca_limite.json())

#TODO Criar dataframe
df_busca = pd.DataFrame(resposta_busca.json()["seriess"])
# print(df_busca.head())
# print(df_busca[df_busca["title"].str.contains("dollar", case=False)])


SERIE_DOLLAR = "DEXBZUS"

URL_SERIE_DOLLAR = f"https://api.stlouisfed.org/fred/series/observations?series_id={SERIE_DOLLAR}&api_key={key}&file_type=json"
resposta_dollar = requests.get(URL_SERIE_DOLLAR)
# resposta_dollar.status_code
df_dollar = pd.DataFrame(resposta_dollar.json()["observations"])

df_dollar = df_dollar.drop(columns=["realtime_start", "realtime_end"])

# converter a coluna date para datetime
df_dollar["date"] = pd.to_datetime(df_dollar["date"])

# substituindo os valores "." por NaN
df_dollar["value"] = df_dollar["value"].replace(".", float("NaN"))

# converter a coluna value para float
df_dollar["value"] = df_dollar["value"].astype(float)

# colocar a coluna date como index
df_dollar = df_dollar.set_index("date")

print(df_dollar.head())