#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    arg = sys.argv
    var = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(var.format(arg[1], arg[2], arg[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        print("{}: {}".format(state.id, state.name))
