print('Olá, mundo!')

print(2 + 3)

print('O resultado da soma de 2+3 é:', 2 + 3)

print(10 * (5 + 7) / 4)

nota = 8.5
disciplina = 'Lógica de programação e Algoritmos'

print(nota)
print(disciplina)

print('Disciplina:', disciplina, 'Nota', nota)

a = 1  # a recebe 1
b = 5  # b recebe 5

resposta = a == b
print(resposta)

resposta = a != b
print(resposta)

# CONCATENAÇÃO

s1 = 'Logica de Programação'
s1 = s1 + 'e algoritmos'
print(s1)

# REPETINDO STRINGS NA CONCATENAÇÃO

s1 = 'A' + '-' * 10 + 'B'
print(s1)

s1 = 'A' + ' ' * 10 + 'B'
print(s1)

# VARIAS VARIÁVEIS

nota = 8.9
s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1)

# LIMITANDO AS CASAS DECIMAIS:

nota = 8.5
s1 = 'Você tirou %.2f na disciplina de Algoritmos' % nota
print(s1)

# VARIAS VARIÁVEIS

nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)

# COMPOSIÇÃO MODERNA

nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou {} na disciplina de {}'.format(nota, disciplina)
print(s1)

# COMPOSIÇÃO COM f-string

nota = 8.5
disciplina = 'Algoritmos'
s1 = f'Você tirou {nota} na disciplina de {disciplina}'
print(s1)

# FATIAMENTO

# quero escrever só a palavra LÓGICA
s1 = 'Logica de Programação'
print(s1[0:6])

# quero escrever só a palavra ALGORITMOS
s1 = 'Logica de Programação'
print(s1[24:34])

# Uma forma simplificada de escrever em vez de "0:6" fica apenas ":6"
s1 = 'Logica de Programação'
print(s1[:6])

# TAMANHO(length)

s1 = 'Logica de Programação'
tamanho = len(s1)
print(tamanho)

# FUNÇÃO DE ENTRADA E FLUXO DE EXECUÇÃO DO PROGRAMA

# Função entrada

idade = input('Qual a sua idade? ')
print(idade)

nome = input('Qual seu nome? ')
print(f'Olá, {nome}, seja bem-vindo!')

# CONVERTENDO DADOS DE ENTRADA(casting)

nota = float(input('Qual nota você recebeu na disciplina? '))
print(f'Você tirou nota {nota}.')

# FLUXO DE EXECUÇÃO DO PROGRAMA(teste de mesa)

x = 1
y = 1
z = x + y  # z=2

print(z)

x = x + 2  # x recebe o valor atual dele que é 1 + 2 que é igual a 3
y = y - 1  # y = 1 - 1 = 0
z = x + y  # z = 3 + 0 z = 3

print(z)

x = y + 1  # x = 0 + 1 = 1
y = x - 1  # y = 1 - 1 = 0
z = x + y  # z = 1 + 0 = 1

print(z)  # z = 1

# EXERCÍCIO
# Desenvolva um algoritmo que solicite ao usuário dois números inteiros. Imprima a soma desses dois números na tela

numero1 = int(input('Digite um número inteiro\n'))
numero2 = int(input('Digite mais um número inteiro\n'))
print(numero1 + numero2)


# soma = numero1 + numero2


# print(f'O resultado da soma do numer {numero1} + {numero2} é igual a: {soma}')
#
# frase_reasultado = f'O resultado da soma do numer {numero1} + {numero2} é igual a: {soma}'
#
# print(frase_reasultado)
