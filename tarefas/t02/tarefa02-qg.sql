CREATE OR REPLACE FUNCTION count_activity(id INT)
	returns int
	LANGUAGE plpgsql
	AS 
	$$
		DECLARE
		num INT;
		
		BEGIN
			SELECT COUNT (*) as num_atividades INTO num FROM atividade_projeto ap JOIN atividade att ON ap.codatividade = att.codigo
									JOIN atividade_membro am ON att.codigo = am.codatividade
									JOIN membro m ON am.codmembro = m.codigo
									JOIN funcionario f ON m.codfuncionario = f.codigo
									WHERE f.codigo = id;
			RETURN num;
		END;
	$$;
