import datetime

# Variáveis para armazenar os depósitos e saques
movimentacoes = []
data_ultima_operacao = None
limite_saques_diarios = 3

# Saldo inicial da conta
saldo = 0

# Função para realizar um depósito
def depositar():
    valor = float(input('Digite o valor que deseja depositar: '))
    global saldo
    saldo += valor
    movimentacoes.append(f'Depósito: R$ {valor:.2f}')
    atualizar_data_ultima_operacao()

# Função para realizar um saque
def sacar():
    valor = float(input('Digite o valor que deseja sacar: '))
    global saldo, limite_saques_diarios
    if saldo >= valor:
        if limite_saques_diarios > 0:
            saldo -= valor
            movimentacoes.append(f'Saque: R$ {valor:.2f}')
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
    if len(movimentacoes) > 0:
        for movimentacao in movimentacoes:
            print(movimentacao)
        print(f'Saldo atual: R$ {saldo:.2f}')
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
    print('    1 - Depositar')
    print('    2 - Sacar')
    print('    3 - Extrato')
    print('    4 - Sair')
    
    opcao = input('Digite a opção desejada: ')
    
    if opcao == '1':
        depositar()
    elif opcao == '2':
        sacar()
    elif opcao == '3':
        extrato()
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
