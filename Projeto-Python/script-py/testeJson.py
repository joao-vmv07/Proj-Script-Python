import json
import random
from funcoes import *

with open("script-py/mapeamento_cadastros.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

dadosCliente = dados["simplifique"]["clientes"]["campos"]
for dadosC in dadosCliente:
    camposAlgortimo = dadosC["algoritmo"]
    function_name = camposAlgortimo
    result = eval(f'{function_name}()')
    print(result)
    print(camposAlgortimo)
    print("-----------------------------------")
    
