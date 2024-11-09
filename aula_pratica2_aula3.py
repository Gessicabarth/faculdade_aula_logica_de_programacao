#                   EXPRESSÕES BOOLEANAS

# CONDICIONAL SIMPLES:
'''
EXERCICIO 1
- Escreva as seguintes expressoes booleanas em linguagem python
    a) O somatório de 2 com 2 é menor que 4
    b) O valor 7 // 3 é igual a 1 + 1
    c) A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
    d) A soma de 2, 4 e 6 é maior que 12
'''

#  a) O somatório de 2 com 2 é menor que 4
# não vai dar certo por isso vou comentar pois para dar certo deveria ser: if (2 +2 <= 4): por isso vou comentar pois o
# que o exercicio pede é o que esta abaixo

# if (2 + 2 < 4):
#     print('verdadeiro')


# b) O valor 7 // 3 é igual a 1 + 1

if (7 // 3 == 1 + 1):
    print('verdadeiro')

# c) A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25

if (3**2 + 4**2 == 25):
    print('verdadeiro')

# d) A soma de 2, 4 e 6 é maior que 12 - não vai dar nada pois não é maior. por isso vou comentar

# if (2 + 4 + 6 > 12):
#     print('verdadeiro')

'''
EXERCICIO 2
- Escreva as seguintes expressoes booleanas em linguagem python 
   a) 1387 é divisivel por 19
   b) 31 é par
   c) o menor valor entre: 34, 29 e 31 é menor que 30
'''

# a) 1387 é divisivel por 19

if (1387 % 19 == 0):
    print('verdadeiro')

# b) 31 é par - não dará nada pois 31 é impar, vou comentar

# if (31 % 2 == 0):
#     print('verdadeiro')

# c) o menor valor entre: 34, 29 e 31 é menor que 30

if (min(34, 29, 31) < 30):
    print('verdadeiro')


# EXERCICIO DE CONDICIONAL SIMPLES

'''
- Traduza as afirmações a seguir para condicionais em python
    a) Se a idade é maior que 60, escreva: "você tem direitos aos beneficios"
    b) Se dano é maior que 10 e escudo é igual a 0, escreva: "Você esta morto!"
    c) Se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"
'''

# a) Se a idade é maior que 60, escreva: "você tem direito aos benefícios"

idade = 62
if (idade > 60):
    print('Você tem direito aos benefícios!')

# b) Se dano é maior que 10 e escudo é igual a 0, escreva: "Você esta morto!"

dano = 13
escudo = 0

if (dano > 10 and escudo == 0):
    print('Você está morto!')

# c) Se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"

norte = True
sul = False
leste = False
oeste = False

if (norte == True or sul == True or leste == True or oeste == True):
    print('Você escapou!')


# CONDICIONAL COMPOSTA:

'''
- Traduza as afirmações a seguir para condicionais em python
    a) Se ano é divisivel por 4, escreva: "Pode ser ano bissexto". Caso contrário, escreva: "Definitivamente não é um 
ano bissexto
    b) Se ambas as variáveis booleanas cima e baixo fore True, escreva: "Decida-se!", caso contrário, escreva: "Você 
escolheu um caminho!"
'''

# a) Se ano é divisivel por 4, escreva: "Pode ser ano bissexto". Caso contrário, escreva: "Definitivamente não é um
# ano bissexto

ano = 1993

if (ano % 4 == 0):
    print('Pode ser ano bissexto!')
else:
    print('Definitivamente não é um ano bissexto!')

# b) Se ambas as variáveis booleanas cima e baixo fore True, escreva: "Decida-se!", caso contrário, escreva: "Você
# escolheu um caminho!"

cima = True
bauxo = True

if (cima == True and bauxo == True):
    print('Decida-se!')
    else:
    print('Você escolheu um caminho!!')


''' EXERCICIO 1:  
- Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique 
se os valores formam um triângulo e classifique como
    a) EQUILÁTERO (três lados iguais)
    b) ISÓSCELES (dois lados iguais)
    c) ESCALENO (três lados diferentes)
- Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do 
que a soma dos outros dois
'''

A = int(input('Digite o 1o do triângulo'))