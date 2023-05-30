from models import *
from connect import connect

session = connect()

atividades = session.query(Atividade).join(AtividadeProjeto, Atividade.codigo == AtividadeProjeto.codAtividade).join(Projeto, AtividadeProjeto.codProjeto == Projeto.codigo).all()

for a in atividades:
    print(a.codigo, a.descricao)

session.close()