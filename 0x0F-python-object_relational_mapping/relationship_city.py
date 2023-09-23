#!/usr/bin/python3
"""definition of a City class"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """Class declaration"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
