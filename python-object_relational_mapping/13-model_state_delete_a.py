#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect
    metadata = MetaData()
    session = Session(engine)
    found = []

    for row in session.query(State).filter(State.name.like('%a%')):
        session.delete(row)

    session.commit()

    session.close()
