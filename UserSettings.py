import ChangeInformation
import UserScreen
import CloseAccount

#CONFIGURAÇÕES DE USUÁRIO

def configuracoes_sistema(nome_cliente):

    while(True):

        print("---CONFIGURAÇÕES DO USUÁRIO---\n")

        print("[1] Alterar informações pessoais")
        print("[2] Encerrar conta")
        print("Digite 'voltar' para voltar pra tela de usuário\n")

        opcao = input("O que deseja fazer?")

        if opcao.lower() == 'voltar': #DIGITANDO ESSA OPÇÃO VOCÊ RETORNA PRA TELA DE USUÁRIO
            UserScreen.tela_usuario(nome_cliente)
            return
        elif opcao == '1': #DIGITANDO ESSA OPÇÃO VOCÊ IRÁ PRA PARTE DA ALTERAÇÃO DE INFORMAÇÕES PESSOAIS
            ChangeInformation.alteracao_informacoes()
        elif opcao == '2': #DIGITANDO ESSA OPÇÃO VOCÊ IRÁ PRA PARTE DE ENCERRAR A CONTA
            CloseAccount.finalizar_conta()
        else:
            print("Opção inválida, tente novamente")
            continue