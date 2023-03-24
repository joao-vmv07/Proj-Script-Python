from menu.mensagens import *
from repositories.dev.connectionMongoConnectContSocial import connectionMongoContSocialDev
from repositories.homolog.connectionMongoConnectContSocial import connectionMongoContSocialHomolog

def checkArgumentoStr(opcoesValidas, messageOpcoes):
    argResposta = str(input()).lower()
    while argResposta not in opcoesValidas:
        print(f'Opcão {argResposta} {opcaoInvalidaMessage}')
        print(f'Opções: {messageOpcoes}')
        argResposta = str(input())
    return argResposta

def checkArgumentoInt():
    argResposta = None
    while argResposta is None:
        try:
            argResposta = int(input())
        except ValueError:
                print("Por favor, digite apenas caracteres Númericos!!")
    return argResposta

def emailIsValid(ambiente):
    argRespostaEmail = str(input())
    infoContmaticIds = checkEmail(argRespostaEmail, ambiente)
    while infoContmaticIds is None:
        argRespostaEmail = str(input("\nEmail inválido, digite novamente por favor: "))
        infoContmaticIds = checkEmail(argRespostaEmail, ambiente)
    if len(infoContmaticIds) > 1:
        print("\nExiste mais de 1 contrato registrados em sua conta:")
        for index, infoContmaticId in enumerate(infoContmaticIds):
            print(f'{index} - CNPJ: {infoContmaticId["cpfCnpj"]} Razão Social: {infoContmaticId["razaoSocial"]} ')
        return infoContmaticIds[int(input("\nSelecione o registro que deseja digitando número: "))]
    return infoContmaticIds[0]

def checkEmail(argRespostaEmail, ambiente):
    if ambiente == "-d":
        infoContmaticIds = connectionMongoContSocialDev(argRespostaEmail)
        return infoContmaticIds
    if ambiente == "-h":
        infoContmaticIds = connectionMongoContSocialHomolog(argRespostaEmail)
        return infoContmaticIds