CREATE OR REPLACE FUNCTION is_delayed(id INT)
	RETURNS int
	LANGUAGE plpgsql
	AS 
	$$
		DECLARE
			days INT;
		BEGIN
			SELECT att.datafim - att.dataconclusao INTO days FROM atividade att
			WHERE att.codigo = id;
			RETURN days;
		END;
	$$;
