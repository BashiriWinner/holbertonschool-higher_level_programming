#!/usr/bin/python3
"""
Connecting to database and listing it

"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states WHERE name = %s ORDER BY id ASC")

    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)

    cursor.close()
    db.close()

