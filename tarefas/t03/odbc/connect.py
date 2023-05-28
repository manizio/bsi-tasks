import psycopg2
from decouple import config

HOST = config('HOST')
DATABASE = config('DATABASE')
USER = config('USER')
PASS = config('PASSWORD')

def connect():

    conn = None
    try:

        print('Conectando ao banco de dados...')
        conn = psycopg2.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASS,
            port=8001
        )
        
        return conn

    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

if __name__ == '__main__':
    connect()


