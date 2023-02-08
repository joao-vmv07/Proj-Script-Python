import json
import random
from funcoes import *

with open("script-py/mapeamento_cadastros.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

with open("script-py/mapeamento_campos.json", encoding='utf-8') as meu_json:
    dadosJsonCamposObrigatorios = json.load(meu_json)

camposObrigatoriosPessoaJuridica = dadosJsonCamposObrigatorios["simplifique"]["parceiros"]["pessoaJuridica"]["campos"]
camposPrioritarios  = dadosJsonCamposObrigatorios["simplifique"]["parceiros"]["camposPrioritarios"]

print(type(camposPrioritarios))

for dadosC in camposPrioritarios:
    print(dadosC["cabecalho"])
    
