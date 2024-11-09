# EXECICIO VIDEO 3 CONDICIONAL SIMPLES E COMPOSTA
# - Desenvolva um programa que leia dois valores numéricos inteiros e compare se o primeiro é maior do que o segundo,
# utilizando uma condicional simples.
# - Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro valor digitado
# é maior do que o segundo.

numero1 = int(input('Escolha um número inteiro \n'))
numero2 = int(input('Escolha mais um número inteiro \n'))
if numero1 > numero2:
    print(f'O primeiro número que você escolheu, {numero1} é maior do que o segundo número, {numero2}')

# E SE QUISERMOS IMPRIMIR A MENSAGEM CONTRÁRIA, QUE O SEGUNDO É MAIOR QUE O PRIMEIRO PODEMOS FAZER DE FORMA SOMPLES
# CONFORME ABAIXO.

if numero1 < numero2:
    print(
        f'O primeiro número que você escolheu, {numero1} é menor do que o segundo número que você escfolheu, {numero2}')

# FORMA CORRETA DE TER AS DUAS RESPOSTAS NESTE BLOCO DE CÓDIGOS

numero1 = int(input('Escolha um número inteiro \n'))
numero2 = int(input('Escolha mais um número inteiro \n'))
if numero1 > numero2:
    print(f'O primeiro número que você escolheu, {numero1} é maior do que o segundo número, {numero2}')
else:
    print(
        f'O primeiro número que você escolheu, {numero1} é menor do que o segundo número que você escfolheu, {numero2}')

# EXERCÍCIO
# - Desenvolva um programa que leia um valor inteiro e descubra se ele é par ou ímpar

num = int(input('digite um número inteiro \n'))
if num % 2 == 0:
    print('Seu numero escolhido é par')
else:
    print('Seu numero escolhido é ímpar')

# outro exemplo mas que não é para utilizarmos essa forMA
# num = int(input('digite um número inteiro \n'))
# if num % 2 == 0:
#     print('Seu numero escolhido é par')
# if num % 2 == 1:
#     print('Seu numero escolhido é ímpar')

# not
x = True
y = False
print(not x)
print(not y)

# and
x = False
y = True
print(x and y)

# or
x = False
y = False
print(x or y)

# EXPRESÕES LÓGICAS/BOOLEANAS

X = 10
Y = 1
res = not X > Y
print(res)

x = 10
y = 1
z = 5.5
res = (x > y) and (z == y)  # True and False
print(res)

x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x  # 1.55
# res = True or not False and True
# res= True or True and true
# res = True or True
# res = True
print(res)

# EXERCÍCIO
# - UM ALUNO, PARA PASSAR DE ANO, PRECIS SER APROVADO EM TODAS AS MATÉRIAS QUE ESTA CURSANDO
# - ASSUMA QUE A MÉDIA PARA APROVAÇÃO É A PARTIR  DE 7 E QUE O ALUNO CURSA 3 MATÉRIAS, SOMENTE. ESCREVA UM ALGORITMO QUE
# LEIA A NOTA FINAL DO ALUNO EM CADA MATÉRIA E INFORME, NA TELA SE ELE PASSOU DE ANO OU NÃO (MENEZES, 2019, 9. 60)

materia1 = float(input('Digita a nota da primeira matéria: \n'))
materia2 = float(input('Digita a nota da segunda matéria: \n'))
materia3 = float(input('Digita a nota da terceira matéria: \n'))
if materia1 >= 7 and materia2 >= 7 and materia3 >= 7:
    print('Parabens está aprovado!')
else:
    print('você reprovou!')

''''CONDICIONAIS ANINHADAS
EXERCÍCIO
- ESCREVA UM ALGORITMO EM PYTHON EM QUE O USUÁRIO ESCOLHE SE QUER COMPRAR MAÇAS , LARANJAS OU BANANAS. DEVERÁ SER
APRESENTADO NA TELA UM MENU COM AS OPÇÕES: 1 PARA MAÇA, 2 PARA LARANJA E 3 PARA BANANA
-Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O Algoritmo deve calcular o preço total a
pagar do produto escolhido e mostra-lo na tela
- considere que uma maça custa R$2,30, uma laranja, R$3,60, e uma banana, R$ 1,85'''



# OPÇÃO FEITA PELO PROFESSOR COM if e else:

# print('Escolha o que deseja comprar: ')
# print('1 - maça')
# print('2 - laranja')
# print('3 - banana')
# produto = int(input('Qual a sua escolha? '))
# quantidade = int(input('Quantas unidades? '))
# if produto == 1:
#     pagar = quantidade * 2.3
#     print(f'Você comprou {quantidade} maças. Total à pagar: {pagar}')
# else:
#     if produto == 2:
#         pagar = quantidade * 3.6
#         print(f'Você comprou {quantidade} laranjas. Total à pagar: {pagar}')
#     else:
#         if produto == 3:
#             pagar = quantidade * 1.85
#             print(f'Você comprou {quantidade} bananas. Total à pagar: {pagar}')
#         else:
#             print('Produto inexistente!')

# MAIS UMA OUTRA FORMA DE FAZER O MESMO EXERCICIO:

# print('Para maça digite 1, para laranja digite 2 e para banana digite 3')
# produto = int(input('Digite a opção desejada \n'))
# if produto != 1 and produto != 2 and produto != 3:
#     print('Produto indisponivel')
# else:
#     quantidade = int(input('Quantas unidades?'))
#     if produto == 1:
#         produto = quantidade * 2.30
#         print(f'O valor total é de: {produto}')
#     else:
#         if produto == 2:
#             produto = quantidade * 3.60
#             print(f'O valor total é de: {produto}')
#         else:
#             if produto == 3:
#                 produto = quantidade * 1.85
#                 print(f'O valor total é de: {produto}')

# UMA TERCEIRA FORMA DE FAZER O MESMO EXERCICIO

print('Para maça digite 1, para laranja digite 2 e para banana digite 3')
produto = int(input('Digite a opção desejada \n'))
if produto == 1 or produto == 2 or produto == 3:
    quantidade = int(input('Quantas unidades?'))
    if produto == 1:
        produto = quantidade * 2.30
        print(f'O valor total é de: {produto}')
    elif produto == 2:
        produto = quantidade * 3.60
        print(f'O valor total é de: {produto}')
    elif produto == 3:
        produto = quantidade * 1.85
        print(f'O valor total é de: {produto}')
else:
    print('Produto indisponivel')

# - Escreva um algoritmo que leia um nome e uma idade.
# --Caso o nome digitado seja vinicius, escreva isso na tela.
# --- Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menos que 18 anos, informe que é de menor.
# Se for maior que 100 anos, informe que esta pessoal possívelmente não existe.

# nome = input('Qual seu nome? ')
# idade = int(input('Qual a sua idade? '))
# if nome == 'Vinicius':
#     print('Vinicius')
# else:
#     if idade < 18:
#         print('Menor de idade')
#     else:
#         if idade > 100:
#             print('Esta pessoa possivelmente não existe')

nome = input('Qual seu nome? ')
idade = int(input('Qual a sua idade? '))
if nome == 'Vinicius':
    print('Vinicius')
elif idade < 18:
    print('Menor de idade')
elif idade > 100:
    print('Esta pessoa possivelmente não existe')

# E se o nome não for vinicius e tiver a idade entre 18 e 100 anos de a mensagem de parabéns

nome = input('Qual seu nome? ')
idade = int(input('Qual a sua idade? '))
if nome == 'Vinicius':
    print('Vinicius')
elif idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade <= 100:
    print('Parabens')
elif idade > 100:
    print('Esta pessoa possivelmente não existe')
