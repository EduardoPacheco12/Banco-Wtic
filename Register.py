
#TELA DE CADASTRO

def registro_pessoal():

    

    nome_register = input("Digite o seu nome completo:\n")

    idade_register = input("Digite a sua idade:\n")

    cpf_register = input("Digite seu cpf:\n")

    senha_register = input("Digite sua senha:\n")

    nome = 'nome.txt'
    idade = 'idade.txt'
    cpf = 'cpf.txt'
    senha = 'senha.txt'

    arquivo_nome = open(nome, 'w')
    arquivo_nome.write(nome_register)
    arquivo_nome.close()

    arquivo_idade = open(idade, 'w')
    arquivo_idade.write(idade_register)
    arquivo_idade.close()

    arquivo_cpf = open(cpf, 'w')
    arquivo_cpf.write(cpf_register)
    arquivo_cpf.close()

    arquivo_senha = open(senha, 'w')
    arquivo_senha.write(senha_register)
    arquivo_senha.close()


