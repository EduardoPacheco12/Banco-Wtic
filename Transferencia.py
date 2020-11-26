import BankingOperations

#TRANSFERÊNCIA

def realizando_transferencia(nome_cliente):

    saldo = open(f'{nome_cliente}/saldo.txt',"r")
    saldo_cliente = saldo.read()
    saldo.close()

    print("<$>TRANSFERÊNCIA<$>")
    print("Digite 'voltar' para voltar para as operações bancárias\n")

    quantia = input("Quanto você deseja transferir?\n")

    if quantia.lower() == 'voltar': #SE DIGITAR PRA VOLTAR ELE RETORNARÁ PRAS OPERAÇÕES BANCÁRIAS
        BankingOperations.transações_bancárias(nome_cliente)
        return
    elif quantia.isnumeric() == False: #SE DIGITAR ALGO QUE NÃO SEJA NÚMEROS O PROGRAMA NÃO IRÁ CONSIDERAR
        print("Digite uma quantia numérica\n")
        BankingOperations.transações_bancárias(nome_cliente)
        return
    else:
        quantia = int(quantia)
        saldo_cliente = int(saldo_cliente)
        
        if quantia > saldo_cliente:
            print('Dinheiro insuficiente pra realizar a transação!\n')
            BankingOperations.transações_bancárias(nome_cliente)
            return
        else:
            print('Valor confirmado!\n')

            favorecido = input('Qual o nome de usuário do favorecido?\n')

            try:
                nome_fav = open(f'{favorecido}/nome.txt',"r")
                ler_nome = nome_fav.read()
                nome_fav.close()
            except:
                print("Nome de usuário não encontrado\n")
                BankingOperations.transações_bancárias(nome_cliente)
                return
            else:
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