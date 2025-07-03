#!/usr/bin/python3
"""This script prints all City objects
from the hbtn_0e_14_usa database."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State,
                                              City.state_id == State.id).order_by(City.id).all()
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

