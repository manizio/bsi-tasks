CREATE VIEW func_resp AS SELECT f.codigo, f.nome AS responsavel, COUNT(a.codigo) AS num_atividades FROM funcionario f INNER JOIN atividade a ON f.codigo = a.cod_responsavel
GROUP BY f.codigo;

SELECT v.responsavel, v.num_atividades FROM funcionario f LEFT JOIN func_resp v ON v.codigo = f.codigo
