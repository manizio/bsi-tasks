from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/tarefa03')
Session = sessionmaker(bind=engine)
session = Session()

atividades = session.query(Atividade).join(AtividadeProjeto, Atividade.codigo == AtividadeProjeto.codAtividade).join(Projeto, AtividadeProjeto.codProjeto == Projeto.codigo).all()

for a in atividades:
    print(a.codigo, a.descricao)

session.close()