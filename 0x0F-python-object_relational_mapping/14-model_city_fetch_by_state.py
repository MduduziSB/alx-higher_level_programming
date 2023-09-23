#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa:
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
import sys


if __name__ == "__main__":
    arg = sys.argv
    var = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(var.format(arg[1], arg[2], arg[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    s = (session.query(State.name, City.id, City.name)
         .filter(State.id == City.state_id))
    for r in s:
        print(r[0] + ": (" + str(r[1]) + ") " + r[2])
