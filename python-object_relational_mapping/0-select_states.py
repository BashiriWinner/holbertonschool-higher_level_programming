#!/usr/bin/python3
"""This script connects to the hbtn_0e_0_usa database and lists all states
from the states table, sorted by id in ascending order."""


if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    rows = cusrsor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        db.close

