#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    rows = session.query(State).order_by(State.id).all()
    res = ""

    for row in rows:
        if sys.argv[4] in row.name:
            res = row.id            
    if res != "":
        print(res)
    else:
        print("Not Found")
        
    session.close()
