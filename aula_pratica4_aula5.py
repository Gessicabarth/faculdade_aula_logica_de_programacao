# '''
# EXERCÍCIO 1
# - Escreva uma função que calcule o fatorial de um número recebido como parâmetro e retorne o seu resultado.
# - Faça uma validação dos dados por meio de uma outra função, permitindo que somente valores positivos sejam aceitos.
# - Crie o help da sua função.
# '''
#
#
# def calcular_fatorial(n):
#     # n * n-1 definição de fatorial
#     '''
#     Funcção que calcula a fatorial de um número inteiro
#
#     :param n: número fatorial
#     :return: como o número fatorial é n*n-1 foi necessario retornar o 1 para o programa entender que quando ele chegasse
#     no 1 ele voltaria a multiplicação para chegar no resultado fatorial do número passado.
#     '''
#
#
#     if validar_numero_positivo(n) == False:
#         return 0
#
#     if n == 1:
#         return 1
#     else:
#         return n * calcular_fatorial(n - 1)
#
#
# def validar_numero_positivo(n):
#     if n > 0:
#         return True
#     else:
#         return False
#
#
# validar_numero_positivo(2)
# res = calcular_fatorial(-4)
# print(res)
# help(calcular_fatorial)
#
#
#
# # exercicio com o while
# def calcular_fatorial1(n):
#     resultado = 1
#     while n >= 1:
#         resultado = resultado * n
#         n = n - 1
#     return resultado
#
#
# res = calcular_fatorial1(4)
# print(res)


'''
EXERCÍCIO 2
- Suponha que você é um colecionador de jogos de videogame. Escreva um algoritmo que permita cadastrar esses jogos 
informando o nome e a qual videogame ele pertence
- Para isso, crie um menu de opções contendo: cadastrar novo item, listar tudo o que foi cadastrado e sair.
- Para resolver esse exercício crie pelo menos uma função para cada item do menu
- Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados
'''


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existe_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso! \n')
def cadastrar_jogo(nome_arquivo, nome_jogo, nome_videogame):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write(f'{nome_jogo};{nome_videogame} \n')
    finally:
        a.close()
def listar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

# Programa principal
arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente.')
    criar_arquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if (op == 1):  # novo item
        print('Opção de cadastrar novo item selecionada... \n')
        nome_jogo = input('Nome do jogo: ')
        nome_videogame = input('Nome do videogame: ')
        cadastrar_jogo(arquivo, nome_jogo, nome_videogame)
    elif (op == 2):  # listar
        print('Opção de listar selecionada... \n')
        listar_arquivo(arquivo)
    elif (op == 3):
        print('Encerrando o programa...')
        break
    else:
        print('Arquivo inexistente.')








# opção 1: PRECISA SER FINALIZADO AINDA
# print('escolha umas das opções abaixo:')
# resposta = int(input('Cadastrar novo item digite 1 \n Listar tudo o que foi cadastrado digite 2 \n Sair digite 3 \n'))
# lista_jogos = []
# while resposta != 3:
#     resposta = int(input('Cadastrar novo item digite 1 \n Listar tudo o que foi cadastrado digite 2 \n Sair digite 3
#     \n'))
#     if resposta == 1:
#         item = input('Digite o nome do jogo e o videogame que ele pertence')
#         lista_jogos.append(item)
#     elif resposta == 2:
#         print(lista_jogos)
#     else:
#         print('Finalizado com sucesso!')


# i1 = 'cebola'
# i2 = 'tomate'
# lista_de_compra = [i1, i2, 'papel higienico']
#
# i3 = 'agua'
# lista_de_compra.append(i3)
# lista_de_compra.append('batata')
# print(lista_de_compra)
