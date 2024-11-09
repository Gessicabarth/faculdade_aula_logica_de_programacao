# NOSSA PRIMEIRA FUNÇÃO

print('|', '__' * 10, '|')
print('|', '__' * 10, '|')
print('            MENU')
print('|', '__' * 10, '|')
print('|', '__' * 10, '|')


# CRIANDO NOSSA FUNÇÃO DO EXEMPLO ACIMA

def realce():
    # corpo da função
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')


# Programa principal
realce()
print('            MENU')
realce()


# PARÂMETROS EM FUNÇÕES

def realce(s1):
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')
    print(s1)
    print('|', '__' * 10, '|')
    print('|', '__' * 10, '|')


# Programa principal
realce('            MENU')


def sub2(x, y):
    res = x - y
    print(res)


# Programa principal
sub2(7, 5)


# PARAMETROS OPCIONAIS

def soma3(x, y, z):
    res = x + y + z
    print(res)


def soma3(x=0, y=0, z=0):
    res = x + y + z
    print(res)


soma3(1, 2, 3)
soma3(1, 2)  # z foi omitido
soma3(1)  # y e z foram omitidos
soma3()  # x, y e z foram omitidos


# exercício aula 5 -
# Escreva uma rotina que crie uma borda ao redor de uma palavra, para destacá-la como seno um título. A rotina deve
# receber como parametro a palavra a ser destacada. O tamanho da caixa de texto deverá ser adaptável, de acordo com o
# tamanho da palavra. Por exemplo:   +--------+   +---+
#                                    |VINICIUS|   |OLÁ|
#                                    +--------+   +---+

def borda(s1):
    tamanho = len(s1)
    # só imprime caso exista algum caractere
    if tamanho:
        print('+', '-' * tamanho, '+')
        print('|', s1, '|')
        print('+', '-' * tamanho, '+')


# Programa principal
borda('Olá, mundo!')
borda('Lógica de Programação e Algoritmos')


# ESCOPO DE VARIÁVEIS

def omelete():
    print(ovos)  # variável local


# Programa principal
ovos = 12  # variavel global
omelete()

'''exemplo 1:

def omelete():
    ovos = 12
    bacon()
    print(ovos)

def bacon():
    ovos = 6

# Programa principal
omelete()'''

'''exemplo 2:

def omelete():
    global ovos
    ovos = 6
    bacon()
    
def bacon():
    ovos = 12
    pimenta()
    
def pimenta():
    print(ovos)
    
# Programa Principal
ovos = 4
omelete()
print(ovos)
'''


# RETORNO DE VALORES EM FUNÇÕES

def soma3(x=0, y=0, z=0):
    res = x + y + z
    return res


# Programa principal
retornado = soma3(1, 2, 3)
print(retornado)

# forma alternativa simplificada
print(soma3(2, 2))

# Programa principal
retornado1 = soma3(1, 2, 3)
retornado2 = soma3(1, 2)
retornado3 = soma3()
print(f'Somatórios: {retornado1}, {retornado2}, e {retornado3}.')

'''Exercicios
- escreva uma função para validar uma string. Essa função recebe como parâmetro a string, o número mínimo e máximo de 
caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de minimo e máximo, e falso, caso 
contrário.
'''


def validar_string(palavra, minimo, maximo):
    if len(palavra) > minimo and len(palavra) < maximo:
        return True
    else:
        return False


# programa principal
res = validar_string('Gabriel', 0, 15)
print(res)

''' exemplo de correção de erro:
while True:
    try:
        x=int(input('Por favor digite um número: '))
        break
    except ValueError:
        print('Oops! Número inálido. Tente novamente...')
'''
# FUNÇÃO LAMBDA

res = lambda x: x * x
print(res(3))

soma = lambda x, y: x + y
print(soma(3, 5))

''' exercicio
- faça uma função lambda que recebe dois valores numérico como parametro. Ao primeiro valor, sempre some 5. Em seguida,
multiplique ambos e retorne o resultado
'''

dois_valores_numericos = lambda x, y: (x+5) * y
print(dois_valores_numericos(5,10))
