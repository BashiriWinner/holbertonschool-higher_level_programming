#!/usr/bin/python3
"""This script connects to the hbtn_0e_0_usa database and lists all states
from the states table, sorted by id in ascending order."""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        db.close

