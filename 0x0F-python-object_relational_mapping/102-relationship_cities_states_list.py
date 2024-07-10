#!/usr/bin/python3


"""
Lists all City objects from the database hbtn_0e_101_usa.
"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    # Get MySQL credentials and database name from the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}",
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()
    # Query all states and their corresponding cities
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    # Close the session
    session.close()
