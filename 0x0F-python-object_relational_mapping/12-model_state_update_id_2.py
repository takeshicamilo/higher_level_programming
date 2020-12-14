#!/usr/bin/python3
"""
changes the name of the State object where id=2 to New Mexico from a database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter_by(id=2).first()
    states.name = 'New Mexico'

    session.commit()
