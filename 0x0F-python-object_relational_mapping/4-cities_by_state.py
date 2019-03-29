#!/usr/bin/python3
''' Connects to a db and queries for all cities from all states'''
from sys import argv
import MySQLdb


if __name__ == "__main__":
    if len(argv) == 4:
        db = MySQLdb.connect(host="localhost",
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3],
                             port=3306)
        cur = db.cursor()
        cur.execute("""SELECT cities.id, cities.name, states.name FROM states
        INNER JOIN cities ON states.id=cities.state_id
        ORDER BY cities.id ASC""")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
