#!/usr/bin/python3
"""This script prints the first State object 
from the hbtn_0e_6_usa database
using SQLAlchemy, based on the lowest id."""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import crate_engine
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()

