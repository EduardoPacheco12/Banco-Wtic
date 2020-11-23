
#TELA DO USUÁRIO
def tela_usuario(nome_cliente):
    
    roda=True
    
    while(roda):

        print(f"SEJA BEM VINDO(A) {nome_cliente} AO BANCO WTIC, Digite a operação desejada.\n")

        print("[1]Operações Bancárias")
        print("[2]Configurações do Usuário")
        print("Digite 'sair' se deseja fechar o programa\n")

        opcao = input("O QUE DESEJA FAZER?\n")

        if opcao.lower() == "sair":
            print("Até logo")
            roda=False
        elif opcao == "1":
            operacao=input('[1] Para sacar\n[2] Para depositar\n[3] Para fazer transferencia\n[4] Para ver seu saldo\n[5] Para finalizar o programa.\n')

            if operacao == '1':
                saldo = open(f'{nome_cliente}/saldo.txt',"r")
                alterar_saldo=saldo.read()
                saldo.close()
                saldo2 = open(f'{nome_cliente}/saldo.txt',"w")

                sacar_dinheiro = (input('Quanto você deseja sacar?\n'))

                #transformo em string para salvar no arquivo
                alteracao=int(alterar_saldo) - int(sacar_dinheiro)
                alteracao=str(alteracao)

                saldo2.write(alteracao)
                saldo2.close()

            elif operacao == '2':
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

            elif operacao == '5':
                print('Obrigado pela preferencia, programa finalizado com sucesso!\n')
                roda=False

            else:
                print("DIGITE UMA OPÇÃO VÁLIDA")
