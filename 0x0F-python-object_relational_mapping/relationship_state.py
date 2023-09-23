#!/usr/bin/python3
"""definition of a State class"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mdata = MetaData()
Base = declarative_base(metadata=mdata)


class State(Base):
    """Class declaration"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
