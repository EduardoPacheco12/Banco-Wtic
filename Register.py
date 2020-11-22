
import validar_nome
import MainScreen
import os
import Login
import RegisterTratamentos
#TELA DE CADASTRO

def registro_pessoal():

    print("-------REGISTRO DO BANCO WTIC-------")

    nome_register = input("Digite o seu nome de usuário (este nome vai representar você em todas as ocasiões):\n")

    idade_register = input("Digite a sua idade:\n")

    cpf_register = input("Digite seu cpf:\n")

    senha_register = input("Digite sua senha:\n")

    #valido=validar_nome(nome_register)

    #if valido == 1:
    pasta_cliente = f'{nome_register}'#CRIA A PASTA
    os.mkdir(pasta_cliente)

    #COLOCA O NOME DENTRO DE UM ARQUIVO NA PASTA
    arquivo_nome = open(f'{pasta_cliente}/nome.txt',"w")
    arquivo_nome.write(nome_register)
    arquivo_nome.close()

    #COLOCA A IDADE DENTRO DE UM ARQUIVO NA PASTA
    arquivo_idade = open(f'{pasta_cliente}/idade.txt',"w")
    arquivo_idade.write(idade_register)
    arquivo_idade.close()

    #COLOCA O CPF DENTRO DE UM ARQUIVO NA PASTA
    arquivo_cpf = open(f'{pasta_cliente}/cpf.txt',"w")
    arquivo_cpf.write(cpf_register)
    arquivo_cpf.close()

    #COLOCA O NOME DENTRO DE UM ARQUIVO NA PASTA
    arquivo_senha= open(f'{pasta_cliente}/senha.txt',"w")
    arquivo_senha.write(senha_register)
    arquivo_senha.close()

    entrar = input('cadastro efetuado com sucesso, deseja fazer login?\n')

    if entrar.lower() == 'sim':
        Login.entrar_programa()
    elif entrar.lower() == 'não':
        MainScreen.tela_entrada()
    else:
        print("Digite uma opção válida")