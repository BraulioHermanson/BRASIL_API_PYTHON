import requests
import pandas as pd

URL_DDD = "https://brasilapi.com.br/api/ddd/v1/"

#resposta_ddd_11 = requests.get(URL_DDD + "11")
resposta_ddd = requests.get("".join([URL_DDD,"21"]))

#print(resposta_ddd.status_code)

#print(resposta_ddd.json())
df_ddd_21 = pd.DataFrame(resposta_ddd.json()).assign(ddd=21)
print(df_ddd_21)