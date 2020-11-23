import UserScreen
import Register
import MainScreen
import pathlib

#TELA DE LOGIN

def entrar_programa():
    
    print("-------LOGIN NO BANCO WTIC-------\n")

    nome_cliente = input("Digite seu nome de usuário:\n")

    try:
        nick = open(f'{nome_cliente}/nome.txt',"r")
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

    print(ver_senha)

    while senha_verificaçao != ver_senha:
        senha_verificaçao = input("Senha incorreta, tente novamente.\n")
    
    print("Logado com sucesso!")
    UserScreen.tela_usuario(nome_cliente)