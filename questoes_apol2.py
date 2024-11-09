# questões apol 2
# Questão 3

cont = 5
soma = 0
while cont <= 25:
    soma = soma + cont
    cont = cont + 5
print(soma)

# questão 4

x = int(input('digite um valor no intervalo de -100 ate 100: '))
while x > 100 or x < -100:
    x = int(input('digite um valor no intervalo de -100 ate 100: '))
print('encerrando...')

for i in range(7, 26, 3):
    print(i)

for i in range(100, 1000, 10):
    print(i)

i = 100
while i <= 999:
    print(i)
    i += 10


x = 10
while x <= 100:
    print(x)
    x += 1

x = 5
print(x)
x += 5
# x = x + 5
x -= 5
x *= 5
print(x)
x += 5
print(x)
x += 5
print(x)
x += 5
print(x)

x = 5
while x <= 25:
    print(x)
    x += 5

for i in range(10, 20):
    for j in range(10, 20, 2):
        print('{} + {} = {}'. format(i, j, i + j))

# for i in range(10, 20):
x = 10
while x < 20:
    for j in range(10, 20, 2):
        print('{} + {} = {}'. format(x, j, x + j))
    x += 1

lista = ['ovos', 'banana', 'sorvete']
for item in lista:
    print(item)

i = 88
while i >= 0:
    print(i)
    i -= 4

for i in range(88, -1, -4):
    print(i)

# testando break e continue
for i in range(0, 10):
    if i == 5:
        continue
    if i == 7:
        break
    print(i)