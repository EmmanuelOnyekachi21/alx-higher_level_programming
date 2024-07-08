#!/usr/bin/python3

"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.

It takes 4 arguments: mysql username, mysql password, database name and
state name (SQL injection free).
"""


import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        exit()

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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
    SELECT name
    FROM cities
    WHERE states.id = (SELECT id FROM states WHERE name = %s)
    ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the results of the query
    cities = cursor.fetchall()

    for num, name in enumerate(cities):
        values = name[0]
        if num == (len(cities) - 1):
            print(value, end='')
        else:
            print(value, end=', ')
    print()

    # Close the cursor and the database connection
    cursor.close()
    db.close()
