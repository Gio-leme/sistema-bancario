menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True :
    opção = input(menu)
    if opção == 'd':
        valor = float(input('por favor me infome o valor?'))

        if valor >0:
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"
            
        else:
            print("operação errada! o valor informado é invalido.")

    elif opção == "s":
        valor = float(input("Informe valor do saque? "))
        ultrapassou_saldo =valor > saldo
        ultrapassou_limite = valor> limite
        ultrapassou_saque = numero_saques >= LIMITE_SAQUES
        
        if ultrapassou_saldo:
            print("operação errada! não tem saldo suficiente.")
            
        elif ultrapassou_limite:
            print(" operação errada! o valor do saque excedeu limite.")

        elif ultrapassou_saque :
            print(" operação errada! numero de saque excedido.")

        elif saldo > 0:
                saldo -= valor
                extrato += f"Saque :R$ {valor:.2f}\n"
                numero_saques += 1

        else:
            print("operação errada! o valor informado é invalido.")

    elif opção == "e":
        print("\n =======EXTRATO======")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n saldo ; R$ {saldo :.2f}")
        print("===================================")

    elif opção == "q":
        break

    else:
        print("operação invalida! por favor selecione a opção desejada.") 
        

