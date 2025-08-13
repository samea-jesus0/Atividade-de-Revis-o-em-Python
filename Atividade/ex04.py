acertos_alunos = []
contador_alunos = 0

GABARITO = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B']

PERGUNTAS = [
    "1) Quanto é 2 + 2?\nA) 4\nB) 5\nC) 3\nD) 6",
    "2) Quanto é 5 - 3?\nA) 1\nB) 2\nC) 3\nD) 4",
    "3) Quanto é 3 x 3?\nA) 6\nB) 8\nC) 9\nD) 12",
    "4) Quanto é 8 ÷ 2?\nA) 2\nB) 3\nC) 6\nD) 4",
    "5) Quanto é 10 - 7?\nA) 3\nB) 2\nC) 1\nD) 4",
    "6) Quanto é 6 + 1?\nA) 5\nB) 7\nC) 8\nD) 6",
    "7) Quanto é 9 ÷ 3?\nA) 2\nB) 4\nC) 3\nD) 6",
    "8) Quanto é 4 x 2?\nA) 6\nB) 5\nC) 7\nD) 8",
    "9) Quanto é 7 + 1?\nA) 8\nB) 9\nC) 7\nD) 6",
    "10) Quanto é 12 - 4?\nA) 8\nB) 7\nC) 6\nD) 9"
]

while True:
    contador_alunos += 1
    acertos_alunos.append(0)
    
    for i, pergunta in enumerate(PERGUNTAS):
        print(pergunta)
        while True:
            resposta = input('Sua resposta: ').upper()
            if resposta in ('A', 'B', 'C', 'D'):
                if resposta == GABARITO[i]:
                    acertos_alunos[contador_alunos - 1] += 1
                break
            print('Resposta inválida, insira uma das letras de A à D.')
    if input('Outro aluno deseja fazer a prova? (S/N)?') != 'S':
        break

print(f'A maior nota entre os alunos foi de {max(acertos_alunos)} pontos e a menor foi de {min(acertos_alunos)} pontos.')
print(f'O total de alunos que utilizaram o sistema foi de {contador_alunos}.')
print(f'A média das notas da turma foi de {(sum(acertos_alunos) / len(acertos_alunos)):.2f}')