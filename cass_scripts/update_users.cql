UPDATE cassdb.users
SET email = 'david@gmail.com'
WHERE id = UUID_HERE;

UPDATE cassdb.users
SET curso = {'Sistemas de Informação' : 'Período 5'}
WHERE id = UUID_HERE