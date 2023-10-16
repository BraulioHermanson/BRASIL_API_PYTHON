#https://restcountries.com/
import requests
import pandas as pd
from pprint import pprint

# URL_ALL = "https://restcountries.com/v3.1/all"

# resposta = requests.get(URL_ALL)
# # print(resposta.status_code)
# # print(resposta.headers)
# # print(resposta.json()[:3])
# resposta_all = resposta.json()
# # pprint(resposta_all[0])
# # print(type(resposta_all[0]))
# # print(resposta_all[0]["name"]["common"])

# for pais in resposta_all:
#     if pais["name"]["common"] == "Brazil":
#         brasil = pais

# pprint(brasil)

# URL_BRASIL = "https://restcountries.com/v3.1/name/brasil"

# resposta_brasil = requests.get(URL_BRASIL).json()
# # print(resposta_brasil)
# print(resposta_brasil[0].keys())
# print(resposta_brasil[0]["population"])

# URL_AMERICA_SUL = "https://restcountries.com/v3.1/region/south%20america"
# # print(requests.get(URL_AMERICA_SUL).status_code)
# resposta_america_sul = requests.get(URL_AMERICA_SUL).json()
# pprint(resposta_america_sul[:1])

URL_AMERICA_SUL_FILTROS = "https://restcountries.com/v3.1/region/south%20america?fields=name,population,capital"
# print(requests.get(URL_AMERICA_SUL_FILTROS).status_code)
resposta_america_sul_filtros = requests.get(URL_AMERICA_SUL_FILTROS).json()
# pprint(resposta_america_sul_filtros[:2])


df_america_sul = pd.DataFrame(resposta_america_sul_filtros)
# print(df_america_sul.head(3))

paises_america_sul = []
for pais in resposta_america_sul_filtros:
    novo_pais = {
        "nome":pais["name"]["common"],
        "capital":pais["capital"][0],
        "populacao":pais["population"]
    }
    paises_america_sul.append(novo_pais)

# print(paises_america_sul)

df_america_sul = pd.DataFrame(paises_america_sul)
print(df_america_sul)