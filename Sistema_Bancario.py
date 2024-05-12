menu = """
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [9] Sair

=> """

SAQUES_DIARIOS = 3
saldo = 0
extrato = ""
limite = 500
numero_saques = 0

message = """
        Bem vindo ao Banco!

        Digite a operação que deseja realizar: 
"""
print(message)

while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("\nDigite o valor que deseja depositar: "))

        if deposito >= 0:
            saldo += deposito
            extrato += f"Depósito R${deposito: .2f}\n"

            print("\nValor depositado com sucesso!\n")
        else:
            print("Operação falhou! Não é permitido o deposito de valores negativos!")
    
    elif opcao == 2:
        if numero_saques < SAQUES_DIARIOS:
            saque = float(input("\nDigite o valor que deseja sacar: "))

            if saque >= 0:
                if saque <= limite:
                    if saque <= saldo:
                        saldo -= saque
                        numero_saques += 1
                        extrato += f"Saque R${saque: .2f}\n"

                        print("\nSaque efetuado, retire o dinheiro do caixa.\n")

                    else:
                        print("Operação falhou! Saldo insuficiente.")

                else:
                    print("Operação falhou! O valor solicitado para saque é maior do que o limite de saques diarios.")

            else:
                print("Operação falhou! Não é possivel sacar um valor negativo!")

        else:
            print("Operação falhou! Quantidade de saques diarios excedidos!")
    
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo total R${saldo: .2f}")
        print("==========================================")

    elif opcao == 9:
        break
    
    else:
        print("Operação invalida, digite novamente qual operação deseja: ")