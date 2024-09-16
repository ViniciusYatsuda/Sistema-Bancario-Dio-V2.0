
def saque(*,saldo,valor,extrato,numero_saque,limite_saque):

    if numero_saque < limite_saque:
        if valor > saldo:
            print('Impossivel realizar essa operação')        
        else:
            saldo = saldo - valor
            numero_saque = numero_saque + 1
            extrato += f'\n Saque    : R$ {valor:.2f} '
            print(f"O seu novo saldo é R$ {saldo:.2f}")
    else:
        print('Impossivel realizar saque! Limite diario excedido')

    return saldo,extrato,numero_saque,limite_saque
            
            
def extratos(saldo ,/ ,* ,extrato):    
    
    print('\n ====================================================================================================')

    print('Nao foi realizado movimentações' if not extrato else extrato)
    print(f' O valor de seu saldo é R$ {saldo:.2f}')
    print('\n ====================================================================================================')


def depositar(saldo,valor,extrato,/):
    
    if valor > 0:
        saldo += valor
        print(' \n Deposito realizado com sucesso')
        extrato += f"\n Deposito : R$ {valor:.2f}"
    else: 
        print('Operaçao falhou! O valor informado é invalido')
    
    return saldo, extrato

def menu():
    menu = '''
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuario
    [5] Criar Conta
    [6] Pesquisa Conta
    [0] Sair

    '''

    return float(input(menu))
    
def criar_conta(agencia, numero_conta,usuarios):
    cpf = float(input('Informe o CPF do usuario : '))
    usuario = filtra_usuario(cpf,usuarios)
    print(usuario)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario': usuario}
    else:
        print('oi')
    
def pesquisa_conta(contas):
    for conta in contas:
        linha = f'''
            Agencia: \t{conta['agencia']}
            C/C : \t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        '''
        print(linha)

def cria_usuario(usuarios):
    cpf = float(input("Digite seu CPF : ") )
    print(type(cpf))  
    usuario = filtra_usuario(cpf, usuarios)
    if usuario:
        print('Usuario já cadastrado')
        return

    nome = input("Informe seu nome completo : ")
    dataNascimento = input("Informe seu aniversario : ")
    endereco = input("Informe sua rua : ")

    usuarios.append({'nome':nome,"data de nascimento":dataNascimento, 'cpf': cpf, 'endereco': endereco})

def filtra_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saque = 0 
    limite_saque = 10
    usuario = []
    contas = []
    AGENCIA = '0001'
    numero_conta = 0

    while True:

        opcao = menu()

        if opcao == 1:
            valor = float(input('Qual o valor que deseja depositar? \n ==>R$'))
            saldo,extrato = depositar(saldo,valor,extrato)

        if opcao == 2:
            valor2 = float(input('Qual valor deseja sacar? \n ==>R$'))
            saldo,extrato,numero_saque,limite_saque = saque(saldo=saldo,valor=valor2,extrato=extrato,numero_saque=numero_saque,limite_saque=limite_saque)

        if opcao == 3:
            extratos(saldo,extrato=extrato)

        if opcao == 4:
            cria_usuario(usuario)

        if opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuario)
            if conta:
                contas.append(conta)
        
        if opcao == 6:
            pesquisa_conta(contas)


        if opcao == 0:
            print(' Obrigado por usar nossos serviços. \n Aguardamos seu retorno')
            break

    
main()