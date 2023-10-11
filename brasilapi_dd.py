import requests
import pandas as pd

URL_DDD = "https://brasilapi.com.br/api/ddd/v1/"

#resposta_ddd_11 = requests.get(URL_DDD + "11")
# resposta_ddd = requests.get("".join([URL_DDD,"21"]))

#print(resposta_ddd.status_code)

#print(resposta_ddd.json())

# df_ddd_21 = pd.DataFrame(resposta_ddd.json()).assign(ddd=21)
# print(df_ddd_21)

# varios ddd
# for ddd in range(11,22):
#     resposta = requests.get("".join([URL_DDD, str(ddd)]))
#     print(f"DDD: {ddd} - Status code: {resposta.status_code}")

df_ddd = pd.DataFrame()

for ddd in range(11,22):
    resposta = requests.get("".join([URL_DDD, str(ddd)]))
    if resposta.status_code == 200:
        df_ddd = pd.concat([df_ddd, pd.DataFrame(resposta.json()).assign(ddd=ddd)])


print(df_ddd)