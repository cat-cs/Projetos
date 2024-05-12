menu = """
    [E] Extrato
    [D] Depósito
    [S] Saque

    [Q] Sair
"""
saldo= 0.0
limite_saque= 500
num_saques= 0
limite_diario= 3
extrato= ""

while True:
    print("Bem vindo! Escolha abaixo suas opções:")
    opcao= input(menu)

    if opcao== "d":
        print("-DEPÓSITO-")
        deposito= float(input("Digite o valor a ser depositado:"))

        if deposito>0:
            saldo += deposito
            extrato += f"Depósito= R$ {deposito:.2f}\n"
            print("---Depósito relizado com sucesso---")
        else:
            print("---Digite um valor válido---")

    elif opcao== "s":
        print("-SAQUE-")
        saque= float(input("Digite o valor a ser sacado:"))

        sem_saldo= saldo< saque
        sem_saque= num_saques >= limite_diario
        sem_limite= limite_saque < saque

        if sem_saldo:
            print("---Saldo insuficiente para transação---")
        elif sem_saque:
            print("---Você ultrapassou seu limite diário de saques---")
        elif sem_limite:
            print(f"---O valor ultrapassa seu limite para saques. Seu limite atual é: R$ {limite_saque} ---")
        elif saque>0:
            saldo-= saque
            num_saques += 1
            extrato += f"Saque= R$ {saque:.2f}\n"
            print("---Saque realizado com sucesso---")
        else:
            print("---Digite um valor válido---")
   
    elif opcao == "e":
        print("-EXTRATO-")
        print("Não houve movimentações" if not extrato else extrato)
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
    
    elif opcao== "q":
        break

    else:
        print("---Selecione uma opção válida---")