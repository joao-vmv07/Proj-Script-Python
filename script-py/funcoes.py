
from faker import Faker
import random
from listaValoresPreenchimento import *

locales = 'pt-BR'
fake = Faker(locales)

valorPreenchido = ""

def checkValor(infDadoCriado, campoAlgoritmo, campoCabecalho):
    valor = eval(f'{campoAlgoritmo}({checkInfDadoCriado(infDadoCriado, campoCabecalho, valorPreenchido)})')
    checkCabecalho(infDadoCriado, campoCabecalho, valor, cabecalhosValidar)
    return valor

def checkInfDadoCriado(infDadoCriado, campoCabecalho, valorPreenchido):
    for campo in cabecalhosValidar:
        if campo in infDadoCriado and campoCabecalho in camposValidar:
            valorPreenchido = f"'{infDadoCriado[campo]}'"
    return valorPreenchido

def checkCabecalho(infDadoCriado, campoCabecalho, valor, cabecahoValidar):
    if campoCabecalho in cabecahoValidar:
        infDadoCriado[campoCabecalho] = valor

def generate_status():
    return random.choice(status)


def generate_tipoCadastro():
    return random.choice(tipoCadastro)


def generate_perfilParceiro():
    return random.choice(perfilParceiro)


def generate_documentoIdentificacao(perfilParceiro):
    return checkTipoPessoa(perfilParceiro)


def generate_razaoSocial_or_name(tipoPessoa):
    if tipoPessoa == "Pessoa Física" or "Estrangeiro":
        return fake.name()
    if tipoPessoa == "Pessoa Jurídica":
        return fake.company()


def generate_nome():
    return fake.name()


def generate_nomeFantasia(tipoPessoa):
    return fake.bs() if tipoPessoa == "Pessoa Jurídica" else ''


def generate_dataAniversario(tipoPessoa):
    return format(fake.date_of_birth(), "%d/%m/%Y") if tipoPessoa == "Pessoa Física" else ''


def generate_CNAE(tipoPessoa):
    return random.choice(cnae) if tipoPessoa == "Pessoa Jurídica" else ''


def generate_inscricaoMunicipal():
    return fake.pyint()


def generate_tipoInscricaoEstadual():
    return random.choice(tipoInscricaoEstadual)


def generate_inscricaoEstadual(inscricaoEstadual):
    return fake.pyint() if inscricaoEstadual != "Isento" else '' 


def generate_SUFRAMA():
    return random.choice(suframa)


def generate_documento():
    return random.choice([fake.cpf(), fake.cnpj()])


def generate_areaResponsavel():
    return fake.bs()


def generate_recebeXML():
    return random.choice(['Sim', 'Não'])


def generate_tipoTelefone():
    return random.choice(tipoTelefone)


def generate_telefone():
    return fake.phone_number()


def generate_email():
    return fake.ascii_free_email()


def generate_tipoEndereco():
    return random.choice(tipoEndereco)


def generate_CEP():
    return fake.postcode()


def generate_logradouro():
    return fake.street_name()


def generate_numeroPropriedade():
    return fake.building_number()


def generate_complemento():
    return fake.address()


def generate_municipio():
    return fake.neighborhood()


def generate_bairro():
    return fake.bairro()


def generate_UF():
    return fake.estado_sigla()


def generate_pais():
    return "Brasil"


def checkTipoPessoa(tipoPessoa):
    if tipoPessoa == "Pessoa Física":
        return fake.cpf()
    if tipoPessoa == "Pessoa Jurídica":
        return fake.cnpj()
    if tipoPessoa == "Estrangeiro":
        return fake.ssn()
