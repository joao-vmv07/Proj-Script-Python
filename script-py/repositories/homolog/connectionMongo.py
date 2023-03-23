from pymongo import MongoClient

#Conexão com o banco Dados Homolog GET documentos
# Fornecedor 
# Cliente
# Empresa

def connectionMongoHomolog(contmaticId):
    mongoclient = MongoClient(
        host='mongodb://arquivo:%40rquivo@192.168.5.175:27017',
        authSource='admin'
    )
    db_parceiro = mongoclient["parceiro_homolog"]
    coll_parceiro_fornecedor = db_parceiro["clienteFornecedor"]
    coll_parceiro_cliente = db_parceiro["clienteFornecedor"]

    queryDocForncedor = {"fornecedor": True, "_id.contmaticId": contmaticId}
    queryDocCliente = {"cliente": True, "_id.contmaticId": contmaticId}
    projection = {
        "_id": 1, 
    } 
    cursorFornecedor = coll_parceiro_fornecedor.find(queryDocForncedor, projection)
    cursorCliente = coll_parceiro_cliente.find(queryDocCliente, projection)

    parceiro_fornecedor = list(cursorFornecedor)
    parceiro_cliente = list(cursorCliente)
    cursorFornecedor.close()
    cursorCliente.close()

    documentosFornecedor = list(map(lambda fornecedorDoc: fornecedorDoc["_id"]["documento"], parceiro_fornecedor))
    documentosCliente = list(map(lambda clienteDoc: clienteDoc["_id"]["documento"], parceiro_cliente))
    mongoclient.close()
    return documentosCliente, documentosFornecedor

