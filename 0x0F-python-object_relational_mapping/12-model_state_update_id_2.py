#!/usr/bin/python3
''' Updating a state in the the database state table '''
from sys import argv
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(argv) == 4:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        session.query(State).filter(State.id == 2).update(
            {State.name: """New Mexxico"""}, synchronize_session=False)
        session.commit()
        session.close()
