import UserScreen
import Register
import MainScreen

#TELA DE LOGIN

def entrar_programa():
    while(True):
    
        print("-------LOGIN NO BANCO WTIC-------\n")

        nome_cliente = input("Digite seu nome de usuário:\n")

        try:
            nick = open(f'{nome_cliente}/nome.txt',"r")
            ver_nick = nick.read()
            nick.close()

        except:
            cadastrar = input("Nome informado não possui cadastro, deseja cadastrar?\n")

            if cadastrar.lower() == 'sim':
                Register.registro_pessoal()
            elif cadastrar.lower() == 'não':
                MainScreen.tela_entrada()
            else:
                print("Digite uma opção válida")

        senha_verificaçao = input("Digite sua senha:\n")

        senha= open(f'{nome_cliente}/senha.txt',"r")
        ver_senha = senha.read()
        senha.close()

        if senha_verificaçao != senha:
            print("Senha incorreta, tente novamente.\n")
            continue
        else:
            print("Logado com sucesso!")
            UserScreen.tela_usuario()



    #conteudo_arquivo=open(arquivo,'r')
