# da aula 2

# EXPRESSÕES ALGÉBRICAS
# - Escreva as seguintes expressoes algébricas em linguagem de python:
# a) o somatório dos 5 primeiros números inteiros e positivos
# b) a média entre 23,19 e 31
# c) o número de vezes que 73 cabe em 403
# d) a sobra quando 403 é dividido por 73

print(1 + 2 + 3 + 4 + 5)  # a)
print((23 + 19 + 31) / 3)  # b)
print(403 // 73)  # c)
print(403 % 73)  # d)

# e) 2 elevado à 10ª potencia
# f) o valor absoluto da diferença entre 54 e 57
# g) o menor valor entre 34, 29 e 31

print(2 ** 10)  # e)
print(abs(54 - 57))  # f)   abs() para saber o valor absoluto
print(min(34, 29, 31))

# ATRIBUIÇÃO
# - Escreva as expressões em python para:
# a) atribuir o valor inteiro 3 à variável a
# b) atribuir o valor 4 à variavel b
# c) atribuir à variavel c o valor da expressão a*a + b*b

a = 3  # a)
b = 4  # b)
c = a * a + b * b  # c)
print(c)

# STRINGS
# Execute as seguintes atribuições:
# s1 = 'ant'
# s2 = 'bat'
# s3 = 'cod'

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# agora, utilizando operadores + e *, crie as saídas a seguir:
# a) 'ant bat cod'
# b) 'ant ant ant ant ant ant ant ant ant ant '
# c) 'ant bat bat cod cod cod'
# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'

res = s1 + ' ' + s2 + ' ' + s3  # a)
print(res)

res = 10 * (s1 + ' ')  # a)
print(res)

res = 10 * (s1 + ' ') + 2 * (s2 + ' ') + 3 * (s3 + ' ')  # c)
print(res)

# d) fazer

# e) fazer
