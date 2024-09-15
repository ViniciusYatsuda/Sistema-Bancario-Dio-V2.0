menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0 
Limite_saque = 3

while True:

    print(' \n Seja bem vindo ao seu banco')

    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe o valor do deposito : '))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"
        else: 
            print('Operaçao falhou! O valor informado é invalido')

    elif opcao == '2':
        if numero_saque < Limite_saque:
            valor2 = float(input('Informe o valor do saque :'))
            if valor2 > saldo:
                 print('Impossivel realizar essa operação')        
            else:
                saldo = saldo - valor2
                numero_saque = numero_saque + 1
                extrato += f'Saque : {valor2:.2f} \n'
                print(f"O seu novo saldo é R$ {saldo:.2f} \n")
        else:
            print('Impossivel realizar saque! Limite diario excedido')
            
    elif opcao == '3':
        print('\n ====================================================================================================')
        print(extrato)
        print('Nao foi realizado movimentações' if not extrato else extrato)
        print(f'O valor de seu saldo é R$ {saldo:.2f}')
        print('\n ====================================================================================================')
            
    elif opcao == '0':
        break

    else:
        print('Opcao invalida! Selecione uma opcao valida')