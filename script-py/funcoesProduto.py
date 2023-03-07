from faker import Faker
import random
import string
from funcoesParceiro import *
from listaValoresPreenchimento import *
from connectionMongo import *
from connectionPostgres import *

locales = 'pt-BR'
fake = Faker(locales)

# def getDadosDataBaseProduto(contmaticId):
#     listaAtributos, listaGrupos, listaCodigoTributacao = connectionPostgres(contmaticId)
#     return listaAtributos, listaGrupos, listaCodigoTributacao

listaAtributos, listaGrupos, listaCodigoTributacao = connectionPostgres(317)
documentosCliente, documentosFornecedor = connectionMongo(317)

def valorProduto(campoAlgoritmo):
    valorProduto = eval(f'{campoAlgoritmo}()')
    return valorProduto


def generate_codigoProduto():
    return fake.pyint()


def generate_status():
    return random.choice(status)


def generate_nomeProduto():
    return fake.pystr()


def generate_codigoBarras():
    return fake.ean()


def generate_precoVenda():
    return round(random.uniform(0.00, 1000.00), 3)


def generate_marca():
    return ''.join(random.choices(string.ascii_uppercase, k=5))


def generate_peso():
    return round(random.uniform(0.00, 100.00), 2)


def generate_unidadeMedida():
    return random.choice(unidadeMedida)


def generate_valorAtributo():
    return ''.join(random.choices(string.ascii_uppercase, k=5))


def generate_informacoesAdicionais():
    return fake.catch_phrase()


def generate_estoqueMinimo():
    return '1'


def generate_estoque():
    return fake.pyint()


def generate_origem():
    return random.choice(origem)


def generate_tipoProduto():
    return random.choice(tipoProduto)


def generate_NCM():
    return random.choice(ncm)


def generate_exTipi():
    return fake.pyint(100, 999)


def generate_controleFCI(size=31, chars=string.digits):
    return 'A'+''.join(random.choice(chars) for _ in range(size))


def generate_aliquotaTributosFederal():
    return round(random.uniform(10.00, 90.00), 2)


def generate_aliquotaTributosEstadual():
    return round(random.uniform(10.00, 90.00), 2)


def generate_CEST():
    return random.choice(cest)


def generate_codigoTributacao():
    return random.choice(listaCodigoTributacao)


def generate_codigoBeneficioUF():
    return "12548791"


def generate_fornecedor():
    return random.choice(documentosFornecedor)


def generate_atributo():
    return random.choice(listaAtributos)


def generate_grupo():
    return random.choice(listaGrupos)
