import warnings
import openpyxl
import json
from faker import Faker
from Parceiro.funcoesParceiro import *
from Produto.funcoesProduto import *

def checkValorPreencher(infDadoCriado, campoAlgoritmo, campoCabecalho, telaCadastro):
    if telaCadastro == "parceiros":
        return valorParceiro(infDadoCriado, campoAlgoritmo, campoCabecalho)
    if telaCadastro == "produtos":
        return valorProduto(campoAlgoritmo)

def cadastrar(projName, telaCadastro, tipoCadastro, argQuantidadeCadastro):
    checkTipoCadastro(projName, telaCadastro, tipoCadastro, argQuantidadeCadastro)

def checkTipoCadastro(projName, telaCadastro, tipoCadastro, argQuantidadeCadastro):
    if tipoCadastro == "todosCampos":
        preencherPlanilhaTodosCampos(argQuantidadeCadastro, telaCadastro, carregarCamposJson(projName, telaCadastro))
    if tipoCadastro == "camposObrigatorios":
        preencherPlanilhaCamposObrigatorios(argQuantidadeCadastro, telaCadastro, carregarCamposJson(projName, telaCadastro))

def getDadosBase(telaCadastro, contmaticId):
    if telaCadastro == "parceiros":
        get_info_parceiros(contmaticId)
    if telaCadastro == "produtos":
        get_info_produtos(contmaticId)  

def carregarPlanilha(telacadastro):
    warnings.simplefilter(action='ignore', category=UserWarning)
    planilha = openpyxl.load_workbook(f'../excel/planilhas/importar-{telacadastro}.xlsx')
    paginaDaPlanilha = planilha[f'importar-{telacadastro}']
    return planilha, paginaDaPlanilha

def carregarCamposJson(projName, telaCadastro):
    with open("mapeamentos-json/mapeamento_cadastros.json", encoding='utf-8') as meu_json:
        dadosJson = json.load(meu_json) 
    camposJson = dadosJson[f'{projName}'][f'{telaCadastro}']["campos"]
    return camposJson

def preencherPlanilhaCamposObrigatorios(argQuantidadeCadastro, telaCadastro, camposJson):
    planilha, paginaDaPlanilha = carregarPlanilha(telaCadastro)
    for linhaPlanilha in range (POSICAO_PRIMEIRA_LINHA_PREENCHIMENTO, calcQuantidadeCadastro(argQuantidadeCadastro) ):
        infDadoCriado = {}
        for colunaPlanilha, campo in [(y + 1, campo) for (y, campo) in enumerate(camposJson)]:
            if campo["obrigatorio"]:
                paginaDaPlanilha.cell(row = linhaPlanilha, column = colunaPlanilha , value = checkValorPreencher(infDadoCriado, campo['algoritmo'], campo['cabecalho'], telaCadastro))
            else:
                paginaDaPlanilha.cell(row = linhaPlanilha, column = colunaPlanilha, value = "")
    planilha.save(f'../excel/planilhasGerada/importar-{telaCadastro}.xlsx')

def preencherPlanilhaTodosCampos(argQuantidadeCadastro, telaCadastro, camposJson): 
    planilha, paginaDaPlanilha = carregarPlanilha(telaCadastro)
    for linhaPlanilha in range (POSICAO_PRIMEIRA_LINHA_PREENCHIMENTO, calcQuantidadeCadastro(argQuantidadeCadastro) ):
        infDadoCriado = {}
        for colunaPlanilha, campo in [(y + 1, campo) for (y, campo) in enumerate(camposJson)]:
            paginaDaPlanilha.cell(row = linhaPlanilha, column = colunaPlanilha , value = checkValorPreencher(infDadoCriado, campo['algoritmo'],  campo['cabecalho'], telaCadastro))
    planilha.save(f'../excel/planilhasGerada/importar-{telaCadastro}.xlsx')