#   CAMPOS
#   Atributo
#   Grupo
#   Código tributação
from sqlalchemy import create_engine,text

def connectionPostgres(contmaticId):
    conn = create_engine('postgresql+psycopg2://postgres@192.168.5.27/erp')
    queryNomeAtributo = f'''
        SELECT nome
        FROM atributo
        WHERE contmatic_id = {contmaticId}
    '''
    queryNomeGrupo = f'''
        SELECT nome
        FROM grupo
        WHERE contmatic_id = {contmaticId}
    '''
    queryTributacao = f'''
        SELECT codigo
        FROM tributacao 
        WHERE contmatic_id = {contmaticId};
    '''

    resultAtributo = conn.connect().execute(text(queryNomeAtributo))
    resultGrupo = conn.connect().execute(text(queryNomeGrupo))
    resultTributacao = conn.connect().execute(text(queryTributacao))

    listaAtributos = list(map(lambda atributo: atributo[0], list(resultAtributo)))
    listaGrupos = list(map(lambda grupo: grupo[0], list(resultGrupo)))
    listaCodigoTributacao = list(map(lambda tributacao: tributacao[0], list(resultTributacao)))
    return listaAtributos, listaGrupos , listaCodigoTributacao