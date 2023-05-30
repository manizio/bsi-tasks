from datetime import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Funcionario,Projeto, Departamento, Equipe, Membro, Atividade, AtividadeMembro, AtividadeProjeto
from decouple import config

DATABASE = config('DATABASE')
PORT = config('PORT')
USER = config('USER')
PASSWORD = config('PASSWORD')
HOST = config('HOST')
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
Session = sessionmaker(bind=engine)
session = Session()

def relatorio_projetos():
    # Consulta para obter informações dos projetos

    # Exibição das informações
    for projeto in session.query(Projeto):
        id_r = projeto.responsavel_id
        name_g = None
        cont_memb =0
        cont_ativ = 0
        cont_ativ_atra = 0
        data_atual = datetime.now()
        cont_atraso_day_ativ= 0
        atraso = data_atual - projeto.dataFim
        for f in session.query(Funcionario):
            if f.codigo == id_r:
                name_g = f.nome
        for m in session.query(Membro):
            if projeto.equipe_id == m.codEquipe_id:
                cont_memb +=1
        for ap in session.query(AtividadeProjeto):
            if projeto.codigo == ap.codProjeto:
                cont_ativ+=1
                for a in session.query(Atividade):
                    if (a.codigo == ap.codAtividade) and a.situacao.lower() !="concluído":
                        cont_ativ_atra+=1
                        atraso_ativ= data_atual- a.dataFim
                        cont_atraso_day_ativ+= atraso_ativ.days

        print(f"Código do Projeto: {projeto.codigo}")
        print(f"Nome do Projeto: {projeto.descricao}")
        print(f"Nome do Gerente: {name_g}")
        print(f"Quantidade de Membros da Equipe: {cont_memb}")
        print("O atraso em dias é:", atraso.days if projeto.situacao.lower() != "concluído" and atraso.days>0 else "N/A")
        print("A quantidade de atividades no projeto é:", cont_ativ)
        print("A quantidade de atividades não concluídas no projeto é:", cont_ativ_atra)
        print("A soma de dias das atividades atrasadas é:", cont_atraso_day_ativ if cont_atraso_day_ativ>0 else "N/A")
        print("---------------------------------------------------")

# Chamada do procedimento
relatorio_projetos()
