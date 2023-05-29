from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from decimal import Decimal
from random import choice
from faker import Faker


engine = create_engine('postgresql://postgres:postgres@127.0.0.1:8001/tarefa03')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def populate_funcionario(num_rows):
    funcionarios = []
    
    for _ in range(num_rows):
        name = fake.name()
        gender=fake.random_element(['M', 'F'])
        dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
        salary = fake.pydecimal(left_digits=5, right_digits=2, positive=True)
        Funcionario(
            nome=name, 
            sexo=gender, 
            dataNasc=dob, 
            salario=salary
        ),
        
        funcionarios.append(Funcionario)
    session.add_all(funcionarios)
    session.commit()
    



funcionarios = session.query(Funcionario).all()
for i in range(len(funcionarios) - 1):
    supervisor = choice(funcionarios[:i] + funcionarios[i+1:])
    funcionarios[i].supervisor = supervisor

ultimo_funcionario = funcionarios[-1]
funcionario_aleatorio = choice(funcionarios[:-1])
funcionario_aleatorio.supervisor = ultimo_funcionario

session.commit()

projetos = [
    Projeto(descricao='Projeto 1', dataInicio=datetime(2023, 1, 1), dataFim=datetime(2023, 12, 31),
            situacao='Em andamento', dataConclusao=None),
    Projeto(descricao='Projeto 2', dataInicio=datetime(2023, 2, 1), dataFim=datetime(2023, 11, 30),
            situacao='Em andamento', dataConclusao=None),
    Projeto(descricao='Projeto 3', dataInicio=datetime(2023, 3, 1), dataFim=datetime(2023, 10, 31),
            situacao='Em andamento', dataConclusao=None)
]

session.add_all(projetos)
session.commit()

for p in session.query(Projeto).all():
    departamento = choice(session.query(Departamento).all())
    responsavel = choice(session.query(Funcionario).all())
    p.depto = departamento
    p.responsvel = responsavel

session.commit()

atividades = [
    Atividade(descricao='Atividade 1', dataInicio=datetime(2023, 1, 1), dataFim=datetime(2023, 1, 10),
              situacao='Concluída', dataConclusao=datetime(2023, 1, 11)),
    Atividade(descricao='Atividade 2', dataInicio=datetime(2023, 1, 15), dataFim=datetime(2023, 1, 25),
              situacao='Concluída', dataConclusao=datetime(2023, 1, 26)),
    Atividade(descricao='Atividade 3', dataInicio=datetime(2023, 2, 1), dataFim=datetime(2023, 2, 10),
              situacao='Em andamento', dataConclusao=datetime(2023,3,3))
]

session.add_all(atividades)
session.commit()

for atividade in session.query(Atividade).all():
    membros = session.query(Funcionario).order_by(Funcionario.codigo).limit(2).all()
    for membro in membros:
        atividade_membro = AtividadeMembro(atividade=atividade, membro=membro)
        session.add(atividade_membro)
session.commit()

for atividade in session.query(Atividade).all():
    projeto = choice(session.query(Projeto).all())
    atividade_projeto = AtividadeProjeto(atividade=atividade, projeto=projeto)
session.commit()

equipes = [
    Equipe(nomeEquipe='OPC'),
    Equipe(nomeEquipe='Equipe Azul'),
    Equipe(nomeEquipe='Equipados')
]

session.add_all(equipes)
session.commit()

membros = [
    Membro(membro_equipe=choice(session.query(Equipe).all()), funcionario=choice(session.query(Funcionario).all())),
    Membro(membro_equipe=choice(session.query(Equipe).all()), funcionario=choice(session.query(Funcionario).all())),
    Membro(membro_equipe=choice(session.query(Equipe).all()), funcionario=choice(session.query(Funcionario).all()))
]

session.add_all(membros)
session.commit()

session.close()
