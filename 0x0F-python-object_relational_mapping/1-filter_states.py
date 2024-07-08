#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password and database name.
"""


import MySQLdb
import sys

if __name__ == '__main__':
    # Get the MySQL credentials and database name from the command
    # line arguments
    if len(sys.argv) != 4:
        exit()

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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
    stmt = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(stmt)

    # Fetch all the esults of the query
    states = cursor.fetchall()

    # Prints each  state in the required format
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
