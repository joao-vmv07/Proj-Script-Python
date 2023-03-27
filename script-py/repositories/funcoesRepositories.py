
from repositories.homolog.connectionMongoERP import connectionMongoHomolog
from repositories.homolog.connectionPostgresERP import connectionPostgresHomolog
from repositories.dev.connectionMongoERP import connectionMongoDev
from repositories.dev.connectionPostgresERP import connectionPostgresDev

def getBaseDados(telacadastro, ambiente ,contmaticId):
    if telacadastro =="-par" and ambiente == "-d":
        documentosCadastrados = connectionMongoDev(contmaticId)
        return documentosCadastrados
    if telacadastro =="-par" and ambiente == "-h":
        documentosCadastrados = connectionMongoHomolog(contmaticId)
        return documentosCadastrados
    if telacadastro == "-pro" and ambiente == "-d":
        documentosCliente, documentosFornecedor = connectionMongoDev(contmaticId)
        listaAtributos, listaGrupos, listaCodigoTributacao = connectionPostgresDev(contmaticId)
        return documentosCliente, documentosFornecedor, listaAtributos, listaGrupos, listaCodigoTributacao
    if telacadastro == "-pro" and ambiente == "-h":
        documentosCliente, documentosFornecedor = connectionMongoHomolog(contmaticId)
        listaAtributos, listaGrupos, listaCodigoTributacao = connectionPostgresHomolog(contmaticId)
        return documentosCliente, documentosFornecedor, listaAtributos, listaGrupos, listaCodigoTributacao