#!/usr/bin/python3
''' Connects to a db and queries for specific states from given arg'''
from sys import argv
import MySQLdb


if __name__ == "__main__":
    if len(argv) == 5:
        db = MySQLdb.connect(host="localhost",
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3],
                             port=3306)
        cur = db.cursor()
        cur.execute("""SELECT * FROM states WHERE name LIKE BINARY
        '{}' ORDER BY id ASC""".format(argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
