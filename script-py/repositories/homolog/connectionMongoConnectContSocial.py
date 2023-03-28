from pymongo import MongoClient

def connectionMongoContSocialHomolog(email):
    mongoclient = MongoClient(
            host='mongodb://arquivo:%40rquivo@192.168.5.175:27017',
            authSource='admin'
    )

    db_connecticont_social = mongoclient["connectcont-social-homolog"]
    coll_usuario = db_connecticont_social["usuario"]

    query_usuario_email = {"email": f'{email}'}
    projection = {
            "_id": 1, 
    }
    cursor_usuario = coll_usuario.find(query_usuario_email, projection)
    object_id = list(cursor_usuario)
    
    if not object_id:
        cursor_usuario.close()
        mongoclient.close()
        return None

    id_usuario = str(object_id[0]["_id"]).split('\'')[0]

    cursor_usuario.close()

    coll_usuario_contrato = db_connecticont_social["usuarioContrato"]
    query_usuario_id = {"_id.codigo": f'{id_usuario}'}
    projection = {
        "_id.contmaticId": 1,
    }

    cursor_usuario_contrato = coll_usuario_contrato.find(query_usuario_id, projection)
    cursor_usuario.close()

    lista_contratos = list(cursor_usuario_contrato)
    contmatic_id = list(map(lambda contrato: contrato["_id"]["contmaticId"], lista_contratos))

    if len(contmatic_id) > 1:
        lista_Info_contratos = []
        for contmaticid in contmatic_id:
            coll_usuario_contrato_contmaticId = db_connecticont_social["contrato"]
            query_contimatic_id = {"_id": contmaticid}
            projection = {
                "razaoSocial": 1,
                "cpfCnpj" : 1
            }
            cursor_contrato = coll_usuario_contrato_contmaticId.find(query_contimatic_id, projection)
            lista_Info_contratos.append(cursor_contrato.next())
        cursor_contrato.close()    
        mongoclient.close()
        return lista_Info_contratos
    mongoclient.close()
    return list(contmatic_id) 
   

    

    



