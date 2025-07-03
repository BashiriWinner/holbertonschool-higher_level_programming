#!/usr/bin/python3
"""This script prints all City objects
from the hbtn_0e_14_usa database."""

from sys import argv
from model_state import State as s
from model_city import Base, City as c
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    ses = Session()

    r = ses.query(c,s).join(s,c.state_id == s.id).order_by(c.id).all()
    for city, state in r:
        print(f"{state.name}: ({city.id}) {city.name}")

    ses.close()

