def saque(*,saldo, valor, extrato, numero_saques, LIMITE_SAQUES, limite):
    if valor > saldo:
        print("\n Saldo insuficiente!")
    elif valor > limite:
        print("\n Valor do saque ultrapassou o limite diário permitido!")
    elif numero_saques >= LIMITE_SAQUES:
        print("\n Número máximo de saques atingido!")
    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque de R${valor:.2f}\n"
        numero_saques += 1
        print(f"\n Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("\n Valor inválido, o saque deve ser maior que zero!")
    return saldo, extrato, numero_saques



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
    if not contas:
        print("\n Não há contas para serem listadas.\n")
    else:
        for conta in contas:
            agencia = f"Agência:\t{conta['agencia']}"
            numero_conta = f"C/C:\t\t{conta['numero_conta']}"
            titular = f"Titular:\t{conta['usuario']['nome']}"

            print("=" * 100)
            print(agencia)
            print(numero_conta)
            print(titular)

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R${valor:.2f}\n"
        print(f"\n Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("\n Valor inválido, o depósito deve ser maior que zero!")
    return saldo, extrato

def imprimir_extrato(saldo, contas, /, *, extrato=""):
    print("\n" + "=" * 100)
    print("EXTRATO".center(35))
    print("=" * 100)

    if not contas:
        print("\n Você precisa criar uma conta corrente para visualizar o extrato!")

    else:
        if not extrato:
                print("\n Não foram realizadas movimentações nessa conta.".center(35))
        else:
            for linha in extrato.split('\n'):
                if linha:
                    print(linha.center(35))
    if contas:
        print("=" * 100)
        print(f"Saldo: R${saldo:.2f}".center(35))
        print("=" *100)


def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for user in usuarios:
        if user ["cpf"] == str(cpf):
            print("\n Usuário com CPF já cadastrado.")
            return usuarios
    nome = nome.capitalize()
    usuario = {"nome":nome, "data_nascimento":data_nascimento, "cpf":str(cpf),"endereço":endereco}
    usuarios.append(usuario)
    print(f"\n Novo usuário {nome} cadastrado com sucesso!")
    return usuarios


def criar_conta_corrente(contas, usuarios, cpf):
    usuario_encontrado = filtrar_usuario(cpf, usuarios)

    if usuario_encontrado:
        for conta in contas:    
            if conta["usuario"]["cpf"] == str(cpf):
                print("\n Este usuário já possui uma conta corrente.")
                return contas
                
        numero_conta = len(contas) + 1
        conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario_encontrado}
        contas.append(conta)
        print("\n Conta corrente criada com sucesso!")
    else:
        print("\n Usuário não encontrado, cadastre-se primeiro para poder criar sua nova conta!")

    return contas



def main ():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Novo Usuário
    [lc] Listar Contas
    [cc] Nova Conta Corrente
    [q] Sair

    => """

    while True:

        opcao = input(menu)

        if opcao == 'd':
            if not contas:
                print("Você precisa criar uma conta corrente para realizar depósitos!")
            else:
                valor = float(input("Informe o valor do depósito: "))
                saldo,extrato = deposito(saldo, valor, extrato)

        elif opcao == 's':
            if not contas:
                print("Você precisa criar uma conta corrente para realizar saques!")
            else:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = saque(
                    saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=
                    numero_saques, LIMITE_SAQUES=LIMITE_SAQUES
                )


        elif opcao == 'e':
           imprimir_extrato(saldo, contas, extrato=extrato)


        elif opcao == 'c':
            nome = input("Informe o nome: ")
            data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
            cpf = input("Informe o CPF (somente números): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            usuarios = criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)
            

        elif opcao == 'cc':
            cpf = input("Informe o CPF do usuário: ")
            contas = criar_conta_corrente(contas, usuarios, cpf)

        elif opcao == "lc":
                    listar_contas(contas)

        elif opcao == 'q':
            break  

        else:     
            print('Operação inválida, por favor selecione novamente a operação desejada.')


if __name__ == "__main__":
    main()
