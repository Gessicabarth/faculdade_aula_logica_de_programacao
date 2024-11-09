# Como fazer a importação de uma biblioteca para utilizar no python

# importando toda a biblioteca para conseguir utilizar a função desejada
import math  # sera necessario fazer este comando onde dizemos o que queremos importar da biblioteca

print(math.sqrt(9))  # para a função funcionar precisaremos colocar também o nome da pasta junto com a função math.sqrt

'''
PODEMOS TAMBÉM IMPORTAR SOMENTE A FUNÇÃO DESEJADA SEM PRECISAR IMPORTAR TODA A BIBLIOTECA PODENDO DAR PROBLEMA COM MEU 
PROGRAMA POR CONTA DE ESPAÇO
'''
# PARA ISSO USAMOS O FROM E O NOME DA FUNÇÃO DESEJADA CONFORME ABAIXO

from math import sqrt  # CONFORME MOSTRA AQUI IREMOS SOMENTE EXPORTAR A FUNÇÃO QUE VAMOS UTILIZAR

print(sqrt(9))  # E AI NÃO PRECISA ESCREVER O NOME DA BIBLIOTECA MAIS, CONFORME MOSTRA, O PRINT É PARA APARECER NA TELA

'''
EXERCÍCIOS DE FIXAÇÃO:
- LISTA:
    - Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressao para:
                notas = [9,7,7,10,3,9,6,6,2]
        a) Encontrar quantos anlunos tiraram nota 7
        b) Alterar a ultima nota para 4
        c) Encontrar a maior nota
        d) Ordenar a lista de notas
        e) A média das notas

'''
# a) Encontrar quantos alunos tiraram nota 7
# para isto usamos o metodo .count que irá verificar areaves do poarametro que passarmos quantas vezes aquele número
# apareceu na lista conforme abaixo:

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(notas.count(7))

# b) Alterar a ultima nota para 4
# utilizamos o metodo .count pois ele retorna o num de ocorrencias de item na lista
# para pegar o ultimo valor podemos usar o -1 que pega o ultimo item da lista, por isso notas[-1] e então para
# substituir atribuimos o valor que queremos subtituir, conforme abaixo:

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

notas[-1] = 4
print(notas)

# c) Encontrar a maior nota
# posso utilizar o metodo max e dentro dele por a lista. max(notas) ai ele vai me dar qual o maior valor conforme
# abaixo:

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(max(notas))

# d) Ordenar a lista de notas
# pode ser usado o metodo sort() ai ele faz a ordenação. Mas ele precisa estar separado do print se não da erro.
# Apos eu chamo a função conforme esta abaixo:

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
notas.sort()
print(notas)

# e) A média das notas
# para calcular a medida será necessario fazer uma pequena conta com a função sum() eu consigo fazer a soma de todos os
# itens da lista, ai não é necessario fazer a varedura de item por item. Eu pego o somatório sum() dividido pelo tamanho
# da lista len()

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(sum(notas) / len(notas))

'''
PROBLEMAS - EXERCICIO 1
 - Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro dessa dupla as vogais de cada palavra.
 Faça um print na tela com o nome da palavra e suas respectivas vogais
'''
# como eu tenho uma dupla indexação vou utilizar o for ___ in ___ duas vezes uma para a palavra e outra para a letra
# para verificar cada letra para saber se é volgal vou utilizar o if letra.lower o .lower tranforma toda a string em
# minusculo para garantir que todas as letras estarão do mesmo tamanho e então fazemos um teste de expressão in'aeiou':
# se eu colocar as vogais dentro dessas aspas é como se eu tivesse dizendo, se(if) a minha letra minuscula (letra.lower)
# estiver contida(in) em a,e,i,o,u('aeiou') ele vai me dar o print da letra. no print vamos colocar as letras em
# maiusculo por isso o metodo .upper e também vamos por para que cada print seja dado sem dar enter utilizando o end=' '
# Entre um laço e outro, no caso os for, vamos colocar um print para imprimir na tela uma mensagem junto para sabermos
# também quais são as palavras.

palavras = ('queijo', 'gessica', 'gabriel', 'megui', 'celular')

for palavra in palavras:
    print(f'\nPalavra:{palavra.upper()}. Vogais:')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

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
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor(j1, j2):
    global v1, v2, empate
    if j1 == 1: # pedra
        if j2 == 1:  # pedra
            empate += 1
        elif j2 == 2:   #papel
            v2 += 1
        elif j2 == 3:  # tesoura
            v1 += 1
    elif j1 == 2:  # papel
        if j2 == 1:  #pedra
            v1 += 1
        elif j2 == 2:  #papel
            empate += 1
        elif j2 == 3:  #tesoura
            v2 += 1
    elif j1 == 3:  #tesoura
        if j2 == 1: #pedra
            v2 += 1
        elif j2 == 2:  #papel
            v1 += 1
        elif j2 == 3:  #tesoura
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
    jogador2 = random.randint(1,3)
    jogadas.append([jogador1, jogador2])
    resultados = vencedor(jogador1, jogador2)


for jogada in jogadas:
    for dado in jogada:
        print(dado, end=' ')
    print()

print(f'Números de vitórias do Jogador 1: {resultados[0]}')
print(f'Números de vitórias do Jogador 2: {resultados[1]}')
print(f'Números de empates: {resultados[2]}')


'''
EXERCÍCIO 3
 - Crie um programa para ler o nome de nascimento e sexo de diferentes pessoas
 - Armazene os dados em um dicionário com listas
 - Ao encerrar o cadastro, apresente:
        - O total de cadastros efetuados
        - A media das idades das pessoas
        - Uma lista de mulheres com menos de 30 anos
        - Uma lista de homens com idade a cima da média
        
'''
cadastro = {'nome':[], 'sexo':[], 'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO.')
        continue

    nome = input('Qual o nome?')
    sexo = input('Qual o sexo?')
    ano = input('Qual o ano de nascimento?')
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['ano'].append(ano)

print(cadastro)

# finalizar