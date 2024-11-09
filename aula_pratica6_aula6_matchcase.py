# EXERCICIO FEITO COM ELIF

print('Escolha o que deseja comprar: ')
print('1 - maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual a sua escolha? '))
qtd = int(input('Quantas unidades? '))

if produto == 1:
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maças. Total à pagar: {pagar}')
elif produto == 2:
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} laranjas. Total à pagar: {pagar}')
elif produto == 3:
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} bananas. Total à pagar: {pagar}')
else:
    print('Produto inexistente!')

# COMO RESOLVER ESSE MESMO EXERCICIO COM Match-Case

print('Escolha o que deseja comprar: ')
print('1 - maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual a sua escolha? '))
quantidade = int(input('Quantas unidades? '))

match (produto):
    case 1:
        pagar = quantidade * 2.3
        print(f'Você comprou {quantidade} maças. Total à pagar: {pagar}')
    case 2:
        pagar = quantidade * 3.6
        print(f'Você comprou {quantidade} laranjas. Total à pagar: {pagar}')

    case 3:
        pagar = quantidade * 1.85
        print(f'Você comprou {quantidade} bananas. Total à pagar: {pagar}')
    case _:
        print('Produto inexistente!')

'''
OUTRO EXERCICIO COM match-case
 - Checagem de tipo de um dado
'''
def checagem_tipo(dado):
    match dado:
        case str(dado):
            print("String:", dado)
        case int(dado):
            print("Inteiro:", dado)
        case float(dado):
            print("Float:", dado)
        case _:
            print("Tipo desconhecido de dado.")


dados = ['Python', 42, 3.14, 23, 'C']
for dado in dados:
    checagem_tipo(dado)



