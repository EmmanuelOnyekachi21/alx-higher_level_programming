#!/usr/bin/python3

"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

It takes 4 arguments: mysql username, mysql password, database name and
state name searched.
"""


import MySQLdb
import sys

if __name__ == '__main__':
    # Get the MySQL credentials and database name from the command
    # line arguments
    if len(sys.argv) != 5:
        exit()

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Establish a connection
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            database=database_name
            )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    stmt = (
        "SELECT * FROM states WHERE BINARY name"
        "= '{}' ORDER BY id ASC".format(state_name_searched)
        )
    cursor.execute(stmt)

    # Fetch all the esults of the query
    states = cursor.fetchall()

    # Prints each  state in the required format
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
