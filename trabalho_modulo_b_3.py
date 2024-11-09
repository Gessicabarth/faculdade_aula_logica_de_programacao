print('Bem-vindos a Fábrica de Camisetas da Gessica Barth')


def escolha_modelo():
    """
    Solicita ao usuário a escolha do modelo da camiseta e retorna valor do modelo escolhido
    """

    print('MCS - Manga Curta Simples')
    print('MLS - Manga Longa Simples')
    print('MCE - Manga Curta Estampada')
    print('MLE - Manga Longa Estampada')

    while True:
        modelo = input('Qual o modelo desejado? ')

        if modelo == 'MCS':
            valor_do_modelo = 1.8
        elif modelo == 'MLS':
            valor_do_modelo = 2.1
        elif modelo == 'MCE':
            valor_do_modelo = 2.9
        elif modelo == 'MLE':
            valor_do_modelo = 3.2
        else:
            print('Modelo não existe. Tente novamente')
            continue
        return valor_do_modelo


def num_camisetas():
    """
    Solicita ao usuário a quatidade de camisetas e retorna a quantidade de camisetas com o desconto aplicado
    """

    while True:

        try:
            qtd = int(input("Quantas camisetas deseja?"))
        except ValueError:  # caso o usuário digitar algo que não seja um número
            print('Valor digitado inválido')
            continue

        if qtd < 20:
            desconto = 0 / 100
        elif qtd >= 20 and qtd < 200:
            desconto = 5 / 100
        elif qtd >= 200 and qtd < 2000:
            desconto = 7 / 100
        elif qtd >= 2000 and qtd <= 20000:
            desconto = 12 / 100
        else:
            print('Quantidade inválida')
            continue

        calculo = qtd * (1 - desconto)
        return calculo

def frete():
    """
    Solicita ao usuário o tipo de frete e retorna o valor extra do serviço de acordo com a opção desejada
    """

    print('Tipos de fretes:')
    print('1 - Frete por Transportadora - R$ 100.00')
    print('2 - Sedex - R$ 200.00')
    print('0 - Retirar na Fábrica - R$ 0.00')

    while True:
        tipo_frete = int(input('Qual o tipo de frete desejado? '))

        if tipo_frete == 1:
            valor_extra = 100.00
        elif tipo_frete == 2:
            valor_extra = 200.00
        elif tipo_frete == 0:
            valor_extra = 0
        else:
            print('Opção inválida')
            continue

        return valor_extra

modelo = escolha_modelo()
qtd_camisetas = num_camisetas()
valor_frete = frete()

total = modelo * qtd_camisetas + valor_frete
print(f'O valor do modelo escolhido foi: R$ {modelo}, a quantidade foi: {qtd_camisetas}, o valor do frete foi: R$ {valor_frete}, totalizando: R$ {round(total, 2)}')
