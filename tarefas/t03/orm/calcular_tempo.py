from connect import connect
from report import relatorio_projetos
from models import *

import time

session = connect()

def select_first_thousand():
    get_func = session.query(Funcionario).limit(1000).all()
    get_dep = session.query(Departamento).limit(1000).all()
    get_atv = session.query(Atividade).limit(1000).all()
    get_proj = session.query(Projeto).limit(1000).all()

def calcular_tempo(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

def log_time():
    logs = session.query(Log).all()
    num = len(logs)

    session.add(Log(
        log="Log " + str(num),
        time=calcular_tempo(select_first_thousand)
    ))
    session.commit()

def log_report():
    logs = session.query(Log).all()
    num = len(logs)

    session.add(Log(
        log="Log " + str(num),
        time=calcular_tempo(relatorio_projetos)
    ))
    session.commit()
    
if __name__ == '__main__':
    log_time()
    log_report()

