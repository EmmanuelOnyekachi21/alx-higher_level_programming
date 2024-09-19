#!/usr/bin/python3
""" This is a script that uses MySQLdb to lists all cities available for a
given state which is passed as an argument, using the database hbtn_0e_4_usa
and provides protection against SQL injection attacks.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) != 5:
        exit()
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query, (sys.argv[4],))
    cities = cur.fetchall()
    
    print(", ".join([city[0] for city in cities]))
    cur.close()
    db.close()
