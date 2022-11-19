#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))
    engine.connect()
    metadata = MetaData()
    session = Session(engine)
    found = []

    for state in session.query(State).order_by(State.id).all():
        if sys.argv[4] == state.name:
            found.append(state.id)

    if len(found) > 0:
        print(found[0])
    else:
        print("Not found")

    session.close()
