#!/usr/bin/python3

"""
This script lists all cities from the database hbtn_0e_4_usa.
It takes 3 arguments: mysql username, mysql passwrd, and database name.
The results are sorted in ascending order by cities.id.
"""


import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        exit()

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the results of the query
    cities = cursor.fetchall()

    # Print each city in the required format
    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
