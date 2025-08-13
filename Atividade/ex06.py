'''# Primeira parte do exercicio que pede um salário especifico
ano_salario = 1995
ano_atual = 2025
salario = 1000

percentual = 1.5/100

for ano_salario in range(ano_salario+1,ano_atual+1):
    acrescimo = salario * percentual
    salario += acrescimo
    percentual *= 2 

print(f"O salário do trabalhador em {ano_atual} é de {salario:.2f}")'''

ano_salario = int(input("Digite o ano em que começou a receber seu salário: "))
ano_atual = int(input("Digite o ano atual: "))
salario = float(input("Digite o seu salário: "))

percentual = 1.5/100

for ano_salario in range(ano_salario+1,ano_atual+1):
    acrescimo = salario * percentual
    salario += acrescimo
    percentual *= 2 

print(f"O salário do trabalhador em {ano_atual} é de {salario:.2f}")