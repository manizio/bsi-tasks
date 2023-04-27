CREATE TABLE funcionario (
	codigo int,
  	nome varchar(255),
  	sexo varchar(10),
  	dt_nasc date,
  	salario real,
  	cod_depto int,
	PRIMARY KEY(codigo)
);

CREATE TABLE departamento(
	codigo int,
  	descricao varchar(255),
  	cod_gerente int,
  
  	PRIMARY KEY (codigo)
);

CREATE TABLE projeto(
	codigo int,
  	nome varchar(100),
  	descricao varchar(255),
  	cod_depto int,
  	cod_responsavel int,
  	data_inicio date,
  	data_fim date,
  
  	PRIMARY KEY(codigo)
);

CREATE TABLE atividade (
	codigo int,
  	nome varchar(255),
  	descricao varchar(255),
  	cod_responsavel int,
  	data_inicio date,
  	data_fim date,
  
  	PRIMARY KEY(codigo)
);

CREATE TABLE atividade_projeto(
	cod_projeto int,
  	cod_atividade int,
  
  	PRIMARY KEY(cod_projeto, cod_atividade)
);

ALTER TABLE funcionario ADD CONSTRAINT fk_depto FOREIGN KEY (cod_depto) REFERENCES departamento(codigo);

ALTER TABLE departamento ADD CONSTRAINT fk_gerente FOREIGN KEY (cod_gerente) REFERENCES funcionario(codigo);

ALTER TABLE projeto ADD CONSTRAINT fk_depto_proj FOREIGN KEY (cod_depto) REFERENCES departamento (codigo);

ALTER TABLE projeto ADD CONSTRAINT fk_resp FOREIGN KEY (cod_responsavel) REFERENCES funcionario(codigo);

ALTER TABLE atividade ADD CONSTRAINT fk_resp_ativ FOREIGN KEY (cod_responsavel) REFERENCES funcionario(codigo);

ALTER TABLE atividade_projeto ADD CONSTRAINT fk_projeto FOREIGN KEY (cod_projeto) REFERENCES projeto(codigo);

ALTER TABLE atividade_projeto ADD CONSTRAINT fk_atividade FOREIGN KEY (cod_atividade) REFERENCES atividade(codigo);
