from util.funcoesUtil import cadastrar
from util.funcoesUtil import checkDataBase
from menu.mensagens import *
from menu.funcoes import *
from menu.opcoesValidas import *
import os


def menuConsoleCadastro(): 
    print("\n SCRIPT-PY GERADOR DADOS PARA CADASTROS EM CSV:\n")
    
    print(f'Para qual projeto a massa de dados será feita? \nOpções: {projetosOpcoesMessage}')
    inputProjteto = checkArgumentoStr(opcoesProjeto, projetosOpcoesMessage)

    print(f'\nQual o tipo da massa de dados? \nOpções: {massaOpcoesMessage}')
    inputTelaCadastro = checkArgumentoStr(opcoesTelaCadastro, massaOpcoesMessage)
    
    print(f'\nSerá utilizada em qual ambiente? \nOpções: {ambienteBancoOpcoesMessage}')
    inputAmbiente = checkArgumentoStr(opcoesAmbiente, ambienteBancoOpcoesMessage)

    print(f'\nQual o tipo de preenchimento para o cadastro? \nOpções: {preenchimentoOpcoesMessage}')
    inputTipoCadastro = checkArgumentoStr(opcoesTipoCadastro, preenchimentoOpcoesMessage )

    print("\nQual a quantidade de registros?")
    inputquantidadeRegistros = checkArgumentoInt()

    print("\nInforme o e-mail da sua conta:")
    inputEmail = emailIsValid(inputAmbiente)

    checkDataBase(inputTelaCadastro, inputAmbiente, inputEmail)
    cadastrar(inputProjteto, inputTelaCadastro, inputTipoCadastro, inputquantidadeRegistros)

    print("\nArquivo .CSV gerado com SUCESSO!!")
    print("Verifique a pasta excel/planilhasGerada\n")
    os.system("PAUSE")