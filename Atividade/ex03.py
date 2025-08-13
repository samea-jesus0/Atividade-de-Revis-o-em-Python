nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))

media = (nota_1 + nota_2) / 2
conceito = 'A'

if media < 4:
    conceito = 'e'
elif media < 6:
    conceito = 'D'
elif media < 7.5:
    conceito = 'C'
elif media < 9:
    conceito = 'B'

print(f"Suas notas foram de {nota_1:.2f} e {nota_2:.2f}")
print(f'Suas média é {media:.2f}')
print(f'O conceito correspondente é de {conceito}')

if media >= 6:
    print('Você está APROVADO.')
else:
    print('Você está REPROVADO.')