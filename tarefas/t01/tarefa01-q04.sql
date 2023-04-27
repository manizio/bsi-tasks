SELECT f.nome, f.salario, f.cod_depto FROM funcionario f WHERE f.nome NOT IN (SELECT f.nome FROM funcionario f, departamento d WHERE d.cod_gerente = f.codigo)
ORDER BY f.cod_depto
