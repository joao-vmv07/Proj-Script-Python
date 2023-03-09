import sys
from funcoesProduto import *
from funcoesParceiro import *
from util.funcoesUtil import *

def __init__():
    projName = sys.argv[1]
    telaCadastro = sys.argv[2]
    tipoCadastro = sys.argv[3]
    quantidadeCadastros = int(sys.argv[4])
    contmaticId = int(sys.argv[5])
    cadastrar(projName, telaCadastro, tipoCadastro, quantidadeCadastros)
    set_listas_Produtos(contmaticId)

__init__()

