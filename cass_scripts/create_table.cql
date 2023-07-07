CREATE TABLE cassdb.users (
    id UUID PRIMARY KEY DEFAULT uuid(),
    nome text,
    email text,
    telefone text
);
