from connect import connect


def listar_atividades():
    conn = connect()
    cur = conn.cursor()

    script = '''
    SELECT p.codigo as codigo_projeto, p.descricao, a.codigo as codigo_atividade, a.descricao
    FROM projeto p 
    JOIN atividade_projeto ap ON p.codigo = ap.codprojeto 
    JOIN atividade a ON a.codigo = ap.codatividade
    '''
    cur.execute(script)

    atividades = cur.fetchall()
    cur.close()
    conn.close()

    return atividades


if __name__ == "__main__":
    res = listar_atividades()

    for i in res:
        print (i)


