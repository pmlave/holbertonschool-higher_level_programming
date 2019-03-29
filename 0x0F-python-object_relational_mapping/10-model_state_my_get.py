#!/usr/bin/python3
''' Querying for a given state name '''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) == 5:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        i = 0
        queried = session.query(State).order_by(State.id).all()
        for state in queried:
            if argv[4] in state.name:
                print("{}".format(state.id))
                break
            elif i is len(queried) - 1:
                print("Not found")
            i += 1
        session.close()
