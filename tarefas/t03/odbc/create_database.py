from connect import connect

conn = connect()
cur = conn.cursor()

def create_database():
    try:
        with open('../script/equipe_create_postgres.sql', 'r', encoding='UTF-8') as script:
            cur.execute(script.read())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()

if __name__ == '__main__':
    create_database()
