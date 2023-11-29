import configparser
import os
from sqlalchemy import VARCHAR, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         '../', 'config.ini')))
username = config['pgsql']['username']
password = config['pgsql']['password']
host = config['pgsql']['host']
port = config['pgsql']['port']
database_name = config['pgsql']['database_name']
schema = config['pgsql']['schema']

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database_name}")

schema = schema
metadata = MetaData(schema=schema)
Base = declarative_base()


class Register(Base):
    __tablename__ = 'register_user'
    username = Column(VARCHAR, primary_key=True)
    password = Column(VARCHAR)

    def __init__(
            self,
            username,
            password,
    ):
        self.username = username
        self.password = password


Base.metadata.create_all(engine)
