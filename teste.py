# CONDICIONAIS ANINHADAS
# EXERCÍCIO
# - ESCREVA UM ALGORITMO EM PYTHON EM QUE O USUÁRIO ESCOLHE SE QUER COMPRAR MAÇAS , LARANJAS OU BANANAS. DEVERÁ SER
# APRESENTADO NA TELA UM MENU COM AS OPÇÕES: 1 PARA MAÇA, 2 PARA LARANJA E 3 PARA BANANA
# -Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O Algoritmo deve calcular o preço total a
# pagar do produto escolhido e mostra-lo na tela
# - considere que uma maça custa R$2,30, uma laranja, R$3,60, e uma banana, R$ 1,85


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

print('Para maça digite 1, para laranja digite 2 e para banana digite 3')
produto = int(input('Digite a opção desejada \n'))
if produto == 1 or produto == 2 or produto == 3:
    quantidade = int(input('Quantas unidades?'))
    if produto == 1:
        produto = quantidade * 2.30
        print(f'O valor total é de: {produto}')
    else:
        if produto == 2:
            produto = quantidade * 3.60
            print(f'O valor total é de: {produto}')
        else:
            if produto == 3:
                produto = quantidade * 1.85
                print(f'O valor total é de: {produto}')
else:
    print('Produto indisponivel')
