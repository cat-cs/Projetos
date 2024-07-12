

#MENU 1
def criar_user ():
    
    pessoa= dict(nome="", nasc="", cpf="")
    endereco= dict(logadouro="", num="", cidade="", estado="")
    
   
    pessoa['nome']= input("Digite seu nome completo--")
    pessoa['nasc']= input ("Digite sua data de nascimento (DD/MM/AA)--")
        
    while True:
        cpf_pessoa = input ("Digite seu CPF (Apenas números)--" )
        if len(cpf_pessoa)== 11 and cpf_pessoa != pessoa['cpf']:   
            pessoa['cpf']= cpf_pessoa
            break
        else:     
            print("Digite um CPF válido!--")  
   
    endereco['logadouro'] = input("Qual seu logadouro?--")
    endereco['num'] = input ("Digite o número da residência--")
    endereco['cidade'] = input ("Digite o nome de sua cidade--")
    endereco['estado'] = input ("Digite a sigla de seu estado--")
        
    pessoa['endereco']= endereco
        
    return pessoa
      
def criar_conta(usuario):
    conta= dict(agnc="001", num_conta=0, cpf=0)
    
    while True:
        cpf_conta= input ("Digite seu CPF")   
        if cpf_conta == usuario['cpf']:   
            conta['num_conta'] =+ 1
            conta['cpf']= cpf_conta
            break
        elif cpf_conta != usuario['cpf']:
            print("CPF não cadastrado. Crie uma conta no menu.")
        else:
            print("CPF inválido")
    
    return conta
            
def login_conta (usuario, conta_user):
    login_cpf = int(input("Digite seu CPF:"))
    login_numconta = int (input("Digite o número de sua conta:"))

    if login_cpf == conta_user['cpf'] and login_numconta == conta_user['num_conta_user']:
        print (f"Bem vindo {usuario['nome']}")
    else:
        print("Conta não localizada! Crie um usuário/conta e tente novamente.")


#MENU 2

def depositar (saldo, deposito, extrato):
    if deposito>0:
        saldo += deposito
        extrato += f"Depósito= R$ {deposito:.2f}\n"
        print("---Depósito relizado com sucesso---")
    else:
        print("---Digite um valor válido---")
    return saldo, extrato

def sacar (saldo, limite_saque, num_saques, extrato, saque, sem_saldo, sem_saque, sem_limite):
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
    return saldo, extrato

def extrair (saldo, extrato):
    print("-EXTRATO-")
    print("Não houve movimentações" if not extrato else extrato)
    print(f"Seu saldo atual é de: R$ {saldo:.2f}")
    return saldo, extrato