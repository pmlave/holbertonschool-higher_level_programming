#!/usr/bin/python3
''' Querying for all state objects containing the letter 'a' '''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        for state in session.query(State).order_by(State.id).all():
            if 'a' in state.name:
                print("{}: {}".format(state.id, state.name))
        session.close()
