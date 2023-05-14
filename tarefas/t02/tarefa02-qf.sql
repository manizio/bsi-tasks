CREATE OR REPLACE PROCEDURE show_project_members(id INT)
	LANGUAGE plpgsql
	AS 
	$$
		BEGIN
			SELECT f.nome, d.sigla FROM funcionario f, departamento d, projeto p
			WHERE f.
			;
		END;
	$$;
