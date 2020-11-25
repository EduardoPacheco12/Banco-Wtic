import OperaçoesBancarias

#SAQUE
def realizando_saque(nome_cliente):

    saldo = open(f'{nome_cliente}/saldo.txt',"r")
    alterar_saldo=saldo.read()
    saldo.close()
    saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

    print('<!>SAQUE<!>')
    print('Digite "voltar" para voltar para as operações bancárias\n')

    sacar_dinheiro = input('Quanto você deseja sacar?\n')
    
    if sacar_dinheiro.lower() == 'voltar': #SE DIGITAR PRA VOLTAR ELE RETORNARÁ PRAS OPERAÇÕES BANCÁRIAS
        OperaçoesBancarias.transações_bancárias(nome_cliente)
    elif sacar_dinheiro.isnumeric() == False: #VALIDAÇÃO PRA QUE NÃO POSSA SER DIGITADO ALGO FORA DE NÚMEROS
        print('Digite uma quantia numérica\n')
        OperaçoesBancarias.transações_bancárias(nome_cliente)
    else: #OPERAÇÃO EM SI SENDO EFETUADA
        sacar_dinheiro = int(sacar_dinheiro)
        alterar_saldo = int(alterar_saldo)
        if sacar_dinheiro > alterar_saldo: #SE A PEDIDA DO SAQUE FOR MAIOR DO Q O VALOR ATUAL NA CONTA O SAQUE NÃO SERÁ REALIZADO
            print('Dinheiro insuficiente pra realizar a transação!\n')
            alterar_saldo = str(alterar_saldo)
            saldo2.write(alterar_saldo)
            saldo2.close()
            OperaçoesBancarias.transações_bancárias(nome_cliente)
        else: #SAQUE SENDO REALIZADO
            print('Saque realizado com sucesso!')
            alteracao = int(alterar_saldo) - int(sacar_dinheiro)
            alteracao = str(alteracao)
            saldo2.write(alteracao)
            saldo2.close()
            OperaçoesBancarias.transações_bancárias(nome_cliente)