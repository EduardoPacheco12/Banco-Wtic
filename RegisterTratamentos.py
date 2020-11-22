import MainScreen

def nome_tratamento():

    if nome_register.lower() == "voltar":
        MainScreen.tela_entrada()
    elif nome_register.isalpha() == False:
        print("Digite uma opção válida\n")
    else:
        print("Próxima pergunta\n")
