import os,sys
import MainScreen
import UserSettings
#ALTERAR INFORMAÇÕES PESSOAIS

def alteracao_informacoes(nome_cliente):

    while(True):

        abrir_senha = open(f'{nome_cliente}/senha.txt','r')
        senha_antiga = abrir_senha.read()
        abrir_senha.close()

        print("<!>ALTERAR INFORMAÇÕES PESSOAIS<!>")
        print("Digite 'voltar' para voltar para as configurções de usuário")
        print("- Usuário")
        print("- Senha\n")

        informação = input("Que informação você deseja mudar?\n")

        if informação.lower() == 'usuário': #DIGITANDO ESSA OPÇÃO VOCÊ IRÁ ALTERAR SEU NOME DE USUÁRIO NO BANCO

            nome = input("Digite seu novo nome de usuário:\n")

            ver = input("Digite sua senha para confirmar o processo:\n")
            while senha_antiga != ver: #LAÇO CRIADO PARA QUE HAJA A VERIFICAÇÃO DA SENHA DO USUÁRIO PRA ELE MUDAR DE NOME
                ver = input("Senha incorreta, tente novamente\n")

            os.rename(f"{nome_cliente}" , f"{nome}")

            nome_antigo = open(f'{nome}/nome.txt','w')
            nome_antigo.write(f'{nome}')
            nome_antigo.close()

            print("Nome alterado com sucesso! faça o login novamente para atualização no sistema.\n")
            MainScreen.tela_entrada()
            return

        elif informação.lower() == 'senha': #DIGITANDO ESSA OPÇÃO VOCÊ IRÁ ALTERAR SUA SENHA NO BANCO
            
            nova_senha = input("Digite sua nova senha:\n")

            ver = input("Digite sua senha antiga para confirmar o processo:\n")
            while senha_antiga != ver: #LAÇO CRIADO PARA QUE HAJA A VERIFICAÇÃO DA SENHA DO USUÁRIO PRA ELE MUDAR DE SENHA
                ver = input("Senha incorreta, tente novamente\n")

            alterar_senha = open(f'{nome_cliente}/senha.txt','w')
            alterar_senha.write(nova_senha)
            alterar_senha.close()
            print("senha alterada com sucesso!")
        elif informação.lower() == 'voltar': #DIGITANDO ESSA OPÇÃO VOCÊ RETORNA PARA AS CONFIGURAÇÕES DE USUÁRIO
            UserSettings.configuracoes_sistema(nome_cliente)
            return
        else: #QUALQUER OUTRA COISA DIGITADA SERÁ INVALIDADA PARA O BOM FUNCIONAMENTO DO CÓDIGO
            print("Opção inválida, tente novamente")
            continue

