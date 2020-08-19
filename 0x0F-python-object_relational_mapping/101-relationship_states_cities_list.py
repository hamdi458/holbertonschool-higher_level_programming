#!/usr/bin/python3
"""
 file that contains the class definition of a State
"""
from relationship_city import City
from relationship_state import Base, State
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).order_by(State.id).all()
    for stt in state:
        print("{}: {}".format(stt.id, stt.name))
        for cit in stt.cities:
            print("\t{}: {}".format(cit.id, cit.name))
    session.close()
