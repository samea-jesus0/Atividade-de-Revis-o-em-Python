import requests

sigla = input("Digite a sigla da moeda: ").upper()

url = "https://api.exchangerate-api.com/v4/latest/BRL"
requestar = requests.get(url)

if requestar.status_code == 200:
    dados = requestar.json()
    taxas = dados["rates"]

    if sigla in taxas:
        valor = taxas[sigla]
        print(f"1 Real vale {valor:.2f} {sigla}.")
    else:
        print("Sigla de moeda não encontrada.")
else:
    print("Erro ao acessar a API.")

