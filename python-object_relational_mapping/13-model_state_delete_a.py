#!/usr/bin/python3
"""delete all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).filter(State.name.ilike('%a%')).all()
    for s in st:
        session.delete(s)
    session.commit()

    session.close()
