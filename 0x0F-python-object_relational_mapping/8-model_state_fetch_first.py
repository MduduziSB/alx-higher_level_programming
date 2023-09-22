#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
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
    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
