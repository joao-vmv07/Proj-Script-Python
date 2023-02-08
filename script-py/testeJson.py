import json
import random
from funcoes import *

with open("script-py/mapeamento_cadastros.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

with open("script-py/mapeamento_campos.json", encoding='utf-8') as meu_json:
    dadosJsonCamposObrigatorios = json.load(meu_json)

camposObrigatorios = dadosJsonCamposObrigatorios["simplifique"]["parceiros"]["pessoaJuridica"]["campos"]

dadosCliente = dados["simplifique"]["clientes"]["campos"]

print(camposObrigatorios)

# for dadosC in camposObrigatorios:
#     print(dadosC["cabecalho"])
    
