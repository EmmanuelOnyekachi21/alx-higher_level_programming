#!/usr/bin/python3


"""
This script prints the first State object from the database hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    # Get MySQL credentials and database name from the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/"
        f"{database_name}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the first state object from the database
    statesWithA = session.query(State).filter(
            State.name.like('%a%')
            ).order_by(State.id).all()

    # Print each state in the required format
    for state in statesWithA:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
