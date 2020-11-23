import UserScreen
import Saque

#OPERAÇÕES BANCÁRIAS

def transações_bancárias(nome_cliente):

    while(True):

        print('---OPERAÇÕES BANCÁRIAS---\n')

        operacao=input('[1] Para sacar\n[2] Para depositar\n[3] Para fazer transferencia\n[4] Para ver seu saldo\nDigite "voltar" para voltar pra tela de usuário\n')

        if operacao == '1': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO O SAQUE
            Saque.realizando_saque(nome_cliente)
        elif operacao == '2': #DIGITANDO ESSA OPÇÃO SERÁ REALIZADO O DEPÓSITO
            saldo = open(f'{nome_cliente}/saldo.txt',"r")
            alterar_saldo=saldo.read()
            saldo.close()
            saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

            depositar_dinheiro = (input('Quanto você deseja depositar?\n'))

            #transformo em string para salvar no arquivo
            alteracao=int(alterar_saldo) + int(depositar_dinheiro)
            alteracao=str(alteracao)

            saldo2.write(alteracao)
            saldo2.close()

        elif operacao == '3':
            quantia = int(input('Quanto você deseja transferir?\n'))
            favorecido = input('Qual o nome de usuário do favorecido?\n')

            #Alteração do saldo para transferencia
            saldo = open(f'{nome_cliente}/saldo.txt',"r")
            alterar_saldo=saldo.read()
            saldo.close()
            saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

            alteracao=int(alterar_saldo) - int(quantia)
            alteracao=str(alteracao)

            saldo2.write(alteracao)
            saldo2.close()

            #Alteração do saldo do favorecido

            fav_saldo = open(f'{favorecido}/saldo.txt',"r")
            fav_saldo.close()
            fav_saldo2 = open(f'{favorecido}/saldo.txt',"w")

            fav_alteracao=int(alterar_saldo) + int(quantia)
            fav_alteracao=str(fav_alteracao)

            fav_saldo2.write(fav_alteracao)
            fav_saldo2.close()

        elif operacao == '4':
            saldo = open(f'{nome_cliente}/saldo.txt',"r")
            alterar_saldo=saldo.read()
            saldo.close()

            print(f'{nome_cliente} seu saldo é de R${float(alterar_saldo)}\n')

        elif operacao.lower() == 'voltar':
            UserScreen.tela_usuario(nome_cliente)

        else:
            print("DIGITE UMA OPÇÃO VÁLIDA")