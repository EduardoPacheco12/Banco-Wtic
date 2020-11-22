import UserScreen
import Register

#TELA DE LOGIN

def entrar_programa():

    print("-------LOGIN NO BANCO WTIC-------\n")

    nome_cliente = input("Digite seu nome de usuário:\n")

    try:
        nick = open(f'{nome_cliente}/nome.txt',"r")
        ver_nick = nick.read()
        nick.close()

    except:
        cadastrar=input('Nome informado não possui cadastro, deseja cadastrar?\n')

        if cadastrar == 'sim':
            print('entrou')
            Register.registro_pessoal()
        
        return

    cpf_verificaçao = input("Digite o seu CPF (apenas numeros):\n")

    senha_verificaçao = input("Digite sua senha: ")

    ver_senha= open(f'{nome_cliente}/senha.txt',"r")

    if senha_verificaçao != ver_senha:
        while(senha_verificaçao != ver_senha):
            senha_verificaçao=input('Senha incorreta, tente novamente.\n')



    #conteudo_arquivo=open(arquivo,'r')
