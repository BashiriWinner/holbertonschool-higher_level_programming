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
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in (session.query(State)
                  .filter(State.name.like('%a%'))
                  .order_by(State.id)):
        print("{}: {}".format(state.id, state.name))

        session.close()
