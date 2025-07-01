#!/usr/bin/python3
"""This script defines a State class and creates the states table
in the hbtn_0e_6_usa database using SQLAlchemy."""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    States table in MySQL
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
