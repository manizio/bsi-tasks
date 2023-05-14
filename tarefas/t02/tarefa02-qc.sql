CREATE OR REPLACE PROCEDURE get_above_avg_age()
	LANGUAGE plpgsql
	AS
	$$
		DECLARE
		f RECORD;
		media RECORD;
		BEGIN
			FOR f IN SELECT * FROM funcionario as func, departamento d
			WHERE func.depto = d.codigo
			LOOP
				FOR media IN SELECT * FROM get_average_age()
				LOOP
					IF get_age(f.datanasc) > media.media AND f.depto = media.id THEN
						RAISE NOTICE 'funcionario % está acima da media do seu departamento', f.nome;
					END IF;
				END LOOP;
			END LOOP;
		END;
	$$;
			
