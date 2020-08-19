#!/usr/bin/python3
"""
 file that contains the class definition of a State
"""

from model_state import Base, State
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
    session.query(State).filter(State.name.ilike('%a%')) \
        .delete(synchronize_session=False)
    session.commit()
    session.close()
