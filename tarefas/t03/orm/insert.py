from models import *
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from decimal import Decimal
from random import choice
from faker import Faker
import sys


engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/tarefa03')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def populate_funcionario(num_rows):
    for i in range(int(num_rows)):
        name = fake.name()
        gender=fake.random_element(['M', 'F'])
        dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
        salary = fake.pydecimal(left_digits=5, right_digits=2, positive=True)
        session.add (Funcionario(
            nome=name, 
            sexo=gender, 
            dataNasc=dob, 
            salario=salary
        )),
        session.commit()
    for f in session.query(Funcionario):
        if f.supervisor is None:
            supervisor = choice(session.query(Funcionario).filter(Funcionario != f).all())
            f.supervisor_id = supervisor.codigo
            session.commit()
    

def populate_departamento(num_rows):
    fixed_letters = 'DP' 
    fixed_dp = 'Departamento'
    for i in range( int (num_rows)):
        third_character = fake.random_digit() 
        department = fixed_letters + str(third_character)
        description = fixed_dp + str(third_character)
        session.add(Departamento (
            sigla=department,
            descricao=description))
        session.commit()
    for d in session.query(Departamento):
        if d.gerente is None:
            f = choice(session.query(Funcionario).all())
            d.gerente = f
            d.gerente_id= f.codigo
            session.commit()
    for f in session.query(Funcionario):
        if f.depto_id is None:
            dep= choice(session.query(Departamento).all())
            d_id= dep.codigo
            f.depto_id= d_id
            session.commit()
   
            
def populate_equipe(num_rows):
    fixed_eqp ="Equipe "
    for i in range (int(num_rows)):
        color= fake.color_name()
        name = fixed_eqp + str(color)
        session.add(Equipe(
            nomeEquipe= name
        )
        )
        session.commit()
        

def populate_membro(num_rows):
    team = choice(session.query(Equipe).all())
    team_id=  team.codigo
    f = choice(session.query(Funcionario).all())
    f_id = f.codigo
    for i in range(int(num_rows)):
        session.add(Membro(
            codEquipe_id= team_id,
            codFuncionario_id= f_id
        )
        )
        session.commit()

def populate_projeto(num_rows):
    cont = len(session.query(Projeto).all())
    fixed_proj = 'Projeto'
    for i in range(int (num_rows)):
        cont+=1
        last_character = cont
        description = fixed_proj + str(last_character)
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = fake.date_between(start_date=start_date, end_date='+1y')
        conclusion_date = fake.date_between(start_date=start_date, end_date=end_date)
        status_options = ["Em andamento", "Concluído"]
        status = fake.random_element(status_options)
        session.add(Projeto(
            descricao=description,
            dataInicio=start_date,
            dataFim= end_date,
            situacao=status,
            dataConclusao=conclusion_date
            ))
        session.commit()
    for p in session.query(Projeto):
        if p.depto is None:
            departamento = choice(session.query(Departamento).all())
            p.depto = departamento
            p.depto_id= departamento.codigo
            session.commit()
        if p.responsavel is None:        
            responsavel = choice(session.query(Funcionario).all())
            p.responsavel_id = responsavel.codigo
            session.commit()


session.commit()

def populate_atividade(num_rows):
    cont = len(session.query(Atividade).all())
    fixed_atv="Atividade"
    for i in range(int(num_rows)):
        cont+=1
        last_character = cont
        description = fixed_atv + str(last_character)
        start_date = fake.date_between(start_date='-1y', end_date='today')
        end_date = fake.date_between(start_date=start_date, end_date='+1y')
        conclusion_date = fake.date_between(start_date=start_date, end_date=end_date)
        status_options = ["Em andamento", "Concluído"]
        status = fake.random_element(status_options)
        session.add(Atividade(
            descricao=description,
            dataInicio=start_date,
            dataFim=end_date,
            situacao=status,
            dataConclusao=conclusion_date
            ))
        session.commit()

def populate_atividadeMembro(num_rows):
    for i in range (int(num_rows)):
        m_id = choice(session.query(Membro).all()).codigo
        a_id = choice(session.query(Atividade).all()).codigo
        if not session.query(AtividadeMembro).all():
            session.add(AtividadeMembro(
                codAtividade=a_id,
                codMembro=m_id
            ))
            session.commit()
        else:
            for am in session.query(AtividadeMembro).all():
                m_id = choice(session.query(Membro).all()).codigo
                a_id = choice(session.query(Atividade).all()).codigo
                if (am.codAtividade != a_id and am.codMembro != m_id):
                    if(am.codAtividade is None):
                        session.add(AtividadeMembro(
                            codAtividade=a_id,
                            codMembro=m_id
                        ))
            session.commit()


def populate_atividadeProjeto(num_rows):
    for i in range (int(num_rows)):
        p_id = choice(session.query(Projeto).all()).codigo
        a_id = choice(session.query(Atividade).all()).codigo
        if not session.query(AtividadeProjeto).all():
            session.add(AtividadeProjeto(
                codAtividade=a_id,
                codProjeto=p_id
            ))
        else:
            for ap in session.query(AtividadeProjeto).all():
                p_id = choice(session.query(Projeto).all()).codigo
                a_id = choice(session.query(Atividade).all()).codigo
                if (ap.codAtividade != a_id and ap.codProjeto != p_id):
                    if(ap.codAtividade is None):
                        session.add(AtividadeProjeto(
                            codAtividade=a_id,
                            codProjeto=p_id 
                        ))
        session.commit()        



session.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        argumento = sys.argv[1]
        populate_funcionario(argumento)
        populate_departamento(argumento)
        populate_equipe(argumento)
        populate_membro(argumento)
        populate_projeto(argumento)
        populate_atividade(argumento)
        populate_atividadeMembro(argumento)
        populate_atividadeProjeto(argumento)
    else:
        print("Nenhum argumento fornecido.")
