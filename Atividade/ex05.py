pedido = {
    100: ("cachorro quente", 1.20),
    101: ("bauru simples", 1.30),
    102: ("bauru com ovo", 1.50),
    103: ("hamburguer", 1.30),
    104: ("cheeseburguer", 1.30),
    105: ("refrigerante", 1.30)
}

total_pedido = 0

for codigo, (produto, preco) in pedido.items():
    print(f"{produto} tem o código: {codigo} e custa R${preco:.2f}")
print("Para finalizar o seu pedido escreva um zero.")

while True:
    cod = int(input("Digite o código do que deseja pedir: "))

    if cod == 0:
        break
    if cod in pedido:
        qtd = int(input("Quantos você deseja? "))
        produto, preco = pedido[cod]
        valor_produto = preco * qtd
        total_pedido += valor_produto
        print(f"Valor atual do seu pedido: {total_pedido:.2f}")
    else:
        print("Insira um código válido.")

print(f"O total do seu pedido foi de: {total_pedido:.2f}")