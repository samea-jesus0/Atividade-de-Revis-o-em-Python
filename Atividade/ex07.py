#
numeros = []

print("Se não quiser inserir mais, coloque -1.")
while True:
    num = int(input("Insira um número: "))

    if num == -1:
        break

    numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)

print(f"Quantidade de valores lidos: {len(numeros)}")
print("Valores em ordem de entrada: ")
for num in numeros:
    print(num, end=" ")

print("\nValores em ordem inversas: ")
for num in reversed(numeros):
    print(num, end=" ")

print(f"\nA soma é: {soma}")
print(f"A média é: {media}")
print("Valores acima da média: ")
for num in numeros:
    if num > media:
        print(num, end=" ")
        