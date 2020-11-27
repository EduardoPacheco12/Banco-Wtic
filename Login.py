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

        while(True):
            if cadastrar.lower() == 'sim': #DIGITANDO SIM VOCÊ É DIRECIONADO PARA A TELA DE REGISTRO
                Register.registro_pessoal()
                return
            elif cadastrar.lower() == 'não': #DIGITANDO NÃO VOCÊ É DIRECIONADO PARA O MENU PRINCIPAL
                MainScreen.tela_entrada()
                return
            else: #QUALQUER OUTRA COISA DIGITADA SERÁ INVALIDADA PARA O BOM FUNCIONAMENTO DO CÓDIGO
                cadastrar = input("Opção inválida, tente novamente.\n")

    senha_verificaçao = input("Digite sua senha:\n")

    senha= open(f'{nome_cliente}/senha.txt',"r")
    ver_senha = senha.read()
    senha.close()

    while senha_verificaçao != ver_senha:
        senha_verificaçao = input("Senha incorreta, tente novamente.\n")
    
    print("Logado com sucesso!")
    UserScreen.tela_usuario(nome_cliente)