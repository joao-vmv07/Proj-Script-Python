from menu.mensagens import *
from repositories.funcoesRepositories import checkEmail

def checkArgumentoStr(opcoesValidas, messageOpcoes):
    argResposta = str(input()).lower()
    while argResposta not in opcoesValidas:
        print(f'\nOpcão {argResposta} {opcaoInvalidaMessage}')
        print(f'Opções: {messageOpcoes}')
        argResposta = str(input())
    return argResposta

def checkArgumentoInt():
    argResposta = None
    while argResposta is None:
        try:
            argResposta = int(input())
            if argResposta < 1:
                print("Quantidade inválida, digite novamente: ")
                argResposta = None
        except ValueError:
                print("Por favor, digite apenas caracteres númericos!!")

    return argResposta 

def checkOpcaoRegistro(listaRegistros):
    argResposta = None
    while argResposta is None:
        try:
            argResposta = int(input())
            listaRegistros[argResposta]
        except ValueError:
                print("Por favor, digite apenas caracteres Númericos!!")
        except IndexError:
                argResposta = None
                print("Opção selecionada inválida, digite novamente por favor:")

    return listaRegistros[argResposta]["_id"]

def emailIsValid(ambiente):
    argRespostaEmail = str(input())
    infoEmail = checkEmail(argRespostaEmail, ambiente)
    while infoEmail is None:
        argRespostaEmail = str(input(f'\nE-mail não encontrado no ambiente de {checkAmbiente(ambiente)}, digite novamente por favor: '))
        infoEmail = checkEmail(argRespostaEmail, ambiente)
    if len(infoEmail) > 1:
        print("\nExiste mais de 1 empresa registrada em sua conta:")
        for index, infoEmailRegistro in enumerate(infoEmail):
            print(f'{index} - CNPJ: {infoEmailRegistro["cpfCnpj"]} Razão Social: {infoEmailRegistro["razaoSocial"]} ')
        print("\nSelecione o registro que deseja gerar o cadastro, digitando o número: ")
        return checkOpcaoRegistro(infoEmail)
    return infoEmail[0]

def checkAmbiente(ambiente):
    if ambiente == '-d':
        return 'Desenvolvimento'
    if ambiente == '-h':
        return 'Homologação'