#!/usr/bin/python3
''' Connects to a db and queries for all cities from all states'''
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM states
    INNER JOIN cities ON states.id=cities.state_id WHERE states.name
    LIKE %s ORDER BY cities.id ASC""", [argv[4]])
    rows = cur.fetchall()
    i = 0
    for row in rows:
        print(row[0], end='')
        if i < len(rows) - 1:
            print(", ", end='')
        i += 1
    print()
    cur.close()
    db.close()
