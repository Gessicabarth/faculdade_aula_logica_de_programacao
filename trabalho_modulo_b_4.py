print('Bem-vindos a empresa da Gessica Barth')
lista_funcionario = []
id_global = 4836005


def cadastrar_funcionario(id):
    nome = input('Digite o nome: ')
    setor = input('Digite o setor: ')
    salario = input('Digite o salario do funcionário: ')

    funcionario = {
        'nome': nome,
        'setor': setor,
        'salario': salario,
        'id': id
    }

    lista_funcionario.append(funcionario.copy())


def consultar_funcionarios():
    while True:
        print('1. Consultar Todos \n2. Consultar por Id \n3. Consultar por Setor \n4. Retornar ao menu')

        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            for funcionario in lista_funcionario:
                for chave, valor in funcionario.items():
                    print(f'{chave}: {valor}')
        elif opcao == 2:
            id = int(input('Informe o ID para busca: '))
            for funcionario in lista_funcionario:
                if funcionario['id'] == id:
                    print(f'Nome: {funcionario['nome']}')
                    print(f'Setor: {funcionario['setor']}')
                    print(f'Salario: {funcionario['salario']}')
                    print(f'Id: {funcionario['id']}')
        elif opcao == 3:
            setor = input('Informe o setor para busca: ')
            for funcionario in lista_funcionario:
                if funcionario['setor'] == setor:
                    print(f'Nome: {funcionario['nome']}')
                    print(f'Setor: {funcionario['setor']}')
                    print(f'Salario: {funcionario['salario']}')
                    print(f'Id: {funcionario['id']}')
        elif opcao == 4:
            return
        else:
            print('Opção inválida')
            continue


def remover_funcionario():
    id = int(input('Infome o ID do funcionário que deseja remover: '))
    for funcionario in lista_funcionario:
        if funcionario['id'] == id:
            lista_funcionario.remove(funcionario)
            print('Funcionário removido com sucesso!')
            return
    print('Id Inválido')


while True:
    print('1. Cadastrar Funcionário \n2. Consultar Funcionário \n3. Remover Funcionário \n4. Encerrar Programa')
    opcao_desejada = int(input('Digite a opção desejada: '))
    if opcao_desejada == 1:
        id_global = id_global + 1
        cadastrar_funcionario(id_global)
    elif opcao_desejada == 2:
        consultar_funcionarios()
    elif opcao_desejada == 3:
        remover_funcionario()
    elif opcao_desejada == 4:
        break
    else:
        print('Opção inválida. Tente novamente.')
        continue
