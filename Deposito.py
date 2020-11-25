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
        
        abrir_senha=open(f'{nome_cliente}/senha.txt',"r")
        ver_senha=abrir_senha.read()
        abrir_senha.close()
        verificar_senha = input('Digite sua senha para a confirmação.\n')
        while ver_senha!=verificar_senha:
            verificar_senha = input('Senha incorreta, digite novamente.\n')
            volta=input('Digite "voltar" para voltar às operações bancárias.\n')
            if volta.lower()=='voltar':
                OperaçoesBancarias.transações_bancárias(nome_cliente)
                return

        print('Depósito realizado com sucesso!')
        alteracao = int(alterar_saldo) + int(depositar_dinheiro)
        alteracao = str(alteracao)
        saldo2.write(alteracao)
        saldo2.close()
        OperaçoesBancarias.transações_bancárias(nome_cliente)