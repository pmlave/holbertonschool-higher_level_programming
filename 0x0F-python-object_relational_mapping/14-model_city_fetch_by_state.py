#!/usr/bin/python3
''' Deleting states in the the database state table that contain an "a" '''
from sys import argv
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(argv) == 4:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        matches = session.query(City, State).filter(
                State.id == City.state_id).order_by(City.id)
        for city, state in matches:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.commit()
        session.close()
