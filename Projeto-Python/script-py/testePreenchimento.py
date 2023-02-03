import openpyxl
import json
from faker import Faker
from funcoes import *

# main(projName, TelaCadastro, quantidadeCadastros)

planilha = openpyxl.load_workbook('excel/planilhas/importar-parceiro.xlsx')
paginaParceiro = planilha['importar-parceiros']
positionPrimeiraLinhaPreenchimento = 3

with open("script-py/mapeamento_cadastros.json", encoding='utf-8') as meu_json:
    dadosJson = json.load(meu_json)

campos = dadosJson["simplifique"]["clientes"]["campos"]

def preecherPlanilhaCompleto(argQuantidadeCadastro): 
    for linhaPlanilha in range(positionPrimeiraLinhaPreenchimento, positionPrimeiraLinhaPreenchimento + argQuantidadeCadastro ):
        infDadoCriado = {}
        for colunaPlanilha, campo in [(y + 1, campo) for (y, campo) in enumerate(campos)]:
            campoAlgoritmo = campo['algoritmo']
            campoCabecalho =  campo['cabecalho']
            paginaParceiro.cell(row = linhaPlanilha, column = colunaPlanilha , value = checkValor(infDadoCriado, campoAlgoritmo, campoCabecalho))

preecherPlanilhaCompleto(10)
planilha.save('excel/planilhasGerada/importar-parceiros-teste.xlsx')