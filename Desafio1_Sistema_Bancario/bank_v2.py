import datetime

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    numero_conta = 0
    agencia = "0001"

    def __init__(self, usuario):
        Conta.numero_conta += 1
        self.numero_conta = Conta.numero_conta
        self.agencia = Conta.agencia
        self.usuario = usuario
        self.saldo = 0

    def __str__(self):
        return f"Agência: {self.agencia} - Número da Conta: {self.numero_conta} - Titular: {self.usuario.nome}"

# Listas para armazenar os usuários e contas
usuarios = []
contas = []

# Função para criar um novo usuário
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (formato: dd/mm/aaaa): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário: ")

    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado. Não é possível criar o usuário.")
            return

    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso.")

# Função para criar uma nova conta
def criar_conta():
    cpf = input("Digite o CPF do usuário para vincular à conta: ")

    # Verifica se o CPF do usuário existe
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("Usuário não encontrado. Não é possível criar a conta.")
        return

    nova_conta = Conta(usuario_encontrado)
    contas.append(nova_conta)
    print(f"Conta criada com sucesso. Número da conta: {nova_conta.agencia} {nova_conta.numero_conta}")

# Função para listar as contas e seus respectivos titulares
def listar_contas():
    for conta in contas:
        print(conta)

# Função para desativar uma conta
def desativar_conta():
    numero_conta = int(input("Digite o número da conta que deseja desativar: "))

    conta_encontrada = None
    for conta in contas:
        if conta.numero_conta == numero_conta:
            conta_encontrada = conta
            break

    if conta_encontrada is None:
        print("Conta não encontrada.")
        return

    contas.remove(conta_encontrada)
    print("Conta desativada com sucesso.")


# Variáveis para armazenar os depósitos e saques
movimentacoes = []
data_ultima_operacao = None
limite_saques_diarios = 3

# Saldo inicial da conta
saldo = 0

# Função para realizar um depósito em uma conta específica
def depositar():
    numero_conta = int(input('Digite o número da conta em que deseja depositar: '))
    valor = float(input('Digite o valor que deseja depositar: '))

    # Encontra a conta com o número fornecido
    conta_encontrada = None
    for conta in contas:
        if conta.numero_conta == numero_conta:
            conta_encontrada = conta
            break

    if conta_encontrada is None:
        print("Conta não encontrada.")
        return

    # Realiza o depósito na conta encontrada
    conta_encontrada.saldo += valor
    movimentacoes.append(f'Depósito na Conta {numero_conta}: R$ {valor:.2f}')
    atualizar_data_ultima_operacao()

# Restante do código...

# Função para realizar um saque
def sacar():
    numero_conta = int(input('Digite o número da conta em que deseja sacar: '))
    valor = float(input('Digite o valor que deseja sacar: '))

    # Encontra a conta com o número fornecido
    conta_encontrada = None
    for conta in contas:
        if conta.numero_conta == numero_conta:
            conta_encontrada = conta
            break

    if conta_encontrada is None:
        print("Conta não encontrada.")
        return

    global limite_saques_diarios
    if conta_encontrada.saldo >= valor:
        if limite_saques_diarios > 0:
            conta_encontrada.saldo -= valor
            movimentacoes.append(f'Saque na Conta {numero_conta}: R$ {valor:.2f}')
            limite_saques_diarios -= 1
            atualizar_data_ultima_operacao()
        else:
            print('Limite de saques diários atingido')
    else:
        print('Saldo insuficiente')


# Função para atualizar a data da última operação
def atualizar_data_ultima_operacao():
    global data_ultima_operacao
    data_ultima_operacao = datetime.date.today()

# Função para exibir o extrato
def extrato():
    numero_conta = int(input('Digite o número da conta que deseja ver o extrato: '))

    # Encontra a conta com o número fornecido
    conta_encontrada = None
    for conta in contas:
        if conta.numero_conta == numero_conta:
            conta_encontrada = conta
            break

    if conta_encontrada is None:
        print("Conta não encontrada.")
        return

    if len(movimentacoes) > 0:
        for movimentacao in movimentacoes:
            if f'Conta {numero_conta}' in movimentacao:
                print(movimentacao)
        print(f'Saldo atual da Conta {numero_conta}: R$ {conta_encontrada.saldo:.2f}')
    else:
        print('Não foram realizadas movimentações')

# Verifica se a data atual é diferente da data da última operação e redefine o limite de saques diários
def verificar_novo_dia():
    global limite_saques_diarios
    if data_ultima_operacao != datetime.date.today():
        limite_saques_diarios = 3

# interação com o usuário
while True:
    verificar_novo_dia()

    print('######## MENU ########')
    print('    1 - Criar Usuário')
    print('    2 - Criar Conta')
    print('    3 - Listar Contas')
    print('    4 - Depositar')
    print('    5 - Sacar')
    print('    6 - Extrato')
    print('    7 - Desativar Conta')
    print('    8 - Sair')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        criar_usuario()
    elif opcao == '2':
        criar_conta()
    elif opcao == '3':
        listar_contas()
    elif opcao == '4':
        depositar()
    elif opcao == '5':
        sacar()
    elif opcao == '6':
        extrato()
    elif opcao == '7':
        desativar_conta()
    elif opcao == '8':
        break
    else:
        print('Opção inválida')
