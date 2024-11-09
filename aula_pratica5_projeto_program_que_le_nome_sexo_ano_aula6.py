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
cadastro = {'nome': [], 'sexo': [], 'ano': []}

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

# precisa finalizar
