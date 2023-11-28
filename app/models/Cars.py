import configparser
import os
from sqlalchemy import Integer, VARCHAR, Column, MetaData
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

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database_name}")

schema = 'public'
metadata = MetaData(schema=schema)
Base = declarative_base()


class Cars(Base):
    __tablename__ = 'cars_new_two'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(VARCHAR)
    model = Column(VARCHAR)
    year = Column(Integer)

    def __init__(
            self,
            brand,
            model,
            year
    ):
        self.brand = brand
        self.model = model
        self.year = year


Base.metadata.create_all(engine)
