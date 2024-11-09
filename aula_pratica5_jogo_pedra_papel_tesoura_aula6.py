'''
EXERCICIO 2
- Crie um JOGO de PEDRA, PAPEL ou TESOURA(Jokenpô). Você deverá jogar contra o computador. Você ira sempre escolher uma
das opções: 1- pedra, 2- papel, 3- tesoura
  - O computador irá sempre sortear um número de 1 até 3 para jogar
  - Armazene todos os resultados em uma lista, no final apresente o vencedor
  - encerre o programa ao digitar zero
'''

import random


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def vencedor(j1, j2):
    global v1, v2, empate
    if j1 == 1:  # pedra
        if j2 == 1:  # pedra
            empate += 1
        elif j2 == 2:  # papel
            v2 += 1
        elif j2 == 3:  # tesoura
            v1 += 1
    elif j1 == 2:  # papel
        if j2 == 1:  # pedra
            v1 += 1
        elif j2 == 2:  # papel
            empate += 1
        elif j2 == 3:  # tesoura
            v2 += 1
    elif j1 == 3:  # tesoura
        if j2 == 1:  # pedra
            v2 += 1
        elif j2 == 2:  # papel
            v1 += 1
        elif j2 == 3:  # tesoura
            empate += 1

    resultados = [v1, v2, empate]
    return resultados


# Programa principal

print('JOKENPÔ')
print('1 - pedra')
print('2 - papel')
print('3 - tesoura')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0

while True:
    jogador1 = valida_int('Escolha sua jogada: ', 0, 3)
    if not jogador1:
        break
    jogador2 = random.randint(1, 3)
    jogadas.append([jogador1, jogador2])
    resultados = vencedor(jogador1, jogador2)

for jogada in jogadas:
    for dado in jogada:
        print(dado, end=' ')
    print()

print(f'Números de vitórias do Jogador 1: {resultados[0]}')
print(f'Números de vitórias do Jogador 2: {resultados[1]}')
print(f'Números de empates: {resultados[2]}')
