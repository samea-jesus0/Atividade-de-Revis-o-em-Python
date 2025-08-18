import requests

zonas_sp = {
    "Zona Norte": ["Santana", "Casa Verde", "Tucuruvi", "Vila Maria", "Jaçanã"],
    "Zona Sul": ["Santo Amaro", "Capão Redondo", "Jabaquara", "Campo Limpo", "Socorro"],
    "Zona Leste": ["Itaquera", "Penha", "São Mateus", "Guaianases", "Aricanduva"],
    "Zona Oeste": ["Lapa", "Butantã", "Pinheiros", "Perdizes", "Jaguaré"],
    "Centro": ["Sé", "República", "Consolação", "Bela Vista", "Liberdade"]
}

def identificar_zona(bairro):
    for zona, lista_bairros in zonas_sp.items():
        for b in lista_bairros:
            if b.lower() in bairro.lower():
                return zona
    return None

cep = input("Digite o CEP do destino: ")

url = f'https://viacep.com.br/ws/{cep}/json/'
requestar = requests.get(url)

if requestar.status_code == 200:
    dados = requestar.json()
    zona = identificar_zona(dados['bairro'])
    print(f"")
else:
    print("Erro ao acessar a API.")
