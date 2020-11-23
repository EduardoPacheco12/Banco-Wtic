import os
import Login
import RegisterTratamentos
#TELA DE CADASTRO

def registro_pessoal():

    print("-------REGISTRO DO BANCO WTIC-------")

    #recebendo e validando nome
    nome_register = input("Digite o seu nome de usuário (este nome vai representar você em todas as ocasiões):\n")
    nome_register = RegisterTratamentos.validando_nome(nome_register)
    
    #recebendo e validando idade
    idade_register = input("Digite a sua idade:\n")
    idade_register = RegisterTratamentos.validando_idade(idade_register)

    #recebendo e validando cpf
    cpf_register = input("Digite seu cpf:\n")
    cpf_register = RegisterTratamentos.validando_cpf(cpf_register)

    senha_register = input("Digite sua senha:\n")

    #recebendo e validando saldo
    saldo_register = input("Digite a quantidade a ser depositada:\n")
    saldo_register = RegisterTratamentos.validando_saldo(saldo_register)

    #cria a pasta
    pasta_cliente = f'{nome_register}'
    os.mkdir(pasta_cliente)

    #Coloca a idade dentro de um arquivo na pasta
    arquivo_idade = open(f'{pasta_cliente}/idade.txt',"w")
    arquivo_idade.write(idade_register)
    arquivo_idade.close()

    #Coloca o cpf dentro de um arquivo na pasta
    arquivo_cpf = open(f'{pasta_cliente}/cpf.txt',"w")
    arquivo_cpf.write(cpf_register)
    arquivo_cpf.close()
            
    #Coloca a senha dentro de um arquivo na pasta
    arquivo_senha= open(f'{pasta_cliente}/senha.txt',"w")
    arquivo_senha.write(senha_register)
    arquivo_senha.close()

    #Coloca o nome dentro de um arquivo na pasta
    arquivo_nome= open(f'{pasta_cliente}/nome.txt',"w")
    arquivo_nome.write(nome_register)
    arquivo_nome.close()

    #Coloca a quandidade depositada dentro de um arquivo na pasta
    arquivo_saldo= open(f'{pasta_cliente}/saldo.txt',"w")
    arquivo_saldo.write(saldo_register)
    arquivo_saldo.close()

    #Salva o extrato dentro de um arquivo na pasta
    arquivo_extrato= open(f'{pasta_cliente}/extrato.txt',"w")
    arquivo_extrato.close()

    entrar=input('Cadastro efetuado com sucesso, deseja fazer login?\n')

    if entrar == 'sim':
        Login.entrar_programa()