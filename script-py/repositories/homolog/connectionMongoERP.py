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

    query_doc_forncedor = {"fornecedor": True, "_id.contmaticId": contmaticId}
    query_doc_cliente = {"cliente": True, "_id.contmaticId": contmaticId}
    projection = {
        "_id": 1, 
    } 
    cursor_fornecedor = coll_parceiro_fornecedor.find(query_doc_forncedor, projection)
    cursor_cliente = coll_parceiro_cliente.find(query_doc_cliente, projection)

    parceiro_fornecedor = list(cursor_fornecedor)
    parceiro_cliente = list(cursor_cliente)
    cursor_fornecedor.close()
    cursor_cliente.close()

    documentos_fornecedor = list(map(lambda fornecedorDoc: fornecedorDoc["_id"]["documento"], parceiro_fornecedor))
    documentos_cliente = list(map(lambda clienteDoc: clienteDoc["_id"]["documento"], parceiro_cliente))
    mongoclient.close()
    return documentos_cliente, documentos_fornecedor