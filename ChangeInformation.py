import os

#ALTERAR INFORMAÇÕES PESSOAIS

def alteracao_informacoes(nome_cliente):

    while(True):

        print("<!>ALTERAR INFORMAÇÕES PESSOAIS<!>")
        print("- Usuário")
        print("- Idade")
        print("- CPF")
        print("- Senha")

        informação = input("Que informação você deseja mudar?")

        if informação.lower() == 'usuário':