#!/usr/bin/python3


"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/"
        f"{database_name}",
        pool_pre_ping=True
    )
    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for all City objects and join with State to get the state name
    results = session.query(State, City).filter(
            City.state_id == State.id).order_by(
            City.id).all()

    # Display the results
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
