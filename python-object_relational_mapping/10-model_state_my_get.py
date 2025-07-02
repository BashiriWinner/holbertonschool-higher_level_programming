#!/usr/bin/python3
"""This script prints the State object's id with the given name
from the hbtn_0e_6_usa database using SQLAlchemy."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = Session()

    state = (session.query(State).filter(State.name == argv[4]).first())


    if state is None:
        print("Not found")
    else:
        print("state.id")

    session.close()

