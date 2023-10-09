import requests
import json
import pandas as pd
from pprint import pprint

URL_BANCOS = "https://brasilapi.com.br/api/banks/v1"

resposta_bancos = requests.get(URL_BANCOS)

# print(resposta_bancos.status_code)
# print('-'*20)
# print(resposta_bancos.headers)
# print('-'*20)

bancos = resposta_bancos.json()

# pprint(bancos[:5])
# print('-'*20)

# with open("bancos.json","w") as arquivo:
#     json.dump(bancos,arquivo)

# with open("bancos.json","r") as arquivo:
#     bancos_arquivo = json.load(arquivo)

# pprint(bancos_arquivo)

#transformando em df
df_bancos = pd.DataFrame(bancos)

print(df_bancos.head())
print('-'*20)
print(df_bancos.info())
print('-'*20)
print(df_bancos.iloc[-2:])

df_bancos = df_bancos.copy()
df_bancos = df_bancos.iloc[:-2]

print('-'*20)
print(df_bancos.tail())
print('-'*20)
print(df_bancos[df_bancos["code"].isnull()])
df_bancos = df_bancos.dropna(subset=["code"])
print(df_bancos.info())
print('-'*20)
df_bancos["code"] = df_bancos["code"].astype(int)
print(df_bancos.info())
# df_bancos.to_csv("api_bancosbrasil.csv",index=False)

URL_WARREN = "https://brasilapi.com.br/api/banks/v1/371"
resposta_warren = requests.get(URL_WARREN)
print(resposta_warren.status_code)
pprint(resposta_warren.json())