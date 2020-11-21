import UserScreen

#TELA DE LOGIN

arquivo='clientes.txt'

def entrar_programa():

    print("-------LOGIN NO BANCO WTIC-------\n")

    cpf_verificaçao = input("Digite o seu CPF:\n")

    nome_cliente = input("Digite seu nome de usuário:\n")

    senha_verificaçao = input("Digite sua senha: ")

    conteudo_arquivo=open(arquivo,'r')

    for ver in conteudo_arquivo:
        nome = ver.split('-')
        if nome[0] == nome_cliente:
            print('apagar')
            #PARA DE MEXER NO LOGIN SE VC AINDA N FEZ O REGISTER