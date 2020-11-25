import OperaçoesBancarias

#TRANSFERÊNCIA

def realizando_transferencia(nome_cliente):

    print("<!>TRANSFERÊNCIA<!>")
    print('Digite "voltar" para voltar para as operações bancárias\n')

    quantia = input('Quanto você deseja transferir?\n')

    if quantia.lower() == 'voltar': #SE DIGITAR PRA VOLTAR ELE RETORNARÁ PRAS OPERAÇÕES BANCÁRIAS
        OperaçoesBancarias.transações_bancárias(nome_cliente)
    elif quantia.isnumeric() == False: #VALIDAÇÃO PRA QUE NÃO POSSA SER DIGITADO ALGO FORA DE NÚMEROS
        print('Digite uma quantia numérica\n')
        OperaçoesBancarias.transações_bancárias(nome_cliente)
    else:
        print('Valor confirmado!\n')

        favorecido = input('Qual o nome de usuário do favorecido?\n')
        
        #ALTERAÇÃO DO SALDO PARA TRANSFERêNCIA
        print('Transferência realizada!')
        saldo = open(f'{nome_cliente}/saldo.txt',"r")
        alterar_saldo = saldo.read()
        saldo.close()
        saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

        alteracao = int(alterar_saldo) - int(quantia)
        alteracao = str(alteracao)

        saldo2.write(alteracao)
        saldo2.close()

        #ALTERAÇÃO DO SALDO DO FAVORECIDO
        fav_saldo = open(f'{favorecido}/saldo.txt',"r")
        alterar_saldo2 = fav_saldo.read()
        fav_saldo.close()
        fav_saldo2 = open(f'{favorecido}/saldo.txt',"w")

        fav_alteracao = int(alterar_saldo2) + int(quantia)
        fav_alteracao = str(fav_alteracao)

        fav_saldo2.write(fav_alteracao)
        fav_saldo2.close()
