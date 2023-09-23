#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from sqlalchemy.orm import relationship
import sys


if __name__ == "__main__":
    arg = sys.argv
    if len(arg) < 4:
        exit(1)
    var = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(var.format(arg[1], arg[2], arg[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    s = session.query(State).order_by(State.id).all()
    for r in s:
        print("{}: {}".format(r.id, r.name))
        for c in r.cities:
            print("\t{}: {}".format(c.id, c.name))
