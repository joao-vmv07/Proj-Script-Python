from util.funcoesUtil import cadastrar
from util.funcoesUtil import checkDataBase
from menu.mensagens import *
from menu.funcoes import *
import os

opcoesProjeto = ['-s']
opcoesTelaCadastro = ['-pro', '-par']
opcoesAmbiente = ['-d', '-h']
opcoesTipoCadastro = ['-op', '-o']

def menuConsoleCadastro(): 
    print("\nSCRIPT-PY GERADOR DADOS PARA CADASTROS EM CSV:\n")
    
    print("Para qual projeto a massa de dados será feita? \nOpções: Simplifique (-s)")
    inputProjteto = checkArgumentoStr(opcoesProjeto, projetosMessage)

    print("\nQual o tipo da massa de dados? \nOpções: Produtos (-pro) Parceiros (-par)")
    inputTelaCadastro = checkArgumentoStr(opcoesTelaCadastro, massaMessage)
    
    print("\nSerá utilizada em qual ambiente? \nOpções: Desenvolvimento (-d) Homologação (-h)")
    inputAmbiente = checkArgumentoStr(opcoesAmbiente, ambienteBancoMessage)

    print("\nQual o tipo de preenchimento para o cadastro? \nOpções: Todos campos opcionais (-op) Campos obrigatórios (-o)")
    inputTipoCadastro = checkArgumentoStr(opcoesTipoCadastro, preenchimentoMessage )

    print("\nQual a quantidade de registros?")
    inputquantidadeRegistros = checkArgumentoInt()

    print("\nQual o E-mail da sua conta?")
    inputEmail = emailIsValid(inputAmbiente)

    checkDataBase(inputTelaCadastro, inputAmbiente, inputEmail)
    cadastrar(inputProjteto, inputTelaCadastro, inputTipoCadastro, inputquantidadeRegistros)

    print("\nArquivo CSV gerado com SUCESSO!!")
    print("Verifique a pasta excel/planilhasGerada\n")
    os.system("PAUSE")