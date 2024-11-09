# CONSTRUINDO E MANIPULANDO TUPLAS

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

print(mochila[0])  # print do elemento 1 - indice 0
print(mochila[2])  # print do elemento 3 - indice 2
print(mochila[0:2])  # print dos elementos 1 e 2 - indice 0
print(mochila[2:])  # print dos elementos a partit do indice 2
print(mochila[-1])  # print do último

# forma um de como listar os itens de uma lista

for item in mochila:
    print(f'Na minha mochila tem: {item}')

# outra forma para listar os itens  - é uma forma mais dificil de fazer esta.

tam = len(mochila)
for i in range(0, tam, 1):
    print(f'Na minha mochila tem: {mochila[i]}')

# uma opção para inserir mais item na lista

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade  # para que os novos itens sejam colocados na lista a partir do ultimo item dessa
# lista sempre colocar o upgrade após a mochila
print(mochila)
print(upgrade)
print(mochila_grande)


# DESEMPACOTAMENTO DE PARÂMETROS EM FUNÇÕES

def soma(*num):
    acumulador = 0
    print(f'Tupla: {num}')
    for i in num:
        acumulador += i
    return acumulador


# Programa principal
print(f'Resultado: {soma(1, 2)} \n')
print(f'Resultado: {soma(1, 2, 3, 4, 5, 6, 7, 8, 9)} \n')

# DIFERENÇA ENTRE LISTA E TUPLA
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')  # TUPLA
print('Tupla:', mochila)

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']  # LISTA
print('Lista:', mochila)

# MANIPULANDO LISTAS

mochila.append('Ovos')  # adiciona no final da lista o item passado
print('Lista', mochila)

mochila.insert(1, 'Canivete')  # insere na posição informada
print('Lista', mochila)

del mochila[1]  # deleta do indice informado
print('Lista', mochila)

mochila.remove('Ovos')  # deleta o dado informado
print('Lista', mochila)

# como fazer COPIA DE LISTA - ao atribuir a original a referenciada colocar o [:]

lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original[:]  # quando coloco os colchetes dois pontos significa que peguei a lista toda
print(lista_original)
print(lista_referenciada)

# STRINGS E LISTAS DENTRO DE LISTAS
# lista
MOCHILA = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0])

# DUPLA INDEXAÇÃO - se eu quiser acessar itens expecificos da lista
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0])
print(mochila[2][1])

# ITERRAR CARACTER POR CARACTER DE CADA UMA DAS PALAVRAS (Serve também para verificar se algum padrão existe.)

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila:  # como tenho duas indexações eu vou precisar de dois laços - cada item da mochila
    for letra in item:
        print(letra, end='')  # o end='' é so para não dar a quebra de linha
    print()  # print vazio é só uma quebra de linha

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0,len(mochila),1):
    for j in range(0,len(mochila[i]),1):
        print(mochila[i][j], end='')  # o end='' é so para não dar a quebra de linha
    print()

''' 
EXERCICIO:
- Imagine uma situação na qual você deve realizar o cadastro de uma lista de compras em um sistema. Cada produto 
comprado deverá ser registrado com seu nome, quantidade e valor unitário.
'''

# opção 1:

item = []
mercado = []

for i in range(3):
    item.append(input('Digite o nome do item: '))
    item.append(int(input('Digite a quatidade: ')))
    item.append(float(input('Digite o valor: ')))
    mercado.append(item[:])
    item.clear()  # vai limpar a lista
    print(mercado)

# opção 2:

mercado = []

for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quatidade: '))
    valor = float(input('Digite o valor: '))
    mercado.append([nome, qtd, valor])
    print(mercado)

# calculo do valor a ser pago

soma = 0
print('Lista de compras:')
print('-' * 20)
print('item | quantidade | valor unitário | Total item')
for item in mercado:
    print('{} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-' * 20)
print(f'Total a ser pago: {soma}')

# DICIONÁRIOS

# uma TUPLA com parenteses ()

mochila = ('laptop', 'smartphone', 'Power Bank', 'Carregadores e Cabos')
print('Tupla:', mochila)

# uma LISTA com colchetes []

mochila = ['laptop', 'smartphone', 'Power Bank', 'Carregadores e Cabos']
print('Lista:', mochila)

# um DICIONÁRIO com chaves {}

mochila = {'laptop': 1, 'smartphone': 2, 'Power Bank': 3, 'Carregadores e Cabos': 4}
print('Dicionário:', mochila)

# vamos dizer que eu queira cadastrar meus games

game = {'nome': 'Super Mario',
        'desenvolvedora': 'Nintendo',
        'ano': 1990}
print(game)

# como acessar so um dado - acesso por sua palavra chave

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

# METODO PARA DICIONARIO

print(game.values())  # se eu fizer isso, ele me da só os dados, ignora as chaves

for values in game.values():  # posso interar tambem
    print(values)

print(game.keys())  # se eu fizer assim pego so as chaves ai

for keys in game.keys():  # posso interar tambem
    print(keys)

print(game.items())

for keys, values in game.items():  # se ey fizer assim ai consigo pegar a chave e o dado
    print(f'{keys} = {values}')

# LISTAS COM DICIONÁRIOS

# exemplo: para cadastrar todos os meus jogos

game1 = {'nome': 'Super Mario',
         'Videogame': 'Super Nintendo',
         'ano': 1990}
game2 = {'nome': 'Zelda Ocarina Of Time',
         'Videogame': 'Nintendo 64',
         'ano': 1998}
game3 = {'nome': 'Pokemon Yellow',
         'Videogame': 'Game Boy',
         'ano': 1999}
games = [game1, game2, game3]


# outra maneira para fazer mesma implementação

game = {}
games1 = []

for i in range(3):
    game['nome'] = input('Qual o nome do jogo?')
    game['videogame'] = input('Para qual video-game ele foi lançado?')
    game['ano'] = input('Qual o ano de lançamento?')
    games1.append(game.copy())
print('-' * 20)
for jogos in games:
    for chave, valor in jogos.items():
        print(f'O campo {chave} tem o valor {valor}')

# GRANDES DICIONARIOS COM LISTAS DENTRO COMO FAZER:

games = {'nome': ['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yellow'],
         'videogame': ['Super Nintendo', 'Nintendo 64', 'Game Boy'],
         'ano': [1990, 1998, 1999]}
print(games)

games = {'nome': [], 'videogame': [], 'ano': []}
for i in range(3):
    nome = input('Qual o nome do jogo?')
    videogame = input('Para qual video-game ele foi lançado?')
    ano = input('Qual o ano de lançamento?')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)

# TRABALHANDO COM METODOS EM STRINGS - fazendo alteração de uma string

s1 = list('Algoritmos')
print(s1)  # print separado
print(''.join(s1))  # print agrupado

s1[0] = 'a'
print(''.join(s1))

# VERIFICANDO CARACTERES

s1 = 'Lógica de Programação e Algoritmos'
s1.startswith('Lógica')   # testa se a string começa com a palavra Lógica

s1 = 'Lógica de Programação e Algoritmos'
s1.endswith('Algoritmos')  # testa se uma string termina com a palavra Algoritmos

s1 = 'Lógica de Programação e Algoritmos'
s1.endswith('algoritmos')  # se colocarmos para testar o endswith da palavra algotirmo em minusculo dara falso, porque o
# caracter minusculo pe diferente do caracter maiusculo da frase analisada. então ele não entende que é a mesma coisa
# então retorna false(falso)

s1 = 'Lógica de Programação e Algoritmos'
s1.lower().endswith('algoritmos')  # para que possa retornar que é verdadeiro, e ignorar se o caracter é maiusculo ou
# minusculo, eu posso usar a opção lower que primeiro vai converter toda a frase para minusculo, depois a opção endswith
# vai verificar se termina com o algoritmo em minusculo e então irá retornar True(verdadeiro).

s1 = 'Lógica de Programação e Algoritmos'
print(s1.upper())  # se pegarmos uma string e por .upper ele vai transformar tudo para maiúsculo.
print(s1.lower())  # se pegarmos uma string e colocarmos .lower ele vai por tudo em minúsculo

# CONTANDO CARACTERES

s1 = 'Lógica de Programação e Algoritmos'
s1.count('a')  # quantas letras 'a' tem na frase, lembrando que ele não considera acentuação e nem letras maiusculas

s1 = 'Lógica de Programação e Algoritmos'
s1.lower().count('a')  # se eu quiser que conte todas as letras 'a', primeiro tenho que deixar todas as letras do mesmo
# tamanho, ou todas minusculas ou todas maiusculas. O .lower deixa todas minusculas ai passa a ter um 'a' a mais
# comparado com o exemplo anterior

s1 = 'Um mafagafinho, dois mafagafinho, três mafagafinhos...'
s1.lower().count('mafagafinho')  # podemos contar o padrão também, por exemplo quantas vezes tal palavra aparece na
# frase, no caso deste exemplo é quantas vezes aparece na frase a palavra mafagafinho

# QUEBRANDO STRING

s1 = 'Um mafagafinho, dois mafagafinho, três mafagafinhos...'
s1.split(' ')   # posso quebrar uma string também, e jogar cada parte que eu quero dentro de uma lista

# SUBSTITUINDO STRING

s1 = 'Um mafagafinho, dois mafagafinho, três mafagafinhos...'
s1.replace('mafagafinho', 'gatinho')  # posso subtituir uma palavra dentro da minha string, neste caso
# subtituimos o mafagafinhos por gatinhos

s1 = 'Um mafagafinho, dois mafagafinho, três mafagafinhos...'
s1.replace('mafagafinho', 'gatinho',1)  # aqui também, posso subtituir uma palavra dentro da minha string, neste caso
# estou também informando quantas vezes eu quero subtituir o mafagafinhos por gatinhos

# VALIDANDO TIPOS DE DADOS

s1 = 'Lógica de Programação e Algoritmos'
s2 = '42'

print(s1.isalnum())  # deu falso pois o .isalnum (é somente letras e números; acentos são aceitos (espaço não)
print(s2.isalnum())  # deu verdadeiro pois tem somente numeros

print(s1.isalpha())  # deu falso pois o .isalpha (é somente letras; acentos são aceitos)
print(s2.isalpha())   # deu falso

s1 = 'LógicadeProgramaçãoeAlgoritmos'
print(s1.isalpha())  # agora sim deu verdadeiro pois foi tirado todos os espaços da frase
