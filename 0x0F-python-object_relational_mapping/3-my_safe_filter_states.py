#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument (safe from SQL injection).
It takes 4 arguments: mysql username, mysql password, database name, and state name searched.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials, database name, and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to select states matching the given name using parameterized query
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Fetch all the results of the query
    states = cursor.fetchall()

    # Print each state in the required format
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
