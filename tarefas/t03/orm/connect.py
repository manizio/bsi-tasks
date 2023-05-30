from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

def connect():
    DATABASE = config('DATABASE')
    PORT = config('PORT')
    USER = config('USER')
    PASSWORD = config('PASSWORD')
    HOST = config('HOST')
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
    Session = sessionmaker(bind=engine)

    return Session()

