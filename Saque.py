import UserScreen
import OperaçoesBancarias

#SAQUE
def realizando_saque(nome_cliente):

    saldo = open(f'{nome_cliente}/saldo.txt',"r")
    alterar_saldo=saldo.read()
    saldo.close()
    saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

    print('<!>SAQUE<!>')
    print('Digite "voltar" para voltar para as operações bancárias\n')

    sacar_dinheiro = (input('Quanto você deseja sacar?\n'))
    
    if sacar_dinheiro.lower() == 'voltar': #SE DIGITAR PRA VOLTAR ELE RETORNARÁ PRAS OPERAÇÕES BANCÁRIAS
        OperaçoesBancarias.transações_bancárias(nome_cliente)
    elif sacar_dinheiro.isnumeric() == False: #VALIDAÇÃO PRA Q NÃO POSSA SER DIGITADO ALGO FORA DE NÚMEROS
        print('Digite um valor numérico\n')
        OperaçoesBancarias.transações_bancárias(nome_cliente)
    else: #OPERAÇÃO EM SI SENDO EFETUADA
        alteracao=int(alterar_saldo) - int(sacar_dinheiro)
        if sacar_dinheiro > alterar_saldo: #SE A PEDIDA DO SAQUE FOR MAIOR DO Q O VALOR ATUAL NA CONTA O SAQUE NÃO SERÁ REALIZADO
            saldo2.write(alterar_saldo)
            saldo2.close()
            print('Dinheiro insuficiente pra realizar a transação!\n')
            OperaçoesBancarias.transações_bancárias(nome_cliente)
        else: #SAQUE SENDO REALIZADO
            print('Transferência realizada com sucesso!')
            alteracao=str(alteracao)
            saldo2.write(alteracao)
            saldo2.close()
            OperaçoesBancarias.transações_bancárias(nome_cliente)