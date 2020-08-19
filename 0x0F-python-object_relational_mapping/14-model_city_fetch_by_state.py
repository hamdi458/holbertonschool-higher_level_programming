#!/usr/bin/python3
"""
 file that contains the class definition of a State
"""

from model_state import Base, State
from model_city import Base, City
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
    item = session.query(City, State).join(State, State.id == City
                                           .state_id).order_by(City.id).all()
    for city in item:
        print("{}: ({}) {}".format(city.State.name, city.City.id,
                                   city.City.name))
    session.close()
