import requests

nome_pais = input("Insira o nome do país que deseja em inglês: ").lower()

url = f'https://restcountries.com/v3.1/name/{nome_pais}'
requestar = requests.get(url)
dados = requestar.json()
pais = dados[0]

nome = pais['name']['common']
sigla_ling = list(pais['languages'].keys())[0] 
linguagem = pais['languages'][sigla_ling]
regiao = pais['region']
sub_regiao = pais['subregion']
capital = pais['capital']
sigla_moeda = list(pais['currencies'].keys())[0]
nome_moeda = pais['currencies'][sigla_moeda]['name']
simbolo_moeda = pais['currencies'][sigla_moeda]['symbol']
paises_fronteira = list(pais['borders'])

print(f"Nome do país: {nome.upper()} | Linguagem(s): {linguagem} | Região: {regiao} | Sub-região: {sub_regiao} | Capital: {capital}")
print(f'Sigla da moeda: {sigla_moeda} | Nome: {nome_moeda.upper()} | Símbolo da moeda: {simbolo_moeda}')
print(f'Países que fazem fronteira com o(a) {nome_pais}: {", ".join(paises_fronteira)}')

