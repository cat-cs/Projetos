from banco_funcao import *

menu_1 = """
    
    [1] Criar usuário
    [2] Criar Conta
    [3] Entrar na conta
"""

menu_2 = """
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
    opcao= input(menu_1)

    if opcao== "1":
        print("-Vamos criar seu usuário-")
        usuario= criar_user()
        print ("-Seu usuário foi criado!-", usuario)
    
    elif opcao == "2":
        
        conta_user= criar_conta(usuario)

        print ("--Conta criada com sucesso--")
        print (f">>Agência: {conta_user['agnc']}")
        print (f">>Número Conta: {conta_user['num_conta']}")
        print (f">>CPF: {conta_user['cpf']}")
    elif opcao== "3":
        login_conta(usuario, conta_user)
        break


while True:
    print("Bem vindo! Escolha abaixo suas opções:")
    opcao= input(menu_2)

    if opcao== "d":
        print("-DEPÓSITO-")
        deposito= float(input("Digite o valor a ser depositado:"))
        saldo, extrato= depositar (saldo, deposito, extrato)
        
    elif opcao== "s":
        print("-SAQUE-")
        saque= float(input("Digite o valor a ser sacado:"))

        sem_saldo= saldo< saque
        sem_saque= num_saques >= limite_diario
        sem_limite= limite_saque < saque

        saldo, extrato = sacar (saldo, limite_saque, num_saques, extrato, saque, sem_saldo, sem_saque, sem_limite)
    
    elif opcao == "e":
        saldo, extrato = extrair (saldo, extrato)
        
    elif opcao== "q":
        break

    else:
        print("---Selecione uma opção válida---")