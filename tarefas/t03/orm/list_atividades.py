from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

DATABASE = config('DATABASE')
PORT = config('PORT')
USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
Session = sessionmaker(bind=engine)
session = Session()

atividades = session.query(Atividade).join(AtividadeProjeto, Atividade.codigo == AtividadeProjeto.codAtividade).join(Projeto, AtividadeProjeto.codProjeto == Projeto.codigo).all()

for a in atividades:
    print(a.codigo, a.descricao)

session.close()