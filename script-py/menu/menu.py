from util.funcoesUtil import cadastrar
from util.funcoesUtil import checkDataBase
from menu.mensagensMenu import *
from menu.funcoesMenu import *

opcoesProjeto = ['-s']
opcoesTelaCadastro = ['-pro', '-par']
opcoesAmbiente = ['-d', '-h']
opcoesTipoCadastro = ['-op', '-o']
opcoesConfima = ['s','S', 'n', 'N']

def menuConsoleCadastro(): 
    print()
    print("SCRIPT-PY GERADOR DADOS PARA CADASTROS EM CSV:")
    print()
    
    print("Para qual projeto a massa de dados será feita?")
    print("Opções: Simplifique -s")
    inputProjteto = checkArgumentoStr(opcoesProjeto, projetosMessage)
    print()

    print("Qual o tipo da massa de dados?")
    print("Opções: Produtos -pro Parceiros -par")
    inputTelaCadastro = checkArgumentoStr(opcoesTelaCadastro, massaMessage)
    print()
    
    print("Será utilizada em qual ambiente?")
    print("Opções: Desenvolvimento -d Homologação -h")
    inputAmbiente = checkArgumentoStr(opcoesAmbiente, ambienteBancoMessage)
    print()

    print("Qual o tipo de preenchimento para o cadastro?")
    print("Opções: Todos campos opcionais -op Campos obrigatórios -o")
    inputTipoCadastro = checkArgumentoStr(opcoesTipoCadastro, preenchimentoMessage )
    print()

    print("Qual a quantidade de registros?")
    inputquantidadeRegistros = checkArgumentoInt()
    print()

    print("Qual o contmaticId?")
    inputContmaticId = checkArgumentoInt()
    print()

    checkDataBase(inputTelaCadastro, inputAmbiente, inputContmaticId)
    cadastrar(inputProjteto, inputTelaCadastro, inputTipoCadastro, inputquantidadeRegistros)

    print()
    print("Arquivo CSV gerado com SUCESSO!!")
    print("Verifique a pasta excel/planilhasGerada")