
import validar_nome
import os
#TELA DE CADASTRO

def registro_pessoal():

    print("-------REGISTRO DO BANCO WTIC-------")

    nome_register = input("Digite o seu nome de usuário (este nome vai representar você em todas as ocasiões):\n")

    idade_register = input("Digite a sua idade:\n")

    cpf_register = input("Digite seu cpf:\n")

    senha_register = input("Digite sua senha:\n")

    #valido=validar_nome(nome_register)

    #if valido == 1:
    print('entrou')
    pasta_cliente = f'{nome_register}'
    os.mkdir(pasta_cliente)
    print('fim =)')
            

