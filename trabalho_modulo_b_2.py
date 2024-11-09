print('Bem-vindos a loja de marmitas da Gessica Barth')
print('                      MENU                         ')
print('Tamanho | Bife Acebolado (BA) | Filé de Frango (FF)')
print('  P     |     16.00           |     15.00          ')
print('  M     |     18.00           |     17.00          ')
print('  G     |     22.00           |     21.00          ')

total_pedido = 0

while True:  # repete enquanto cliente desejar mais alguma coisa
    while True:
        sabor = input('Escolha o sabor desejado (BA/FF): ')
        if sabor != 'BA' and sabor != 'FF':
            print('Sabor inválido. Tente novamente.')
        else:
            break

    tamanho = input('Escolha a opção do tamanho desejado (P/M/G): ')

    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente')
        continue  # caso o cliente erre o tamanho voltará a primeira pergunta sobre o sabor

    if sabor == 'BA':
        if tamanho == 'P':
            total_pedido += 16.00
            print(f'Você pediu um Bife Acebolado no tamanho {tamanho}: R$ 16.00')
        elif tamanho == 'M':
            total_pedido += 18.00
            print(f'Você pediu um Bife Acebolado no tamanho {tamanho}: R$ 18.00')
        else:  # Para G
            total_pedido += 22.00
            print(f'Você pediu um Bife Acebolado no tamanho {tamanho}: R$ 22.00')
    else:  # Para FF
        if tamanho == 'P':
            total_pedido += 15.00
            print(f'Você pediu um Filé de Frango no tamanho {tamanho}: R$ 15.00')
        elif tamanho == 'M':
            total_pedido += 17.00
            print(f'Você pediu um Filé de Frango no tamanho {tamanho}: R$ 17.00')
        else:  # Para G
            total_pedido += 21.00
            print(f'Você pediu um Filé de Frango no tamanho {tamanho}: R$ 21.00')

    resposta = input('Deseja pedir mais alguma coisa? ')

    if resposta != 'sim':
        print(f'O total do pedido ficou: {total_pedido}')
        break
        