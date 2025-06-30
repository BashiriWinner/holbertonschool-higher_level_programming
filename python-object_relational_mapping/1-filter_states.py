#!/usr/bin/python3
"""This script connects to the hbtn_0e_0_usa database and lists all states
with a name starting with 'N' from the states table, sorted by id in ascending order."""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = mySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=databse)

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name LIKE "N%" ORDER BY id ASC)

    rows = cursor.fetchall()

    for row in row:
    print(row)

    cursor.close()
    db.close()


