SELECT pj.nome, d.descricao AS nome_departamento, f.nome AS responsavel,  df.descricao AS departamento_responsavel
FROM projeto pj INNER JOIN departamento d ON pj.cod_depto = d.codigo INNER JOIN funcionario f ON pj.cod_responsavel = f.codigo INNER JOIN departamento df ON df.codigo = f.cod_depto 
