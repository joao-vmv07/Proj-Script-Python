from menu.mensagensMenu import *

def checkArgumentoStr(opcoesValidas, messageOpcoes):
    argResposta = str(input()).lower()
    while argResposta not in opcoesValidas:
        print(f'Opcão {argResposta} {opcaoInvalidaMessage}')
        print(f'Opções: {messageOpcoes}')
        argResposta = str(input())
    return argResposta

def checkArgumentoInt():
    try:
        argResposta = int(input())
    except ValueError:
            print("Por favor, digite apenas caracteres Númericos!!")
            argResposta = int(input())
    return argResposta
