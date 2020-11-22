
#TELA DO USUÁRIO
def tela_usuario():

    print("SEJA BEM VINDO(A) AO BANCO WTIC, Digite a operação desejada.\n")

    print("[1]Operações Bancárias")
    print("[2]Configurações do Usuário")
    print("Digite 'sair' se deseja fechar o programa\n")

    opcao = input("O QUE DESEJA FAZER?\n")

    if opcao.lower() == "sair":
        print("Até logo")
    elif opcao == "1":
        print('opçao 1')

    elif opcao == "2":
        print('opção 2')
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA")
        