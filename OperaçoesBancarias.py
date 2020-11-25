import UserScreen
import Saque
import Deposito
import Transferencia
import Saldo

#OPERAÇÕES BANCÁRIAS

def transações_bancárias(nome_cliente):

    while(True):

        print('---OPERAÇÕES BANCÁRIAS---\n')

        operacao = input('[1] Para sacar\n[2] Para depositar\n[3] Para fazer transferencia\n[4] Para ver seu saldo\n[5] Para ver seu extrato\nDigite "voltar" para voltar pra tela de usuário\n')

        if operacao == '1': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO O SAQUE
            Saque.realizando_saque(nome_cliente)
        elif operacao == '2': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO O DEPÓSITO
            Deposito.realizando_deposito(nome_cliente)
        elif operacao == '3': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO UMA TRANSFERêNCIA
            Transferencia.realizando_transferencia(nome_cliente)
        elif operacao == '4': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO UMA CONSULTA DE SALDO
            Saldo.realizando_saldo(nome_cliente)
        elif operacao == '5': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO O EXTRATO
            print('Extrato será realizado')
        elif operacao.lower() == 'voltar':
            UserScreen.tela_usuario(nome_cliente)

        else:
            print("DIGITE UMA OPÇÃO VÁLIDA")