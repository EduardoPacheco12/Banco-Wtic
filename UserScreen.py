import MainScreen
import OperaçoesBancarias
#TELA DO USUÁRIO
def tela_usuario(nome_cliente):
    
    while(True):

        print(f"SEJA BEM VINDO(A) {nome_cliente} AO BANCO WTIC, DIGITE A OPERAÇÃO DESEJADA.\n")

        print("[1]Operações Bancárias")
        print("[2]Configurações do Usuário")
        print("Digite 'sair' se deseja fechar o programa\n")

        opcao = input("O QUE DESEJA FAZER?\n")

        if opcao.lower() == "sair":
            print("Até logo")
            exit(0)
        elif opcao == "1":
            OperaçoesBancarias.transações_bancárias(nome_cliente)
        elif opcao == "2":
            print("Configurações do Usuário(Não disponível ainda)")
            continue
        else:
            print("Opção inválida, tente novamente")
            continue