from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()
#engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/tarefa03')
engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/tarefa04')

class Funcionario(Base):
    __tablename__ = 'funcionario'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    sexo = Column(String, nullable=False)
    dataNasc = Column(DateTime, nullable=False)
    salario = Column(Numeric, nullable=False)
    supervisor_id = Column(Integer, ForeignKey('funcionario.codigo'), nullable=True)
    depto_id = Column(Integer, ForeignKey('departamento.codigo'), nullable=True)

    supervisor = relationship('Funcionario', remote_side=[codigo], backref='supervisor_func')
    depto = relationship('Departamento', backref='depto_funcionario', foreign_keys=[depto_id])

    membro = relationship('Membro', backref='membro_funcionario')
    projeto = relationship('Projeto', backref='resp_projeto')

    atividade_membro = relationship('AtividadeMembro', backref='atv_membro')


class Departamento(Base):
    __tablename__ = 'departamento'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    sigla = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    gerente_id = Column(Integer, ForeignKey('funcionario.codigo'))

    gerente = relationship('Funcionario', backref='gerente_depto', foreign_keys=[gerente_id])

    projeto = relationship('Projeto', backref='depto_projeto')

class Equipe(Base):
    __tablename__ = 'equipe'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    nomeEquipe = Column(String, nullable=False)

    equipe_membro = relationship('Membro', backref='equipe_membro')
    projeto = relationship('Projeto', backref='projeto_equipe')

class Membro(Base):
    __tablename__ = 'membro'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    codEquipe_id = Column(Integer, ForeignKey('equipe.codigo'))
    codFuncionario_id = Column(Integer, ForeignKey('funcionario.codigo'))

    membro_equipe = relationship('Equipe', backref='membro_equipe')
    funcionario = relationship('Funcionario', backref='equipe_funcionario')


class Projeto(Base):
    __tablename__ = 'projeto'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)
    depto_id = Column(Integer, ForeignKey('departamento.codigo'))
    responsavel_id = Column(Integer, ForeignKey('funcionario.codigo'))
    dataInicio = Column(DateTime, nullable=False)
    dataFim = Column(DateTime, nullable=False)
    situacao = Column(String, nullable=False)
    dataConclusao = Column(DateTime, nullable=True)
    equipe_id = Column(Integer, ForeignKey('equipe.codigo'))

    depto = relationship('Departamento', backref='depto_projeto')
    responsavel = relationship('Funcionario', backref='resp_projeto')
    equipe = relationship('Equipe', backref='projeto_equipe')

    atividade = relationship('AtividadeProjeto', backref='projeto_atv')

class Atividade(Base):
    __tablename__ = 'atividade'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)
    dataInicio = Column(DateTime, nullable=False)
    dataFim = Column(DateTime, nullable=False)
    situacao = Column(String, nullable=False)
    dataConclusao = Column(DateTime, nullable=True)

    atividade_membro = relationship('AtividadeMembro', backref='atividade_atividade')
    atividade_projeto = relationship('AtividadeProjeto', backref='atv_projeto')

class AtividadeMembro(Base):
    __tablename__ = 'atividade_membro'
    codAtividade = Column(Integer, ForeignKey('atividade.codigo'), primary_key=True)
    codMembro = Column(Integer, ForeignKey('funcionario.codigo'), primary_key=True)

    atividade = relationship('Atividade', backref='atividade_atividade')
    membro = relationship('Funcionario', backref='atv_membro')

class AtividadeProjeto(Base):
    __tablename__ = 'atividade_projeto'
    codAtividade = Column(Integer, ForeignKey('atividade.codigo'), primary_key=True)
    codProjeto = Column(Integer, ForeignKey('projeto.codigo'), primary_key=True)

    atividade = relationship('Atividade', backref='atv_projeto')
    projeto = relationship('Projeto', backref='projeto_atv')

Base.metadata.create_all(engine)