import OperaçoesBancarias

#DEPÓSITO

def realizando_deposito(nome_cliente):

    saldo = open(f'{nome_cliente}/saldo.txt',"r")
    alterar_saldo = saldo.read()
    saldo.close()
    saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

    print('<!>DEPÓSITO<!>')
    print('Digite "voltar" para voltar para as operações bancárias\n')

    depositar_dinheiro = input('Quanto você deseja depositar?\n')

    if depositar_dinheiro.lower() == 'voltar': #SE DIGITAR PRA VOLTAR ELE RETORNARÁ PRAS OPERAÇÕES BANCÁRIAS
        OperaçoesBancarias.transações_bancárias(nome_cliente)
    elif depositar_dinheiro.isnumeric() == False: #VALIDAÇÃO PRA QUE NÃO POSSA SER DIGITADO ALGO FORA DE NÚMEROS
        print('Digite uma quantia numérica\n')
        OperaçoesBancarias.transações_bancárias(nome_cliente)
    else: #OPERAÇÃO EM SI SENDO EFETUADA
        print('Depósito realizado com sucesso!')
        alteracao = int(alterar_saldo) + int(depositar_dinheiro)
        alteracao = str(alteracao)
        saldo2.write(alteracao)
        saldo2.close()
        OperaçoesBancarias.transações_bancárias(nome_cliente)