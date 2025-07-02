#!/usr/bin/python3
"""This script lists all State objects 
from the hbtn_0e_6_usa database
using SQLAlchemy, sorted by id in ascending order."""

import SQLAlchemy
from model_state import Base, State
from sys import argv

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))


    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    
        session.close()

