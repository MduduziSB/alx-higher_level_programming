#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    arg = sys.argv
    if ";" in arg or len(arg) < 5:
        exit(1)

    var = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(var.format(arg[1], arg[2], arg[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).filter(State.name.like(arg[4])).all()
    if len(states) > 0:
        print("{}".format(states[0].id))
    else:
        print("Not found")
