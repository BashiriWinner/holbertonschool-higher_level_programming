#!/usr/bin/python3
"""This script lists all State objects 
with a name containing the letter 'a'
from the hbtn_0e_6_usa database 
using SQLAlchemy, sorted by id."""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = Session()

    [print("{}: {}".format(
        state.id, state.name)
        ) for state in session.query(
            State
            ).order_by(
                State.id
                ) if 'a' in state.name]




