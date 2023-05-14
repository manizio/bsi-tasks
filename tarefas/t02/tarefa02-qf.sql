CREATE OR REPLACE PROCEDURE show_project_members(id INT)
	LANGUAGE plpgsql
	AS 
	$$
		DECLARE 
			res RECORD;
		BEGIN
			FOR RES IN SELECT f.nome, d.sigla FROM projeto p
						JOIN equipe e ON p.equipe = e.codigo
						JOIN membro m ON m.codequipe = e.codigo
						JOIN funcionario f ON f.codigo = m.codfuncionario
						JOIN departamento d ON f.depto = d.codigo
						WHERE p.codigo = id
			LOOP
			RAISE NOTICE 'Funcionário: %, Departamento: %', res.nome, res.sigla;
			END LOOP;
		END;
	$$;
	
