# 1. ESTRUTURA DE REPETIÇÃO

print(1)
print(2)
print(3)
print(4)
print(5)

x = 1
print(x)
x = 2
print(x)
x = 3
print(x)
x = 4
print(x)
x = 5
print(x)

x = 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)

# 2. ESTRUTURA DE REPETIÇÃO WHILE

x = 1
while x <= 5:
    print(x)
    x = x + 1

x = 1
while x <= 5:
    print(x)
    # x = x + 1 (sem essa linha, sem incrementar a variavel, entramos em um loop infinito)

x = 0
while x <= 99:  # mudou a condição do while
    print(x)
    x = x + 1

x = 0
while x < 99:  # mudou a condição do while
    print(x)
    x = x + 1

# Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado pelo usuário e que sejam
# numeros pares

inicial = int(input('Qual valore deseja iniciar a contagem? '))
final = int(input('Qual valore deseja encerrar a contagem? '))

x = inicial
while x <= final:
    # verifica se o numero é par
    if x % 2 == 0:
        print(x)
        x = x + 1

# ACOMULADORES
# - escreva um algoritmo que calcule a sua média de notas em determinada disciplina
#  --vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas

soma = 0
contagem = 1
while contagem <= 5:
    x = float(input(f'Digite a {contagem}ª nota: '))
    soma = soma + x
    contagem = contagem + 1
media = soma / 5
print(f'Média final: {media} ')

# reescrito usando outra forma

soma = 0
contagem = 1
while contagem <= 5:
    x = float(input(f'Digite a {contagem}ª numero: '))
    soma += x  # equivalente: soma = soma + x
    contagem += 1  # contagem = contagem + 1
print(f'Somatório: {soma} ')

# VALIDANDO DADOS DE ENTRADA
# EXEMPLO:
# - crie um algoritmo que recebe um valor do tipo inteiro via teclado
# -- No entanto, o programa so deve aceitar, obrigatóriamente, valores inteiros
# --- Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor deve ser solicitado

# vaidando a entrada
x = int(input('digite um valor maior do que zero: '))
while x <= 0:
    x = int(input('digite um valor maior do que zero: '))
    print(f'voce digitou {x}. encerrando programa...')

# - escreva um algoritmo que fique recebendo frases ou palavras digitadas pelo usuário
# -- encerre o algoritmo quando a palacra "sair" for digitada

print('digite uma mensagem que irei repetir para você! ')
print('para encerrar escreva "sair". ')

while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break

print('encerrando... ')

# exercicio
# - escreva um algoritmo que realize um login em um sistema
# -- o usuario deve informar o seu nome e senha

while True:
    nome = input('qual o seu nome? ')
    if nome != 'Lenhadorzinho':
        continue  # volta para o inicio do laço
    senha = input('qual a sua senha? ')
    if senha == 'UnInTeR':
        break  # encerra o laço
print('acesso concedido')

# VALORES "TRUTHY" E "FALSEY"

nome = ''  # Falsey
while not nome:  # not falsey vira thuthy/true
    # encerra o laço quando nome não estiver vazio
    nome = input('digite seu nome: ')

valor = int(input('digite um numero qualquer: '))
if valor:  # equivalente if valor != 0:
    print('você digitou um valor diferente de zero')
else:
    print('voceê digitou zero.')

# ESTRUTURA DE REPETIÇÃO for(PARA)

for i in range(6):
    print(i)

for i in range(0,6,1):
    print(i)

# VARREDURA DE STRING

frase = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1):
    print(frase[i], end="")

# exercicio
# - escreva o algoritmo que calcule a média dos números pares de 1 ate 100 (1 e 100 inclusos. Implemente o laço usando
# for.

soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
       soma += i
       qtd += 1
media = soma / qtd
print(f'a media dos pares de 1 ate 100 é: {media}')

# ESTRUTURA DE REPETIÇÃO ANINHADAS

# EXERCICIO
# escreva um algoritmo em python que calcule a tabuada de todos os números de 1 ate 10, e, para cada número, vamos
# calcular a tabuada multiplicando-o pelo intervalo de 1 ate 10. - vamos resolver no python diferentes implementações
# -- 2-while
# ---- 2-for
# ----- while+for

# 2x while
tabuada = 1
while tabuada <= 10:
    i = 1
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    tabuada += 1

# 2x for
for tabuada in range(1, 11, 1):
    print(f'TABUADA DO {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * i}')

# while + for
tabuada = 1
while tabuada <= 10:
    print(f'TABUADA DO {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * i}')
    tabuada += 1