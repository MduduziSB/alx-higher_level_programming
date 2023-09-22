#!/usr/bin/python3
"""definition of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user = 'your_username'
db_password = 'your_password'
db_host = 'localhost'
db_port = 3306
db_name = 'your_database_name'
db_url = f'mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class State(Base):
    """Class declaration"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
session.close
