#   CAMPOS
#   Atributo
#   Grupo
#   Código tributação
from sqlalchemy import create_engine,text

def connectionPostgresHomolog(contmaticId):
    conn = create_engine('postgresql+psycopg2://postgres:ContSQL2017@192.168.5.29:5432/erp_homolog')
    queryNomeAtributo = f'''
        SELECT nome
        FROM atributo
        WHERE contmatic_id = {contmaticId["_id"]}
    '''
    queryNomeGrupo = f'''
        SELECT nome
        FROM grupo
        WHERE contmatic_id = {contmaticId["_id"]}
    '''
    queryTributacao = f'''
        SELECT codigo
        FROM tributacao 
        WHERE contmatic_id = {contmaticId["_id"]}
    '''

    dbConnection = conn.connect()
    resultAtributo = dbConnection.execute(text(queryNomeAtributo))
    resultGrupo = dbConnection.execute(text(queryNomeGrupo))
    resultTributacao = dbConnection.execute(text(queryTributacao))

    listaAtributos = list(map(lambda atributo: atributo[0], list(resultAtributo)))
    listaGrupos = list(map(lambda grupo: grupo[0], list(resultGrupo)))
    listaCodigoTributacao = list(map(lambda tributacao: tributacao[0], list(resultTributacao)))
    dbConnection.close()
    return listaAtributos, listaGrupos , listaCodigoTributacao