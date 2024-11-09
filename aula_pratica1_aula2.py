# 1. desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a
# ele. calcule e exiba o valor do desconto e o preço final do produto

preco = float(input('digite o preço do produto: '))
percentual = float(input('digite o percentual de desconto (0-100%): '))

desconto = preco * (percentual / 100)
final = preco - desconto

print(f'o preço do produto é {preco}. desconto de {percentual}%')
print(f'o valor calculado de desconto: {desconto}. valor final do produto {final}')

# 2. escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a
# quatidade de dias pelos quais o carro foi alugado. calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
# e R$ 0,15 por km rodado

km = int(input('quantos km foram percorridos? '))
dias = int(input('quantos dias foram percorridos? '))

preco = 60 * dias + 0,15 * km
print(f'km = {km}. dias: {dias}.')
print(f'o valor a ser pago: {preco}.')

# 3. crie uma variavel de string que receba uma frase qualquer. crie uma segunda variável, agora contendo a metade da
# string digitada. imprima na tela somente os dois ultimos caracteres da segunda variável do tipo string

frase = input('digite uma frase: ')
tam = len(frase)

frase2 = frase[:int(tam/2)]

print(frase2[-2:])