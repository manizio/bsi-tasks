SELECT f.nome FROM funcionario f
WHERE f.salario > (SELECT MAX(f.salario) FROM funcionario f WHERE f.cod_depto = 2)
