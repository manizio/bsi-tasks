INSERT INTO departamento (descricao, cod_gerente) VALUES ('departamento de historia', NULL);

INSERT INTO departamento (descricao, cod_gerente) VALUES ('departamento de matematica', NULL);

INSERT INTO departamento (descricao, cod_gerente) VALUES ('departamento de bsi', NULL);

INSERT INTO departamento (descricao, cod_gerente) VALUES ('departamento de contabeis', NULL);

INSERT INTO departamento (descricao, cod_gerente) VALUES ('departamento de geografia', NULL);


INSERT INTO funcionario (nome, sexo, dt_nasc, salario, cod_depto) VALUES ('josé', 'M', '1999-02-17', 5555, 1);

INSERT INTO funcionario (nome, sexo, dt_nasc, salario, cod_depto) VALUES ('maria', 'F', '1996-03-17', 5757, 2);

INSERT INTO funcionario (nome, sexo, dt_nasc, salario, cod_depto) VALUES ('joão', 'M', '2000-05-05', 3000, 3);

INSERT INTO funcionario (nome, sexo, dt_nasc, salario, cod_depto) VALUES ('david', 'M', '1993-01-24', 3000, 4);

INSERT INTO funcionario (nome, sexo, dt_nasc, salario, cod_depto) VALUES ('paula', 'M', '1995-07-23', 3001, 5);

UPDATE departamento SET cod_gerente = 1 WHERE codigo = 1;
UPDATE departamento SET cod_gerente = 2 WHERE codigo = 2;


INSERT INTO projeto(nome, descricao, cod_depto, cod_responsavel, data_inicio, data_fim) VALUES ('projeto 01', 'primeiro projeto',1, 1, '2021-12-12' , '2022-01-04');

INSERT INTO projeto(nome, descricao, cod_depto, cod_responsavel, data_inicio, data_fim) VALUES ('projeto 02', 'segundo projeto',2, 2, '2022-12-12' , '2023-01-04');

INSERT INTO projeto(nome, descricao, cod_depto, cod_responsavel, data_inicio, data_fim) VALUES ('projeto 03', 'terceiro projeto',3, 3, '2024-12-12' , '2025-01-04');

INSERT INTO projeto(nome, descricao, cod_depto, cod_responsavel, data_inicio, data_fim) VALUES ('projeto 04', 'quarto projeto',4, 4, '2026-12-12' , '2027-01-04');

INSERT INTO projeto(nome, descricao, cod_depto, cod_responsavel, data_inicio, data_fim) VALUES ('projeto 05', 'quinto projeto',5, 5, '2028-12-12' , '2029-01-04');

INSERT INTO atividade (nome, descricao, cod_responsavel, data_inicio, data_fim) VALUES ('atividade 01', 'primeira atividade', 1, '2021-12-12' , '2022-01-04');

INSERT INTO atividade (nome, descricao, cod_responsavel, data_inicio, data_fim) VALUES ('atividade 02', 'segunda atividade', 2, '2022-12-12' , '2023-01-04');

INSERT INTO atividade (nome, descricao, cod_responsavel, data_inicio, data_fim) VALUES ('atividade 03', 'terceira atividade', 3, '2023-12-12' , '2024-01-04');

INSERT INTO atividade (nome, descricao, cod_responsavel, data_inicio, data_fim) VALUES ('atividade 04', 'quarta atividade', 4, '2025-12-12' , '2026-01-04');

INSERT INTO atividade (nome, descricao, cod_responsavel, data_inicio, data_fim) VALUES ('atividade 05', 'quinta atividade', 5, '2027-12-12' , '2028-01-04');

INSERT INTO atividade_projeto (cod_projeto, cod_atividade) VALUES (1, 1);

INSERT INTO atividade_projeto (cod_projeto, cod_atividade) VALUES (2, 2);

INSERT INTO atividade_projeto (cod_projeto, cod_atividade) VALUES (3, 3);

INSERT INTO atividade_projeto (cod_projeto, cod_atividade) VALUES (4, 4);

INSERT INTO atividade_projeto (cod_projeto, cod_atividade) VALUES (5, 5);
