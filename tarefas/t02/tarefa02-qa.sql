CREATE FUNCTION get_age(idade date)
	returns int
	language plpgsql
	as $$
	declare 
		func_age int;
	begin
		SELECT extract(year from age(idade)) into func_age
		from funcionario;
		
		return func_age;
	end;
	$$;
