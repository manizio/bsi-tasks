CREATE OR REPLACE FUNCTION get_average_age()
	returns table(departamento VARCHAR, media NUMERIC)
	language plpgsql
	as $$
	begin
		RETURN QUERY SELECT d.sigla as departamento, AVG(get_age(f.datanasc)) as media
		from funcionario f, departamento d
		WHERE f.codigo = d.codigo
		GROUP BY d.codigo;
	end;
	$$;
