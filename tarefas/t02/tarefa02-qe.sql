CREATE OR REPLACE FUNCTION is_project_delayed(id INT)
	RETURNS int
	LANGUAGE plpgsql
	AS 
	$$
		DECLARE
			days INT;
		BEGIN
			SELECT p.datafim - p.dataconclusao INTO days FROM projeto p WHERE p.codigo = id;
			RETURN days;
		END;
	$$;
