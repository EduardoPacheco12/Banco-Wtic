def validando_nome(nome): #TRATAMENTO DE ERROS DE NOME

    while(True):

        while nome.isnumeric() == True:
            nome = input("Nome inválido, digite novamente\n")

        try:
            open(f'{nome}/nome.txt')
            nome = input("Nome já existente, digite novamente\n")

        except:
            return nome

def validando_cpf(cpf): #TRATAMENTOS DE ERROS DO CPF
    while (cpf.isnumeric() == False) or (len(cpf) != 11):
        cpf=input("CPF inválido, digite novamente.\n")

    return cpf

def validando_idade(idade): #TRATAMENTOS DE ERROS DE IDADE
    while (idade.isnumeric() == False) or (int(idade) < 18):
            idade = input("Idade inválida, digite novamente.\n")

    return idade

def validando_saldo(saldo): #TRATAMENTO DE ERROS DO SALDO
    while (saldo.isnumeric()==False) or (int(saldo) < 0):
        saldo=input("Quantia inválida, digite novamente\n")

    return saldo