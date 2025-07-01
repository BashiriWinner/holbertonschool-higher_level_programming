#!/usr/bin/python3
"""This script connects to the hbtn_0e_0_usa database and lists all states
with a name starting with 'N' from the states table, sorted by id in ascending order."""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = mySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
    print(row)

    cursor.close()
    db.close()

