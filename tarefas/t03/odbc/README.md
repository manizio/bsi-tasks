### Criar container postgres-server

``docker run --name postgres-server -e "POSTGRES_USER=postgres" -e "POSTGRES_PASSWORD=postgres" -p 8001:5432 -v $HOME/dev/docker/volumes/postgres/conf:/var/lib/postgresql -v $HOME/dev/docker/volumes/postgres/data:/var/lib/postgresql/data --network=postgres-network -d postgres``