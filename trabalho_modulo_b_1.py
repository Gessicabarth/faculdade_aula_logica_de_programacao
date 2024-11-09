print('Bem-vindos a loja da Gessica Barth')
valor_do_pedido = float(input('Qual o valor do pedido?'))
quantidade_de_parcelas = int(input('Qual a quantidade de parcelas?'))

if quantidade_de_parcelas < 4:  # Quantidade de parcelas menor que 4, juros 0%
    juros = 0 / 100
elif quantidade_de_parcelas >= 4 and quantidade_de_parcelas < 6:  # Quantidade de parcelas entre [4 e 6), juros 4%
    juros = 4 / 100
elif quantidade_de_parcelas >= 6 and quantidade_de_parcelas < 9:  # Quantidade de parcelas entre [6 e 9), juros 8%
    juros = 8 / 100
elif quantidade_de_parcelas >= 9 and quantidade_de_parcelas < 13:  # Quantidade de parcelas entre [9 e 13), juros 16%
    juros = 16 / 100
else:
    juros = 32 / 100   # a cima de 16, juros 32%

valor_da_parcela = valor_do_pedido * (1 + juros) / quantidade_de_parcelas
valor_total_parcelado = valor_da_parcela * quantidade_de_parcelas

print(f'O valor da parcela é: R$ {round(valor_da_parcela, 2)}')
print(f'O valor total parcelado é: R$ {round(valor_total_parcelado, 2)}')