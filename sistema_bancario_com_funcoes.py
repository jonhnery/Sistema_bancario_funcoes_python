
def depositar(saldo, valor, extrato,/):
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("\nDepósito realizado")
            else:
                print("\nO valor informado é inválido")
            
            return saldo, extrato
 

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
            if valor > saldo:
                print("Saldo insuficiente")

            elif valor > limite:
                print("Valor de saque excede o limite por operação")

            elif numero_saques >= LIMITE_SAQUES:
                print("Limite de saque diário excedido")
            
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("\nSaque realizado!")

            else:
                print("O valor informado é inválido")
            
            return saldo, extrato

def exbir_extrato(saldo, /, *, extrato):
            print("\n########## EXTRATO ##########")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("#".center(40,"#"))

def criar_usuario(usuarios):
     cpf = input("Informe o CPF (somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\nJá existe usuário com esse CPF!")
          return
     nome = input("Informe o nome: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

     print("Usuario criado!")
    

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, nro_conta, usuarios):
     cpf = input("Informe o cpf do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          return {"agencia": agencia,"nro_conta": nro_conta, "usuario": usuario}
     
     print("\nUsuário não encontrado, conta não criada!")     

def listar_contas(contas):
     for conta in contas:
          linha = f"""\
                Agência:\t{conta['agencia']}
                Conta:\t\t{conta['nro_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
          print("m" * 100)
          print(linha)
          

     

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    nro_conta = 1

    while True:
        print("""   MENU    
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Novo Usuário
            [5] Nova Conta
            [6] Listar Contas
            [0] Sair     
            """)
        opcao = int(input("Digite sua opção: "))

        if opcao == 1: #depositar#
            valor = float(input("Valor do depósito: "))

            saldo, extrato = depositar(saldo,valor,extrato)

        
        elif opcao == 2: #sacar#
            valor = float(input("Valor de saque: "))

            saldo, extrato = sacar(
                 saldo=saldo,
                 valor=valor,
                 extrato=extrato,
                 limite=limite,
                 numero_saques=numero_saques,
                 LIMITE_SAQUES=LIMITE_SAQUES,
            )
            
        elif opcao == 3: #extrato#
            exbir_extrato(saldo,extrato=extrato)

        elif opcao == 4: #criar usuario#
             criar_usuario(usuarios)
        
        elif opcao == 5: #criar conta#
             conta = criar_conta(AGENCIA, nro_conta, usuarios)

             if conta:
                  contas.append(conta)
                  nro_conta += 1
                  print("\nConta Criada")
        
        elif opcao == 6: #listar contas#
             listar_contas(contas)

        elif opcao == 0: #sair#
            break
        else:
            print("Opção Inválida")



main()



        




