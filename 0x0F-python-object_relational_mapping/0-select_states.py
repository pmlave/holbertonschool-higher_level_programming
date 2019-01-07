#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    This script will list all states in the database
    """
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
