
#TELA DO USUÁRIO
def tela_usuario(nome_cliente):

    print(f"SEJA BEM VINDO(A) {nome_cliente} AO BANCO WTIC, Digite a operação desejada.\n")

    print("[1]Operações Bancárias")
    print("[2]Configurações do Usuário")
    print("Digite 'sair' se deseja fechar o programa\n")

    opcao = input("O QUE DESEJA FAZER?\n")

    if opcao.lower() == "sair":
        print("Até logo")
    elif opcao == "1":
        operacao=input('[1] Para sacar\n[2] Para depositar\n[3] Para fazer transferencia\n')

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

        if operacao == '2':
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
    elif opcao == "2":
        print('opção 2')
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA")
        