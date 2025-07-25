#!/usr/bin/python3
"""This script connects to the hbtn_0e_0_usa database and lists all states
with a name starting with 'N', sorted by id in ascending order."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states \
                   WHERE name LIKE 'N%' ORDER BY id ASC")

    for state in cursor.fetchall():
        if state[1][0] == "N":
            print(state)

    cursor.close()
    db.close()
