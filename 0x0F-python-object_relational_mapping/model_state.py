#!/usr/bin/python3
"""definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


mdata = MetaData()

Base = declarative_base(metadata=mdata)


class State(Base):
    """Class declaration"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
