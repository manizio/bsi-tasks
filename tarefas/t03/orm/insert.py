from models import *
from sqlalchemy import Null, create_engine
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
    for f in session.query(Funcionario).all():
        if f.supervisor is Null:
            supervisor = choice(session.query(Funcionario).filter(Funcionario != f).all())
            f.supervisor_id = supervisor.codigo
            session.commit
    

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
    for d in session.query(Departamento).all():
        if d.gerente is Null:
            f = choice(session.query(Funcionario).all())
            d.gerente = f
            d.gerente_id= f.codigo
    session.commit


def populate_projeto(num_rows):
    
    fixed_proj = 'Projeto'
    for i in range(int (num_rows)):
        last_character = fake.random_digit()
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
    for p in session.query(Projeto).all():
        if p.depto is Null:
            departamento = choice(session.query(Departamento).all())
            p.depto = departamento
            p.depto_id= departamento.codigo
        if p.responsavel is Null:        
            responsavel = choice(session.query(Funcionario).all())
            p.responsvel = responsavel
    session.commit()


session.commit()

def populate_atividade(num_rows):
    fixed_atv="Atividade"
    for i in range(int(num_rows)):
        last_character = fake.random_digit()
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

session.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        argumento = sys.argv[1]
        populate_funcionario(argumento)
        populate_departamento(argumento)
        populate_projeto(argumento)
        populate_atividade(argumento)
    else:
        print("Nenhum argumento fornecido.")