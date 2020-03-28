#!/usr/bin/python3
"""script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    state_query = session.query(State).filter(
        State.name == sys.argv[4]).order_by(State.id).first()
    if state_query is None:
        print("Not found")
    else:
        print(state_query.id)
    Base.metadata.create_all(engine)
    session.close()
