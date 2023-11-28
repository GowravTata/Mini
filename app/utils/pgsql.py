import configparser
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                         '..', 'config.ini')))
username = config['pgsql']['username']
password = config['pgsql']['password']
host = config['pgsql']['host']
port = config['pgsql']['port']
database_name = config['pgsql']['database_name']


class SqlDB:
    def __init__(self):
        self.url = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"
        self.engine = create_engine(self.url)
        self.session_factory = sessionmaker(bind=self.engine)

    @contextmanager
    def transaction(self):
        session = scoped_session(self.session_factory)
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
