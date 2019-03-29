#!/usr/bin/python3
''' Adding a new state to the database state table '''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) == 4:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)
        session.close()
