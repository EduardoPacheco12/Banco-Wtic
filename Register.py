import os
import Login
import RegisterTratamentos
import MainScreen
#TELA DE CADASTRO

def registro_pessoal():

    print("-------REGISTRO DO BANCO WTIC-------")

    #RECEBENDO E VALIDANDO NOME
    nome_register = input("Digite o seu nome de usuário (este nome vai representar você em todas as ocasiões):\n")
    nome_register = RegisterTratamentos.validando_nome(nome_register)
    
    #RECEBENDO E VALIDANDO IDADE
    idade_register = input("Digite a sua idade:\n")
    idade_register = RegisterTratamentos.validando_idade(idade_register)

    #RECEBENDO E VALIDANDO CPF
    cpf_register = input("Digite seu cpf:\n")
    cpf_register = RegisterTratamentos.validando_cpf(cpf_register)

    senha_register = input("Digite sua senha:\n")

    #RECEBENDO E VALIDANDO SALDO
    saldo_register = input("Digite a quantidade a ser depositada:\n")
    saldo_register = RegisterTratamentos.validando_saldo(saldo_register)

    #CRIAÇÃO DA PASTA
    pasta_cliente = f'{nome_register}'
    os.mkdir(pasta_cliente)

    #COLOCA A IDADE DENTRO DE UM ARQUIVO NA PASTA
    arquivo_idade = open(f'{pasta_cliente}/idade.txt',"w")
    arquivo_idade.write(idade_register)
    arquivo_idade.close()

    #COLOCA O CPF DENTRO DE UM ARQUIVO NA PASTA
    arquivo_cpf = open(f'{pasta_cliente}/cpf.txt',"w")
    arquivo_cpf.write(cpf_register)
    arquivo_cpf.close()
    
    #COLOCA A SENHA DENTRO DE UM ARQUIVO NA PASTA
    arquivo_senha= open(f'{pasta_cliente}/senha.txt',"w")
    arquivo_senha.write(senha_register)
    arquivo_senha.close()

    #COLOCA O NOME DENTRO DE UM ARQUIVO NA PASTA
    arquivo_nome= open(f'{pasta_cliente}/nome.txt',"w")
    arquivo_nome.write(nome_register)
    arquivo_nome.close()

    #COLOCA A QUANTIDADE DEPOSITADA DENTRO DE UM ARQUIVO NA PASTA
    arquivo_saldo= open(f'{pasta_cliente}/saldo.txt',"w")
    arquivo_saldo.write(saldo_register)
    arquivo_saldo.close()

    #SALVA O EXTRATO DENTRO DE UM ARQUIVO NA PASTA
    arquivo_extrato= open(f'{pasta_cliente}/extrato.txt',"w")
    arquivo_extrato.close()

    entrar=input('Cadastro efetuado com sucesso, deseja fazer login?\n')

    if entrar.lower() == 'sim':
        Login.entrar_programa()
    elif entrar.lower() == 'não':
        MainScreen.tela_entrada()
    else:
        print("Opção inválida, tente novamente")