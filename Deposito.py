import BankingOperations

#DEPÓSITO

def realizando_deposito(nome_cliente):

    saldo = open(f'{nome_cliente}/saldo.txt',"r")
    alterar_saldo = saldo.read()
    saldo.close()
    saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

    print("<$>DEPÓSITO<$>")
    print("Digite 'voltar' para voltar para as operações bancárias\n")

    depositar_dinheiro = input("Quanto você deseja depositar?\n")

    if depositar_dinheiro.lower() == 'voltar': #SE DIGITAR PRA VOLTAR ELE RETORNARÁ PRAS OPERAÇÕES BANCÁRIAS
        saldo2.write(alterar_saldo)
        saldo2.close()
        BankingOperations.transações_bancárias(nome_cliente)
        return

    elif depositar_dinheiro.isnumeric() == False: #VALIDAÇÃO PRA QUE NÃO POSSA SER DIGITADO ALGO FORA DE NÚMEROS
        print("Digite uma quantia numérica\n")
        saldo2.write(alterar_saldo)
        saldo2.close()
        BankingOperations.transações_bancárias(nome_cliente)
        return

    else: #OPERAÇÃO EM SI SENDO EFETUADA
        print("Depósito realizado com sucesso!")
        alteracao = int(alterar_saldo) + int(depositar_dinheiro)
        alteracao = str(alteracao)
        saldo2.write(alteracao)
        saldo2.close()
        BankingOperations.transações_bancárias(nome_cliente)
        return