import requests
import pandas as pd

SIGLA = "SP"
# https://brasilapi.com.br/api/ibge/municipios/v1/{siglaUF}?providers=dados-abertos-br,gov,wikipedia
URL_MUNICIPIOS ="https://brasilapi.com.br/api/ibge/municipios/v1/"+SIGLA+"?providers=dados-abertos-br,gov,wikipedia"

resposta_mun_sp = requests.get(URL_MUNICIPIOS)
print(resposta_mun_sp.status_code)
print(resposta_mun_sp.json()[:5])

df_sp = pd.DataFrame(resposta_mun_sp.json())
print(df_sp.head())