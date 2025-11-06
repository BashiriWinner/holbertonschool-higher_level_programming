#!/usr/bin/python3
"""This script safely connects to the hbtn_0e_0_usa database and lists
all states with a name matching the user-provided argument,
sorted by id in ascending order."""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * \
                    FROM `states` \
                    ORDER BY id")

    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)

    if cursor:
        cursor.close()
    if db:
        db.close()

