CREATE VIEW total_funcionarios AS SELECT d.codigo, d.descricao AS departamento, COUNT (f.codigo) AS total_funcionarios FROM departamento d LEFT JOIN funcionario f ON f.cod_depto = d.codigo
GROUP BY d.codigo;

SELECT d.descricao, f.nome AS gerente, v.total_funcionarios FROM departamento d LEFT JOIN funcionario f ON d.cod_gerente = f.codigo LEFT JOIN total_funcionarios v ON d.codigo = v.codigo 
