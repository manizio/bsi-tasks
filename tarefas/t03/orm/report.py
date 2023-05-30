from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Projeto, Departamento, Equipe, Membro, Atividade, AtividadeMembro, AtividadeProjeto

# Criação da conexão com o banco de dados (substitua as informações de acordo com o seu banco)
engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/tarefa03')
Session = sessionmaker(bind=engine)
session = Session()

def relatorio_projetos():
    # Consulta para obter informações dos projetos
    projetos_info = session.query(
        Projeto.codigo,
        Projeto.descricao
    )

    # Exibição das informações
    for projeto in projetos_info:
        print(f"Código do Projeto: {projeto.codigo}")
        print(f"Nome do Projeto: {projeto.descricao}")
        print("---------------------------------------------------")

# Chamada do procedimento
relatorio_projetos()
