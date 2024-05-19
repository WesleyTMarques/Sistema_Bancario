menu = """
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Nova Conta
        [5] Listar Contas
        [6] Novo Usuário
        [9] Sair

=> """

SAQUES_DIARIOS = 3
AGENCIA = "0001"

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
users = []
contas = []

message = """
        Bem vindo ao Banco!

        Digite a operação que deseja realizar: 
"""
print(message)

while True:

    def deposito(saldo, valor, extrato, /):

        if valor >= 0:
            saldo += valor
            extrato += f"Depósito R${valor: .2f}\n"

            print("\nValor depositado com sucesso!\n")
        else:
            print("Operação falhou! Não é permitido o deposito de valores negativos!")


        return saldo, extrato
    
    def realizar_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        if valor > 0:
            if valor <= limite:
                if valor <= saldo:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque R${valor: .2f}\n"

                    print("\nSaque efetuado, retire o dinheiro do caixa.\n")

                else:
                    print("Operação falhou! Saldo insuficiente.")

            else:
                print("Operação falhou! O valor solicitado para saque é maior do que o limite de saques diarios.")

        else:
            print("Operação falhou! Não é possivel sacar um valor zerado ou negativo!")

        return saldo, extrato
    
    def mostra_extrato(saldo, /, *, extrato):
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo total R${saldo: .2f}")
        print("==========================================")

        return saldo, extrato

    def cad_user(usuarios):
        cpf = input("Informe o CPF (somente números): ")
        usuario = users_filters(cpf, usuarios)

        if usuario:
            print("\n Usuário já cadastrado")
            return

        nome = input("Informe o nome completo: ")
        data_nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado): ")

        users.append({"nome": nome, "data_nasc": data_nasc, "cpf":cpf, "endereco": endereco})

        print("\nUsuário criado com sucesso!")

    def users_filters(cpf, user):
        find_user = [usuario for usuario in user if usuario["cpf"] == cpf]
        return find_user[0] if find_user else None

    def cad_contas(agencia, numero_conta, user):
        cpf = input("Gentileza informar o CPF para cadastro da conta: ")
        usuario = users_filters(cpf, user)

        if usuario:
            print("\n Conta criada com sucesso!")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
        print("\n Usuário não encontrado! Operação canelada.")

    def listar_contas(contas):
        for conta in contas:
            linha = f"""\
                Agência: {conta['agencia']}
                C/C: {conta['numero_conta']}
                Titular: {conta['usuario']['nome']}
            """
            print("=" * 100)
            print(linha)

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("\nDigite o valor que deseja depositar: "))

        saldo, extrato = deposito(saldo, valor, extrato)
    
    elif opcao == 2:
        if numero_saques < SAQUES_DIARIOS:
            valor = float(input("\nDigite o valor que deseja sacar: "))

            saldo, extrato = realizar_saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=SAQUES_DIARIOS)

        else:
            print("Operação falhou! Quantidade de saques diarios excedidos!")
    
    elif opcao == 3:
        saldo, extrato = mostra_extrato(saldo, extrato=extrato)

    elif opcao == 4:
        numero_conta = len(contas) + 1
        conta = cad_contas(AGENCIA, numero_conta, users)

        if conta:
            contas.append(conta)

    elif opcao == 5:
        listar_contas(contas)

    elif opcao == 6:
        cad_user(users)

    elif opcao == 9:
        break
    
    else:
        print("Operação invalida, digite novamente qual operação deseja: ")