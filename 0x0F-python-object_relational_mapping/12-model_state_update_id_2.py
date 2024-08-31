#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State with id = 2
    state = session.query(State).get(2)

    # Check if the state exists
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with id = 2 not found.")

    # Close session
    session.close()

